from gtts import gTTS
from playsound import playsound
import os

text = "Welcome to EdgeGuard AI. Vehicle is healthy."

tts = gTTS(text=text, lang='en')

tts.save("voice.mp3")

playsound("voice.mp3")

os.remove("voice.mp3")
