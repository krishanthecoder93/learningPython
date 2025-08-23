from gtts import gTTS
import os

text = open("inputfile.txt",'r').read()
language = 'hi'
output = gTTS(text = text, lang=language,slow = False)
output.save('fileoutput.mp3')
os.system("afplay fileoutput.mp3")