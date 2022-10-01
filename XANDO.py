#A small code by abhishek(just a simple X and O game)
#thank you for having a glance at it
from ast import Delete, main
from cProfile import label
from glob import glob
from html.entities import name2codepoint
from pickle import FRAME
from re import T
from sqlite3 import Row
from tkinter import *
from tkinter import colorchooser
from tkinter import commondialog
from tkinter import messagebox
from tkinter.font import BOLD
from tkinter.tix import COLUMN, ROW
from tracemalloc import start
from turtle import bgcolor, left
from unicodedata import name

#to get opponet names
def get_opo_names():
    global name11,name22
    name11 = entry_1.get()
    name22 = entry_2.get()

   

#the function to show winner  and its logic function
def showwin():
        get_opo_names()
        values = [bt1["text"],bt2["text"],bt3["text"],bt4["text"],bt5["text"],bt6["text"],bt7["text"],bt8["text"],bt9["text"]]
        #possibilites of x's
        if    values[0]=="X" and values[1]=="X" and values[2]=="X":
            messagebox.showinfo("winner"," {} won thw match".format(name11))
        elif   values[0]=="X" and values[3]=="X" and values[6]=="X":
            messagebox.showinfo("winner","{} won thw match".format(name11))
        elif   values[0]== "X" and values[4]== "X" and values[8]== "X":
            messagebox.showinfo("winner","{} won thw match".format(name11))
        elif   values[3]== "X" and values[4]== "X" and values[5]== "X":
            messagebox.showinfo("winner","{} won thw match".format(name11))
        elif   values[6]== "X" and values[7]== "X" and values[8]== "X":
            messagebox.showinfo("winner","{} won thw match".format(name11))
        elif   values[2]== "X" and values[4]== "X" and values[6]== "X":
            messagebox.showinfo("winner","{} won thw match".format(name11))
        elif   values[1]== "X" and values[4]== "X" and values[7]== "X":
            messagebox.showinfo("winner","{} won thw match".format(name11))
        elif   values[2]== "X" and values[5]== "X" and values[8]== "X":
            messagebox.showinfo("winner","{} won thw match".format(name11))
        
        #possibilities of O's'''

        if values[0]== "O" and values[1]== "O" and values[2]== "O":
                messagebox.showinfo("winner"," {} won thw match".format(name22))
        elif   values[0]== "O" and values[3]== "O" and values[6]== "O":
            messagebox.showinfo("winner","{} won thw match".format(name22))
        elif   values[0]== "O" and values[4]== "O" and values[8]== "O":
            messagebox.showinfo("winner","{} won thw match".format(name22))
        elif  values[3]== "O" and values[4]== "O" and values[5]== "O":
            messagebox.showinfo("winner","{} won thw match".format(name22))
        elif   values[6]== "O" and values[7]== "O" and values[8]== "O":
            messagebox.showinfo("winner","{} won thw match".format(name22))
        elif   values[2]== "O" and values[4]== "O" and values[6]== "O":
            messagebox.showinfo("winner","{} won thw match".format(name22))
        elif  values[1]== "O" and values[4]== "O" and values[7]== "O":
            messagebox.showinfo("winner","{} won thw match".format(name22))
        elif   values[2]== "O" and values[5]== "O" and values[8]== "O":
            messagebox.showinfo("winner","{} won thw match".format(name22))
        
#event for start button
def start():
    mesage=messagebox.showinfo("start","Let's Begun the game")

#to destry a window
def win_destry():
    window.destroy()

#for restart button (event to retsart window)
def restart():
    win_destry()
    guistart()

#starting of window
def guistart():
    global window,bt1,bt2,bt3,bt4,bt5,bt6,bt7,bt8,bt9,btstrt,bteval,btrestrt
    window = Tk()
    frame0 = Frame(window,bg="#adedd7")
    frame0.pack()
    frame1 = Frame(window,padx=30,pady=30,bg="#adedd7")
    frame1.pack()
    frame2 = Frame(window,padx=20,pady=20)
    frame2.pack()


#label for title 
    labeT = Label(frame0,text="X AND O GAME",font=("Simplifica"),bg="#adedd7")
    frame1.pack()
    labeT.pack()
