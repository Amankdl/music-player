import os
import pygame
from tkinter.filedialog import askdirectory
from tkinter import *

window = Tk()
window.iconbitmap("icon.ico")
window.minsize(width=400,height=500)
window.maxsize(width=400,height=500)
window.title("Sangeet v1.0")
songList = Listbox(window)
songList.grid(padx=20,pady=40)

browseImage = PhotoImage(file="monito.png")
playImage = PhotoImage(file="play.png")
previousImage = PhotoImage(file="previous.png")
nextImage = PhotoImage(file="skip.png")
stopImage = PhotoImage(file="stop.png")
exitImage = PhotoImage(file="exit.png")

song_list = []
i = 0

#browseFunction
def browse():
    pygame.mixer.init()
    directory = askdirectory()
    os.chdir(directory)
    for file in os.listdir(directory):
        if file.endswith(".mp3"):
           song_list.append(file)
    song_list.reverse()
    for x in song_list:
        songList.insert(0,x)
browseButton = Button(image=browseImage,command=browse)
browseButton.grid(row = 1,column = 11)

#forPlay
def play():
    pygame.mixer.music.load(song_list[i])
    pygame.mixer.music.play()
playButton = Button(image=playImage,command=play)
playButton.grid(row = 2,column = 11)


#forPreviousSong
def previous():
    global i
    if i==0:
        pygame.mixer.music.load(song_list[0])
        pygame.mixer.music.play()
    else:
        i = i-1
        pygame.mixer.music.load(song_list[i])
        pygame.mixer.music.play()
previousButton = Button(image=previousImage,command=previous)
previousButton.grid(row = 2,column = 10)


#forNextSong
def next():
    global i
    i = i+1
    if i < len(song_list):
        pygame.mixer.music.load(song_list[i])
        pygame.mixer.music.play()
    else:
        i = 0
        pygame.mixer.music.load(song_list[-1])
        pygame.mixer.music.play()
nextButton = Button(image=nextImage,command=next)
nextButton.grid(row = 2,column = 14)


#forStop
def stop():
    pygame.mixer.music.stop()
stopButton = Button(image=stopImage,command=stop)
stopButton.grid(row = 1,column = 10)


#forExit
def quit():
    exit()
exitButton = Button(image=exitImage,command=quit)
exitButton.grid(row =1,column = 14)
window.mainloop()
