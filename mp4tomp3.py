import os
from moviepy.editor import *
import tkinter

def convert():
    path_to_mp4 = entry.get()
    path_to_mp3 = entry2.get()
    video = VideoFileClip(os.path.join(path_to_mp4))
    video.audio.write_audiofile(os.path.join(path_to_mp3))
    msg_splash = tkinter.Tk()
    msg_splash.title("MSG Splash")
    l = tkinter.Label(msg_splash, text="Filed saved to " + path_to_mp3)
    l.pack()
    m = tkinter.Button(msg_splash, text='Ok', command=msg_splash.destroy)
    m.pack()

root = tkinter.Tk()
root['background']='grey'
root.title("Mp3 to Mp4 Converter")
root.geometry('218x150')

l = tkinter.Label(root, text='Mp4 to Mp3 Converter', bg='grey')
l.pack()
l = tkinter.Label(root, text='Path to mp4 file', bg='grey')
l.place(x=0,y=30)
entry = tkinter.Entry(width=30)
entry.place(x=0, y=50)
l = tkinter.Label(root, text='Path to mp3 file (with .mp3)', bg='grey')
l.place(x=0,y=70)
entry2 = tkinter.Entry(width=30)
entry2.place(x=0, y=93)
m = tkinter.Button(root, text = 'Convert', command=convert, bg='grey')
m.place(x=0,y=118)
m = tkinter.Button(root, text = 'Exit', command=exit, bg='grey')
m.place(x=70,y=118)
root.mainloop()