from tkinter import *
import webbrowser

root = Tk()
root.geometry("650x500") #size
root.title("Process Scheduling Algorithms")# title
root.config(background='#f6ead4')

def callback(url):
    webbrowser.open_new(url)

title= Label(root, text=" Process Scheduling Algorithms ", 
        font=('Rockwell Extra Bold', 25), foreground= '#1fbfb8', background='#f6ead4'). place(x= 10, y=10)

non_preemptive = Label(root, text="Non- Preemptive", font=('Times New Roman', 15), background='#f6ead4', cursor="hand2").place(x= 100, y=80)
fcfs = Label(root, text="First Come First Serve", fg="black", font=('Times New Roman', 15), background='#f47a60',  cursor="hand2")
fcfs.place(x = 100, y=120)
fcfs.bind("<Button-1>", lambda e: callback("fcfs.py"))

sjf = Label(root, text="Shortest Process Next", fg="black", font=('Times New Roman', 15), background='#f47a60', cursor="hand2")
sjf.place(x = 100, y=220)
sjf.bind("<Button-1>", lambda e: callback("spn.py"))

preemptive = Label(root, text="Preemptive",font=('Times New Roman', 15), background='#f6ead4', cursor="hand2").place(x= 400, y=80)
srt = Label(root, text="Shortest Remaining Time First", fg="black", font=('Times New Roman', 15), background='#f47a60', cursor="hand2")
srt.place(x = 400, y=220)
srt.bind("<Button-1>", lambda e: callback("srt.py"))

rr = Label(root, text="Round Robin", fg="black", font=('Times New Roman', 15), background='#f47a60', cursor="hand2")
rr.place(x = 400, y=120)
rr.bind("<Button-1>", lambda e: callback("rr.py"))


root.mainloop()