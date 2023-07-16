import numpy as np
import soundfile as sf
from pathlib import Path

from clonerDep.encoder import inference as encoder
from clonerDep.encoder.params_model import model_embedding_size as speaker_embedding_size
from clonerDep.synthesizer.inference import Synthesizer
from clonerDep.vocoder import inference as vocoder

def cloner(sentence: str) -> str:

    encoder.load_model(Path("clonerDep/encoder/models/encoder.pt"))
    synthesizer = Synthesizer(Path("clonerDep/synthesizer/models/synthesizer.pt"))
    vocoder.load_model(Path("clonerDep/vocoder/models/vocoder.pt"))

    while True:
        
        try:

                in_fpath = Path("static/recorded_audio.wav")

                ## Computing the embedding
                # First, we load the wav using the function that the speaker encoder provides. This is
                # important: there is preprocessing that must be applied.

                # The following two methods are equivalent:
                # - Directly load from the filepath:
                preprocessed_wav = encoder.preprocess_wav(in_fpath)

                # Then we derive the embedding. There are many functions and parameters that the
                # speaker encoder interfaces. These are mostly for in-depth research. You will typically
                # only use this function (with its default parameters):
                embed = encoder.embed_utterance(preprocessed_wav)

                # The synthesizer works in batch, so you need to put your data in a list or numpy array
                texts = [sentence]
                embeds = [embed]
                # If you know what the attention layer alignments are, you can retrieve them here by
                # passing return_alignments=True
                specs = synthesizer.synthesize_spectrograms(texts, embeds)
                spec = specs[0]

                # Synthesizing the waveform is fairly straightforward. Remember that the longer the
                # spectrogram, the more time-efficient the vocoder.
                generated_wav = vocoder.infer_waveform(spec)


                ## Post-generation
                # There's a bug with sounddevice that makes the audio cut one second earlier, so we
                # pad it.
                generated_wav = np.pad(generated_wav, (0, synthesizer.sample_rate), mode="constant")

                # Trim excess silences to compensate for gaps in spectrograms (issue #53)
                generated_wav = encoder.preprocess_wav(generated_wav)

                # Save it on the disk
                filename = "static/output.wav"
                sf.write(filename, generated_wav.astype(np.float64), synthesizer.sample_rate)
                
                break

        except Exception as e:
            print("Encountered an Error: %s" % repr(e))
            print("Restarting\n")