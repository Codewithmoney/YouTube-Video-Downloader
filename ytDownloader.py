# importing all the nessacary stuff
from tkinter import *
from tkinter import filedialog as fldg
import pytube
import threading

# all the function
def videoDownloader(PATH):
    try:
        url = urlBox.get()
        pytube.YouTube(url).streams.first().download(PATH)
    except Exception as e:
        print(f'Sorry !!! Think that you won\'t have internet connection and the error = [{e}]')


def fileToDownload():
    filePATH = fldg.askdirectory()
    thread = threading.Thread(target = videoDownloader, args=(filePATH, ))
    thread.daemon = 1
    thread.start()

# creating the window and setting it up
root = Tk()
root.title("MoneyCademy - YouTube Video Downloader")
root.geometry("350x200")
root.resizable(0, 0)
root.configure(bg = "#01030d")

# main activity starts here
heading = Label(root, 
                text = "YouTube Video Downloader", 
                bg = "#01030d", 
                fg = "#fff", 
                font = "Dungeon 17 normal")
heading.pack(fill = X, pady = 7)

urlBox = Entry(root, 
                bg = "#232332", 
                fg = "#ff9dea", 
                font = "Verdana 20 normal")
urlBox.pack(fill = X, pady = 10)

downlaodBtn = Button(root, 
                    text = "Download", 
                    bg = "#202021", 
                    fg = "#fff", 
                    font = "Forte 17 normal", 
                    command = fileToDownload)
downlaodBtn.pack(padx = 4, pady = 30)

# looping the root
root.mainloop()
