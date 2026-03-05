import speech_recognition as sr

recognition = sr.Recognizer()

def extract_text(file_path):

    with sr.AudioFile(file_path) as source:
        audio = recognition.record(source)
    try:
        text = recognition.recognize_google(audio)
        print(f"Extracted text: {text}")
        return text
    except Exception as e:
        print(e)