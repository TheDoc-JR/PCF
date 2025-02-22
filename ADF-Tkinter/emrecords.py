from tkinter import messagebox
import pandas as pd
from tkinter import *
from tkinter import ttk
import mysql.connector as sqlc
from PIL import Image, ImageTk



# Config the GUI (Login Window)
root = Tk()
root.title('ABLORH DATA FINDER')
root.geometry("700x300")
root.iconbitmap("C:\\Users\\Gwendarling\\DarlinGit\\Images\\med.ico")
root.resizable(False, False)

# Set a background image
bg = ImageTk.PhotoImage(Image.open("C:\\Users\\Gwendarling\\DarlinGit\\Images\\BGI.jpg"))

canv = Canvas(root, width=500, height=300)
canv.pack(fill="both", expand=True)
canv.create_image(270, 0, image=bg, anchor="nw")

# Create Login frame
# Add a profile picture
log_img = Image.open("C:\\Users\\Gwendarling\\DarlinGit\\Images\\mission.png")
resized = log_img.resize((170,85), Image.ANTIALIAS)
new_pic = ImageTk.PhotoImage(resized)
label = Label(root, image=new_pic, highlightcolor="red", borderwidth=0)

log_img_window = canv.create_window(45, 40, anchor="nw", window=label)

# Create login function
def logpw():
    """Gets the data entered in the password entry and, if it is correct,
    destroys the login window and opens the Data Finder window"""

    global emr,nbg,ncanv,add_p,addp_img,showp_img,addr_img,\
           showr_img,ext_img,extn,ap,id,cnx,mycursor, pid,\
           name,pname,surname,psurname,bd,pbd,age,page,\
           psex,add_patient,idbox
    
    pssw = pw.get()
    
    if pssw == "q":
        root.destroy()
        
        # Store every ID of every patient successfully added to the database
        idbox = []
        
        # Open Data Finder window
        emr = Tk()
        emr.title("ABLORH DATA FINDER")
        emr.geometry("800x400")
        emr.iconbitmap("C:\\Users\\Gwendarling\\DarlinGit\\Images\\med2.ico")
        emr.resizable(False, False)
        
        # Set a background image
        nbg = ImageTk.PhotoImage(Image.open("C:\\Users\\Gwendarling\\DarlinGit\\Images\\bg5.jpg"))

        ncanv = Canvas(emr, width=700, height=400)
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

        # Drop existing tables and create patients table
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
            "Gender CHAR(1))")

        def create_data(test):
            """Using SQL and given a table name as an argument, 
            creates a table to store the data of any patient's tests."""
            
            mycursor.execute("CREATE TABLE {}(\n"
            "Test_ID INT PRIMARY KEY AUTO_INCREMENT,\n" # default data
            "Test_name VARCHAR(80),\n" # default data
            "Result FLOAT,\n" # input data
            "Units VARCHAR(80),\n" # default data
            "Reference_values CHAR(200),\n" # default data
            "Test_date DATE,\n" # input data
            "Patient_ID INT,\n" 
            "FOREIGN KEY (Patient_ID) REFERENCES PATIENT(ID) ON DELETE CASCADE\n" 
        ")".format(test))

        # Create tests tables
        create_data('COMPLETE_BLOOD_COUNT')
        create_data('BIOCHEMISTRY')
        create_data('ENZYMES')

        # Create exit function
        def extn():
            """Confirms with the user whether or not wants to really close the program"""

            x = messagebox.askyesno("","HEY DOC!\nARE TOU SURE YOU WANT TO EXIT?")
            if x == 1:
                emr.destroy()
                root.destroy()
            else: pass

        # Add clear_window function
        def clear_window():
            """Everytime a button is accidentally clicked by the user, 
            instead of showing that button's widgets above the widgets 
            shown currently, it deletes the old ones and displays the new ones"""

            # clear add patient window
            try:
                name.destroy()
                surname.destroy()
                id.destroy()
                bdl.destroy()
                bd_dy.destroy()
                bd_ms.destroy()
                bd_yr.destroy()
                age.destroy()
                female.destroy()
                male.destroy()
                submit_patient.destroy()
            except:
                pass

            # clear find patient(data) window
            try:
                checkid.destroy()
                checkok.destroy()
            except:
                pass

            # clear display patient data
            try:
                ptree.destroy()
                ok.destroy()
                lf.destroy()
            except:
                pass

            # clear find patient (add records) window
            try:
                rid.destroy()
                rok.destroy() 
            except:
                pass           

            # clear select test table(add records) window
            try:
                cbc.destroy()
                bch.destroy()
                enzy.destroy()
                tok.destroy()
                sel.destroy()
            except:
                pass

            # clear CBC entry tests window
            try:
                Rbc.destroy()
                Hb.destroy()
                Ht.destroy()
                tdl.destroy()
                td_dy.destroy()
                td_ms.destroy()
                td_yr.destroy()
                csubmit_test.destroy()
            except:
                pass

            # clear Biochemistry entry tests window
            try:
                Gc.destroy()
                Ct.destroy()
                Ua.destroy()
                tdl.destroy()
                td_dy.destroy()
                td_ms.destroy()
                td_yr.destroy()
                bsubmit_test.destroy()
            except:
                pass

            # clear Enzymes entry tests window
            try:
                ASTr.destroy()
                ALTr.destroy()
                GGTr.destroy()
                tdl.destroy()
                td_dy.destroy()
                td_ms.destroy()
                td_yr.destroy()
                esubmit_test.destroy()
            except:
                pass

            # clear find patient(tests) window
            try:
                tcheckid.destroy()
                tcheckok.destroy()
            except:
                pass
            
            
            # clear select test table(display) window
            try:
                show_sel.destroy()
                show_cbc.destroy()
                show_bch.destroy()
                show_enzy.destroy()
                show_tok.destroy()
                show_all.destroy()
            except:
                pass

            # clear test display window
            try:
                lft.destroy()
                ttree.destroy()
                btn.destroy()
            except:
                pass



        # ADD NEW PATIENT DATA----------------------------------------------------------------------------------------------------------------------------------
        
        # Create ap function
        def ap():
            """When the Add-patient button is clicked this 
            function calls other functions in order to 
            successfully add new patient's data to the database"""

            global id,pid,name,pname,surname,psurname,\
                   bd,pbd,age,page,psex,add_patient,\
                   submit_patient,gender,female,male,\
                   idbox,bd_yr,bd_ms,bd_dy,bdl,sumbitp_img

            clear_window()
            

            # Create dob function
            def dob(e):
                """Gets the data entered by the day entry widget
                and assign it to a variable. If the (string) number 
                is between 1 and 9 it is stored in 01-09 format
                in order to correctly add it to the database"""

                global d, dy_s 
                
                d = bd_dy.get()
                dy_s = d

                if d in ("1","2","3","4","5","6","7","8","9"):
                    dy_s = "0"+ d
                
            # Create mob function
            def mob(e):
                """Gets the data entered by the month entry widget
                and assign it to a variable. It changes the month
                name by a (string) number in format 01-12 in order 
                to correctly add it to the database"""

                global mth_s

                mth_s = bd_ms.get()
                
                if mth_s == "January":
                    mth_s = "01"
                elif mth_s == "February":
                    mth_s = "02"
                elif mth_s == "March":
                    mth_s = "03"
                elif mth_s == "April":
                    mth_s = "04"
                elif mth_s == "May":
                    mth_s = "05"
                elif mth_s == "June":
                    mth_s = "06"
                elif mth_s == "July":
                    mth_s = "07"
                elif mth_s == "August":
                    mth_s = "08"
                elif mth_s == "September":
                    mth_s = "09"
                elif mth_s == "October":
                    mth_s = "10"
                elif mth_s == "November":
                    mth_s = "11"
                elif mth_s == "December":
                    mth_s = "12"

            # Create yob function
            def yob(e):
                """Gets the data entered by the year entry widget
                and assign it to a variable in order to correctly 
                add it to the database"""

                global yr_s

                yr_s = bd_yr.get()

            # Create the data boxes
            id = Entry(emr, font=("Helvetica",13), bd=2, bg="#DEEDEA")
            id.insert(0, "Enter patient's ID")
            
            ncanv.create_window(150, 60, anchor="nw", window=id)

            name = Entry(emr, font=("Helvetica",13), bd=2, bg="#DEEDEA")
            name.insert(0, "Patient's name")
            
            ncanv.create_window(150, 125, anchor="nw", window=name)

            surname = Entry(emr, font=("Helvetica",13), bd=2, bg="#DEEDEA")
            surname.insert(0, "Patient's last name")

            ncanv.create_window(150, 185, anchor="nw", window=surname)

            age = Entry(emr, font=("Helvetica",13), bd=2, bg="#DEEDEA")
            age.insert(0, "Patient's age")
            
            ncanv.create_window(410, 125, anchor="nw", window=age)

            gender = StringVar()
            gender.set(' ')
            female = Radiobutton(emr, text="Female", variable=gender, value='F', font=("Helvetica",12), bg="#DEEDEA")
            male = Radiobutton(emr, text="Male", variable=gender, value='M', font=("Helvetica",12), bg="#DEEDEA")
            ncanv.create_window(410, 185, anchor="nw", window=female)
            ncanv.create_window(530, 185, anchor="nw", window=male)


            bdl = Label(emr, font=("Helvetica",13), bd=2, text="Date of birth", bg="#DEEDEA")
            
            dy = list(range(1,32))

            ms = ["January", "February", "March", "April",
                    "May", "June", "July", "August",
                    "September", "October", "November", "December"]

            yr = list(reversed(range(1900,2023)))


            bd_dy = ttk.Combobox(emr, value=dy, width=5)
            bd_dy.set("DAY")

            bd_ms = ttk.Combobox(emr, value=ms, width=8)
            bd_ms.set("MONTH")

            bd_yr = ttk.Combobox(emr, value=yr, width=5)
            bd_yr.set("YEAR")
            

            
            ncanv.create_window(450, 40, anchor="nw", window=bdl)

            ncanv.create_window(410, 65, anchor="nw", window=bd_dy)

            ncanv.create_window(465, 65, anchor="nw", window=bd_ms)

            ncanv.create_window(540, 65, anchor="nw", window=bd_yr)


            # Create submit-patient button
            sumbitp_img = PhotoImage(file="C:\\Users\\Gwendarling\\DarlinGit\\Images\\addp.png")
            submit_patient = Button(emr, width=180, height=60, text='ADD\nNEW PATIENT', command=add_patient, \
                font=("Helvetica",12), bg="#DEEDEA", image=sumbitp_img, compound="left")
            ncanv.create_window(270, 280, anchor="nw", window=submit_patient)

        
            # Define entry_clear function
            """Clear the text inside the entry boxes when the user clicks inside"""

            def entry_clear(e):
                if id.get() == "Enter patient's ID":
                    id.delete(0, END)
            def entry_clear2(e):
                if name.get() == "Patient's name":
                    name.delete(0, END)
            def entry_clear3(e):
                if surname.get() == "Patient's last name":
                    surname.delete(0, END)
            def entry_clear4(e):
                if age.get() == "Patient's age":
                    age.delete(0, END)
            
                

            # Bind the entry and combo boxes
            id.bind("<Button-1>", entry_clear )
            name.bind("<Button-1>", entry_clear2 )
            surname.bind("<Button-1>", entry_clear3 )
            bd_dy.bind("<<ComboboxSelected>>", dob )
            bd_ms.bind("<<ComboboxSelected>>", mob )
            bd_yr.bind("<<ComboboxSelected>>", yob )
            age.bind("<Button-1>", entry_clear4 )
            


        # Create submit-patient function
        def add_patient():
            """Gets the data given by the user and tries to add it 
            to the database. Whether or not the process goes well 
            a message appears to inform the user"""
        
            global pid,pname,psurname,pbd,page,psex,bd

            pid = id.get()
            pname = name.get()
            psurname = surname.get()
            bd = "{}-{}-{}".format(yr_s, mth_s, dy_s)
            pbd = bd
            page = age.get()
            psex = gender.get()

            

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
                (pid, pname.upper(),psurname.upper(), pbd, page, psex))

                # commit changes
                cnx.commit()

                messagebox.showinfo('GOOD NEWS! :)','PATIENT SUCCESSFULLY  ADDED!')

                idbox.append(pid)
                
            except:
                messagebox.showerror('BAD NEWS :(','IT HAS BEEN AN ERROR ADDING THIS PATIENT')

            # close connection
            cnx.close()

            # destroy the entry boxes and submit button
            name.destroy()
            surname.destroy()
            id.destroy()
            bdl.destroy()
            bd_dy.destroy()
            bd_ms.destroy()
            bd_yr.destroy()
            age.destroy()
            female.destroy()
            male.destroy()
            submit_patient.destroy()


        # SEARCH AND DISPLAY PATIENT DATA-------------------------------------------------------------------------------------------------------------------------

        # Create show patients records function
        def display():
            """When the Search-patient button is clicked this 
            function calls other functions in order to 
            display a patient's data"""

            global checkid, cnx, checkok, checkok_img

            clear_window()

            # Create the id box
            checkid = Entry(emr, font=("Helvetica",13), bd=2, bg="#87BFB5")
            checkid.insert(0, "Enter patient's ID")
            
            ncanv.create_window(290, 170, anchor="nw", window=checkid)

            # Define id_clear function
            def id_clear(e):
                if checkid.get() == "Enter patient's ID":
                    checkid.delete(0, END)

            # Bind the id box
            checkid.bind("<Button-1>", id_clear )

            # Create ok button
            checkok_img = PhotoImage(file="C:\\Users\\Gwendarling\\DarlinGit\\Images\\find.png")
            checkok = Button(emr, text="FIND\nPATIENT", font=("Helvetica",13), command=checkokr,\
                 image=checkok_img, compound="left", width=180, height=70, bg="#87BFB5")
            ncanv.create_window(290, 250, anchor="nw", window=checkok)
            

        
        # Check if patient in database
        def checkokr():
            """Ask for a patient's ID in order to check whether or not
            is in the database. If not, a message informs the user.
            If patient in database, a treeview appears to show the 
            patient's data"""
            
            global pcheckid, ok_img, ptree, ok, lf

            pcheckid = checkid.get()
            
            if pcheckid in idbox:
                checkid.destroy()
                checkok.destroy()

                # establish connection to the database
                cnx = sqlc.connect(
                user="root",
                password="TheDoctor3005",
                host="localhost",
                database="perez"
            )
                cur = cnx.cursor()

                cur.execute("SELECT * FROM PATIENT WHERE ID = {}".format(pcheckid))
                show = cur.fetchall()
                
                # Create a Label Frame
                lf = LabelFrame(ncanv, width=400, height=200, text="PATIENT", bg="#87BFB5")
                lf.pack()
                
                # Create the treeview 
                ptree = ttk.Treeview(lf, height=1)
                ptree.pack()

                # Define the columns
                ptree["columns"] = ("ID", "NAME", "LASTNAME", "DOB", "AGE", "GENDER")

                # Format the columns
                ptree.column("#0", width=0, stretch=NO)
                ptree.column("ID", width=80 , anchor="center")
                ptree.column("NAME", width=120, anchor="w")
                ptree.column("LASTNAME", width=120, anchor="w")
                ptree.column("DOB", width=100, anchor="center")
                ptree.column("AGE", width=40, anchor="center")
                ptree.column("GENDER", width=60, anchor="center")
                

                # Define the headings
                ptree.heading("#0", text="")
                ptree.heading("ID", text="ID", anchor="center")
                ptree.heading("NAME", text="NAME", anchor="w")
                ptree.heading("LASTNAME", text="LAST NAME", anchor="w")
                ptree.heading("DOB", text="DATE OF BIRTH", anchor="center")
                ptree.heading("AGE", text="AGE", anchor="center")
                ptree.heading("GENDER", text="GENDER", anchor="center")
                
                # Add DB data to the screen
                count = 0

                for record in show:
                    ptree.insert(parent="", index="end", iid=count, \
                                text="", values=(record[0], record[1], \
                                record[2], record[3], record[4], record[5]))
                    count += 1

                # Display the results
                ncanv.create_window(80, 100, anchor="nw", window=lf)

                # Close connection
                cur.close()

                # Define Ok button function
                def okf():
                    ptree.destroy()
                    ok.destroy()
                    lf.destroy()
                
                # Create OK button
                ok_img = PhotoImage(file="C:\\Users\\Gwendarling\\DarlinGit\\Images\\done.png")
                ok = Button(emr, text="DONE", font=("Helvetica",13), command=okf, \
                    image=ok_img, compound="left", width=120, height=30, bg="#87BFB5")
                ncanv.create_window(300, 250, anchor="nw", window=ok)
            
            else:
                messagebox.showerror("BAD NEWS :(","NO PATIENT IN DATABASE WITH THIS ID NUMBER")
                checkid.destroy()
                checkok.destroy()


           
        # ADD TEST DATA-----------------------------------------------------------------------------------------------------------------------------------------

        # Create add-records function
        def addr():
            """When the Add-tests button is clicked this 
            function calls other functions in order to 
            add patient's tests data to the database"""

            global rid,prid,rok,rok_img

            clear_window()
            
            # Create the id check box
            rid = Entry(emr, font=("Helvetica",13), bd=2, bg="#DEEDEA")
            rid.insert(0, "Enter patient's ID")
            
            ncanv.create_window(290, 170, anchor="nw", window=rid)

            # Define id_clear function
            def id_clear(e):
                if rid.get() == "Enter patient's ID":
                    rid.delete(0, END)

            # Bind the id box
            rid.bind("<Button-1>", id_clear )

            # create ok button
            rok_img = PhotoImage(file="C:\\Users\\Gwendarling\\DarlinGit\\Images\\find.png")
            rok = Button(emr, text="CHECK", font=("Helvetica",13), command=okr,\
                 image=rok_img, compound="left", width=180, height=70, bg="#DEEDEA")
            ncanv.create_window(290, 250, anchor="nw", window=rok)

        # Check if patient in database
        def okr():
            """Ask for a patient's ID in order to check whether or not
            is in the database. If not, a message informs the user.
            If patient in database, radiobuttons appears in order 
            to select the test you want to add data in"""

            global prid,okt,tok,tokk_img,sumbitp_img, \
                cbc, bch, enzy, sel

            prid = rid.get()
            sumbitp_img = PhotoImage(file="C:\\Users\\Gwendarling\\DarlinGit\\Images\\addt.png")
            
            # create ok function
            def okt():
                
                global Rbc, Hb, Ht, csubmit_test, \
                    Gc, Ct, Ua, bsubmit_test, \
                       ASTr, ALTr, GGTr, esubmit_test

                # Clear the window
                cbc.destroy()
                bch.destroy()
                enzy.destroy()
                tok.destroy()
                sel.destroy()

                # Add data depending on the test selected
                test = tests.get()

                # Create dot function
                def dot(e):
                    global dt, dy_t 
                    
                    dt = td_dy.get()
                    dy_t = dt

                    if dt in ("1","2","3","4","5","6","7","8","9"):
                        dy_t = "0"+ dt
                    
                # Create mot function
                def mot(e):
                    global mth_t

                    mth_t = td_ms.get()
                    
                    if mth_t == "January":
                        mth_t = "01"
                    elif mth_t == "February":
                        mth_t = "02"
                    elif mth_t == "March":
                        mth_t = "03"
                    elif mth_t == "April":
                        mth_t = "04"
                    elif mth_t == "May":
                        mth_t = "05"
                    elif mth_t == "June":
                        mth_t = "06"
                    elif mth_t == "July":
                        mth_t = "07"
                    elif mth_t == "August":
                        mth_t = "08"
                    elif mth_t == "September":
                        mth_t = "09"
                    elif mth_t == "October":
                        mth_t = "10"
                    elif mth_t == "November":
                        mth_t = "11"
                    elif mth_t == "December":
                        mth_t = "12"

                # Create yot function
                def yot(e):
                    global yr_t

                    yr_t = td_yr.get()
                
                # Create display-tests_date function
                def dt_date():
                    """Creates and displays a label and comboboxes in order to
                    select the date each group of tests were made"""

                    global tdl,tdy,tms,\
                        tyr,td_dy,td_ms,td_yr

                    tdl = Label(emr, font=("Helvetica",14), bd=2, text="Test date", bg="#DEEDEA")
            
                    tdy = list(range(1,32))

                    tms = ["January", "February", "March", "April",
                            "May", "June", "July", "August",
                            "September", "October", "November", "December"]

                    tyr = list(reversed(range(1900,2023)))


                    td_dy = ttk.Combobox(emr, value=tdy, width=5)
                    td_dy.set("DAY")

                    td_ms = ttk.Combobox(emr, value=tms, width=8)
                    td_ms.set("MONTH")

                    td_yr = ttk.Combobox(emr, value=tyr, width=5)
                    td_yr.set("YEAR")
                    

                    ncanv.create_window(305, 140, anchor="nw", window=tdl)

                    ncanv.create_window(265, 165, anchor="nw", window=td_dy)

                    ncanv.create_window(320, 165, anchor="nw", window=td_ms)

                    ncanv.create_window(395, 165, anchor="nw", window=td_yr)


                if test == 'COMPLETE BLOOD COUNT':


                    # create test boxes
                    Rbc = Entry(emr, font=("Helvetica",13), bd=2, bg="#DEEDEA")
                    Rbc.insert(0, "Red blood cells (RBC)")
                    
                    ncanv.create_window(265, 20, anchor="nw", window=Rbc)

                    Hb = Entry(emr, font=("Helvetica",13), bd=2, bg="#DEEDEA")
                    Hb.insert(0, "Hemoglobin (Hb)")
                    
                    ncanv.create_window(265, 60, anchor="nw", window=Hb)

                    Ht = Entry(emr, font=("Helvetica",13), bd=2, bg="#DEEDEA")
                    Ht.insert(0, "Hematocrit")
                    
                    ncanv.create_window(265, 100, anchor="nw", window=Ht)

                    dt_date()

                    # Create submit-test functions
                    def add_cbc():
                        """Gets the data given by the user and tries to add it 
                        to the COMPLETE BLOOD COUNT table. Whether or not the 
                        process goes well a message appears to inform the user"""

                        global tRbc,tHb,tHt, t

                        t = "{}-{}-{}".format(yr_t, mth_t, dy_t)

                        tRbc = Rbc.get()
                        tHb = Hb.get()
                        tHt = Ht.get()
                        tctd = t

                        cts = [['Red blood cells (RBC)','10^6/µl','(4.3-5.6)'],
                                ['Hemoglobin (Hb)','g/dL','(13.7-16.5)'],
                                ['Hematocrit','%','(40-50)']] 

                        cdata = [cts[0][0], cts[0][1], cts[0][2]]
                        cdata2 = [cts[1][0], cts[1][1], cts[1][2]]
                        cdata3 = [cts[2][0], cts[2][1], cts[2][2]]

                        try:
                            mycursor.execute("INSERT INTO COMPLETE_BLOOD_COUNT(Test_name,Result,Units,Reference_values,Test_date,Patient_ID)\n"
                            "VALUES(%s,%s,%s,%s,%s,%s)", (cdata[0],tRbc,cdata[1],cdata[2],tctd,prid))

                            mycursor.execute("INSERT INTO COMPLETE_BLOOD_COUNT(Test_name,Result,Units,Reference_values,Test_date,Patient_ID)\n"
                            "VALUES(%s,%s,%s,%s,%s,%s)", (cdata2[0],tHb,cdata2[1],cdata2[2],tctd,prid))

                            mycursor.execute("INSERT INTO COMPLETE_BLOOD_COUNT(Test_name,Result,Units,Reference_values,Test_date,Patient_ID)\n"
                            "VALUES(%s,%s,%s,%s,%s,%s)", (cdata3[0],tHt,cdata3[1],cdata3[2],tctd,prid))

                            messagebox.showinfo("GOOD NEWS! :)","DATA SUCCESSFULLY ADDED!")

                            # commit the changes
                            cnx.commit()
                            
                        except:
                            messagebox.showerror("BAD NEWS :(","PROCESS FAILED.")
                        
                        finally:
                            # Clear the window
                            Rbc.destroy()
                            Hb.destroy()
                            Ht.destroy()
                            tdl.destroy()
                            td_dy.destroy()
                            td_ms.destroy()
                            td_yr.destroy()
                            csubmit_test.destroy()

                    # Create submit-test button
                    csubmit_test = Button(emr, width=160, height=65, text='ADD\nTESTS', font=("Helvetica",13), \
                        command=add_cbc, bg="#DEEDEA", image=sumbitp_img, compound="left")
                    ncanv.create_window(270, 290, anchor="nw", window=csubmit_test)
                
                    # Define test_clear function
                    def test_clear(e):
                        if Rbc.get() == "Red blood cells (RBC)":
                            Rbc.delete(0, END)
                    def test_clear2(e):
                        if Hb.get() == "Hemoglobin (Hb)":
                            Hb.delete(0, END)
                    def test_clear3(e):
                        if Ht.get() == "Hematocrit":
                            Ht.delete(0, END)
                    

                    # Bind the entry boxes
                    Rbc.bind("<Button-1>", test_clear )
                    Hb.bind("<Button-1>", test_clear2 )
                    Ht.bind("<Button-1>", test_clear3 )
                    td_dy.bind("<<ComboboxSelected>>", dot )
                    td_ms.bind("<<ComboboxSelected>>", mot )
                    td_yr.bind("<<ComboboxSelected>>", yot )
                
                if test == 'BIOCHEMISTRY':

                    # create test boxes
                    Gc = Entry(emr, font=("Helvetica",13), bd=2, bg="#DEEDEA")
                    Gc.insert(0, "Glucose")
                    
                    ncanv.create_window(265, 20, anchor="nw", window=Gc)

                    Ct = Entry(emr, font=("Helvetica",13), bd=2, bg="#DEEDEA")
                    Ct.insert(0, "Creatinine")
                    
                    ncanv.create_window(265, 60, anchor="nw", window=Ct)

                    Ua = Entry(emr, font=("Helvetica",13), bd=2, bg="#DEEDEA")
                    Ua.insert(0, "Uric acid")
                    
                    ncanv.create_window(265, 100, anchor="nw", window=Ua)

                    dt_date()

                    # Create submit-test function
                    def add_bio():
                        """Gets the data given by the user and tries to add it 
                        to the BIOCHEMISTRY table. Whether or not the process 
                        goes well a message appears to inform the user"""

                        global tGc,tCt,tUa

                        t = "{}-{}-{}".format(yr_t, mth_t, dy_t)

                        tGc = Gc.get()
                        tCt = Ct.get()
                        tUa = Ua.get()
                        tbtd = t

                        bts = [['Glucose','mg/dL','(74-109)'],
                            ['Creatinine','mg/dL','(0.7-1.2)'],
                            ['Uric acid','mg/dL','(3.4-7.0)']]

                        bdata = [bts[0][0], bts[0][1], bts[0][2]]
                        bdata2 = [bts[1][0], bts[1][1], bts[1][2]]
                        bdata3 = [bts[2][0], bts[2][1], bts[2][2]]

                        try:
                            mycursor.execute("INSERT INTO BIOCHEMISTRY(Test_name,Result,Units,Reference_values,Test_date,Patient_ID)\n"
                            "VALUES(%s,%s,%s,%s,%s,%s)", (bdata[0],tGc,bdata[1],bdata[2],tbtd,prid))

                            mycursor.execute("INSERT INTO BIOCHEMISTRY(Test_name,Result,Units,Reference_values,Test_date,Patient_ID)\n"
                            "VALUES(%s,%s,%s,%s,%s,%s)", (bdata2[0],tCt,bdata2[1],bdata2[2],tbtd,prid))

                            mycursor.execute("INSERT INTO BIOCHEMISTRY(Test_name,Result,Units,Reference_values,Test_date,Patient_ID)\n"
                            "VALUES(%s,%s,%s,%s,%s,%s)", (bdata3[0],tUa,bdata3[1],bdata3[2],tbtd,prid))

                            messagebox.showinfo("GOOD NEWS! :)","DATA SUCCESSFULLY ADDED!")

                            # commit the changes
                            cnx.commit()

                        except:
                            messagebox.showerror("BAD NEWS :(","PROCESS FAILED.")
                        
                        finally:
                            # Clear the window
                            Gc.destroy()
                            Ct.destroy()
                            Ua.destroy()
                            tdl.destroy()
                            td_dy.destroy()
                            td_ms.destroy()
                            td_yr.destroy()
                            bsubmit_test.destroy()

                    # Create submit-test button
                    bsubmit_test = Button(emr, width=160, height=65, text='ADD\nTESTS', font=("Helvetica",13),\
                         command=add_bio, bg="#DEEDEA", image=sumbitp_img, compound="left")
                    ncanv.create_window(270, 290, anchor="nw", window=bsubmit_test)
                
                    # Define test_clear function
                    def test_clear(e):
                        if Gc.get() == "Glucose":
                            Gc.delete(0, END)
                    def test_clear2(e):
                        if Ct.get() == "Creatinine":
                            Ct.delete(0, END)
                    def test_clear3(e):
                        if Ua.get() == "Uric acid":
                            Ua.delete(0, END)
                

                    # Bind the entry boxes
                    Gc.bind("<Button-1>", test_clear )
                    Ct.bind("<Button-1>", test_clear2 )
                    Ua.bind("<Button-1>", test_clear3 )
                    td_dy.bind("<<ComboboxSelected>>", dot )
                    td_ms.bind("<<ComboboxSelected>>", mot )
                    td_yr.bind("<<ComboboxSelected>>", yot )

                if test == "ENZYMES":

                    # create test boxes
                    ASTr = Entry(emr, font=("Helvetica",13), bd=2, bg="#DEEDEA")
                    ASTr.insert(0, "AST/GOT")
                    
                    ncanv.create_window(265, 20, anchor="nw", window=ASTr)

                    ALTr = Entry(emr, font=("Helvetica",13), bd=2, bg="#DEEDEA")
                    ALTr.insert(0, "ALT/GPT")
                    
                    ncanv.create_window(265, 60, anchor="nw", window=ALTr)

                    GGTr = Entry(emr, font=("Helvetica",13), bd=2, bg="#DEEDEA")
                    GGTr.insert(0, "GGT")
                    
                    ncanv.create_window(265, 100, anchor="nw", window=GGTr)

                    dt_date()

                    # Create submit-test function
                    def add_enzy():
                        """Gets the data given by the user and tries to add it 
                        to the ENZYMES table. Whether or not the process goes 
                        well a message appears to inform the user"""

                        global tASTr,tALTr,tGGTr

                        t = "{}-{}-{}".format(yr_t, mth_t, dy_t)

                        tASTr = ASTr.get()
                        tALTr = ALTr.get()
                        tGGTr = GGTr.get()
                        tetd = t

                        ets = [['AST','UI/L','(5-40)'],
                            ['ALT','UI/L','(5-41)'],
                            ['Gamma-GT','UI/L','(<60)']]

                        edata = [ets[0][0], ets[0][1], ets[0][2]]
                        edata2 = [ets[1][0], ets[1][1], ets[1][2]]
                        edata3 = [ets[2][0], ets[2][1], ets[2][2]]

                        try:
                            mycursor.execute("INSERT INTO ENZYMES(Test_name,Result,Units,Reference_values,Test_date,Patient_ID)\n"
                            "VALUES(%s,%s,%s,%s,%s,%s)", (edata[0],tASTr,edata[1],edata[2],tetd,prid))

                            mycursor.execute("INSERT INTO ENZYMES(Test_name,Result,Units,Reference_values,Test_date,Patient_ID)\n"
                            "VALUES(%s,%s,%s,%s,%s,%s)", (edata2[0],tALTr,edata2[1],edata2[2],tetd,prid))

                            mycursor.execute("INSERT INTO ENZYMES(Test_name,Result,Units,Reference_values,Test_date,Patient_ID)\n"
                            "VALUES(%s,%s,%s,%s,%s,%s)", (edata3[0],tGGTr,edata3[1],edata3[2],tetd,prid))

                            messagebox.showinfo("GOOD NEWS! :)","DATA SUCCESSFULLY ADDED!")

                            # commit the changes
                            cnx.commit()

                        except:
                            messagebox.showerror("BAD NEWS :(","PROCESS FAILED.")
                        
                        finally:
                            # Clear the window
                            ASTr.destroy()
                            ALTr.destroy()
                            GGTr.destroy()
                            tdl.destroy()
                            td_dy.destroy()
                            td_ms.destroy()
                            td_yr.destroy()
                            esubmit_test.destroy()

                    # Create submit-test button
                    esubmit_test = Button(emr, width=160, height=65, text='ADD\nTESTS', font=("Helvetica",13), \
                        command=add_enzy, bg="#DEEDEA", image=sumbitp_img, compound="left")
                    ncanv.create_window(270, 290, anchor="nw", window=esubmit_test)
                
                    # Define test_clear function
                    def test_clear(e):
                        if ASTr.get() == "AST/GOT":
                            ASTr.delete(0, END)
                    def test_clear2(e):
                        if ALTr.get() == "ALT/GPT":
                            ALTr.delete(0, END)
                    def test_clear3(e):
                        if GGTr.get() == "GGT":
                            GGTr.delete(0, END)
                    

                    # Bind the entry boxes
                    ASTr.bind("<Button-1>", test_clear )
                    ALTr.bind("<Button-1>", test_clear2 )
                    GGTr.bind("<Button-1>", test_clear3 )
                    td_dy.bind("<<ComboboxSelected>>", dot )
                    td_ms.bind("<<ComboboxSelected>>", mot )
                    td_yr.bind("<<ComboboxSelected>>", yot )

            if prid in idbox:
                rid.destroy()
                rok.destroy()
                
                # Show test tables to select
                sel = Label(emr, text="SELECT THE TEST YOU WANT TO ADD DATA IN", font=("Helvetica",15), bg="#DEEDEA")
                ncanv.create_window(110, 70, anchor="nw", window=sel)
                
                tests = StringVar()
                tests.set(" ")
                
                cbc = Radiobutton(emr, text='COMPLETE BLOOD COUNT', variable=tests, \
                    value='COMPLETE BLOOD COUNT', font=("Helvetica",12), bg="#DEEDEA")
                bch = Radiobutton(emr, text="BIOCHEMISTRY", variable=tests, \
                    value='BIOCHEMISTRY', font=("Helvetica",12), bg="#DEEDEA")
                enzy = Radiobutton(emr, text="ENZYMES", variable=tests, \
                    value='ENZYMES', font=("Helvetica",12), bg="#DEEDEA")
                
                ncanv.create_window(150, 160, anchor="nw", window=cbc)
                ncanv.create_window(150, 200, anchor="nw", window=bch)
                ncanv.create_window(420, 160, anchor="nw", window=enzy)

                # create ok button
                tokk_img = PhotoImage(file="C:\\Users\\Gwendarling\\DarlinGit\\Images\\done.png")
                tok = Button(emr, text="OK", font=("Helvetica",13), command=okt, \
                    image=tokk_img, compound="left", width=120, height=30, bg="#DEEDEA")
                ncanv.create_window(300, 250, anchor="nw", window=tok)


            else:
                rid.destroy()
                rok.destroy() 
                messagebox.showerror("ERROR","WRONG ID OR NO PATIENT IN CURRENT DATABASE")  


        # SEARCH AND DISPLAY TESTS DATA----------------------------------------------------------------------------------------------------------------------------

        # Show tests by patient ID
        def tdisplay():
            """When the Search-tests button is clicked this 
            function calls other functions in order to 
            display a patient's tests data"""

            global tcheckid, cnx, tcheckok, tcheckok_img

            clear_window()

            # Create the id box
            tcheckid = Entry(emr, font=("Helvetica",13), bd=2, bg="#87BFB5")
            tcheckid.insert(0, "Enter patient's ID")
            
            ncanv.create_window(290, 170, anchor="nw", window=tcheckid)

            # Define id_clear function
            def tid_clear(e):
                if tcheckid.get() == "Enter patient's ID":
                    tcheckid.delete(0, END)

            # Bind the id box
            tcheckid.bind("<Button-1>", tid_clear )

            # create ok button
            tcheckok_img = PhotoImage(file="C:\\Users\\Gwendarling\\DarlinGit\\Images\\find.png")
            tcheckok = Button(emr, text="CHECK", font=("Helvetica",13), \
                command=tcheckokr, image=tcheckok_img, compound="left", width=180, height=70, bg="#87BFB5")
            ncanv.create_window(290, 250, anchor="nw", window=tcheckok)
            

        # Check if patient in database
        def tcheckokr():
            """Ask for a patient's ID in order to check whether or not
            is in the database. If not, a message informs the user.
            If patient in database, radiobuttons appears in order 
            to select the test you want to show data from.
            We can show records by table or also all the records 
            that patient has"""

            global tpcheckid, showtok_img, show_sel, \
                show_cbc, show_bch, show_enzy, show_tok, \
                    show_all

            tpcheckid = tcheckid.get()
            

            if tpcheckid in idbox:
                tcheckid.destroy()
                tcheckok.destroy()

                # Create a function to display results in Treeview form
                def tview(fetch):
                    """Creates a treeview to show the data"""

                    global ttree,lft

                    # Create the Label Frame
                    lft = LabelFrame(ncanv, text="TESTS DATA", bg="#87BFB5")
                    lft.pack()

                    # Create the scrollbar
                    tsb = Scrollbar(lft)
                    tsb.pack(side=RIGHT, fill=Y)

                    # Create the Treeview 
                    ttree = ttk.Treeview(lft, yscrollcommand=tsb.set, height=6)
                    ttree.pack()

                    # Configure the scrollbar
                    tsb.config(command=ttree.yview)

                    # Define the columns
                    ttree["columns"] = ("NAME", "LASTNAME", "TESTNAME", "RESULTS", "UNITS", "REF_VALUES", "TESTDATE", "P_ID")

                    # Format the columns
                    ttree.column("#0", width=0, stretch=NO)
                    
                    ttree.column("NAME", width=100, anchor="w")
                    ttree.column("LASTNAME", width=100, anchor="w")
                    ttree.column("TESTNAME", width=110, anchor="w")
                    ttree.column("RESULTS", width=60, anchor="center")
                    ttree.column("UNITS", width=50, anchor="center")
                    ttree.column("REF_VALUES", width=60, anchor="center")
                    ttree.column("TESTDATE", width=100, anchor="center")
                    ttree.column("P_ID", width=80, anchor="center")
                    

                    # Define the headings
                    ttree.heading("#0", text="")
                    ttree.heading("NAME", text="NAME", anchor="w")
                    ttree.heading("LASTNAME", text="LAST NAME", anchor="w")
                    ttree.heading("TESTNAME", text="TEST", anchor="w")
                    ttree.heading("RESULTS", text="RESULTS", anchor="center")
                    ttree.heading("UNITS", text="UNITS", anchor="center")
                    ttree.heading("REF_VALUES", text="REF. VALUES", anchor="center")
                    ttree.heading("TESTDATE", text="TEST DATE", anchor="center")
                    ttree.heading("P_ID", text="PATIENT ID", anchor="center")
                    
                    # Add DB data to the screen
                    count = 0

                    for record in fetch:
                        ttree.insert(parent="", index="end", iid=count,\
                                    text="", values=(record[0], record[1],\
                                    record[2], record[3], record[4],\
                                    record[5],record[6], record[7]))
                        count += 1

                    # Display the results
                    ncanv.create_window(10, 20, anchor="nw", window=lft)


                # Create and display an OK button
                def ok_button(fetch):
                    global btn, btn_img
                    
                    if len(fetch) > 0:
                    
                            """If patient has records in the test selected, 
                            a treeview shows the data. Otherwise if patient 
                            has no data in that test, an error message informs 
                            the user and the window is cleared"""
                            
                            tview(fetch)

                            # create ok function
                            def tokf():
                                lft.destroy()
                                ttree.destroy()
                                btn.destroy()
                            
                            # create ok button
                            btn_img = PhotoImage(file="C:\\Users\\Gwendarling\\DarlinGit\\Images\\done.png")
                            btn = Button(emr, text="DONE", font=("Helvetica",13), command=tokf, \
                                image=btn_img, compound="left", width=120, height=30, bg="#87BFB5")
                            ncanv.create_window(300, 250, anchor="nw", window=btn)

                    else:
                        messagebox.showerror("SORRY :(","NO TEST DATA AVAILABLE")

                def show_okt():
                    """Displays the patient's tests data depending 
                    on the table selected by the user"""

                    pshow_tests = show_tests.get()

                    show_sel.destroy()
                    show_cbc.destroy()
                    show_bch.destroy()
                    show_enzy.destroy()
                    show_tok.destroy()
                    show_all.destroy()


                    if pshow_tests == 'COMPLETE BLOOD COUNT':

                        # establish connection to the database
                        cnx = sqlc.connect(
                        user="root",
                        password="TheDoctor3005",
                        host="localhost",
                        database="perez"
                    )
                    
    
                        ccur = cnx.cursor()
                        
                        ccur.execute("SELECT Name,Last_name,Test_name,Result,\
                                        Units,Reference_values,Test_date,Patient_ID \
                                        FROM PATIENT\
                                        JOIN COMPLETE_BLOOD_COUNT\
                                        ON ID = {}".format(tpcheckid))

                        cshow = ccur.fetchall()

                        
                        ok_button(cshow)
                    
                    
                    if pshow_tests == 'BIOCHEMISTRY':

                        # establish connection to the database
                        cnx = sqlc.connect(
                        user="root",
                        password="TheDoctor3005",
                        host="localhost",
                        database="perez"
                    )
                    
                        bcur = cnx.cursor()
                        
                        bcur.execute("SELECT Name,Last_name,Test_name,Result,\
                                        Units,Reference_values,Test_date,Patient_ID \
                                        FROM PATIENT\
                                        JOIN BIOCHEMISTRY\
                                        ON ID = {}".format(tpcheckid))

                        bshow = bcur.fetchall()
                        
                        ok_button(bshow)


                    if pshow_tests == 'ENZYMES':

                        # establish connection to the database
                        cnx = sqlc.connect(
                        user="root",
                        password="TheDoctor3005",
                        host="localhost",
                        database="perez"
                    )
                    
                        ecur = cnx.cursor()
                        
                        ecur.execute("SELECT Name,Last_name,Test_name,Result,\
                                        Units,Reference_values,Test_date,Patient_ID \
                                        FROM PATIENT\
                                        JOIN ENZYMES\
                                        ON ID = {}".format(tpcheckid))

                        eshow = ecur.fetchall()
                        
                        ok_button(eshow)

                    if pshow_tests == 'ALL':

                        # establish connection to the database
                        cnx = sqlc.connect(
                        user="root",
                        password="TheDoctor3005",
                        host="localhost",
                        database="perez"
                    )
                    
                        allcur = cnx.cursor()

                        allcur.execute("SELECT Name,Last_name,Test_name,Result,\
                                        Units,Reference_values,Test_date,Patient_ID \
                                        FROM PATIENT\
                                        JOIN COMPLETE_BLOOD_COUNT\
                                        ON ID = {0}\
                                        UNION\
                                        SELECT Name,Last_name,Test_name,Result,\
                                        Units,Reference_values,Test_date,Patient_ID \
                                        FROM PATIENT\
                                        JOIN BIOCHEMISTRY\
                                        ON ID = {0}\
                                        UNION\
                                        SELECT Name,Last_name,Test_name,Result,\
                                        Units,Reference_values,Test_date,Patient_ID \
                                        FROM PATIENT\
                                        JOIN ENZYMES\
                                        ON ID = {0}".format(tpcheckid))

                        allshow = allcur.fetchall()
                        
                        ok_button(allshow)


                # Show test tables to select
                show_sel = Label(emr, text="SELECT THE TEST YOU WANT TO SHOW DATA FROM", font=("Helvetica",15), bg="#87BFB5")
                ncanv.create_window(110, 70, anchor="nw", window=show_sel)
                
                show_tests = StringVar()
                show_tests.set(" ")
                
                show_cbc = Radiobutton(emr, text='COMPLETE BLOOD COUNT', variable=show_tests, \
                    value='COMPLETE BLOOD COUNT', font=("Helvetica",12), bg="#87BFB5")
                show_bch = Radiobutton(emr, text="BIOCHEMISTRY", variable=show_tests, \
                    value='BIOCHEMISTRY', font=("Helvetica",12), bg="#87BFB5")
                show_enzy = Radiobutton(emr, text="ENZYMES", variable=show_tests, \
                    value='ENZYMES', font=("Helvetica",12), bg="#87BFB5")
                show_all = Radiobutton(emr, text="SHOW ALL TESTS", variable=show_tests, \
                    value='ALL', font=("Helvetica",12), bg="#7DFEF8")
                
                ncanv.create_window(150, 160, anchor="nw", window=show_cbc)
                ncanv.create_window(150, 200, anchor="nw", window=show_bch)
                ncanv.create_window(420, 160, anchor="nw", window=show_enzy)
                ncanv.create_window(420, 200, anchor="nw", window=show_all)

                # create ok button
                showtok_img = PhotoImage(file="C:\\Users\\Gwendarling\\DarlinGit\\Images\\done.png")
                show_tok = Button(emr, text="DONE", font=("Helvetica",13), command=show_okt,\
                    image=showtok_img, compound="left", width=120, height=30, bg="#87BFB5")
                ncanv.create_window(300, 250, anchor="nw", window=show_tok)


            else:
                messagebox.showerror("SORRY :(","NO PATIENT IN DATABASE WITH THIS ID NUMBER")
                tcheckid.destroy()
                tcheckok.destroy()


        
              
        # Create the buttons
        addp_img = PhotoImage(file="C:\\Users\\Gwendarling\\DarlinGit\\Images\\add-user.png")
        add_p = Button(emr, width=92, height=70, image=addp_img, text="ADD\nPATIENT", \
            font=("Helvetica",7), compound="left", command=ap, bg="#DEEDEA")
        ncanv.create_window(700, 0, anchor="nw", window=add_p)
        
        showp_img = PhotoImage(file="C:\\Users\\Gwendarling\\DarlinGit\\Images\\find-user.png")
        show_p = Button(emr, width=92, height=70, image=showp_img, text="SEARCH\nPATIENT", \
            font=("Helvetica",7), compound="left", command=display, bg="#87BFB5")
        ncanv.create_window(700, 80, anchor="nw", window=show_p)
        
        addr_img = PhotoImage(file="C:\\Users\\Gwendarling\\DarlinGit\\Images\\medical-report.png")
        add_r = Button(emr, width=92, height=70, image=addr_img, text="ADD\nTESTS", \
            font=("Helvetica",7), compound="left", command=addr, bg="#DEEDEA")
        ncanv.create_window(700, 160, anchor="nw", window=add_r)
        
        showr_img = PhotoImage(file="C:\\Users\\Gwendarling\\DarlinGit\\Images\\optimization.png")
        show_r = Button(emr, width=92, height=70, image=showr_img, text="SEARCH\nTESTS", \
            font=("Helvetica",7), compound="left", command=tdisplay, bg="#87BFB5")
        ncanv.create_window(700, 240, anchor="nw", window=show_r)
        
        ext_img = PhotoImage(file="C:\\Users\\Gwendarling\\DarlinGit\\Images\\emergency-exit.png")
        ext = Button(emr, width=92, height=73, image=ext_img, command=extn, bg="red")
        ncanv.create_window(702, 321, anchor="nw", window=ext)

        emr.mainloop


        
    # When wrong password is entered, a message informs the user
    else: messagebox.showerror("SORRY","ACCESS DENIED\nWRONG PASSWORD")
    pw.delete(0, END)