##labels for entering names of opponents
    lable_opponent1 = Label(frame2,text ="Enter Name(opponent 1)[x]")
    lable_opponent1.grid(row=1,column=0)

    global entry_1
    entry_1 = Entry(frame2)
    entry_1.grid(row=2,column=0)

    lable_opponent2 = Label(frame2,text ="Enter Name(opponent 2)[0]")
    lable_opponent2.grid(row=3,column=0)

    global entry_2
    entry_2 = Entry(frame2)
    entry_2.grid(row=4,column=0)
#######

##creating a button for start
    btstrt = Button(frame2,text='START',font=("JerseyM54Font"),bg="#55faa5",command=start)
    btstrt.grid(row=5,column=0)
    btrestrt = Button(frame2,text='RESTART',font=("JerseyM54Font"),bg="#55faa5",command=restart)
    btrestrt.grid(row=6,column=0)

##creating a button to insert values in box
    bteval = Button(frame2,text='CLICK TO INSERT VALUE IN THE BOX',font=("JerseyM54Font"),bg="#32558a",command=Entervalue)
    bteval.grid(row=0,column=0)

#creating boxes with buttons
    bt1 = Button(frame1,text='  ',font=("JerseyM54Font"),bg="white",padx=10,pady=5,command=click1)
    bt1.grid(row=0,column=0)
    bt2 = Button(frame1,text='  ',font=("JerseyM54Font"),bg="white",padx=10,pady=5,command=click2)
    bt2.grid(row=0,column=1)
    bt3 = Button(frame1,text='  ',font=("JerseyM54Font"),bg="white",padx=10,pady=5,command=click3)
    bt3.grid(row=0,column=2)
    bt4 = Button(frame1,text='  ',font=("JerseyM54Font"),bg="white",padx=10,pady=5,command=click4)
    bt4.grid(row=1,column=0)
    bt5 = Button(frame1,text='  ',font=("JerseyM54Font"),bg= "white",padx=10,pady=5,command=click5)
    bt5.grid(row=1,column=1)
    bt6 = Button(frame1,text='  ',font=("JerseyM54Font"),bg= "white",padx=10,pady=5,command=click6)
    bt6.grid(row=1,column=2)
    bt7 = Button(frame1,text='  ',font=("JerseyM54Font"),bg= "white",padx=10,pady=5,command=click7)
    bt7.grid(row=2,column=0)
    bt8 = Button(frame1,text='  ',font=("JerseyM54Font"),bg= "white",padx=10,pady=5,command=click8)
    bt8.grid(row=2,column=1)
    bt9 = Button(frame1,text='  ',font=("JerseyM54Font"),bg= "white",padx=10,pady=5,command=click9)
    bt9.grid(row=2,column=2)
    window.geometry("620x520")
    window.title("X AND O GAME")
    window.configure(bg="#adedd7")
    window.mainloop()

#event for inserting values in box button   
def Entervalue():
    poupwin()

##creating a event for pop up window
def poupwin():
  
    global top  
    top= Toplevel(window)
    top.geometry("380x140")
    lable3=Label(top,text="Enter X or O")
    lable3.pack()
    global entry
    entry= Entry(top, width= 25)
    entry.pack()
    ibtn=Button(top,text="close",command=close)
    ibtn.pack()
    lable3=Label(top,text="AFTER ENTERING CLICK ON A DESIRED BOX TO INSERT VALUE IN IT")
    lable3.pack() 
    
    ##

#event function for closing popup window
def close():
    top.destroy()

#creating 9 click functions for 9 buttons
def click1():
    ipt =entry.get()
    bt1['text']=ipt
    close()
    showwin()
def click2():
    ipt=entry.get()
    bt2['text']=ipt
    close()
    showwin()
def click3():
    ipt=entry.get()
    bt3['text']=ipt
    close()
    showwin()
def click4():
    ipt=entry.get()
    bt4['text']=ipt
    close()
    showwin()
def click5():
    ipt=entry.get()
    bt5['text']=ipt
    close()
    showwin()
def click6():
    ipt=entry.get()
    bt6['text']=ipt
    close()
    showwin()
def click7():
    ipt=entry.get()
    bt7['text']=ipt
    close()
    showwin()
def click8():
    ipt=entry.get()
    bt8['text']=ipt
    close()
    showwin()
def click9():
    ipt=entry.get()
    bt9['text']=ipt
    close()
    showwin()

####just creating a refernce maqinfunction
def main():
    guistart()

##actual main function
if __name__=="__main__":
    main()
   