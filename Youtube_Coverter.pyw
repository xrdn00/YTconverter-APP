import customtkinter
from tkinter import *
from PIL import Image, ImageTk
from urllib.request import urlopen
from pytube import YouTube
import threading
import requests
import os
from tkinter import filedialog


from pytube. innertube import _default_clients

_default_clients[ "ANDROID"][ "context"]["client"]["clientVersion"] = "19.08.35"
_default_clients["IOS"]["context"]["client"]["clientVersion"] = "19.08.35"
_default_clients[ "ANDROID_EMBED"][ "context"][ "client"]["clientVersion"] = "19.08.35"
_default_clients[ "IOS_EMBED"][ "context"]["client"]["clientVersion"] = "19.08.35"
_default_clients["IOS_MUSIC"][ "context"]["client"]["clientVersion"] = "6.41"
_default_clients[ "ANDROID_MUSIC"] = _default_clients[ "ANDROID_CREATOR" ]



app = Tk()
dl_type = ''
#default directory
file_dir = f"{os.environ['UserProfile']}/Downloads"

"""FUNCTIONS INCLUDE Clipboard, Convert Button, Download Button and Options for dropdown menu"""

    
def clipboard():
    paste=app.clipboard_get()
    entry.delete(0,'end')
    entry.insert('end',paste)
def options(choice):
    print(choice)
    global dl_type
    dl_type = choice
    print(dl_type)
    if choice == 'Download Type':
        file_format.configure(text='File Format: ')
        button0.configure(state='disabled')
        button1.configure(state='disabled')
    elif choice == 'Audio Download':
        file_format.configure(text='File Format: MP4 (Audio)')
        button0.configure(state='normal')
    elif choice == 'Video Download':
        file_format.configure(text='File Format: MP4 (Video)')
        button0.configure(state='normal')

        


def convert():
    dl_progress.configure(text='')
    button0.configure(state='disabled')
    progressbar.set(0)
    download_percentage.configure(text='0 %')
    check = entry.get()
    def enable():
        button0.configure(state='normal')

    
    #Info
    def info_update():
        
        yt_url = entry.get()
        try:
            yt = YouTube(yt_url)
            
            
        except:
            print("NOT A YOUTUBE VIDEO exception error")
            def destroy_inv_url():
                

                invalid = customtkinter.CTkLabel(master=app,text="Invalid URL",text_color="red",fg_color="black",font=("Arial",50),width=853,height=480)
                invalid.place(x=102,y=102)
                
                def inv():
                    
                    invalid.destroy()
                app.after(1000,inv)
            destroy_inv_url()
            button1.configure(state='disabled')
            
        #image from url to pillow
        try:
            
            url=yt.thumbnail_url
            u = urlopen(url)
            raw_data = u.read()
            u.close()
            #853x480 or more image(cannot be resize)
            photo = ImageTk.PhotoImage(data = raw_data)

            t_info = yt.title
            vid_title.configure(text=t_info,font=('Arial',20),width=853,text_color='black') 
            thumbnail.configure(image=photo)
            button1.configure(state='normal')
            


        except:
            print("No thumbnail exception error and not a youtube website url")
            button1.configure(state='disabled')
            def destroy_inv_url():
                

                invalid = customtkinter.CTkLabel(master=app,text="Invalid URL",text_color="red",fg_color="black",font=("Arial",50),width=853,height=480)
                invalid.place(x=102,y=102)
                
                def inv():
                    
                    invalid.destroy()
                app.after(1000,inv)
            destroy_inv_url()
            button1.configure(state='disabled')
        
    try:
        #check internet connection
        request = requests.get(check)
    except:
        
        
        print("No Internet (Convert Button)")
        def destroy_inv_url():

            invalid = customtkinter.CTkLabel(master=app,text="No internet",text_color="red",fg_color="black",font=("Arial",50),width=855,height=482)
            invalid.place(x=102,y=102)
            
            def inv():
                invalid.destroy()
            app.after(1000,inv)
        destroy_inv_url()
        button1.configure(state='disabled')

            
    
                
                
               
    
                
    app.after(3000,enable)            
    x = threading.Thread(target=info_update)
    x.start()


    
