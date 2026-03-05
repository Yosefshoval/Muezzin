import speech_recognition as sr
from config import Config

logger = Config.logger

recognition = sr.Recognizer()

def extract_text(file_path):

    with sr.AudioFile(file_path) as source:
        audio = recognition.record(source)
        logger.info('audio file opened.')
    try:
        text = recognition.recognize_google(audio)
        logger.info(f"Extracted text from file {file_path}")
        return text
    except Exception as e:
        logger.error(e)