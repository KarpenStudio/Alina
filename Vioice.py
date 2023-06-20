import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 165)
engine.setProperty('volume', 150.0)
engine.say("Привет я Алина я голосовой асистент!")
engine.runAndWait()