from tkinter import *
from tkinter.ttk import *
import time

global frame

# ***************
# NEXT BUTTON 
# prompt for burst time for each process
# Open new window with animations 
# ***************
def nxt():
    global process, p1bt_entry, p2bt_entry, p3bt_entry, q_entry, p1ac_entry, p2ac_entry, p3ac_entry
    process = combo.get()

    if process == "1":
        p1ac_lb = Label(window, text = "Enter Arrival Time for Process 1: ", font=('Times New Roman', 15), background='#f6ead4' )
        p1ac_lb.place(x=0, y= 110)
        p1ac_entry = Entry(window, width = 10)
        p1ac_entry.place(x=280, y= 110)
        p1bt_lb = Label(window, text = "Enter Burst Time for Process 1: ", font=('Times New Roman', 15), background='#f6ead4' )
        p1bt_lb.place(x=370, y= 110)
        p1bt_entry = Entry(window, width = 10)
        p1bt_entry.place(x=630, y= 110)

        q_lb = Label(window, text = "Enter quantum: ", font=('Times New Roman', 15), background='#f6ead4')
        q_lb.place(x = 0, y = 150)
        q_entry = Entry(window, width = 10)
        q_entry.place(x = 280, y = 150)
    if process == "2":
        p1ac_lb = Label(window, text = "Enter Arrival Time for Process 1: ", font=('Times New Roman', 15), background='#f6ead4' )
        p1ac_lb.place(x=0, y= 110)
        p1ac_entry = Entry(window, width = 10)
        p1ac_entry.place(x=280, y= 110)
        p1bt_lb = Label(window, text = "Enter Burst Time for Process 1: ", font=('Times New Roman', 15), background='#f6ead4' )
        p1bt_lb.place(x=370, y= 110)
        p1bt_entry = Entry(window, width = 10)
        p1bt_entry.place(x=630, y= 110)

        p2ac_lb = Label(window, text = "Enter Arrival Time for Process 2: ", font=('Times New Roman', 15), background='#f6ead4' )
        p2ac_lb.place(x=0, y= 150)
        p2ac_entry = Entry(window, width = 10)
        p2ac_entry.place(x=280, y= 150)
        p2bt_lb = Label(window, text = "Enter Burst Time for Process 2: ", font=('Times New Roman', 15), background='#f6ead4' )
        p2bt_lb.place(x=370, y= 150)
        p2bt_entry = Entry(window, width = 10)
        p2bt_entry.place(x=630, y= 150)

        q_lb = Label(window, text = "Enter quantum: ", font=('Times New Roman', 15), background='#f6ead4')
        q_lb.place(x = 0, y = 190)
        q_entry = Entry(window, width = 10)
        q_entry.place(x = 280, y = 190)

    if process == "3":
        p1ac_lb = Label(window, text = "Enter Arrival Time for Process 1: ", font=('Times New Roman', 15), background='#f6ead4' )
        p1ac_lb.place(x=0, y= 110)
        p1ac_entry = Entry(window, width = 10)
        p1ac_entry.place(x=280, y= 110)
        p1bt_lb = Label(window, text = "Enter Burst Time for Process 1: ", font=('Times New Roman', 15), background='#f6ead4' )
        p1bt_lb.place(x=370, y= 110)
        p1bt_entry = Entry(window, width = 10)
        p1bt_entry.place(x=630, y= 110)

        p2ac_lb = Label(window, text = "Enter Arrival Time for Process 2: ", font=('Times New Roman', 15), background='#f6ead4' )
        p2ac_lb.place(x=0, y= 150)
        p2ac_entry = Entry(window, width = 10)
        p2ac_entry.place(x=280, y= 150)
        p2bt_lb = Label(window, text = "Enter Burst Time for Process 2: ", font=('Times New Roman', 15), background='#f6ead4' )
        p2bt_lb.place(x=370, y= 150)
        p2bt_entry = Entry(window, width = 10)
        p2bt_entry.place(x=630, y= 150)

        p3ac_lb = Label(window, text = "Enter Arrival Time for Process 3: ", font=('Times New Roman', 15), background='#f6ead4' )
        p3ac_lb.place(x=0, y= 190)
        p3ac_entry = Entry(window, width = 10)
        p3ac_entry.place(x=280, y= 190)
        p3bt_lb = Label(window, text = "Enter Burst Time for Process 3: ", font=('Times New Roman', 15), background='#f6ead4' )
        p3bt_lb.place(x=370, y= 190)
        p3bt_entry = Entry(window, width = 10)
        p3bt_entry.place(x=630, y= 190)

        q_lb = Label(window, text = "Enter quantum: ", font=('Times New Roman', 15), background='#f6ead4')
        q_lb.place(x = 0, y = 230)
        q_entry = Entry(window, width = 10)
        q_entry.place(x = 280, y = 230)

    saveButton = Button(window, text="Save", command= save)
    saveButton.place(x=280, y= 260)


