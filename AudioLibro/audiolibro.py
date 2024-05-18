from gtts import gTTS

file = open("./Audiolibro/libro.txt", "r", encoding="utf8")
textBook= file.read()

file.close()

audio = gTTS(text=textBook, lang="es")
audio.save("./Audiolibro/audio.mp3")

