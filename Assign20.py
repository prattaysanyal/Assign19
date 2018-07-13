#question1
from tkinter import *
root=Tk()
root.geometry("300x300")
root = Frame()
root.pack()

d = {"himant":123,"suresh":456,"chintu":789,"rohan":101,"hitman":8130,"creed":257,"Rajan":40,"monty":15,"anurag":420,"kartik":150,"nikki":4567,"goldy":98676}
widget1 = Label(root,text="Name")
widget1.pack(side=BOTTOM)
widget2 = Label(root,text="Phone Number")
widget2.pack(side=TOP)

def handleList(event):
    label = lst.get() 
    print(label)
    ph = d.get(label)
    global widget1,widget2
    widget1.config(text=label)
    widget2.config(text=ph)
    
lst = Listbox(root)
sbar = Scrollbar(root)
sbar.config(command=lst.yview) 
lst.config(yscrollcommand=sbar.set)
sbar.pack(side=RIGHT, fill=Y) 
lst.pack(side=LEFT,expand=YES, fill=BOTH)

lst.bind('<Double-1>', handleList)

for k,v in d.items():
    lst.insert('end',k)
root.mainloop()

#question2
from tkinter import *
root=Tk()
dictt={}
root.geometry("300x300")
use=Label(root,text="key")
use.pack()
useE=Entry(root)
useE.pack()
value=Label(root,text="value")
value.pack()
valueE=Entry(root)
valueE.pack()
lab1=Label(root)
lab1.pack()
lab2=Label(root)
lab2.pack()

def show():
    lab1.configure(text=useE.get())
    lab2.configure(text=valueE.get())
    

def get():
    r=Tk()
    r.geometry("300x300")
    k=useE.get()
    v=valueE.get()
    lab=Label(r)
    lab.pack()
    dictt.update({k:v})
    lab.configure(text=dictt)
    eB=Button(r,text="exit",font="none 15",command=r.destroy)
    eB.pack(side=BOTTOM)
    r.mainloop()
shB=Button(root,text="dictionary",command=show,font="none 15")
shB.pack()
buB=Button(root,text="add",command=get,font="none 15")
buB.pack()
exitB=Button(root,text="exit",font="none 15",command=root.destroy)
exitB.pack(side=BOTTOM)
root.mainloop()
    

