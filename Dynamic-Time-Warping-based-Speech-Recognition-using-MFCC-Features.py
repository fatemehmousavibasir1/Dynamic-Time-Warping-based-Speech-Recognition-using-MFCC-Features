import numpy as np
import librosa
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw


def framing(signal, frame_length, hop_length):
    num_frames = 1 + int((len(signal) - frame_length) / hop_length)
    frames = np.zeros((num_frames, frame_length))
    
    for i in range(num_frames):
        start = i * hop_length
        end = start + frame_length
        frames[i] = signal[start:end]
    
    return frames


def compute_mfcc(frames, sr, n_mfcc=16, n_fft=2048):
    mfcc_features = []
    for frame in frames:
        mfcc = librosa.feature.mfcc(y=frame, sr=sr, n_mfcc=n_mfcc, n_fft=n_fft)
        mfcc_features.append(mfcc.mean(axis=1))  
    return np.array(mfcc_features)

def cepstral_distance(c1, c2):
    return np.sum((c1 - c2) ** 2)

def dtw_distance(mfcc1, mfcc2):
    distance, path = fastdtw(mfcc1, mfcc2, dist=cepstral_distance)
    return distance


signal_yes, sr_yes = librosa.load("C:/Users/Asus/Desktop/bale.wav", sr=None)
signal_no, sr_no = librosa.load("C:/Users/Asus/Desktop/kheir.wav", sr=None)
signal_test, sr_test = librosa.load("C:/Users/Asus/Desktop/bale_test.wav", sr=None)
#signal_test, sr_test = librosa.load("C:/Users/Asus/Desktop/kheir_test.wav", sr=None)

import matplotlib.pyplot as plt
from scipy.io import wavfile
plt.figure(figsize=(10, 6))
plt.plot(signal_yes)
plt.title('Waveform Bale')
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(signal_no)
plt.title('Waveform Kheir')
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(signal_test)
plt.title('Waveform Bale Test')
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()


frame_length = 300
hop_length = 100

frames_yes = framing(signal_yes, frame_length, hop_length)
frames_no = framing(signal_no, frame_length, hop_length)
frames_test = framing(signal_test, frame_length, hop_length)


mfcc_yes = compute_mfcc(frames_yes, sr_yes)
mfcc_no = compute_mfcc(frames_no, sr_no)
mfcc_test = compute_mfcc(frames_test, sr_test)

distance_yes = dtw_distance(mfcc_test, mfcc_yes)
distance_no = dtw_distance(mfcc_test, mfcc_no)

if distance_yes < distance_no:
    print("Detected word: Bale")
else:
    print("Detected word: Kheir")
