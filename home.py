# Import Module
import tkinter
from tkinter import *
from PIL import *

from PIL import  Image
from PIL import ImageTk
import tkinter.messagebox
from tkinter import messagebox, ttk
from prettytable import PrettyTable
# create root window
root = Tk()

# root window title and dimension
root.title("Student Safety System")
# Set geometry(widthxheight)
root.geometry('780x660')
root.configure(bg = '#DAB4A2')


# adding a label to the root window
lbl = Label(root, text="Student Safety System", font = ('Helvetica Bold', 40), fg= 'brown')
lbl.grid(column = 5,  row= 2, padx = 170, pady = 60)
lbl.configure(bg= '#DAB4A2')

img = ImageTk.PhotoImage(Image.open("students.png"))
panel = Label(root, image = img)
panel.grid(column= 5, row=1, padx= 10, pady= 10)
panel.configure(height= 170, width= 180)
# function to display user text when
# button is clicked

def clicked1():
    Emergency = tkinter.Toplevel(root)
    Emergency.title("Emergency Alert System")
    # Set geometry(widthxheight)
    Emergency.geometry('1000x700')
    Emergency.configure(bg='#231f20')
    def record():

        Em = Frame(records)

        Em.pack()

        history = ttk.Treeview(Em)
        history['columns'] = ("No.", "Type of Alert", "Date", "Time", "Location", "Longitude", "Latitude")

        history.column("No.", anchor=CENTER, width=100)
        history.column("Type of Alert", anchor=CENTER, width=100)
        history.column("Date", anchor=CENTER, width=100)
        history.column("Time", anchor=CENTER, width=100)
        history.column("Location", anchor=CENTER, width=100)
        history.column("Longitude", anchor=CENTER, width=100)
        history.column("Latitude", anchor=CENTER, width=100)

        history.heading("No.", text="No", anchor=CENTER)
        history.heading("Type of Alert", text="Type of Alert", anchor=CENTER)
        history.heading("Date", text="Date", anchor=CENTER)
        history.heading("Time", text="Time", anchor=CENTER)
        history.heading("Location", text="Location", anchor=CENTER)
        history.heading("Longitude", text="Longitude", anchor=CENTER)
        history.heading("Latitude", text="Latitude", anchor=CENTER)

        history.insert(parent='', index='1', iid=0, text='',
                       values=('1', 'Flood', '05 March 2020', '5:10 PM', 'UAQ', '25.5325° N', '55.5492° E'))
        history.insert(parent='', index='2', iid=1, text='',
                       values=('2', 'Earthquake', '30 Jan 2020', '8:38 PM', 'Sharjah', "25.3461° N", "55.4210° E"))
        history.insert(parent='', index='3', iid=2, text='',
                       values=('3', 'Tornado', '04 Dec 2020', '09:45 AM', 'Dubai', "25.2048° N", "55.2708° E"))
        history.insert(parent='', index='4', iid=3, text='',
                       values=('4', 'Fire', '13 Sep 2020', '5:49 AM', "Abu Dhabi", "24.4539° N", "54.3773° E"))
        history.insert(parent='', index='5', iid=4, text='',
                       values=('5', 'Medical', '07 Oct 2021', '1:15 PM', 'Ajman', "25.4052° N", "55.5136° E"))
        history.insert(parent='', index='6', iid=5, text='',
                       values=('6', 'Security', '09 Feb 2021', '8:38 AM', 'Fujairah', "25.1288° N", "56.3265° E"))
        history.insert(parent='', index='7', iid=6, text='',
                       values=('7', 'Tornado', '06 May 2021', '9:53 PM', 'RAK', "25.6741° N", "55.9804° E"))

        history.place(relx=40, rely=40)
        history.pack()

        def checkmap():
            map3 = tkinter.Toplevel(Emergency)
            map3.title("Location Map")
            # Set geometry(widthxheight)
            map3.geometry('500x300')
            img1 = PhotoImage(Image.open('unnamed-2.png'))
            panel1= Label(map3, image=img1)
            panel1.place(relx = 20, rely = 20)
            panel1.configure(width = 500, height = 600)
            panel1.pack()
            map3.pack()
            map3.mainloop()
        map1 = tkinter.Button(Emergency, text="Check Emergency Alerts Locations Map", command=checkmap)
        map1.place(relx=60, rely=60)
        map1.configure(fg='red', bg='red', height=3, width=30)
        map1.pack()





    def sel():
     temperature = 36.6

     while temperature < 56:
       temperature += 1

       if temperature > 56:
        messagebox = tkinter.Toplevel(Emergency, background="red")
        messagebox.geometry('800x200')

        def change_color():
                current_color = messagebox.cget("background")
                next_color = "black" if current_color == "red" else "red"
                messagebox.configure(background=next_color)
                messagebox.after(1000, change_color)

        def change_color1():
                current_color = lbl1.cget("background")
                next_color = "black" if current_color == "red" else "red"
                lbl1.configure(background=next_color)
                lbl1.after(1000, change_color1)

        def change_color2():
                current_color = lbl2.cget("background")
                next_color = "black" if current_color == "red" else "red"
                lbl2.configure(background=next_color)
                lbl2.after(1000, change_color2)

        change_color()
        lbl1 = tkinter.Label(messagebox, text="FIRE ALERT", font=('Helvetica Bold', 35),
                                 fg='white',
                                 background='red')
        lbl1.place(relx=5, rely=5)
        lbl1.pack()
        change_color1()
        lbl2 = tkinter.Label(messagebox,
                                 text="A fire has been detected. \n Please evacuate.",
                                 font=('Helvetica Bold', 20), fg='white', background='red')
        lbl2.place(relx=5, rely=20)
        lbl2.pack()
        change_color2()

    def sel2():
         messagebox = tkinter.Toplevel(Emergency, background="red")
         messagebox.geometry('800x200')

         def change_color():
             current_color = messagebox.cget("background")
             next_color = "black" if current_color == "red" else "red"
             messagebox.configure(background=next_color)
             messagebox.after(1000, change_color)

         def change_color1():
             current_color = lbl1.cget("background")
             next_color = "black" if current_color == "red" else "red"
             lbl1.configure(background=next_color)
             lbl1.after(1000, change_color1)

         def change_color2():
             current_color = lbl2.cget("background")
             next_color = "black" if current_color == "red" else "red"
             lbl2.configure(background=next_color)
             lbl2.after(1000, change_color2)

         change_color()
         lbl1 = tkinter.Label(messagebox, text="TORNADO ALERT", font=('Helvetica Bold', 35), fg='white',
                              background='red')
         lbl1.place(relx=5, rely=5)
         lbl1.pack()
         change_color1()
         lbl2 = tkinter.Label(messagebox,
                              text="A tornado has been detected in your area.  \n As a necessary precaution, please take shelter.",
                              font=('Helvetica Bold', 20), fg='white', background='red')
         lbl2.place(relx=5, rely=20)
         lbl2.pack()
         change_color2()

    def sel3():
         vibration = 3.0;
         if vibration > 2.0:
             messagebox = tkinter.Toplevel(Emergency, background="red")
             messagebox.geometry('800x200')

         def change_color():
             current_color = messagebox.cget("background")
             next_color = "black" if current_color == "red" else "red"
             messagebox.configure(background=next_color)
             messagebox.after(1000, change_color)

         def change_color1():
             current_color = lbl1.cget("background")
             next_color = "black" if current_color == "red" else "red"
             lbl1.configure(background=next_color)
             lbl1.after(1000, change_color1)

         def change_color2():
             current_color = lbl2.cget("background")
             next_color = "black" if current_color == "red" else "red"
             lbl2.configure(background=next_color)
             lbl2.after(1000, change_color2)

         change_color()
         lbl1 = tkinter.Label(messagebox, text="EARTHQUAKE ALERT", font=('Helvetica Bold', 35), fg='white',
                              background='red')
         lbl1.place(relx=5, rely=5)
         lbl1.pack()
         change_color1()
         lbl2 = tkinter.Label(messagebox,
                              text="An earthquake has been detected in the area. \n Please take cover.",
                              font=('Helvetica Bold', 20), fg='white', background='red')
         lbl2.place(relx=5, rely=20)
         lbl2.pack()
         change_color2()

    def sel4():
         report = TRUE;
         if report == TRUE:
             messagebox = tkinter.Toplevel(Emergency, background="red")
             messagebox.geometry('800x200')

         def change_color():
             current_color = messagebox.cget("background")
             next_color = "black" if current_color == "red" else "red"
             messagebox.configure(background=next_color)
             messagebox.after(1000, change_color)

         def change_color1():
             current_color = lbl1.cget("background")
             next_color = "black" if current_color == "red" else "red"
             lbl1.configure(background=next_color)
             lbl1.after(1000, change_color1)

         def change_color2():
             current_color = lbl2.cget("background")
             next_color = "black" if current_color == "red" else "red"
             lbl2.configure(background=next_color)
             lbl2.after(1000, change_color2)

         change_color()
         lbl1 = tkinter.Label(messagebox, text="SECURITY ALERT", font=('Helvetica Bold', 35), fg='white',
                              background='red')
         lbl1.place(relx=5, rely=5)
         lbl1.pack()
         change_color1()
         lbl2 = tkinter.Label(messagebox,
                              text="A suspicious person has been seen and reported. \n Please notify the authorities as necessary.",
                              font=('Helvetica Bold', 20), fg='white', background='red')
         lbl2.place(relx=5, rely=20)
         lbl2.pack()
         change_color2()

    def sel5():
         waterlevel = 0.5
         while waterlevel < 2:
             waterlevel += 2
             if waterlevel > 2:
                 messagebox = tkinter.Toplevel(Emergency, background="red")
                 messagebox.geometry('800x200')

             def change_color():
                 current_color = messagebox.cget("background")
                 next_color = "black" if current_color == "red" else "red"
                 messagebox.configure(background=next_color)
                 messagebox.after(1000, change_color)

             def change_color1():
                 current_color = lbl1.cget("background")
                 next_color = "black" if current_color == "red" else "red"
                 lbl1.configure(background=next_color)
                 lbl1.after(1000, change_color1)

             def change_color2():
                 current_color = lbl2.cget("background")
                 next_color = "black" if current_color == "red" else "red"
                 lbl2.configure(background=next_color)
                 lbl2.after(1000, change_color2)

             change_color()
             lbl1 = tkinter.Label(messagebox, text="EARTHQUAKE ALERT", font=('Helvetica Bold', 35), fg='white',
                                  background='red')
             lbl1.place(relx=5, rely=5)
             lbl1.pack()
             change_color1()
             lbl2 = tkinter.Label(messagebox,
                                  text="An earthquake has been detected in the area. \n Please take cover.",
                                  font=('Helvetica Bold', 20), fg='white', background='red')
             lbl2.place(relx=5, rely=20)
             lbl2.pack()
             change_color2()

    def sel5():
         report = TRUE;
         if report == TRUE:
             messagebox = tkinter.Toplevel(Emergency, background="red")
             messagebox.geometry('800x200')

         def change_color():
             current_color = messagebox.cget("background")
             next_color = "black" if current_color == "red" else "red"
             messagebox.configure(background=next_color)
             messagebox.after(1000, change_color)

         def change_color1():
             current_color = lbl1.cget("background")
             next_color = "black" if current_color == "red" else "red"
             lbl1.configure(background=next_color)
             lbl1.after(1000, change_color1)

         def change_color2():
             current_color = lbl2.cget("background")
             next_color = "black" if current_color == "red" else "red"
             lbl2.configure(background=next_color)
             lbl2.after(1000, change_color2)

         change_color()
         lbl1 = tkinter.Label(messagebox, text="FLOOD ALERT", font=('Helvetica Bold', 35), fg='white',
                              background='red')
         lbl1.place(relx=5, rely=5)
         lbl1.pack()
         change_color1()
         lbl2 = tkinter.Label(messagebox,
                              text="A flood alert has been issued. \n Please evacuate or get to higher grounds.",
                              font=('Helvetica Bold', 20), fg='white', background='red')
         lbl2.place(relx=5, rely=20)
         lbl2.pack()
         change_color2()

    def sel6():
         medicalreport = TRUE
         if medicalreport == TRUE:
             messagebox = tkinter.Toplevel(Emergency, background="red")
             messagebox.geometry('800x200')

         def change_color():
             current_color = messagebox.cget("background")
             next_color = "black" if current_color == "red" else "red"
             messagebox.configure(background=next_color)
             messagebox.after(1000, change_color)

         def change_color1():
             current_color = lbl1.cget("background")
             next_color = "black" if current_color == "red" else "red"
             lbl1.configure(background=next_color)
             lbl1.after(1000, change_color1)

         def change_color2():
             current_color = lbl2.cget("background")
             next_color = "black" if current_color == "red" else "red"
             lbl2.configure(background=next_color)
             lbl2.after(1000, change_color2)

         change_color()
         lbl1 = tkinter.Label(messagebox, text="MEDICAL EMERGENCY ALERT", font=('Helvetica Bold', 35), fg='white',
                              background='red')
         lbl1.place(relx=5, rely=5)
         lbl1.pack()
         change_color1()
         lbl2 = tkinter.Label(messagebox,
                              text="A medical emergency has been reported. \n Please take necessary steps until the medics reach.",
                              font=('Helvetica Bold', 20), fg='white', background='red')
         lbl2.place(relx=5, rely=20)
         lbl2.pack()
         change_color2()
    lbl = tkinter.Label(Emergency, text="Emergency Alert System", font=('Helvetica Bold', 40), fg='red')
    lbl.place(relx=5, rely=5)
    lbl.configure(bg='#231f20')
    lbl.pack()

    Sim = tkinter.Button(Emergency, text="Start Simulation")
    Sim.place(relx=10, rely=10)
    Sim.configure(fg='red', bg='red', height=3, width=30)
    Sim.pack()

    notify = tkinter.Button(Emergency, text="Notify Authorities", command=notified)
    notify.place(relx=15, rely=15)
    notify.configure(fg='red', bg='red', height=3, width=30)
    notify.pack()

    records = tkinter.Button(Emergency, text="Check Emergency Alerts History", command=record)
    records.place(relx=20, rely=20)
    records.configure(fg='red', bg='red', height=3, width=30)
    records.pack()

    var = IntVar()
    R1 = Radiobutton(Emergency, text="Fire Alert", variable=var, value=1,
                     command=sel, fg = 'white')
    R1.place(relx=5, rely=20)
    R1.configure(bg='#231f20')
    R1.pack(anchor=W)

    R2 = Radiobutton(Emergency, text="Tornado Alert", variable=var, value=2,
                     command=sel2, fg = 'white')
    R2.place(relx=5, rely=20)
    R2.configure(bg= '#231f20')

    R2.pack(anchor=W)

    R3 = Radiobutton(Emergency, text="Earthquake Alert", variable=var, value=3,
                     command=sel3, fg = 'white')
    R3.place(relx=5, rely=7)
    R3.configure(bg='#231f20')
    R3.pack(anchor=W)

    R4 = Radiobutton(Emergency, text="Security Alert", variable=var, value=4,
                     command=sel4, fg = 'white')
    R4.configure(bg='#231f20')
    R4.place(relx=7, rely=7)

    R4.pack(anchor=W)

    R5 = Radiobutton(Emergency, text="Flood Alert", variable=var, value=5,
                     command=sel5, fg = 'white')
    R5.place(relx=9, rely=7)
    R5.configure(bg='#231f20')
    R5.pack(anchor=W)

    R6 = Radiobutton(Emergency, text="Medical Emergency Alert", variable=var, value=6,
                     command=sel6, fg = 'white')
    R6.place(relx=9, rely=7)
    R6.configure(bg='#231f20')
    R6.pack(anchor=W)
    Emergency.pack()













# Create button, it will change label text



btn1 = Button(root, text="Emergency Alert",
             fg="red", command=clicked1, height= 3, width = 30)

# Set Button Grid
btn1.grid(column=5, row=3)
btn1.configure(background= "white")

btn2 = Button(root, text="Student Attendance Alert",
             fg="red", height= 3, width = 30)

# Set Button Grid
btn2.grid(column=5, row=6)
btn2.configure(bg = 'white')
btn3 = Button(root, text="Covid-19 Alert",
             fg="red", height= 3, width = 30)

# Set Button Grid
btn3.grid(column=5, row=9)
btn3.configure(bg = 'white')
btn4 = Button(root, text="Student Escape Alert",
             fg="red", height= 3, width = 30)

# Set Button Grid
btn4.grid(column=5, row=12)
btn4.configure(bg = 'white')
btn5 = Button(root, text="Electricity Detector",
             fg="red", height= 3, width = 30)


# Set Button Grid
btn5.grid(column=5, row=15)
btn5.configure(bg = 'white')

def notified():
    tkinter.messagebox.showinfo("Notified", "The authorities have been notified. Stay put and take necessary precautions until they take action")




# Execute Tkinter
root.mainloop()