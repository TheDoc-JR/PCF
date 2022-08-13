from tkinter import messagebox
from tkinter.font import BOLD
import pandas as pd
from tkinter import *
import mysql.connector as sqlc
from PIL import Image, ImageTk


# Config the GUI
root = Tk()
root.title('ABLORH® DATA FINDER')
root.geometry("700x300")
root.configure(bg='#E1F0ED')

# Set a background image
bg = ImageTk.PhotoImage(Image.open("C:\\Users\\Gwendarling\\DarlinGit\\Images\\BGI.jpg"))

canv = Canvas(root, width=500, height=300)
canv.pack(fill="both", expand=True)
canv.create_image(300, 0, image=bg, anchor="nw")

# Create Login frame
# Add Dr Image
log_img = Image.open("C:\\Users\\Gwendarling\\DarlinGit\\Images\\LoginImage-modified.png")
resized = log_img.resize((100,100), Image.ANTIALIAS)
new_pic = ImageTk.PhotoImage(resized)
label = Label(root, image=new_pic, highlightcolor="red", borderwidth=0)

log_img_window = canv.create_window(85, 20, anchor="nw", window=label)

# Create login function
def logpw():
    global emr,nbg,ncanv,add_p,addp_img,showp_img,addr_img,\
           showr_img,ext_img,extn,ap,id,cnx,mycursor, pid,\
           name,pname,surname,psurname,bd,pbd,age,page,sex,\
           psex, add_patient
    
    pssw = pw.get()
    
    if pssw == "q":
        # Open new records window
        emr = Toplevel()
        emr.title("ABLORH® DATA FINDER")
        emr.geometry("700x300")
        
        # Set a background image
        nbg = ImageTk.PhotoImage(Image.open("C:\\Users\\Gwendarling\\DarlinGit\\Images\\emr2.jpg"))

        ncanv = Canvas(emr, width=600, height=300)
        ncanv.pack(fill="both", expand=True)
        ncanv.create_image(0, 0, image=nbg, anchor="nw")

        # Establish connection to the database
        cnx = sqlc.connect(
            user="root",
            password="TheDoctor3005",
            host="localhost",
            database="perez"
        )

        # Create a cursor
        mycursor = cnx.cursor()

        # Create patients table
        mycursor.execute("DROP TABLE IF EXISTS ENZYMES")
        mycursor.execute("DROP TABLE IF EXISTS COMPLETE_BLOOD_COUNT")
        mycursor.execute("DROP TABLE IF EXISTS BIOCHEMISTRY")
        mycursor.execute("DROP TABLE IF EXISTS PATIENT")
        mycursor.execute("CREATE TABLE PATIENT(\n"
            "ID INT PRIMARY KEY,\n"
            "Name VARCHAR(20),\n"
            "Last_name VARCHAR(20),\n"
            "Birth_date DATE,\n"
            "Age INT,\n"
            "Sex CHAR(1))")

        # Add exit function
        def extn():
            x = messagebox.askyesno("","Hey Doc!\nAre you sure you want to exit?")
            if x == 1:
                emr.destroy()
                root.destroy()
            else: pass

        # Create ap function
        def ap():
            global id,pid,name,pname,surname,psurname,\
                   bd,pbd,age,page,sex,psex,add_patient
            
            # Create the data boxes
            id = Entry(emr)
            
            ncanv.create_window(30, 20, anchor="nw", window=id)

            name = Entry(emr)
            
            ncanv.create_window(30, 60, anchor="nw", window=name)

            surname = Entry(emr)
            
            ncanv.create_window(30, 100, anchor="nw", window=surname)

            bd = Entry(emr)
            
            ncanv.create_window(30, 140, anchor="nw", window=bd)

            age = Entry(emr)
            
            ncanv.create_window(30, 180, anchor="nw", window=age)

            sex = Entry(emr)
            
            ncanv.create_window(30, 220, anchor="nw", window=sex)
            
            # Create submit-patient button
            submit_patient = Button(emr, width=20, text='Add new patient', command=add_patient)
            ncanv.create_window(30, 260, anchor="nw", window=submit_patient)
        

        # Create submit-patient function
        def add_patient():
            global pid,pname,psurname,pbd,page,psex

            pid = int(id.get())
            pname = name.get()
            psurname = surname.get()
            pbd = bd.get()
            page = age.get()
            psex = sex.get()

            # establish connection to the database
            cnx = sqlc.connect(
            user="root",
            password="TheDoctor3005",
            host="localhost",
            database="perez"
        )

            # create a cursor
            mycursor = cnx.cursor()

            try:
                mycursor.execute("INSERT INTO PATIENT VALUES(%s,%s,%s,%s,%s,%s)", 
                (pid, pname.upper(),psurname.upper(), pbd, page, psex.upper()))

                # commit changes
                cnx.commit()
                messagebox.showinfo('GOOD NEWS! :)','PATIENT SUCCESFULLY ADDED!')
            except:
                messagebox.showerror('BAD NEWS :(','IT HAS BEEN AN ERROR ADDING THIS PATIENT')

            # close connection
            cnx.close()

            # clear the text boxes
            name.delete(0, END)
            surname.delete(0, END)
            id.delete(0, END)
            bd.delete(0, END)
            age.delete(0, END)
            sex.delete(0, END)


        



        # Add buttons
        addp_img = PhotoImage(file="C:\\Users\\Gwendarling\\DarlinGit\\Images\\add-user.png")
        add_p = Button(emr, width=100, height=55, image=addp_img, command=ap)
        ncanv.create_window(600, 0, anchor="nw", window=add_p)
        
        showp_img = PhotoImage(file="C:\\Users\\Gwendarling\\DarlinGit\\Images\\find-user.png")
        show_p = Button(emr, width=100, height=55, image=showp_img)
        ncanv.create_window(600, 60, anchor="nw", window=show_p)
        
        addr_img = PhotoImage(file="C:\\Users\\Gwendarling\\DarlinGit\\Images\\medical-report.png")
        add_r = Button(emr, width=100, height=55, image=addr_img)
        ncanv.create_window(600, 120, anchor="nw", window=add_r)
        
        showr_img = PhotoImage(file="C:\\Users\\Gwendarling\\DarlinGit\\Images\\optimization.png")
        show_r = Button(emr, width=100, height=55, image=showr_img)
        ncanv.create_window(600, 180, anchor="nw", window=show_r)
        
        ext_img = PhotoImage(file="C:\\Users\\Gwendarling\\DarlinGit\\Images\\emergency-exit.png")
        ext = Button(emr, width=100, height=55, image=ext_img, command=extn)
        ncanv.create_window(600, 240, anchor="nw", window=ext)
        
    
    else: messagebox.showerror("","ACCESS DENIED\nWRONG PASSWORD")
    pw.delete(0, END)

