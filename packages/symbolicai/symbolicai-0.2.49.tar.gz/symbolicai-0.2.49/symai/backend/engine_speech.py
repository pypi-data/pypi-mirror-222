import logging
from typing import List

import torch

from .base import Engine
from .settings import SYMAI_CONFIG

try:
    import whisper
except:
    whisper = None


class WhisperEngine(Engine):
    def __init__(self):
        super().__init__()
        self.model = None # lazy loading
        config = SYMAI_CONFIG
        self.model_id = config['SPEECH_ENGINE_MODEL']
        self.old_model_id = config['SPEECH_ENGINE_MODEL']

    def command(self, wrp_params):
        super().command(wrp_params)
        if 'SPEECH_ENGINE_MODEL' in wrp_params:
            self.model_id = wrp_params['SPEECH_ENGINE_MODEL']

    def forward(self, *args, **kwargs) -> List[str]:
        assert whisper is not None, "Whisper is not installed. Please install it first."
        if self.model is None or self.model_id != self.old_model_id:
            device_fallback = 'cpu'
            device = "cuda" if torch.cuda.is_available() else device_fallback
            device = kwargs['device'] if 'device' in kwargs else device # user preference over auto detection
            try:
                self.model = whisper.load_model(self.model_id, device=device)
            except:
                logging.warn(f"Whisper failed to load model on device {device}. Fallback to {device_fallback}.")
                self.model = whisper.load_model(self.model_id, device=device_fallback)
            self.old_model_id = self.model_id

        prompt = kwargs['prompt']
        audio  = kwargs['audio']

        input_handler = kwargs['input_handler'] if 'input_handler' in kwargs else None
        if input_handler:
            input_handler((prompt, audio))

        mel = whisper.log_mel_spectrogram(audio).to(self.model.device)
        if prompt == 'detect_language':
            # detect the spoken language
            _, probs = self.model.detect_language(mel)
            rsp = max(probs, key=probs.get)
        elif prompt == 'decode':
            # decode the audio
            options = whisper.DecodingOptions(fp16 = False)
            result = whisper.decode(self.model, mel, options)
            rsp = result.text
        else:
            raise Exception(f"Unknown whisper command prompt: {prompt}")

        output_handler = kwargs['output_handler'] if 'output_handler' in kwargs else None
        if output_handler:
            output_handler(rsp)

        metadata = {}
        if 'metadata' in kwargs and kwargs['metadata']:
            metadata['kwargs'] = kwargs
            metadata['input']  = (prompt, audio)
            metadata['output'] = rsp

        return [rsp], metadata

    def prepare(self, args, kwargs, wrp_params):
        assert 'audio' in wrp_params, "Whisper requires audio input."
        audio_file = str(wrp_params['audio'])
        # load audio and pad/trim it to fit 30 seconds
        audio = whisper.load_audio(audio_file)
        audio = whisper.pad_or_trim(audio)
        wrp_params['audio'] = audio

