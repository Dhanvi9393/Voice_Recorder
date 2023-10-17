import pyaudio
import wave
import os

# Ask the user when to start recording
input("Press Enter to start recording...")

# Set up the audio stream
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

frames = []

print("Recording...")
while True:
   try:
       data = stream.read(1024)
       frames.append(data)
   except KeyboardInterrupt:
       break  # Stop recording when Ctrl+C is pressed

# Ask the user when to stop recording
input("Press Enter to stop recording...")

# Close the audio stream
print("Recording stopped.")
stream.stop_stream()
stream.close()
p.terminate()

# Save the recorded audio as a WAV file
wf = wave.open("recorded_audio.wav", "wb")
wf.setnchannels(1)
wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
wf.setframerate(44100)
wf.writeframes(b''.join(frames))
wf.close()

print("Audio saved as recorded_audio.wav")
