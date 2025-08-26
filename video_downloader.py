from tkinter import *
from tkinter import filedialog
#from pytube import YouTube
from pytubefix import YouTube
from moviepy.editor import *
import shutil



def download():
    video_path = url_entry.get()
    file_path = path_label.cget("text")
    print("downloading......")
    mp4 = YouTube(video_path).streams.get_highest_resolution().download()
    video_clip = VideoFileClip(mp4)
    

    #Code for mp3
    audio_file = video_clip.audio
    audio_filename = audio_entry.get()
    audio_file.write_audiofile(audio_filename)
    audio_file.close()
    shutil.move(audio_filename, file_path)


    video_clip.close()
    shutil.move(mp4, file_path)
    print("Download complete")


def get_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)


root = Tk()
root.title('Video Downloader')

canvas = Canvas(root,width=400,height=300)
canvas.pack()


#app label
app_label = Label(root,text= "vidoe Downloader",fg= 'blue',font=('Arial,20') )
canvas.create_window(200,20,window = app_label)

#entry to accept to video url
url_label = Label(root,text=" Enter Video URL")
url_entry = Entry(root)
canvas.create_window(200,80,window = url_label)
canvas.create_window(200,120,window = url_entry)
audio_label = Label(root,text=" Enter audio file name")
canvas.create_window(200,200,window = audio_label)
audio_entry = Entry(root) 
canvas.create_window(200,220,window = audio_entry)


#path to download video
path_label= Label(root,text= "Select path to download")
path_button = Button(root,text='Select',command=get_path)
canvas.create_window(200,140,window = path_label)
canvas.create_window(200,170,window = path_button)

#download button
download_button =Button(root,text='Download',command=download)
canvas.create_window(200,250,window = download_button)
root.mainloop()