from tkinter import *
from tkinter import filedialog
root=Tk()
root.title("Addition")
root.minsize(650,650)
root.maxsize(650,650)
from PIL import ImageTk, Image
from tkinter import messagebox
import os
open_ING=ImageTk.PhotoImage(Image.open("open.png"))
save_ING=ImageTk.PhotoImage(Image.open("save.png"))
exit_ING=ImageTk.PhotoImage(Image.open("exit.jpg"))

Label_name=Label(root,text="file name")
Label_name.place(relx=0.28,rely=0.03, anchor=CENTER)

input_name=Entry(root)
input_name.place(relx=0.46,rely=0.03, anchor=CENTER)

my_Text=Text(root,height=40,width=80)
my_Text.place(relx=0.5,rely=0.05,anchor=CENTER)

open_button=Button(root,image=open_ING,text="open file")
open_button.place(relx=0.05,rely=0.03,anchor=CENTER)

name = ""
def openFile():
    global name
    my_Text.delete(1.0, END)
    input_name.delete(0, END)
    text_file = filedialog.askopenfilename(title=" Open Text File",
                                           filetypes=(("Text Files," ".txt"),))
    print(text_file)
    name = os.path.basename(text_file)
    formated_name = name.split('.')[0]
    input_name.insert(END,formated_name)
    root.title(formated_name)
    text_file = open(name,'r')
    paragraph=text_file.read()
    my_Text.insert(END,paragraph)
    text_file.close()
def saveFile():
    input_file=input_name.get()
    file=open(input_file+".txt","w")
    data=my_Text.get(1.0,END)
    print(data)
    file.write(data)
    input_name.delete(0,END)
    my_Text.delete(1.0,END)
    messagebox.showinfo("update","success")
def closewindow():
    root.destroy()
open_button=Button(root,image=open_ING,command = openFile)
open_button.place(relx=0.05,rely=0.03,anchor=CENTER)
save_button=Button(root,image=save_ING,command =saveFile)
save_button.place(relx=0.11,rely=0.03,anchor=CENTER)
exit_button=Button(root,image=exit_ING,command = closewindow)
exit_button.place(relx=0.17,rely=0.03,anchor=CENTER)
root.mainloop()