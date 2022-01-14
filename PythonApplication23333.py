def head1():
    global var_head
    global c
    if var_head.get()=="on":
        c.create_oval((15,15,450,450),fill="pink",outline="black")
        c.create_oval((125,100,175,150),fill="green")
        c.create_oval((250,100,300,150),fill="green")
        c.create_rectangle((250,250,200,200),fill="yellow")
        c.create_arc((100,350,350,350),outline="lightblue", style=CHORD, start=0, extent=150)
    elif var_head.get()=="off":
        c.create_oval((15,15,450,450),fill="white",outline="white")
        c.create_oval((125,100,175,150))
        c.create_oval((250,100,300,150))
        c.create_rectangle((250,250,200,200))
        c.create_arc((100,350,350,350), style=CHORD, start=0, extent=150,outline="black")

def lefteye1():
    global var_lefteye
    global c
    if var_lefteye.get()=="on":
        c.create_oval((125,100,175,150),fill="green")
    elif var_lefteye.get()=="off":
        c.create_oval((125,100,175,150),fill="pink",outline="pink")

def righteye1():
    global var_righteye
    global c
    if var_righteye.get()=="on":
        c.create_oval((250,100,300,150),fill="green")
    elif var_righteye.get()=="off":
       c.create_oval((250,100,300,150),fill="pink",outline="pink")

def nose1():
    global var_nose
    global c
    if var_nose.get()=="on":
        c.create_rectangle((250,250,200,200),fill="yellow")
    elif var_nose.get()=="off":
       c.create_rectangle((250,250,200,200),fill="pink",outline="pink")

def mouth1():
    global var_mouth
    global c
    if var_mouth.get()=="on":
        c.create_arc((100,350,350,350),outline="lightblue", style=CHORD, start=0, extent=150)
    elif var_mouth.get()=="off":
       c.create_arc((100,350,350,350),fill="pink",outline="pink", style=CHORD, start=0, extent=150,)
        
from tkinter import * 
tk = Tk()
fm=Frame(tk)
fm.pack(side=BOTTOM)
c = Canvas(tk, width=500, height=600, bg="white") 
c.create_oval((15,15,450,450),fill="pink")#Лицо
c.create_oval((125,100,175,150),fill="green")#Глаза
c.create_oval((250,100,300,150),fill="green")#Глаза
c.create_rectangle((250,250,200,200),fill="yellow")#нос
c.create_arc((100,350,350,350),outline="lightblue", style=CHORD, start=0, extent=150)#рот
c.pack()
var_head=StringVar()
head=Checkbutton(fm,text="Head",font="Arial 25",fg="red",variable=var_head,onvalue="on",offvalue="off",command=head1)
var_mouth=StringVar()
mouth=Checkbutton(fm,text="Mouth",font="Arial 25",fg="red",variable=var_mouth,onvalue="on",offvalue="off",command=mouth1)
var_lefteye=StringVar()
lefteye=Checkbutton(fm,text="Left Eye",font="Arial 25",fg="red",variable=var_lefteye,onvalue="on",offvalue="off",command=lefteye1)
var_nose=StringVar()
nose=Checkbutton(fm,text="Nose",font="Arial 25",fg="red",variable=var_nose,onvalue="on",offvalue="off",command=nose1)
var_righteye=StringVar()
righteye=Checkbutton(fm,text="Right eye",font="Arial 25",fg="red",variable=var_righteye,onvalue="on",offvalue="off",command=righteye1)
head.pack(side=TOP)
mouth.pack(side=TOP)
lefteye.pack(side=TOP)
righteye.pack(side=TOP)
nose.pack(side=TOP)

from tkinter import *
def kontroll():
    lbl.configure(text=v.get())
    if v.get()==1:
        print("esmaspäev")
    elif v.get()==2:
        print("teisipäev")


win=Tk()
win.title("Okno")
win.geometry("200x200")
v=IntVar()
v.set(1)
rad1=Radiobutton(win,text="Üks",variable=v,value=1,command=kontroll)
rad2=Radiobutton(win,text="Kaks", variable=v,value=2,command=kontroll)
lbl=Label(win, text="...")

rad1.pack()
rad2.pack()
lbl.pack()

win.mainloop()
tk.mainloop


