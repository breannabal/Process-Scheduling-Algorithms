from tkinter import *
from tkinter.ttk import *
import time

# NB: It is assumed that all processes have an arrival time of 0ms

# setting up window 
window = Tk()
window.title("Shortest Process Next Algorithm")
window.geometry('1200x1200')
window.resizable(False, False)

# creating page title 
sjf_lb = Label(window, text = "Shortest Process Next", font = ('Rockwell Extra Bold', 20), foreground = '#1fbfb8', background ='white')
sjf_lb.grid(column = 0, row = 0)

# creating frame
frame = Frame(window)
frame.grid()

# creating label 
intro = Label(frame, text = "Select number of processes: ")
intro.grid(column = 0, row = 1)

# creating combobox widget
# users are able to selected the number of processes and proceed next
combo = Combobox(frame)
combo['values'] = (1, 2, 3, 4)
combo.current(0)
combo.grid(column = 0, row = 2)

# function for when next button is selected
# this function is executed after the next button is selected
def next_action():
    global p1_entry, p2_entry, p3_entry, p4_entry, num
    num = combo.get() # retrieving the number of processes input from user

    if num == "2": # creating labels and entry widgets based on the number of processes selected by user
        p1_lb = Label(frame, text = "Enter Burst Time for P1: ")
        p1_lb.grid(column = 0, row = 4)
        p1_entry = Entry(frame, width = 10)
        p1_entry.grid(column = 1, row = 4)

        p2_lb = Label(frame, text = "Enter Burst Time for P2: ")
        p2_lb.grid(column = 0, row = 5)
        p2_entry = Entry(frame, width = 10)
        p2_entry.grid(column = 1, row = 5)
    if num == "3":
        p1_lb = Label(frame, text = "Enter Burst Time for P1: ")
        p1_lb.grid(column = 0, row = 4)
        p1_entry = Entry(frame, width = 10)
        p1_entry.grid(column = 1, row = 4)
        
        p2_lb = Label(frame, text = "Enter Burst Time for P2: ")
        p2_lb.grid(column = 0, row = 5)
        p2_entry = Entry(frame, width = 10)
        p2_entry.grid(column = 1, row = 5)

        p3_lb = Label(frame, text = "Enter Burst Time for P3: ")
        p3_lb.grid(column = 0, row = 6)
        p3_entry = Entry(frame, width = 10)
        p3_entry.grid(column = 1, row = 6)
    if num == "4":
        p1_lb = Label(frame, text = "Enter Burst Time for P1: ")
        p1_lb.grid(column = 0, row = 4)
        p1_entry = Entry(frame, width = 10)
        p1_entry.grid(column = 1, row = 4)
        
        p2_lb = Label(frame, text = "Enter Burst Time for P2: ")
        p2_lb.grid(column = 0, row = 5)
        p2_entry = Entry(frame, width = 10)
        p2_entry.grid(column = 1, row = 5)

        p3_lb = Label(frame, text = "Enter Burst Time for P3: ")
        p3_lb.grid(column = 0, row = 6)
        p3_entry = Entry(frame, width = 10)
        p3_entry.grid(column = 1, row = 6)

        p4_lb = Label(frame, text = "Enter Burst Time for P4: ")
        p4_lb.grid(column = 0, row = 7)
        p4_entry = Entry(frame, width = 10)
        p4_entry.grid(column = 1, row = 7)
    
    bn = Button(frame, text = "Submit", command = submit_action)
    bn.grid(column = 1, row = 8)

# function for when the submit button is selected
# this function is executed after the submit button is selected
def submit_action():
    global processes, bt, p1, p2, p3, p4
    processes = []
    bt = []
    
    if num == "2": # adding info to the processes array based on the number of processes selected by user
        p1 = int(p1_entry.get()) # getting burst time input from user and converting to integer
        processes.append([1, p1])
        bt.append(p1)
        p2 = int(p2_entry.get())
        processes.append([2, p2]) # adding to processes array
        bt.append(p2) # adding burst time to bt array
    if num == "3":
        p1 = int(p1_entry.get())
        processes.append([1, p1])
        bt.append(p1)
        p2 = int(p2_entry.get())
        processes.append([2, p2])
        bt.append(p2)
        p3 = int(p3_entry.get())
        processes.append([3, p3])
        bt.append(p3)
    if num == "4":
        p1 = int(p1_entry.get())
        processes.append([1, p1])
        bt.append(p1)
        p2 = int(p2_entry.get())
        processes.append([2, p2])
        bt.append(p2)
        p3 = int(p3_entry.get())
        processes.append([3, p3])
        bt.append(p3)
        p4 = int(p4_entry.get())
        processes.append([4, p4])
        bt.append(p4)
    
    bt.sort() # sorting burst time in ascending order
    
    print ("Process ID and Burst Time: ", processes) # displaying all the processes and burst time
    print ("Burst Time of all processes: ", bt) # displaying the burst time 
    
    # creating button to view animation of algorithm
    ani = Button(frame, text = "View Animation", command = animation_action)
    ani.grid(column = 4, row = 8)
        

