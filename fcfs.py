from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
import time

# setting up window 
window = Tk()
window.title("First Come First Serve Algorithm")
window.geometry('800x800')
window.resizable(False, False)

# creating frame
frame = Frame(window)
frame.grid()

#exit gui upon key press
def exit(event):
    window.destroy()
window.bind("<Escape>", exit)

# creating label 
intro = Label(frame, text = "Select number of processes: ")
intro.grid(column = 0, row = 0)

# creating combobox widget
# users are able to selected the number of processes
combo = Combobox(frame)
combo['values'] = (1, 2, 3, 4)
combo.current(0)
combo.grid(column = 0, row = 1)

# function for when next button is selected
# this function is executed after the next button is selected
def next_action():
    global p1_entry, p2_entry, p3_entry, p4_entry, num
    num = combo.get() # retrieving the number of processes input from user
    if num == "1": # creating labels and entry widgets based on the number of processes selected by user
        p1_lb = Label(frame, text = "Enter Arrival Time for P1: ")
        p1_lb.grid(column = 0, row = 3)
        p1_entry = Entry(frame, width = 10)
        p1_entry.grid(column = 1, row = 3)

    if num == "2": # creating labels and entry widgets based on the number of processes selected by user
        p1_lb = Label(frame, text = "Enter Arrival Time for P1: ")
        p1_lb.grid(column = 0, row = 3)
        p1_entry = Entry(frame, width = 10)
        p1_entry.grid(column = 1, row = 3)

        p2_lb = Label(frame, text = "Enter Arrival Time for P2: ")
        p2_lb.grid(column = 0, row = 4)
        p2_entry = Entry(frame, width = 10)
        p2_entry.grid(column = 1, row = 4)
    if num == "3":
        p1_lb = Label(frame, text = "Enter Arrival Time for P1: ")
        p1_lb.grid(column = 0, row = 3)
        p1_entry = Entry(frame, width = 10)
        p1_entry.grid(column = 1, row = 3)
        
        p2_lb = Label(frame, text = "Enter Arrival Time for P2: ")
        p2_lb.grid(column = 0, row = 4)
        p2_entry = Entry(frame, width = 10)
        p2_entry.grid(column = 1, row = 4)

        p3_lb = Label(frame, text = "Enter Arrival Time for P3: ")
        p3_lb.grid(column = 0, row = 5)
        p3_entry = Entry(frame, width = 10)
        p3_entry.grid(column = 1, row = 5)
    if num == "4":
        p1_lb = Label(frame, text = "Enter Arrival Time for P1: ")
        p1_lb.grid(column = 0, row = 3)
        p1_entry = Entry(frame, width = 10)
        p1_entry.grid(column = 1, row = 3)
        
        p2_lb = Label(frame, text = "Enter Arrival Time for P2: ")
        p2_lb.grid(column = 0, row = 4)
        p2_entry = Entry(frame, width = 10)
        p2_entry.grid(column = 1, row = 4)

        p3_lb = Label(frame, text = "Enter Arrival Time for P3: ")
        p3_lb.grid(column = 0, row = 5)
        p3_entry = Entry(frame, width = 10)
        p3_entry.grid(column = 1, row = 5)

        p4_lb = Label(frame, text = "Enter Arrival Time for P4: ")
        p4_lb.grid(column = 0, row = 6)
        p4_entry = Entry(frame, width = 10)
        p4_entry.grid(column = 1, row = 6)
    
    bn = Button(frame, text = "Submit", command = submit_action)
    bn.grid(column = 1, row = 7)

