from tkinter import *
from tkinter import messagebox,filedialog
from pytube import YouTube

def download_video(url,file_path,file_extension):
    try:
        video = YouTube(url)
        stream = video.streams.filter(progressive=True,file_extension=str(file_extension))
        highest_res_stream = stream.get_highest_resolution()
        highest_res_stream.download(output_path=file_path)
    except Exception as e:
        messagebox.showerror("Error !!",e)

file_path = None
root = Tk()
root.title("YouTube Video Downloader")
root.geometry("350x110")
root.iconbitmap("icon.ico")
var = StringVar()
Label1 = Label(root,text="Url: ").grid(row=0,column=0) 
Entry1 = Entry(root,textvariable=var).grid(row=0,column=1)

var2 = StringVar()
Label2= Label(root,text="File Path").grid(row=1,column=0) 
Entry2 = Entry(root,textvariable=var2).grid(row=1,column=1)
def open():
    global file_path
    file_path = filedialog.askopenfilename()
    var2.set(file_path)
btn2 = Button(root,text="Browse",command=open).grid(row=1,column=2)
clicked =StringVar()
Options = [
    "mp4",
    "mov"
]
clicked.set("mp4")
label3 = Label(root,text="File Extension: ").grid(row=2,column=0)
drop = OptionMenu(root,clicked,*Options).grid(row=2,column=1)

btn3 = Button(root,text="Save",command=lambda: download_video(str(var.get()),str(file_path),str(var2.get()))).grid(row=3,column=0)




def Credit():
    messagebox.showinfo("Credits","ALL credits belong to AGNEAY B NAIR")
btn = Button(text="Credits",command=Credit).grid(row=3,column=1)
root.mainloop()