# Add Login button
i = PhotoImage(file="C:\\Users\\Gwendarling\\DarlinGit\\Images\\Login-PNG.png")

logbtn = Button(root, image=i, borderwidth=0, command=logpw)
logbtnwindow = canv.create_window(10, 245, anchor="nw", window=logbtn)

# Create quit function
def xit():
    q = messagebox.askyesno("","HEY DOC!\nARE TOU SURE YOU WANT TO EXIT?")
    if q == 1:
        root.destroy()
    else: pass

# Add Quit button
q = PhotoImage(file="C:\\Users\\Gwendarling\\DarlinGit\\Images\\shutdown.png")

qbtn = Button(root, image=q, borderwidth=0, command=xit)
qwindow = canv.create_window(200, 243, anchor="nw", window=qbtn)

# Add Password entry
pw = Entry(root, font=("Helvetica",13), bd=2, bg="#DEEDEA")
pw.insert(0, "Enter your password")

pw_window = canv.create_window(40, 180, anchor="nw", window=pw)

# Define pw_clear function
def pw_clear(e):
    pw.delete(0, END)
    pw.config(show="*")

# Bind the entry box
pw.bind("<Button-1>", pw_clear )

# Add greeting message
greeting = Label(root, text="WELCOME DOCTOR!", font=("Bauhaus 93",15), fg="#87BFB5")
greeting_txt = canv.create_window(37, 140, anchor="nw", window=greeting)


root.mainloop()