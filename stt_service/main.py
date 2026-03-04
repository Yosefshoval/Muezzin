import speech_recognition as sr

recognizer_instance = sr.Recognizer()

with sr.AudioFile(my_path) as source:
    audio = recognizer_instance.record(source)

try:
    s = recognizer_instance.recognize_google(audio)
    print("Text: " + s)
except Exception as e:
    print(e)
