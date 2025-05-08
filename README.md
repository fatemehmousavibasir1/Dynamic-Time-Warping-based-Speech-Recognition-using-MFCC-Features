
#  Dynamic Time Warping-based Speech Recognition using MFCC Features
This project implements a simple yet effective template-based speech recognition system. It uses Mel-Frequency Cepstral Coefficients (MFCCs) to extract features from speech audio, and applies Dynamic Time Warping (DTW) to compare unknown speech samples against known templates. The project distinguishes between two Persian words: "بله" (Bale) and "خیر" (Kheir), which are commonly used as "Yes" and "No".

## Project Description
The aim is to classify a test utterance as either "Bale" or "Kheir" by comparing its acoustic similarity to reference samples using DTW on MFCC sequences.

The pipeline includes:

1.Audio Loading
   Three audio files are used:

   A reference audio of the word "Bale" (bale.wav)

   A reference audio of the word "Kheir" (kheir.wav)

   A test audio, either of "Bale" or "Kheir" (e.g., bale_test.wav)

   The audio is loaded using Librosa with its original sampling rate.

2.Framing
  Each audio signal is split into overlapping frames using a sliding window:

  Frame length: 300 samples

  Hop length: 100 samples
  Framing is essential to break the signal into small chunks for short-time analysis.

3.MFCC Feature Extraction
  MFCCs are computed from each frame:

  16 MFCC coefficients per frame

  Frame-level MFCCs are averaged across frequency bins (mean over time)
  This results in a sequence of MFCC feature vectors representing the overall spectral content of the word.

4.DTW-Based Matching
  The DTW (Dynamic Time Warping) algorithm is used to align and compare the test signal with each reference template:

  A custom cepstral distance (squared Euclidean distance between MFCC vectors) is used as the frame-level distance metric.

  DTW calculates the minimum cumulative cost to warp one feature sequence into another.

  The template (either "Bale" or "Kheir") that yields the lower DTW distance to the test signal is chosen as the recognized word.

5.Visualization
  Waveforms of all three signals are plotted for manual inspection:

  bale.wav

  kheir.wav

  The test audio (e.g., bale_test.wav)

  This helps understand the shape and relative energy of the audio inputs.

6.Decision Logic
  After calculating the DTW distance between the test MFCC sequence and each reference:

If DTW(test, bale) < DTW(test, kheir), it prints: Detected word: Bale

Otherwise, it prints: Detected word: Kheir