def download():
    dl_progress.configure(text='Downloading')
    
    

    try:

        yt_url = entry.get()
        yt = YouTube(yt_url,on_progress_callback=on_progress)
        button_title = yt.title
        
       
        def Download():

            if 'Audio Download' in dl_type:
                
                print('Downloading Audio')
                mp4 = yt.streams.get_by_itag(140)
                mp4.download(output_path=file_dir)
            if 'Video Download' in dl_type:
                print('Downloading Vid')
                vid = yt.streams.get_highest_resolution()
                vid.download(output_path=file_dir)
            
                
        start_download = threading.Thread(target=Download)
        start_download.start()
        
        button0.configure(state='disabled')
        button1.configure(state='disabled')
        progressbar.set(0)

    except:
        
        def destroy_inv_url():
            print('No internet(Download Button)')
            invalid = customtkinter.CTkLabel(master=app,text="No internet",text_color="red",fg_color="black",font=("Arial",50),width=853,height=480)
            invalid.place(x=102,y=102)
            def inv():
                invalid.destroy()
            app.after(1000,inv)
        destroy_inv_url()
        button1.configure(state='disabled')
        



def on_progress(stream,chunk,bytes_remaining):
    
    
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    percent = str(int(percentage_of_completion))
    download_percentage.configure(text=percent+' %')
    download_percentage.update()

    
    progressbar.set(float(percentage_of_completion)/100)
    if '100' in percent:
        button0.configure(state='normal')
        dl_progress.configure(text='Download Complete.')
    
def save():
    global file_dir
    dir_name = filedialog.askdirectory()
    os.chdir(dir_name)
    curr_dir = os.getcwd()
    file_dir = curr_dir
    print(curr_dir)
    file_directory.configure(text="File Directory: {}".format(file_dir))


#app
app.title("Youtube Converter")

screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
app_width = 1800
app_height = 800
x = (screen_width/2) - (app_width/2)
y = (screen_height/2) - (app_height/2)
app.geometry("{}x{}+{}+{}".format(app_width,app_height,int(x),int(y)))
#widgets

entry = customtkinter.CTkEntry(master = app,width = 400,height=25,corner_radius=0)
entry.place(x=100,y=600)
menu = customtkinter.CTkOptionMenu(master = app,values=["Download Type","Audio Download","Video Download"],corner_radius=10,button_color = 'gray',fg_color = "gray",button_hover_color = "black",dropdown_fg_color='black',dropdown_hover_color = "gray",command=options)
menu.place(x=10,y=10)
button0 = customtkinter.CTkButton(master = app,text = "Convert",text_color="white",height = 25,width = 70,corner_radius=5, command=convert, fg_color="gray",hover_color='black',state='disabled')
button0.place(x=100,y=650)
button1 = customtkinter.CTkButton(master = app,text = "Download",text_color="white",height = 25,width = 70,corner_radius=5,command=download,fg_color="gray",hover_color='black',state='disabled')
button1.place(x=100,y=700)
button2 = customtkinter.CTkButton(master=app,text='Paste',font=('Arial',13),fg_color='gray',width=50,height=20,hover_color='black',command=clipboard,corner_radius=3)
button2.place(x=520,y=601)
vid_title = customtkinter.CTkLabel(master=app,text='',font=('Arial',20),width=853,text_color='black')
vid_title.place(x=101,y=70)
canvas = customtkinter.CTkCanvas(master=app,width=853,height=480,bg='black',highlightthickness=0)
canvas.place(x=100,y=100)

thumbnail = customtkinter.CTkLabel(master=canvas,text='')
thumbnail.place(x=0,y=0)



download_label = customtkinter.CTkLabel(master=app,text='Download Progress: ',font=('Arial',20),text_color='black')
download_label.place(x=1200,y=100)

download_percentage = customtkinter.CTkLabel(master=app,text='0 %',font=('Arial',20),text_color='black')
download_percentage.place(x=1200,y=150)


progressbar = customtkinter.CTkProgressBar(master = app,width=500,height=20,progress_color = 'green')
progressbar.set(0)
progressbar.place(x=1200,y=200)

dl_progress = customtkinter.CTkLabel(master = app,text='',width = 100,height=20,font=('Arial',10),text_color = 'green')
dl_progress.place(x=1200,y=235)

file_format = customtkinter.CTkLabel(master=app,text='File Format: ',font=('Arial',20),text_color='black')
file_format.place(x=1200,y=300)

file_directory = customtkinter.CTkLabel(master = app,text='File Directory: {}'.format(file_dir),font=('Arial',20),text_color='black')
file_directory.place(x=1200,y=350)

save = customtkinter.CTkButton(master=app,text = 'Change file directory',font=('Arial',15),text_color = 'white',fg_color = "gray",hover_color='black',command=save,width = 50,height=20)
save.place(x=1200,y=400)













#shift app to app=Tk() to take effect
icon = PhotoImage(file = 'yt_icon1.png')
app.iconphoto(False, icon)




app.mainloop()

