import speech_recognition as sr

# Создаем объект Recognizer класса
r = sr.Recognizer()

# Задаем микрофон как источник звука
with sr.Microphone() as source:
    # Устанавливаем уровень шума для корректной работы
    r.adjust_for_ambient_noise(source)
    
    # Просим пользователя что-то сказать
    print("Говорите...")
    # Слушаем микрофон и записываем аудио в объект
    audio = r.listen(source)

# Используем Google Speech Recognition для распознавания речи
try:
    # Pass audio to Google Speech Recognition for transcription
    text = r.recognize_google(audio, language="ru-RU")
    print("Вы сказали: " + text)

except sr.UnknownValueError:
    print("Не удалось распознать речь")

except sr.RequestError as e:
    print("Ошибка сервиса {0}".format(e))