# Add Login button
i = PhotoImage(file="C:\\Users\\Gwendarling\\DarlinGit\\Images\\Login-PNG.png")

logbtn = Button(root, image=i, borderwidth=0, command=logpw)
logbtnwindow = canv.create_window(10, 245, anchor="nw", window=logbtn)

# Create quit function
def xit():
    q = messagebox.askyesno("","Hey Doc!\nAre you sure you want to exit?")
    if q == 1:
        root.destroy()
    else: pass

# Add Quit button
q = PhotoImage(file="C:\\Users\\Gwendarling\\DarlinGit\\Images\\shutdown.png")

qbtn = Button(root, image=q, borderwidth=0, command=xit)
qwindow = canv.create_window(200, 243, anchor="nw", window=qbtn)

# Add Password entry
pw = Entry(root, font=("Rockwell",13), bd=2)
pw.insert(0, "Enter your password")

pw_window = canv.create_window(40, 180, anchor="nw", window=pw)

# Define pw_clear function
def pw_clear(e):
    pw.delete(0, END)
    pw.config(show="*")

# Bind the entry box
pw.bind("<Button-1>", pw_clear )

# Add greeting message
greeting = Label(root, text="WELCOME DR. CAROL!", font=("Bauhaus 93",15), fg="#94D3C8")
greeting_txt = canv.create_window(37, 140, anchor="nw", window=greeting)

























root.mainloop()