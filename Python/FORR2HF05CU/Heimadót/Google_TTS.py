from gtts import gTTS
from playsound import playsound
import os

while True:
    tts = gTTS(input(">>>"),lang="en")
    tts.save('tts.mp3')
    tts = ""
    playsound('tts.mp3')
    os.remove("tts.mp3")