def save():
    global frame
    frame=Tk()
    frame.geometry("980x680") #size
    frame.config(background="#f6ead4")

    l1 =Label(frame, text="  Process  ", font=('Times New Roman', 15), background='#f6ead4').grid(row=0, column=0)
    l1 =Label(frame, text="  Access Time  ", font=('Times New Roman', 15), background='#f6ead4').grid(row=0, column=1)
    l1 =Label(frame, text="  Burst Time  ", font=('Times New Roman', 15), background='#f6ead4').grid(row=0, column=2)
    if process == "1":
        p1 = Label(frame, text="P1", font=('Times New Roman', 12), background='#f6ead4').grid(row=1, column=0)
        ac1= Label(frame, text= p1ac_entry.get(), font=('Times New Roman', 12), background='#f6ead4').grid(row=1, column=1)
        bt1= Label(frame, text= p1bt_entry.get(), font=('Times New Roman', 12), background='#f6ead4').grid(row=1, column=2)
        bn = Button(frame, text = "Animate", command = Animate)
        bn.grid(row = 4, column=1)
    if process == "2":
        p1 = Label(frame, text="P1", font=('Times New Roman', 12), background='#f6ead4').grid(row=1, column=0)
        p2 = Label(frame, text="P2", font=('Times New Roman', 12), background='#f6ead4').grid(row=2, column=0)
        ac1= Label(frame, text= p1ac_entry.get(), font=('Times New Roman', 12), background='#f6ead4').grid(row=1, column=1)
        ac2= Label(frame, text= p2ac_entry.get(), font=('Times New Roman', 12), background='#f6ead4').grid(row=2, column=1)
        bt1= Label(frame, text= p1bt_entry.get(), font=('Times New Roman', 12), background='#f6ead4').grid(row=1, column=2)
        bt2= Label(frame, text= p2bt_entry.get(), font=('Times New Roman', 12), background='#f6ead4').grid(row=2, column=2)
        bn = Button(frame, text = "Animate", command = Animate)
        bn.grid(row = 4, column=1)
    if process == "3":
        p1 = Label(frame, text="P1", font=('Times New Roman', 12), background='#f6ead4').grid(row=1, column=0)
        p2 = Label(frame, text="P2", font=('Times New Roman', 12), background='#f6ead4').grid(row=2, column=0)
        p3 = Label(frame, text="P3", font=('Times New Roman', 12), background='#f6ead4').grid(row=3, column=0)
        ac1= Label(frame, text= p1ac_entry.get(), font=('Times New Roman', 12), background='#f6ead4').grid(row=1, column=1)
        ac2= Label(frame, text= p2ac_entry.get(), font=('Times New Roman', 12), background='#f6ead4').grid(row=2, column=1)
        ac3= Label(frame, text= p3ac_entry.get(), font=('Times New Roman', 12), background='#f6ead4').grid(row=3, column=1)
        bt1= Label(frame, text= p1bt_entry.get(), font=('Times New Roman', 12), background='#f6ead4').grid(row=1, column=2)
        bt2= Label(frame, text= p2bt_entry.get(), font=('Times New Roman', 12), background='#f6ead4').grid(row=2, column=2)
        bt3= Label(frame, text= p3bt_entry.get(), font=('Times New Roman', 12), background='#f6ead4').grid(row=3, column=2)
        bn = Button(frame, text = "Animate", command = Animate)
        bn.grid(row = 4, column=1)
    frame.mainloop


