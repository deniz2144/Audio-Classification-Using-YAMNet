import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import csv
import soundfile as sf
import sounddevice as sd
import time
import librosa

# Load the YAMNet model from TensorFlow Hub
model = hub.load('https://tfhub.dev/google/yamnet/1')

# Path to the audio file
audioFilePath = "C:\\Users\\deniz\\Desktop\\Audio-Classification-TensorFlow-Hub\\jinglejazz-200026.mp3"

# Load the audio file
waveform, samplerate = librosa.load(audioFilePath, sr=16000)
print(samplerate)
print(type(waveform))

# Run the model
scores, embeddings, log_mel_spectrogram = model(tf.convert_to_tensor(waveform))

# Get the model labels
class_map_path = model.class_map_path().numpy().decode('utf-8')
class_names = []

with tf.io.gfile.GFile(class_map_path) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        class_names.append(row['display_name'])

print("Class_names : ", class_names)

# Calculate scores and get the index of the highest score
sc = scores.numpy().mean(axis=0)
scMax = sc.argmax()
print(scMax)
print(class_names[scMax])

# Play the audio
sd.play(waveform, samplerate)
time.sleep(10)
