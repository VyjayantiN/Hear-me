from gtts import gTTS
import os
mytext="Welcome to HearMe. Here is a great platform which could help you listen to the text without having the need of reading"
language = 'te'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("welcome.mp3")
os.system("welcome.mp3")
