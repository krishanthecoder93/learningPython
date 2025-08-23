from gtts import gTTS
import os
from tkinter import *
root = Tk()
canvas = Canvas(root,width=400,height=300)
canvas.pack()

def textTOSpeech():
    text = entry.get()
    language = 'en'
    output = gTTS(text=text,lang=language,slow=False)
    output.save('output.mp3')
    os.system("afplay output.mp3")


entry = Entry(root)
canvas.create_window(200,180,window=entry)

button = Button(text="Start",command=textTOSpeech)
canvas.create_window(200,230,window=button)

root.mainloop()