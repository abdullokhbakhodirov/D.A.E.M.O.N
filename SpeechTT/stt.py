import os
import speech_recognition as sr
import openai


def record_audio():
    path = "D:/AI_DANNY/functions/recording.wav"
    openai.api_key = "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"
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now...")
        audio = r.listen(source)
    with open(path, "wb") as f:
        f.write(audio.get_wav_data())
    audio_file= open(path, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    return transcript['text']


def main_speech_to_text():
    path = "D:/AI_DANNY/functions/recording.wav"
    result = record_audio()
    os.remove(path=path)
    return result