# function for when the submit button is selected
# this function is executed after the submit button is selected
def submit_action():
    global processes, at, p1, p2, p3, p4
    processes = []
    at = []
    if num == "1": # adding info to the processes array based on the number of processes selected by user
        p1 = int(p1_entry.get()) # getting arrival time input from user and converting to integer
        processes.append([1, p1])
        at.append(p1)
        
    if num == "2": # adding info to the processes array based on the number of processes selected by user
        p1 = int(p1_entry.get()) # getting arrival time input from user and converting to integer
        processes.append([1, p1])
        at.append(p1)
        p2 = int(p2_entry.get())
        processes.append([2, p2]) # adding to processes array
        at.append(p2) # adding Arrival time to bt array
    if num == "3":
        p1 = int(p1_entry.get())
        processes.append([1, p1])
        at.append(p1)
        p2 = int(p2_entry.get())
        processes.append([2, p2])
        at.append(p2)
        p3 = int(p3_entry.get())
        processes.append([3, p3])
        at.append(p3)
    if num == "4":
        p1 = int(p1_entry.get())
        processes.append([1, p1])
        at.append(p1)
        p2 = int(p2_entry.get())
        processes.append([2, p2])
        at.append(p2)
        p3 = int(p3_entry.get())
        processes.append([3, p3])
        at.append(p3)
        p4 = int(p4_entry.get())
        processes.append([4, p4])
        at.append(p4)
    
    
    at.sort() # sorting arrival time in ascending order
    
    print ("Process ID and Arrival Time ", processes)
    print ("Arrival Time of all processes: ", at)
    
    # creating button to view animation of algorithm
    ani = Button(frame, text = "Show Animation", command = animation_action)
    ani.grid(column = 4, row = 7)
        