# ***************
# BIND FUNCTIONS 
# used to create movement 
# this function were written based on youtube tut: https://youtu.be/uGmMsGOcBB0
# ***************
def drag_start(event):
    global widget
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y
def drag_motion(event):
    global widget
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x, y=y)

# ***************
# Animate function 
# create visual block to represent data
# requires human input to fully demonstrate task
# ***************
def Animate():
    #Variables 
    global frame
    global widget

    label = Label(frame, text=" QUEUE ", font=('Rockwell Extra Bold', 40, 'bold'))
    label.place(x= 20, y=150)
    label.config(background= "white")
    label = Label(frame, text=" PROCESSOR ", font=('Rockwell Extra Bold', 40, 'bold'))
    label.config(background="white")
    label.place(x= 500, y=150)

    canva = Canvas(frame, width=400, height=400, bg = "white")
    canva.place(x=500, y=250)


    if process == "1":
        a=int(p1bt_entry.get())
        length = a

        for i in range(a):
            label = Label(frame, text="P1 ", font=('Rockwell Extra Bold', 20, 'bold'), relief=RAISED)
            label.config(background="red")
            label.place(x= 60, y=250)

            label.bind("<Button-1>",drag_start)
            label.bind("<B1-Motion>",drag_motion)
    if process == "2":
        a=int(p1bt_entry.get())
        b=int(p2bt_entry.get())
        length = (a + b)

        for i in range(a):
            label = Label(frame, text="P1 ", font=('Rockwell Extra Bold', 20, 'bold'), relief=RAISED)
            label.config(background="red")
            label.place(x= 60, y=250)

            label.bind("<Button-1>",drag_start)
            label.bind("<B1-Motion>",drag_motion)

        for i in range(b):
            label = Label(frame, text="P2 ", font=('Rockwell Extra Bold', 20, 'bold'), relief=RAISED)
            label.config(background="purple")
            label.place(x= 60, y=350)

            label.bind("<Button-1>",drag_start)
            label.bind("<B1-Motion>",drag_motion)
    if process == "3":
        a=int(p1bt_entry.get())
        b=int(p2bt_entry.get())
        c=int(p3bt_entry.get())
        length = (a + b + c)

        for i in range(a):
            label = Label(frame, text="P1 ", font=('Rockwell Extra Bold', 20, 'bold'), relief=RAISED)
            label.config(background="red")
            label.place(x= 60, y=250)

            label.bind("<Button-1>",drag_start)
            label.bind("<B1-Motion>",drag_motion)

        for i in range(b):
            label = Label(frame, text="P2 ", font=('Rockwell Extra Bold', 20, 'bold'), relief=RAISED)
            label.config(background="purple")
            label.place(x= 60, y=350)

            label.bind("<Button-1>",drag_start)
            label.bind("<B1-Motion>",drag_motion)

        for i in range(c):
            label = Label(frame, text="P3 ", font=('Rockwell Extra Bold', 20, 'bold'), relief=RAISED)
            label.config(background="yellow")
            label.place(x= 60, y=450)

            label.bind("<Button-1>",drag_start)
            label.bind("<B1-Motion>",drag_motion)

    num = 60
    for i in range(1, length + 1):
        canva.create_text(60, num, text = "" + str(i) , fill = "black")
        num += 30

global window

window=Tk()
window.geometry("1000x500") #size
window.title("RR")# title

window.config(background='#f6ead4')

rrLabel= Label(window, text=" Round Robin ", 
        font=('Rockwell Extra Bold', 20), foreground= '#1fbfb8', background='#f6ead4')
rrLabel.grid(row=0, column =0, columnspan=2) # Page title

num_process = Label(window, text="Number of process: ").place(x=0, y= 40)

# creating combo box widget
combo = Combobox(window)
combo['values']=(1,2,3)
combo.current(0)
combo.place(x=0, y= 60)

# Next button - get user entry 
nextButton= Button(window, text= "Next", command = nxt)
nextButton.place(x=20, y= 81)

window.mainloop()