# ✨ Voice Cloning and Lip Syncing ✨

## Requirments ✔️

- Install the required Python modules with the following command. If you get an error message related to building wheels for webrtcvad on Windows, then please install [C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/ "Build Tools") and then try again.
```bash
pip install -r requirements.txt
```
- Install ffmpeg from their [site](https://ffmpeg.org/download.html "ffmpeg Download Page").
- Download the following files and place them in the specified directories:
  - [encoder.pt](https://drive.google.com/file/d/1q8mEGwCkFy23KZsinbuvdKAQLqNKbYf1/view "encoder.pt") -> ```./clonerDep/encoder/models/encoder.pt```
  - [synthesizer.pt](https://drive.google.com/file/d/1EqFMIbvxffxtjiVrtykroF6_mUh-5Z3s/view "synthesizer.pt") -> ```./clonderDep/synthesizer/models/synthesizer.pt```
  - [vocoder.pt](https://drive.google.com/file/d/1cf2NO6FtI0jDuy8AV3Xgn6leO6dHjIgu/view "vocoder.pt") -> ```./clonerDep/vocoder/models/vocoder.pt```
  - [wav2lip_gan.pth](https://iiitaphyd-my.sharepoint.com/personal/radrabha_m_research_iiit_ac_in/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fradrabha%5Fm%5Fresearch%5Fiiit%5Fac%5Fin%2FDocuments%2FWav2Lip%5FModels%2Fwav2lip%5Fgan%2Epth&parent=%2Fpersonal%2Fradrabha%5Fm%5Fresearch%5Fiiit%5Fac%5Fin%2FDocuments%2FWav2Lip%5FModels&ga=1 "Wav2Lip GAN") -> ```./lipsyncDep/models/wav2lip_gan.pth```
