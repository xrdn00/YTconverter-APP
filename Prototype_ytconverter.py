from pytube import YouTube
from tkinter import *



app = Tk()
app.geometry('500x100')
app.title('yt converter')
def dl_audio():
    url = entry.get()
    yt = YouTube(url)
    audio = yt.streams.get_by_itag(140)
    audio.download()
def dl_vid():
    url = entry.get()
    yt = YouTube(url)
    vid = yt.streams.get_highest_resolution()
    vid.download()
    
entry = Entry(app,width = 100)
entry.pack()

button1 = Button(app,text = 'Download Audio',command = dl_audio)
button1.pack()
button2 = Button(app,text = 'Download Video',command = dl_vid)
button2.pack()

app.mainloop()
