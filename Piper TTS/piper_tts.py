# Download a voice, for example:

# python3 -m piper.download_voices en_US-lessac-medium

import wave
from piper import PiperVoice

voice = PiperVoice.load("en_US-lessac-medium.onnx")  
with wave.open("test.wav", "wb") as wav_file:
    voice.synthesize_wav("what is love ? baby don't hurt me", wav_file)





# Adjust synthesis:

# syn_config = SynthesisConfig(
#     volume=0.5,  # half as loud
#     length_scale=2.0,  # twice as slow
#     noise_scale=1.0,  # more audio variation
#     noise_w_scale=1.0,  # more speaking variation
#     normalize_audio=False, # use raw audio from voice
# )

# voice.synthesize_wav(..., syn_config=syn_config)
# To use CUDA for GPU acceleration:

# voice = PiperVoice.load(..., use_cuda=True)
# This requires the onnxruntime-gpu package to be installed.

# For streaming, use PiperVoice.synthesize:

# for chunk in voice.synthesize("what is love ? baby don't hurt me"):
#     set_audio_format(chunk.sample_rate, chunk.sample_width, chunk.sample_channels)
#     write_raw_data(chunk.audio_int16_bytes)
