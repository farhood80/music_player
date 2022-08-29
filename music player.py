from tkinter import *
from pygame import mixer
import os

def play():
    current_song = playlist.get(ACTIVE)
    print(current_song)
    mixer.music.load(current_song)
    mixer.music.play()

def pause():
    mixer.music.pause()

def stop():
    mixer.music.stop()

 def resume():
     mixer.music.unpause()


root = Tk()
root.title("simple music player")
mixer.init()
playlist = Listbox(root,selectmode=SINGLE,bg="green")
playlist.grid(columnspan=5)
os.chdir('/song')
song = os.listdir()
for x in song:playlist.insert(END,5)
Button(root,text="play", COMMAND=play).grid(row =1,column=0)
Button(root,text="pause", COMMAND=pause).grid(row =1,column=1)
Button(root,text="stop", COMMAND=stop).grid(row =1,column=2)
Button(root,text="resume", COMMAND=resume).grid(row =1,column=3)
mainloop()


