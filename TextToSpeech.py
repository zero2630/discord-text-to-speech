from gtts import gTTS
import os

text = "Тест синтеза речи"
language = 'ru'

def Speak(text):
    speech = gTTS(text = text, lang = language, slow = False)
    speech.save("text.mp3")