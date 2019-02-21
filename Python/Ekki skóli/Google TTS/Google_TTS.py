from gtts import gTTS
from playsound import playsound
import os

tungumal = "en"

while True:
    spila = True
    texti = input(">>>")

    # Checks
    if texti == "":
        spila = False
    if texti[0] == "/":
        spila = False
        if texti[1] == "/":
            tungumal = texti[2::]
        elif texti[1::] == "clear":
            print(chr(27) + "[2J")
        elif texti[1::] == "quit":
            break
        else:
            print("Command not found")

    if spila == True:
        try:
            tts = gTTS(texti,lang=tungumal)
            tts.save('tts.mp3')
            tts = ""
            playsound('tts.mp3')
            os.remove("tts.mp3")
        except ValueError as error:
            error = str(error)
            if error[0:24] == "Language not supported: ":
                print("This language is not supported")
                print("Changing to english")
                tungumal = "en"

print("Bye")