# function for when the view animation button is selected
# this function is executed after the view animation button is selected
def animation_action():
    
    global canva

    # creating a canva to place the queue, processor and processes inside
    canva = Canvas(window, width = 800, height = 800, bg = "black")
    canva.grid(column = 0, row = 4) # setting the size of the canva
   
    # creating images which represent the processsor and flow
    img=Image.open("processor1.png")
    resized_image= img.resize((240,240), Image.ANTIALIAS)
    new_image= ImageTk.PhotoImage(resized_image)
    canva.create_image(345,50,image=new_image,anchor=NW)

    lights=Image.open("lights.png")
    resized_image2= lights.resize((30,50), Image.ANTIALIAS)
    new_image2= ImageTk.PhotoImage(resized_image2)
    canva.create_image(200,5,image=new_image2,anchor=NW)

    # human=Image.open("person.png")
    # resized_image3= human.resize((280,180), Image.ANTIALIAS)
    # new_image3= ImageTk.PhotoImage(resized_image3)
    # canva.create_image(100,5,image=new_image3,anchor=NW)





    # creating a rectangle which represents the queue
    queue = canva.create_rectangle(0, 60, 110, 400, fill = "#b44860")
    q_txt = canva.create_text(30, 420, text = "Queue", fill = "white") # x and y coordindates
    # processor = canva.create_rectangle(200, 30, 300, 250, fill = "#e5d576")
    p_txt = canva.create_text(460, 310, text = "Processor", fill = "white")
    
    if num == "1":
        pro1 = canva.create_oval(50, 100, 80, 80, fill = "white", tag = "p1")
        pro1_txt = canva.create_text(40, 80, text = "P1", fill = "white")
        for i in range(20):
            canva.move("p1", 20, 0) # automatic movement of the processes from the queue to the processor
            canva.update()
            time.sleep(0.10)

    if num == "2":
        pro1 = canva.create_oval(50, 100, 80, 80, fill = "white", tag = "p1")
        pro1_txt = canva.create_text(40, 80, text = "P1", fill = "white")
        pro2 = canva.create_oval(50, 110, 80, 130, fill = "#85c9e0", tag = "p2")
        pro2_txt = canva.create_text(40, 115, text = "P2", fill = "white")

        if processes[0][1] < processes[1][1]:
            for i in range(20):
                canva.move("p1", 20, 0) # automatic movement of the processes from the queue to the processor
                canva.update()
                time.sleep(0.10)
            for x in range(20):
                canva.move("p2", 20, 0)
                canva.update()
                time.sleep(0.10)
        else:
            for i in range(20):
                canva.move("p2", 20, 0)
                canva.update()
                time.sleep(0.10)
            for x in range(20):
                canva.move("p1", 20, 0)
                canva.update()
                time.sleep(0.10)
    if num == "3":
        pro1 = canva.create_oval(50, 100, 80, 80, fill = "white", tag = "p1")
        pro1_txt = canva.create_text(40, 80, text = "P1", fill = "white")
        pro2 = canva.create_oval(50, 110, 80, 130, fill = "#85c9e0", tag = "p2")
        pro2_txt = canva.create_text(40, 115, text = "P2", fill = "white")
        pro3 = canva.create_oval(50, 150, 80, 170, fill = "#e09757", tag = "p3")
        pro3_txt = canva.create_text(40, 150, text = "P3", fill = "white")
        
        if processes[0][1] < processes[1][1] and processes[1][1] < processes[2][1] :
            for i in range(20):
                canva.move("p1", 20, 0) # automatic movement of the processes from the queue to the processor
                canva.update()
                time.sleep(0.10)
            for x in range(20):
                canva.move("p2", 20, 0)
                canva.update()
                time.sleep(0.10)
            for x in range(20):
                canva.move("p3", 20, 0)
                canva.update()
                time.sleep(0.10)
        elif processes[0][1] < processes[2][1] and processes[2][1] < processes[1][1]:
            for i in range(20):
                canva.move("p1", 20, 0) # automatic movement of the processes from the queue to the processor
                canva.update()
                time.sleep(0.10)
            for x in range(20):
                canva.move("p3", 20, 0)
                canva.update()
                time.sleep(0.10)
            for x in range(20):
                canva.move("p2", 20, 0)
                canva.update()
                time.sleep(0.10)
        elif processes[1][1] < processes[0][1] and processes[0][1] < processes[2][1]:
            for i in range(20):
                canva.move("p2", 20, 0) # automatic movement of the processes from the queue to the processor
                canva.update()
                time.sleep(0.10)
            for x in range(20):
                canva.move("p1", 20, 0)
                canva.update()
                time.sleep(0.10)
            for x in range(20):
                canva.move("p3", 20, 0)
                canva.update()
                time.sleep(0.10)
        elif processes[1][1] < processes[0][1] and processes[2][1] < processes[0][1]:
            for i in range(20):
                canva.move("p2", 20, 0) # automatic movement of the processes from the queue to the processor
                canva.update()
                time.sleep(0.10)
            for x in range(20):
                canva.move("p3", 20, 0)
                canva.update()
                time.sleep(0.10)
            for x in range(20):
                canva.move("p1", 20, 0)
                canva.update()
                time.sleep(0.10)  
        elif processes[2][1] < processes[0][1] and processes[0][1] < processes[1][1]:
            for i in range(20):
                canva.move("p3", 20, 0) # automatic movement of the processes from the queue to the processor
                canva.update()
                time.sleep(0.10)
            for x in range(20):
                canva.move("p1", 20, 0)
                canva.update()
                time.sleep(0.10)
            for x in range(20):
                canva.move("p2", 20, 0)
                canva.update()
                time.sleep(0.10)  
        else:
            for i in range(20):
                canva.move("p3", 20, 0)
                canva.update()
                time.sleep(0.10)
            for x in range(20):
                canva.move("p2", 20, 0)
                canva.update()
                time.sleep(0.10)
            for x in range(20):
                canva.move("p1", 20, 0)
                canva.update()
                time.sleep(0.10)
    if num == "4":
        pro1 = canva.create_oval(50, 100, 80, 80, fill = "white", tag = "p1")
        pro1_txt = canva.create_text(40, 80, text = "P1", fill = "white")
        pro2 = canva.create_oval(50, 110, 80, 130, fill = "#85c9e0", tag = "p2")
        pro2_txt = canva.create_text(40, 115, text = "P2", fill = "white")
        pro3 = canva.create_oval(50, 150, 80, 170, fill = "#e09757", tag = "p3")
        pro3_txt = canva.create_text(40, 150, text = "P3", fill = "white")
        pro4 = canva.create_oval(50, 200, 80, 220, fill = "#acb0cd", tag = "p4")
        pro4_txt = canva.create_text(40, 210, text = "P4", fill = "white")
        
        for i in range(len(at)):
            if at[i] == p1:
                for x in range(20):
                    canva.move("p1", 20, 0)
                    canva.update()
                    time.sleep(0.10)
            if at[i] == p2:
                for x in range(20):
                    canva.move("p2", 20, 0)
                    canva.update()
                    time.sleep(0.10)
            if at[i] == p3:
                for x in range(20):
                    canva.move("p3", 20, 0)
                    canva.update()
                    time.sleep(0.10)
            if at[i] == p4:
                for x in range(20):
                    canva.move("p4", 20, 0)
                    canva.update()
                    time.sleep(0.10)

# creating button 
btn = Button(frame, text = "Next", command = next_action)
btn.grid(column = 0, row = 2)

# running the window
window.mainloop()