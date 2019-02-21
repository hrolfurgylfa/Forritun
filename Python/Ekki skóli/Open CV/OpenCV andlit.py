import cv2
import sys
import logging as log
import datetime as dt
from time import sleep
from gtts import gTTS
from playsound import playsound
import os
import threading

# Búa til breytur
tungumal = "en"
tel = 0
fjoldi_andlita = 0

#cv2 stöff
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
log.basicConfig(filename='webcam.log',level=log.INFO)

video_capture = cv2.VideoCapture(0)
anterior = 0

def tala(setning):
    tts = gTTS(setning,lang=tungumal)
    tts.save('tts.mp3')
    tts = ""
    playsound('tts.mp3')
    os.remove("tts.mp3")

def hve_margir_inni(fjoldi_andlita):
    if fjoldi_andlita == 1:
        tala("Their is "+str(fjoldi_andlita)+" person here.")
    elif fjoldi_andlita != 0:
        tala("Their are "+str(fjoldi_andlita)+" people here.")
    return True

while True:
    if not video_capture.isOpened():
        print('Unable to load camera.')
        sleep(5)
        pass

    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    if anterior != len(faces):
        anterior = len(faces)
        log.info("faces: "+str(len(faces))+" at "+str(dt.datetime.now()))

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if 
        t1 = threading.Thread(target = hve_margir_inni, args = [len(faces)])
        t1.start()

    tel += 1

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()