# function for when the view animation button is selected
# this function is executed after the view animation button is selected
def animation_action():
    
    global canva

    # creaing a canva to place the queue, processor and processes inside
    canva = Canvas(window, width = 800, height = 800, bg = "white")
    canva.grid(column = 0, row = 4) # setting the size of the canva

    # creating rectangles which represent the queue and processsor
    queue = canva.create_rectangle(0, 0, 110, 400, fill = "green")
    q_txt = canva.create_text(30, 420, text = "Queue", fill = "black") # x and y coordindates
    processor = canva.create_rectangle(200, 30, 300, 250, fill = "blue")
    p_txt = canva.create_text(250, 300, text = "Processor", fill = "black")

    if num == "2":
        pro1 = canva.create_rectangle(50, 50, 80, 70, fill = "black", tag = "p1")
        pro1_txt = canva.create_text(40, 60, text = "P1", fill = "yellow")
        pro2 = canva.create_rectangle(50, 100, 80, 120, fill = "red", tag = "p2")
        pro2_txt = canva.create_text(40, 110, text = "P2", fill = "yellow")

        for i in range(len(bt)):
            if bt[i] == p1:
                for x in range(20):
                    canva.move("p1", 10, 0) # moving processes
                    canva.update()
                    time.sleep(0.10)
            if bt[i] == p2:
                for x in range(20):
                    canva.move("p2", 10, 0)
                    canva.update()
                    time.sleep(0.10)
    if num == "3":
        pro1 = canva.create_rectangle(50, 50, 80, 70, fill = "black", tag = "p1")
        pro1_txt = canva.create_text(40, 60, text = "P1", fill = "yellow")
        pro2 = canva.create_rectangle(50, 100, 80, 120, fill = "red", tag = "p2")
        pro2_txt = canva.create_text(40, 110, text = "P2", fill = "yellow")
        pro3 = canva.create_rectangle(50, 150, 80, 170, fill = "cyan", tag = "p3")
        pro3_txt = canva.create_text(40, 160, text = "P3", fill = "yellow")

        for i in range(len(bt)):
            if bt[i] == p1:
                for x in range(20):
                    canva.move("p1", 10, 0)
                    canva.update()
                    time.sleep(0.10)
            if bt[i] == p2:
                for x in range(20):
                    canva.move("p2", 10, 0)
                    canva.update()
                    time.sleep(0.10)
            if bt[i] == p3:
                for x in range(20):
                    canva.move("p3", 10, 0)
                    canva.update()
                    time.sleep(0.10)
    if num == "4":
        pro1 = canva.create_rectangle(50, 50, 80, 70, fill = "black", tag = "p1")
        pro1_txt = canva.create_text(40, 60, text = "P1", fill = "yellow")
        pro2 = canva.create_rectangle(50, 100, 80, 120, fill = "red", tag = "p2")
        pro2_txt = canva.create_text(40, 110, text = "P2", fill = "yellow")
        pro3 = canva.create_rectangle(50, 150, 80, 170, fill = "cyan", tag = "p3")
        pro3_txt = canva.create_text(40, 160, text = "P3", fill = "yellow")
        pro4 = canva.create_rectangle(50, 200, 80, 220, fill = "magenta", tag = "p4")
        pro4_txt = canva.create_text(40, 210, text = "P4", fill = "yellow")

        for i in range(len(bt)):
            if bt[i] == p1:
                for x in range(20):
                    canva.move("p1", 10, 0)
                    canva.update()
                    time.sleep(0.10)
            if bt[i] == p2:
                for x in range(20):
                    canva.move("p2", 10, 0)
                    canva.update()
                    time.sleep(0.10)
            if bt[i] == p3:
                for x in range(20):
                    canva.move("p3", 10, 0)
                    canva.update()
                    time.sleep(0.10)
            if bt[i] == p4:
                for x in range(20):
                    canva.move("p4", 10, 0)
                    canva.update()
                    time.sleep(0.10)
    wait_time()
    avg_wt()

# creating button 
btn = Button(frame, text = "Next", command = next_action)
btn.grid(column = 0, row = 3)

# function to calculate the wait time of processes 
def wait_time():
    global wt
    wt = [] # array to store wait time of processes
    wt.append(0)
    processes.sort(key = lambda x:x[1]) # sorting processes by burst time
    processes[0].append(0) # adds the waiting time of the first process to the array which is 0
    for i in range(1, len(processes)):
        waiting = processes[i - 1][1] + processes[i - 1][2] # adding burst time and wait time of the previous process
        wt.append(waiting)
        processes[i].append(waiting)
    print("Processes, Burst Time and Wait Time: ", processes)

# function to calculate the average wait time of processes
def avg_wt():
    sum = 0

    for x in range(len(wt)):
        sum = sum + wt[x]
        avg = sum/len(wt)

    print("Average Wait Time: ", avg)

# running the window
window.mainloop()