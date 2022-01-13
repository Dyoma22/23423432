#Пример 1

from tkinter import * 
tk = Tk() 
c = Canvas(tk, width=500, height=500, bg="white") 
c.create_oval((0,0,90,90))#Лицо
c.create_oval((25,20,35,30))#Глаза
c.create_oval((50,20,60,30))#Глаза
c.create_arc((20,40,70,70))#нос
c.create_arc((20,70,70,70), style=CHORD, start=0, extent=150)#рот
c.pack() 
tk.mainloop() 

from tkinter import *
def kontroll():
    lbl.configure(text=v.get())
    if v.get()==1:
        print("esmaspäev")
    elif v.get()==2:
        print("teisipäev")

        
    #...
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


