#Пример 1

from tkinter import * 
tk = Tk()
fm=Frame(tk)
fm.pack(side=BOTTOM)
c = Canvas(tk, width=500, height=600, bg="white") 
c.create_oval((15,15,450,450))#Лицо
c.create_oval((125,100,175,150))#Глаза
c.create_oval((250,100,300,150))#Глаза
c.create_arc((175,200,350,350))#нос
c.create_arc((100,350,350,350), style=CHORD, start=0, extent=150)#рот
c.pack() 
head=Checkbutton(fm,text="Head",font="Arial 25",fg="lightblue")
mouth=Checkbutton(fm,text="Mouth",font="Arial 25",fg="lightblue")
lefteye=Checkbutton(fm,text="Left Eye",font="Arial 25",fg="lightblue")
nose=Checkbutton(fm,text="Nose",font="Arial 25",fg="lightblue")
righteye=Checkbutton(fm,text="Right eye",font="Arial 25",fg="lightblue")
head.pack(side=TOP)
head.pack(side=TOP)
head.pack(side=TOP)
head.pack(side=TOP)
head.pack(side=TOP)

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


