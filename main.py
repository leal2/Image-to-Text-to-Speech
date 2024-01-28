import cv2
import pyttsx3
import pytesseract
import numpy as np
from translate import Translator
print("test")
pytesseract.pytesseract.tesseract_cmd = 'C:\\tesseract\\tesseract.exe'

lang = ""
vidCap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# print(pytesseract.get_languages(config=''))
print("test")
print("press space to capture frame and translate or press q to quit")
while True:
    ret, frame = vidCap.read()
    cv2.imshow("vid feed", frame)
    if not ret:
        print("Error: Could not capture frame")
        break

    if cv2.waitKey(1) == ord(' '):
        ret, imgToRead = vidCap.read()
        cv2.imshow("captured frame", imgToRead)
        print("type 'e' for english, 's' para espanol, 'p' para Português, 'c' 代表葡萄牙语, or 'q' to quit")
        lan = input()
        while lan != "q":

            if lan == "e":
                translator = Translator(to_lang="en")
                text = pytesseract.image_to_string(imgToRead, lang='eng')
                if text == "":
                    print("could not read words")
                    cv2.destroyAllWindows()
                    break
                translation = translator.translate(text)
                print("The words on the image translated to " + lang + " are : " + translation)
                engine = pyttsx3.init()
                engine.setProperty('volume', .5)
                engine.say(translation)

            elif lan == "s":
                translator = Translator(to_lang="es")
                text = pytesseract.image_to_string(imgToRead, lang='eng')
                if text == "":
                    print("could not read words")
                    cv2.destroyAllWindows()
                    break
                translation = translator.translate(text)
                print("The words on the image translated to " + lang + " are : " + translation)
            elif lan == "p":
                translator = Translator(to_lang="pt")
                text = pytesseract.image_to_string(imgToRead, lang='eng')
                if text == "":
                    print("could not read words")
                    cv2.destroyAllWindows()
                    break
                translation = translator.translate(text)
                print("The words on the image translated to " + lang + " are : " + translation)
            elif lan == "c":
                translator = Translator(to_lang="zh")
                text = pytesseract.image_to_string(imgToRead, lang='eng')
                if text == "":
                    print("could not read words")
                    cv2.destroyAllWindows()
                    break
                translation = translator.translate(text)
                print("The words on the image translated to " + lang + " are : " + translation)
            else:
                print("enter a valid choice")
                continue
            print("if you want to translate to another language,")
            print("type 'e' for english, 's' para espanol, 'p' para Português, 'c' 代表葡萄牙语, or 'q' to quit")
            lan = input()

    elif cv2.waitKey(1) == ord('q'):
        print("closing program..bye!!")
        break
