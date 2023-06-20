import speech_recognition as sr
import pyttsx3
import subprocess

calc = 'C:\\Windows\\System32\\calc.exe'
ege = 'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
sublime = 'C:\Program Files\Sublime Text 3\sublime_text.exe'
enex = 'C:\Program Files (x86)\Internet Explorer\iexplore.exe'

# Создаем объект Recognizer класса
r = sr.Recognizer()

# Задаем микрофон как источник звука
with sr.Microphone() as source:
    # Устанавливаем уровень шума для корректной работы
    r.adjust_for_ambient_noise(source)
    
    # Просим пользователя что-то сказать
    print("Говорите...")
    engine = pyttsx3.init()
    engine.setProperty('rate', 165)
    engine.setProperty('volume', 150.0)
    engine.say("Говорите")
    engine.runAndWait()
    # Слушаем микрофон и записываем аудио в объект
    audio = r.listen(source)

# Используем Google Speech Recognition для распознавания речи
try:
    # Pass audio to Google Speech Recognition for transcription
    text = r.recognize_google(audio, language="ru-RU")
    print(text)

    if text == 'Привет':
        engine = pyttsx3.init()
        engine.setProperty('rate', 165)
        engine.setProperty('volume', 150.0)
        engine.say("Привет я Алина я голосовой асистент!")
        engine.runAndWait()

    elif text == 'Как дела':
        engine = pyttsx3.init()
        engine.setProperty('rate', 165)
        engine.setProperty('volume', 150.0)
        engine.say("У меня все хорошо! А у вас как?")
        engine.runAndWait()
        
    elif text == 'Запусти осла':
        engine = pyttsx3.init()
        engine.setProperty('rate', 165)
        engine.setProperty('volume', 150.0)
        engine.say("Запускаю")
        engine.runAndWait()


except sr.UnknownValueError:
    print("Не удалось распознать речь")

except sr.RequestError as e:
    print("Ошибка сервиса {0}".format(e))
