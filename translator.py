#from cProfile import label
#from fnmatch import translate
from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD 
from googletrans import Translator,LANGUAGES

def change(text="type", src="English", dest="Hindi"):
    text1=text
    src1=src
    dest1=dest
    trans = Translator()
    trans1 = trans.translate(text,src=src1,dest=dest1)
    return trans1.text

def data():
    s = comb_sor.get()
    d = comb_dest.get()
    masg = Sor_txt.get(1.0,END)
    textget = change(text = masg, src=s, dest=d)
    dest_txt.delete(1.0,END)
    dest_txt.insert(END,textget)

root = Tk()
root.title("Translator")
root.geometry("500x700")#give the size of window
root.config(bg="gray")

lab_txt=Label(root,text="Transalator",font=("Time New Roman",20,BOLD))
lab_txt.place(x=100,y=40,height=50,width=300)#size of translator word 

frame = Frame(root).pack(side=BOTTOM)
lab_txt=Label(root,text="Source txt",font=("Time New Roman",20,BOLD),fg="Black",bg="Gray")
lab_txt.place(x=100,y=100,height=20,width=300)#size of translator word 

Sor_txt = Text(frame,font=("Time New Roman",20,BOLD),wrap=WORD)
Sor_txt.place(x=10,y=130,height=150,width=480)

list_text =list(LANGUAGES.values())#to get diff languages from the list
 
comb_sor = ttk.Combobox(frame,value=list_text)
comb_sor.place(x=10,y=300,height=40,width=150)
comb_sor.set("english")

button_change = Button(frame,text="Translate",relief=RAISED,command=data)#RAISED is for click the button
button_change.place(x=170,y=300,height=40,width=150)

comb_dest = ttk.Combobox(frame,value=list_text)
comb_dest.place(x=330,y=300,height=40,width=150)
comb_dest.set("english")

lab_txt=Label(root,text="Dest txt",font=("Time New Roman",20,BOLD),fg="Black",bg="Gray")
lab_txt.place(x=100,y=360,height=20,width=300)

dest_txt = Text(frame,font=("Time New Roman",20,BOLD),wrap=WORD)
dest_txt.place(x=10,y=400,height=150,width=480)


root.mainloop(0)