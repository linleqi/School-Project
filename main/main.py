import mysql.connector as sql
import tkinter
from tkinter import ttk
import copy
import datetime
import random

global testList
testList = ["SAT", "TOEFL", "IELTS", "SAT Maths 2", "SAT Maths 1", "SAT Literature", "SAT Philosophy", "SAT Japanese", "SAT US History", "SAT World History", "JLPTN1", "JLPTN2", "JLPTN3", "JLPTN4", "JLPTN5"]
global subjectList
subjectList = ["Maths", "Physics", "Chemistry", "English", "Biology", "History", "Economics", "Entrepreneurship", "Accounting", "Computer Science", "Psychology"]

con = sql.connect(host="localhost", user = "root", passwd = "grade12", database = "PythonProject")
if (con.is_connected()):
    print("Connection is successfull!!")
else:
    print("Not connected!")
   
def update(Password, FirstName, LastName, Highschool, Undergraduate, Graduate, DOB, Sub1, Sub2, Sub3, Sub4, Sub5, Test1, Test2, Test3, Test4, Test5, Email):
    cursor=con.cursor()
    cursor.execute("SELECT * FROM AccDetails")
    for record in cursor.fetchall():
        print(record)
    print()

    cursor.execute("UPDATE AccDetails SET Password='{}', FirstName= '{}', LastName='{}', Highschool = '{}' ,Undergraduate='{}',Graduate='{}',DOB='{}',Sub1='{}',Sub2='{}',Sub3='{}',Sub4='{}',Sub5='{}',Test1='{}',Test2='{}',Test3='{}',Test4='{}',Test5='{}' WHERE Email = '{}'".format(Password, FirstName, LastName, Highschool, Undergraduate, Graduate, DOB, Sub1, Sub2, Sub3, Sub4, Sub5, Test1, Test2, Test3, Test4, Test5, Email))
    con.commit()

    cursor.execute("SELECT * FROM AccDetails")
    for record in cursor.fetchall():
        print(record)
    print()
    cursor.close()
#update(Password, FirstName, LastName, Highschool, Undergraduate, Graduate, DOB, Sub1, Sub2, Sub3, Sub4, Sub5, Test1, Test2, Test3, Test4, Test5, Email)

def updateprofile():
    window.configure(bg = "Blue")
    window.geometry("1200x500")
    
    # FRAME 3
    global frame5
    
   
    frame5 = tkinter.Frame(window, bg = "PaleTurquoise2", borderwidth = "1", padx = "25", pady = "35", relief = tkinter.GROOVE)
    font1 = ("Verdana", 15, "bold")
    font2 = ("Comic Sans MS", 15, "bold")

    Emaillbl = tkinter.Label(frame5, text = "Email:", bg = "PaleTurquoise1", fg = "Blue4", font = font1)
    Emaillbl.grid(row=0,column=0)
    global Email
    Email = tkinter.Entry(frame5, font = font2)
    Email.grid(row=0,column=1)
    Email.set()

    passwordlbl = tkinter.Label(frame5, text = "Password:", bg = "PaleTurquoise1", fg = "Blue4", font = font1)
    passwordlbl.grid(row=1,column=0)
    global Password
    Password = tkinter.Entry(frame5, show = "*", font = font2)
    Password.grid(row=1,column=1)

    firstnamelbl = tkinter.Label(frame5, text = "First Name:", bg = "PaleTurquoise1", fg = "Blue4", font = font1)
    firstnamelbl.grid(row=2,column=0)
    global FirstName
    FirstName = tkinter.Entry(frame5, font = font2)
    FirstName.grid(row=2,column=1)

    lastnamelbl = tkinter.Label(frame5, text = "Last Name:", bg = "PaleTurquoise1", fg = "Blue4", font = font1)
    lastnamelbl.grid(row=3,column=0)
    global LastName
    LastName = tkinter.Entry(frame5, font = font2)
    LastName.grid(row=3,column=1)

    cancel1=tkinter.Button(frame5, text = "Cancel", bg = "RoyalBlue1", font = font1, command = cancelBtnFunc)
    cancel1.grid(row=4,column=0)
    
    next1=tkinter.Button(frame5, text = "Next", bg = "RoyalBlue1", font = font1, command = nextBtnFunc1)
    next1.grid(row=4,column=1)

    global lblx
    lblx = tkinter.Label(window, bg = "blue", fg = "red")

    frame5.place(relx =0.5, rely=0.5,anchor=tkinter.CENTER)

    # FRAME 4
    global frame6
    frame6=tkinter.Frame(window, bg = "PaleTurquoise2", borderwidth = "1", padx = "15", pady = "15", relief = tkinter.GROOVE)

    hslbl = tkinter.Label(frame6, text = "High School:", bg = "PaleTurquoise1", fg = "Blue4", font = font1)
    hslbl.grid(row=0,column=0)
    global Highschool
    Highschool = tkinter.Entry(frame6, font = font2)
    Highschool.grid(row=0,column=1)
    
    uglbl = tkinter.Label(frame6, text = "Undergraduate School:", bg = "PaleTurquoise1", fg = "Blue4", font = font1)
    uglbl.grid(row=1,column=0)
    global Undergraduate
    Undergraduate = tkinter.Entry(frame6, font = font2)
    Undergraduate.grid(row=1,column=1)

    glbl = tkinter.Label(frame6, text = "Graduate School:", bg = "PaleTurquoise1", fg = "Blue4", font = font1)
    glbl.grid(row=2,column=0)
    global Graduate
    Graduate = tkinter.Entry(frame6, font = font2)
    Graduate.grid(row=2,column=1)

    doblbl = tkinter.Label(frame6, text = "DOB:-", bg = "PaleTurquoise1", fg = "Blue4", font = font1)
    doblbl.grid(row=3,column=0)
    
    yearlbl = tkinter.Label(frame6, text = "Year:", bg = "PaleTurquoise1", fg = "Blue4", font = "Verdana 15")
    yearlbl.grid(row=4, column=0)
    global Year
    Year = ttk.Combobox(frame6, values = getAllYears())
    Year.grid(row=4,column=1)
    Year.bind("<<ComboboxSelected>>", disableYear)
    monthlbl = tkinter.Label(frame6, text = "Month:", bg = "PaleTurquoise1", fg = "Blue4", font = "Verdana 15")
    monthlbl.grid(row=5, column=0)
    global Month
    Month = ttk.Combobox(frame6, values = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
    Month["state"] = "disabled"
    Month.grid(row=5,column=1)
    Month.bind("<<ComboboxSelected>>", disableMonth)
    daylbl = tkinter.Label(frame6, text = "Day:", bg = "PaleTurquoise1", fg = "Blue4", font = "Verdana 15")
    daylbl.grid(row=6, column=0)
    global Day
    Day = ttk.Combobox(frame6, values = [])
    Day["state"]="disabled"
    Day.grid(row=6,column=1)
    resetDOBBtn=tkinter.Button(frame6, text = "Reset DOB",bg = "RoyalBlue1", font = font1, command = resetDOB)
    resetDOBBtn.grid(row=7,column=1)

    subjectSelectlbl = tkinter.Label(frame6, text = "Select subjects and tests you want to TEACH:", font = font1)
    subjectSelectlbl.grid(row=0,column=2, columnspan=4)

    sub1lbl = tkinter.Label(frame6, text = "Subject 1:", bg = "PaleTurquoise1", fg = "Blue4", font = font1)
    sub1lbl.grid(row=1,column=2)
    global Sub1
    Sub1 = ttk.Combobox(frame6, values = ["None"]+subjectList)
    Sub1.current(0)
    Sub1["state"] = "disbaled"
    Sub1.grid(row=1,column=3)
    Sub1.bind("<<ComboboxSelected>>", disableSub1)
    
    sub2lbl = tkinter.Label(frame6, text = "Subject 2:", bg = "PaleTurquoise1", fg = "Blue4", font = font1)
    sub2lbl.grid(row=2,column=2)
    global Sub2
    Sub2 = ttk.Combobox(frame6, values = [])
    Sub2["state"] = "disabled"
    Sub2.grid(row=2,column=3)
    Sub2.bind("<<ComboboxSelected>>", disableSub2)

    sub3lbl = tkinter.Label(frame6, text = "Subject 3:", bg = "PaleTurquoise1", fg = "Blue4", font = font1)
    sub3lbl.grid(row=3,column=2)
    global Sub3
    Sub3 = ttk.Combobox(frame6, values = [])
    Sub3["state"] = "disabled"
    Sub3.grid(row=3,column=3)
    Sub3.bind("<<ComboboxSelected>>", disableSub3)

    sub4lbl = tkinter.Label(frame6, text = "Subject 4:", bg = "PaleTurquoise1", fg = "Blue4", font = font1)
    sub4lbl.grid(row=4,column=2)
    global Sub4
    Sub4 = ttk.Combobox(frame6, values = [])
    Sub4["state"] = "disabled"
    Sub4.grid(row=4,column=3)
    Sub4.bind("<<ComboboxSelected>>", disableSub4)

    sub5lbl = tkinter.Label(frame6, text = "Subject 5:", bg = "PaleTurquoise1", fg = "Blue4", font = font1)
    sub5lbl.grid(row=5,column=2)
    global Sub5
    Sub5 = ttk.Combobox(frame6, values = [])
    Sub5["state"] = "disabled"
    Sub5.grid(row=5,column=3)

    test1lbl = tkinter.Label(frame6, text = "Test 1:", bg = "PaleTurquoise1", fg = "Blue4", font = font1)
    test1lbl.grid(row=1,column=4)
    global Test1
    Test1 = ttk.Combobox(frame6, values = ["None"]+testList)
    Test1.current(0)
    Test1.grid(row=1,column=5)
    Test1.bind("<<ComboboxSelected>>", disableTest1)

    test2lbl = tkinter.Label(frame6, text = "Test 2:", bg = "PaleTurquoise1", fg = "Blue4", font = font1)
    test2lbl.grid(row=2,column=4)
    global Test2
    Test2 = ttk.Combobox(frame6, values = [])
    Test2["state"] = "disabled"
    Test2.grid(row=2,column=5)
    Test2.bind("<<ComboboxSelected>>", disableTest2)

    test3lbl = tkinter.Label(frame6, text = "Test 3:", bg = "PaleTurquoise1", fg = "Blue4", font = font1)
    test3lbl.grid(row=3,column=4)
    global Test3
    Test3 = ttk.Combobox(frame6, values = [])
    Test3["state"] = "disabled"
    Test3.grid(row=3,column=5)
    Test3.bind("<<ComboboxSelected>>", disableTest3)

    test4lbl = tkinter.Label(frame6, text = "Test 4:", bg = "PaleTurquoise1", fg = "Blue4", font = font1)
    test4lbl.grid(row=4,column=4)
    global Test4
    Test4 = ttk.Combobox(frame6, values = [])
    Test4["state"] = "disabled"
    Test4.grid(row=4,column=5)
    Test4.bind("<<ComboboxSelected>>", disableTest4)
    
    test5lbl = tkinter.Label(frame6, text = "Test 5:", bg = "PaleTurquoise1", fg = "Blue4", font = font1)
    test5lbl.grid(row=5,column=4)
    global Test5
    Test5 = ttk.Combobox(frame6, values = [])
    Test5["state"] = "disabled"
    Test5.grid(row=5,column=5)

    resetSubsBtn=tkinter.Button(frame6, text = "Reset Subjects",bg = "RoyalBlue1", font = font1, command = resetSubjects)
    resetSubsBtn.grid(row=6,column=3)

    resetTestsBtn=tkinter.Button(frame6, text = "Reset Tests",bg = "RoyalBlue1", font = font1, command = resetTests)
    resetTestsBtn.grid(row=6,column=5)
    
    cancel2=tkinter.Button(frame6, text = "Cancel",bg = "RoyalBlue1", font = font1, command = cancelBtnFunc)
    cancel2.grid(row=9,column=3)
    
    submit = tkinter.Button(frame6, text = "Sign up",bg = "RoyalBlue1", font = font1, command = checksignup)
    submit.grid(row=9,column=5)

    global lblx2
    lblx2 = tkinter.Label(window, bg = "blue", fg = "red")

def search(subs):
    cursor=con.cursor()
    cursor.execute("SELECT Email, Sub1, Sub2, Sub3, Sub4, Sub5, Test1, Test2, Test3, Test4, Test5 FROM AccDetails;")
    
    searchList = []
    records = cursor.fetchall()
    print(records)
    for record in records:
        check = all(item in record[1:] for item in subs)
        if check is True:
            cursor.execute("SELECT * FROM AccDetails WHERE Email = '{}'".format(record[0]))
            searchList.append(cursor.fetchall())
            print(record)
        else:
            print("No!")
    print(searchList)
    cursor.close()
#search(["SAT Maths2"])

class loginWindow():
    def __init__(self, window):
        window.geometry("1000x500")
        self.frame1 = tkinter.Frame(window)
        self.frame2 = tkinter.Frame(window, bg = "PaleTurquoise1")
        self.frame3 = tkinter.Frame(self.frame2, bg = "PaleTurquoise2", borderwidth = "1", padx = "5", pady = "5", relief = tkinter.GROOVE)

        self.frame1.place(relx = 0, relwidth = 0.7, relheight=1)
        self.frame2.place(relx = 0.7, relwidth = 0.3, relheight=1)
        self.frame3.place(relx =0.5, rely=0.5,anchor=tkinter.CENTER)

        # Frame 1
        canvas1 = tkinter.Canvas(self.frame1, bg="blue")
        canvas1.pack(fill="both", expand=True)
        canvas1.update()
        welcomeText1 = canvas1.create_text(canvas1.winfo_width()//2, 500, text = "Welcome To", fill="White", font = "Verdana 50 bold")
        welcomeText2 = canvas1.create_text(canvas1.winfo_width()//2, 555, text = "Tutor Finder!", fill="White", font = "Verdana 50 bold")
        paratext=canvas1.create_text(canvas1.winfo_width()//2, 680,
                                    text = "Hi! Tutor Finder is a platform where students can \n teach and learn with each other! Blah blah blah..   ",
                                    fill="White", font = "Verdana 15 bold")
        xinc = 0
        yinc = -0.5
        #yinc = -20
        
        while True:
            canvas1.move(welcomeText1, xinc, yinc)
            canvas1.move(welcomeText2, xinc, yinc)
            canvas1.move(paratext, xinc, yinc)
            
            canvas1.update()

            y = canvas1.bbox(welcomeText1)[1]
            if y < 50:
                break

        # Frame 3
        font1 = ("Verdana", 20, "bold")
        font2 = ("Comic Sans MS", 15, "bold")
        Emaillbl = tkinter.Label(self.frame3, text = "Email", bg = "PaleTurquoise1", fg = "Blue4", font = font1)
        Emaillbl.pack()
        self.Email = tkinter.Entry(self.frame3, bg = "alice blue", font = font2)
        self.Email.pack()

        passwordlbl = tkinter.Label(self.frame3, text = "Password", bg = "PaleTurquoise1", fg = "Blue4", font = font1)
        passwordlbl.pack()
        self.password = tkinter.Entry(self.frame3, bg = "alice blue", show = "*", font = font2)
        self.password.pack()

        self.submit = tkinter.Button(self.frame3, text = "Login",bg = "RoyalBlue1", font = font1, command = self.login)
        self.submit.pack(side=tkinter.TOP)
        
        self.signup = tkinter.Button(self.frame3, text = "Create new account",bg = "RoyalBlue1", font = font1, command = self.signupwindow)
        self.signup.pack(side=tkinter.TOP)

        self.loginErrlbl = tkinter.Label(self.frame2, bg = "PaleTurquoise1", fg = "red", font = "Verdana 15", wraplength=self.frame2.winfo_width()-10)

        # Adding bubles in frame1
        #bbl1 = tkinter.Canvas.create_oval(canvas1.winfo_height)

    def login(self):
        email = self.Email.get()
        password = self.password.get()
        cursor=con.cursor()
        cursor.execute("SELECT * FROM AccDetails WHERE Email='"+str(email)+"'AND Password='"+str(password)+"';")
        records=cursor.fetchall()
        if len(records)==1:
            self.loginErrlbl.pack_forget()
            profileWindow(window, records[0])
        else:
            self.loginErrlbl.configure(text="*Incorrect Email or Password. Please try again.*")
            self.loginErrlbl.pack()
        cursor.close()

    def signupwindow(self):
        signupWindow(window)

class signupWindow():
    def __init__(self, window):
        #frame1.destroy()
        #frame2.destroy()
        #frame1.destroy()

        window.configure(bg = "Blue")
        window.geometry("1200x500")
        for widget in window.winfo_children():
            widget.destroy()

        # FRAME 3
        self.frame1 = tkinter.Frame(window, bg = "PaleTurquoise2", borderwidth = "1", padx = "25", pady = "35", relief = tkinter.GROOVE)
        font1 = ("Verdana", 15, "bold")
        font2 = ("Comic Sans MS", 15, "bold")

        Emaillbl = tkinter.Label(self.frame1, text = "Email:", bg = "PaleTurquoise1", fg = "Blue4", font = font1)
        Emaillbl.grid(row=0,column=0)
        global Email
        self.Email = tkinter.Entry(self.frame1, font = font2)
        self.Email.grid(row=0,column=1)

        passwordlbl = tkinter.Label(self.frame1, text = "Password:", bg = "PaleTurquoise1", fg = "Blue4", font = font1)
        passwordlbl.grid(row=1,column=0)
        global Password
        self.Password = tkinter.Entry(self.frame1, show = "*", font = font2)
        self.Password.grid(row=1,column=1)

        firstnamelbl = tkinter.Label(self.frame1, text = "First Name:", bg = "PaleTurquoise1", fg = "Blue4", font = font1)
        firstnamelbl.grid(row=2,column=0)
        global FirstName
        self.FirstName = tkinter.Entry(self.frame1, font = font2)
        self.FirstName.grid(row=2,column=1)

        lastnamelbl = tkinter.Label(self.frame1, text = "Last Name:", bg = "PaleTurquoise1", fg = "Blue4", font = font1)
        lastnamelbl.grid(row=3,column=0)
        global LastName
        self.LastName = tkinter.Entry(self.frame1, font = font2)
        self.LastName.grid(row=3,column=1)

        self.cancel1=tkinter.Button(self.frame1, text = "Cancel", bg = "RoyalBlue1", font = font1, command = self.cancelBtnFunc)
        self.cancel1.grid(row=4,column=0)
        
        self.next1=tkinter.Button(self.frame1, text = "Next", bg = "RoyalBlue1", font = font1, command = self.nextBtnFunc1)
        self.next1.grid(row=4,column=1)

        global lblx
        self.lblx = tkinter.Label(window, bg = "blue", fg = "red")

        self.frame1.place(relx =0.5, rely=0.5,anchor=tkinter.CENTER)

        # FRAME 4
        global frame2
        self.frame2=tkinter.Frame(window, bg = "PaleTurquoise2", borderwidth = "1", padx = "15", pady = "15", relief = tkinter.GROOVE)

        hslbl = tkinter.Label(self.frame2, text = "High School:", bg = "PaleTurquoise1", fg = "Blue4", font = font1)
        hslbl.grid(row=0,column=0)
        global Highschool
        self.Highschool = tkinter.Entry(self.frame2, font = font2)
        self.Highschool.grid(row=0,column=1)
        
        uglbl = tkinter.Label(self.frame2, text = "Undergraduate School:", bg = "PaleTurquoise1", fg = "Blue4", font = font1)
        uglbl.grid(row=1,column=0)
        global Undergraduate
        self.Undergraduate = tkinter.Entry(self.frame2, font = font2)
        self.Undergraduate.grid(row=1,column=1)

        glbl = tkinter.Label(self.frame2, text = "Graduate School:", bg = "PaleTurquoise1", fg = "Blue4", font = font1)
        glbl.grid(row=2,column=0)
        global Graduate
        self.Graduate = tkinter.Entry(self.frame2, font = font2)
        self.Graduate.grid(row=2,column=1)

        doblbl = tkinter.Label(self.frame2, text = "DOB:-", bg = "PaleTurquoise1", fg = "Blue4", font = font1)
        doblbl.grid(row=3,column=0)
        
        yearlbl = tkinter.Label(self.frame2, text = "Year:", bg = "PaleTurquoise1", fg = "Blue4", font = "Verdana 15")
        yearlbl.grid(row=4, column=0)
        self.Year = ttk.Combobox(self.frame2, values = self.getAllYears())
        self.Year.grid(row=4,column=1)
        self.Year.bind("<<ComboboxSelected>>", self.disableYear)
        monthlbl = tkinter.Label(self.frame2, text = "Month:", bg = "PaleTurquoise1", fg = "Blue4", font = "Verdana 15")
        monthlbl.grid(row=5, column=0)
        self.Month = ttk.Combobox(self.frame2, values = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
        self.Month["state"] = "disabled"
        self.Month.grid(row=5,column=1)
        self.Month.bind("<<ComboboxSelected>>", self.disableMonth)
        daylbl = tkinter.Label(self.frame2, text = "Day:", bg = "PaleTurquoise1", fg = "Blue4", font = "Verdana 15")
        daylbl.grid(row=6, column=0)
        self.Day = ttk.Combobox(self.frame2, values = [])
        self.Day["state"]="disabled"
        self.Day.grid(row=6,column=1)
        self.resetDOBBtn=tkinter.Button(self.frame2, text = "Reset DOB",bg = "RoyalBlue1", font = font1, command = self.resetDOB)
        self.resetDOBBtn.grid(row=7,column=1)

        subjectSelectlbl = tkinter.Label(self.frame2, text = "Select subjects and tests you want to TEACH:", font = font1)
        subjectSelectlbl.grid(row=0,column=2, columnspan=4)

        sub1lbl = tkinter.Label(self.frame2, text = "Subject 1:", bg = "PaleTurquoise1", fg = "Blue4", font = font1)
        sub1lbl.grid(row=1,column=2)
        self.Sub1 = ttk.Combobox(self.frame2, values = ["None"]+subjectList)
        self.Sub1.current(0)
        self.Sub1["state"] = "disbaled"
        self.Sub1.grid(row=1,column=3)
        self.Sub1.bind("<<ComboboxSelected>>", self.disableSub1)
        
        sub2lbl = tkinter.Label(self.frame2, text = "Subject 2:", bg = "PaleTurquoise1", fg = "Blue4", font = font1)
        sub2lbl.grid(row=2,column=2)
        self.Sub2 = ttk.Combobox(self.frame2, values = [])
        self.Sub2["state"] = "disabled"
        self.Sub2.grid(row=2,column=3)
        self.Sub2.bind("<<ComboboxSelected>>", self.disableSub2)

        sub3lbl = tkinter.Label(self.frame2, text = "Subject 3:", bg = "PaleTurquoise1", fg = "Blue4", font = font1)
        sub3lbl.grid(row=3,column=2)
        self.Sub3 = ttk.Combobox(self.frame2, values = [])
        self.Sub3["state"] = "disabled"
        self.Sub3.grid(row=3,column=3)
        self.Sub3.bind("<<ComboboxSelected>>", self.disableSub3)

        sub4lbl = tkinter.Label(self.frame2, text = "Subject 4:", bg = "PaleTurquoise1", fg = "Blue4", font = font1)
        sub4lbl.grid(row=4,column=2)
        self.Sub4 = ttk.Combobox(self.frame2, values = [])
        self.Sub4["state"] = "disabled"
        self.Sub4.grid(row=4,column=3)
        self.Sub4.bind("<<ComboboxSelected>>", self.disableSub4)

        sub5lbl = tkinter.Label(self.frame2, text = "Subject 5:", bg = "PaleTurquoise1", fg = "Blue4", font = font1)
        sub5lbl.grid(row=5,column=2)
        self.Sub5 = ttk.Combobox(self.frame2, values = [])
        self.Sub5["state"] = "disabled"
        self.Sub5.grid(row=5,column=3)

        test1lbl = tkinter.Label(self.frame2, text = "Test 1:", bg = "PaleTurquoise1", fg = "Blue4", font = font1)
        test1lbl.grid(row=1,column=4)
        self.Test1 = ttk.Combobox(self.frame2, values = ["None"]+testList)
        self.Test1.current(0)
        self.Test1.grid(row=1,column=5)
        self.Test1.bind("<<ComboboxSelected>>", self.disableTest1)

        test2lbl = tkinter.Label(self.frame2, text = "Test 2:", bg = "PaleTurquoise1", fg = "Blue4", font = font1)
        test2lbl.grid(row=2,column=4)
        self.Test2 = ttk.Combobox(self.frame2, values = [])
        self.Test2["state"] = "disabled"
        self.Test2.grid(row=2,column=5)
        self.Test2.bind("<<ComboboxSelected>>", self.disableTest2)

        test3lbl = tkinter.Label(self.frame2, text = "Test 3:", bg = "PaleTurquoise1", fg = "Blue4", font = font1)
        test3lbl.grid(row=3,column=4)
        self.Test3 = ttk.Combobox(self.frame2, values = [])
        self.Test3["state"] = "disabled"
        self.Test3.grid(row=3,column=5)
        self.Test3.bind("<<ComboboxSelected>>", self.disableTest3)

        test4lbl = tkinter.Label(self.frame2, text = "Test 4:", bg = "PaleTurquoise1", fg = "Blue4", font = font1)
        test4lbl.grid(row=4,column=4)
        self.Test4 = ttk.Combobox(self.frame2, values = [])
        self.Test4["state"] = "disabled"
        self.Test4.grid(row=4,column=5)
        self.Test4.bind("<<ComboboxSelected>>", self.disableTest4)
        
        test5lbl = tkinter.Label(self.frame2, text = "Test 5:", bg = "PaleTurquoise1", fg = "Blue4", font = font1)
        test5lbl.grid(row=5,column=4)
        self.Test5 = ttk.Combobox(self.frame2, values = [])
        self.Test5["state"] = "disabled"
        self.Test5.grid(row=5,column=5)

        self.resetSubsBtn=tkinter.Button(self.frame2, text = "Reset Subjects",bg = "RoyalBlue1", font = font1, command = self.resetSubjects)
        self.resetSubsBtn.grid(row=6,column=3)

        self.resetTestsBtn=tkinter.Button(self.frame2, text = "Reset Tests",bg = "RoyalBlue1", font = font1, command = self.resetTests)
        self.resetTestsBtn.grid(row=6,column=5)
        
        self.cancel2=tkinter.Button(self.frame2, text = "Cancel",bg = "RoyalBlue1", font = font1, command = self.cancelBtnFunc)
        self.cancel2.grid(row=9,column=3)
        
        self.submit = tkinter.Button(self.frame2, text = "Sign up",bg = "RoyalBlue1", font = font1, command = self.checksignup)
        self.submit.grid(row=9,column=5)

        self.lblx2 = tkinter.Label(window, bg = "blue", fg = "red")

    def getAllYears(self):
        yearList = []
        yearNow = datetime.datetime.now().year
        for i in range(yearNow - 100, yearNow+1,1):
            yearList.append(i)
        return yearList

    def getAllDays(self):
        dayList = []
        if self.Month.get() == "Feb":
            if int(Year.get()) % 4 == 0:
                for i in range(1,30,1):
                    dayList.append(i)
            else:
                for i in range(1,29,1):
                    dayList.append(i)
        elif self.Month.get() in ["Apr", "Jun", "Sep", "Nov"]:
            for i in range(1,31,1):
                    dayList.append(i)
        else:
            for i in range(1,32,1):
                dayList.append(i)
        return dayList

    def monthToNum(self, month):
        monthDict = {"Jan" : "1", "Feb" : "2", "Mar" : "3", "Apr" : "4", "May" : "5", "Jun" : "6", "Jul" : "7", "Aug" : "8", "Sep" : "9", "Oct" : "10", "Nov" : "11", "Dec" : "12"}
        return monthDict[month]

    def nextBtnFunc1(self):
        if self.Email.get() == "":
            self.lblx.configure(text = "*Email not entered*")
            self.lblx.pack()
        elif self.Password.get() == "":
            self.lblx.configure(text = "*Password not entered*")
            self.lblx.pack()
        elif self.FirstName.get() == "":
            self.lblx.configure(text = "*First name not entered*")
            self.lblx.pack()
        elif self.LastName.get() == "":
            self.lblx.configure(text = "*Last name not entered*")
            self.lblx.pack()
        else:
            self.lblx.pack_forget()
            self.frame1.place_forget()
            self.frame2.place(relx =0.5, rely=0.5,anchor=tkinter.CENTER)

    def cancelBtnFunc(self):
        loginWindow(window)

    def disableYear(self, *args):
        self.Year["state"] = "disabled"
        self.Month["state"] = "normal"

    def disableMonth(self, *args):
        self.Month["state"] = "disabled"
        self.Day["state"] = "normal"
        self.Day["values"] = self.getAllDays()

    def disableSub1(self, *args):
        self.Sub1["state"] = "disabled"
        self.Sub2["state"] = "normal"
        self.Sub2["values"] = ["None"]+self.changeSubList()
        self.Sub2.current(0)

    def disableSub2(self, *args):
        self.Sub2["state"] = "disabled"
        self.Sub3["state"] = "normal"
        self.Sub3["values"] = ["None"]+self.changeSubList()
        self.Sub3.current(0)

    def disableSub3(self, *args):
        self.Sub3["state"] = "disabled"
        self.Sub4["state"] = "normal"
        self.Sub4["values"] = ["None"]+self.changeSubList()
        self.Sub4.current(0)

    def disableSub4(self, *args):
        self.Sub4["state"] = "disabled"
        self.Sub5["state"] = "normal"
        self.Sub5["values"] = ["None"]+self.changeSubList()
        self.Sub5.current(0)

    def disableTest1(self, *args):
        self.Test1["state"] = "disabled"
        self.Test2["state"] = "normal"
        self.Test2["values"] = ["None"]+self.changeTestList()
        self.Test2.current(0)

    def disableTest2(self, *args):
        self.Test2["state"] = "disabled"
        self.Test3["state"] = "normal"
        self.Test3["values"] = ["None"]+self.changeTestList()
        self.Test3.current(0)

    def disableTest3(self, *args):
        self.Test3["state"] = "disabled"
        self.Test4["state"] = "normal"
        self.Test4["values"] = ["None"]+self.changeTestList()
        self.Test4.current(0)

    def disableTest4(self, *args):
        self.Test4["state"] = "disabled"
        self.Test5["state"] = "normal"
        self.Test5["values"] = ["None"]+self.changeTestList()
        self.Test5.current(0)

    def changeSubList(self):
        subList = copy.deepcopy(subjectList)
        if self.Sub1.get() in subjectList:
            subList.remove(self.Sub1.get())
        if self.Sub2.get() in subjectList:
            subList.remove(self.Sub2.get())
        if self.Sub3.get() in subjectList:
            subList.remove(self.Sub3.get())
        if self.Sub4.get() in subjectList:
            subList.remove(self.Sub4.get())
        if self.Sub5.get() in subjectList:
            subList.remove(self.Sub5.get())
        return subList

    def changeTestList(self):
        tList = copy.deepcopy(testList)
        if self.Test1.get() in tList:
            tList.remove(self.Test1.get())
        if self.Test2.get() in tList:
            tList.remove(self.Test2.get())
        if self.Test3.get() in tList:
            tList.remove(self.Test3.get())
        if self.Test4.get() in tList:
            tList.remove(self.Test4.get())
        if self.Test5.get() in tList:
            tList.remove(self.Test5.get())
        return tList
        
    def resetSubjects(self):
        self.Sub1["values"] = ["None"]+subjectList
        self.Sub1["state"] = "normal"
        self.Sub2["state"] = "disabled"
        self.Sub3["state"] = "disabled"
        self.Sub4["state"] = "disabled"
        self.Sub5["state"] = "disabled"
        self.Sub1.current(0)
        self.Sub2.set("")
        self.Sub3.set("")
        self.Sub4.set("")
        self.Sub5.set("")

    def resetTests(self):
        self.Test1["values"] = ["None"]+testList
        self.Test1["state"] = "normal"
        self.Test2["state"] = "disabled"
        self.Test3["state"] = "disabled"
        self.Test4["state"] = "disabled"
        self.Test5["state"] = "disabled"
        self.Test1.current(0)
        self.Test2.set("")
        self.Test3.set("")
        self.Test4.set("")
        self.Test5.set("")

    def resetDOB(self):
        self.Year["state"]="normal"
        self.Month["state"]="disabled"
        self.Day["state"]="disabled"
        self.Month.set("")
        self.Day.set("")

    def checksignup(self):
        if self.Year.get() == "":
            self.lblx2.configure(text = "Year not entered")
            self.lblx2.pack()
        elif self.Month.get() == "":
            self.lblx2.configure(text = "Month not entered")
            self.lblx2.pack()
        elif self.Day.get() == "":
            self.lblx2.configure(text = "Day not entered")
            self.lblx2.pack()
        else:
            Highschool1=self.Highschool.get()
            if Highschool1 == "":
                Highschool1 = None
            Undergraduate1=self.Undergraduate.get()
            if Undergraduate1 == "":
                Undergraduate1 = None
            Graduate1=self.Graduate.get()
            if Graduate1 == "":
                Graduate1 = None

            DOB1 = self.Year.get()+"-"+self.monthToNum(self.Month.get())+"-"+self.Day.get()

            S1=self.Sub1.get()
            if S1 == "None" or S1 == "":
                S1 = None
            S2=self.Sub2.get()
            if S2 == "None" or S2 == "":
                S2 = None
            S3=self.Sub3.get()
            if S3 == "None" or S3 == "":
                S3 = None
            S4=self.Sub4.get()
            if S4 == "None" or S4 == "":
                S4 = None
            S5=self.Sub5.get()
            if S5 == "None" or S5 == "":
                S5 = None

            T1=self.Test1.get()
            if T1 == "None" or T1 == "":
                T1 = None
            T2=self.Test2.get()
            if T2 == "None" or T2 == "":
                T2 = None
            T3=self.Test3.get()
            if T3 == "None" or T3 == "":
                T3 = None
            T4=self.Test4.get()
            if T4 == "None" or T4 == "":
                T4 = None
            T5=self.Test5.get()
            if T5 == "None" or T5 == "":
                T5 = None

            self.signup(self.Email.get(), self.Password.get(), self.FirstName.get(), self.LastName.get(), Highschool1, Undergraduate1, Graduate1, DOB1, S1, S2, S3, S4, S5, T1, T2, T3, T4, T5)

    def signup(self, Email, Password, FirstName, LastName, Highschool, Undergraduate, Graduate, DOB, Sub1, Sub2, Sub3, Sub4, Sub5, Test1, Test2, Test3, Test4, Test5):
        cursor=con.cursor()
        try:
            cursor.execute("INSERT INTO AccDetails values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(Email, Password, FirstName, LastName, Highschool, Undergraduate, Graduate, DOB, Sub1, Sub2, Sub3, Sub4, Sub5, Test1, Test2, Test3, Test4, Test5))
            con.commit()
            record = [Email, Password, FirstName, LastName, Highschool, Undergraduate, Graduate, DOB, Sub1, Sub2, Sub3, Sub4, Sub5, Test1, Test2, Test3, Test4, Test5]
            profileWindow(window, record)
        except sql.Error as Err:
            print(Err)
 
class profileWindow():
    def __init__(self, window, record):
        for widget in window.winfo_children():
            widget.destroy()
        
        window.configure(bg = "Blue")
        window.geometry("1300x500")
        for widget in window.winfo_children():
            widget.destroy()

        self.frame1 = tkinter.Frame(window, bg = "PaleTurquoise2", borderwidth = "1", padx = "25", pady = "35", relief = tkinter.GROOVE)
        self.frame1.place(relx =0.5, rely=0.5,anchor=tkinter.CENTER)

        # 11 columns
        # Start:3 End:9
        headinglbl = tkinter.Label(self.frame1, text = "Student4Student", font = "Verdana 40 bold")
        headinglbl.grid(row=0, column=0, columnspan=7)

        profilelbl = tkinter.Label(self.frame1, text = "PROFILE", font = "Verdana 20 bold")
        profilelbl.grid(row=1, column=0, columnspan=2, rowspan=2)
        
        pic = self.profilepic()
        piclbl = tkinter.Label(self.frame1, image = pic, font = "Verdana 20 bold")
        piclbl.image = pic
        piclbl.grid(row=3, column=0, columnspan=2, rowspan=6)

        #global dataFrame
        self.dataFrame = tkinter.Frame(self.frame1)
        self.dataFrame.grid(row=3, column=2, rowspan=6, columnspan=4)

        Emaillbl = tkinter.Label(self.dataFrame, text = "Email:", font = "Verdana 20 bold")
        Emaillbl.grid(row=1, column=0)

        EmailVallbl = tkinter.Label(self.dataFrame, text = record[0], font = "Verdana 20")
        EmailVallbl.grid(row=1, column=1)

        FirstNameLbl = tkinter.Label(self.dataFrame, text="First Name:", font = "Verdana 20 bold")
        FirstNameLbl.grid(row=2, column=0)

        FirstNameValLbl = tkinter.Label(self.dataFrame, text=record[2], font = "Verdana 20")
        FirstNameValLbl.grid(row=2, column=1)

        LastNameLbl = tkinter.Label(self.dataFrame, text="Last Name:", font = "Verdana 20 bold")
        LastNameLbl.grid(row=3, column=0)

        LastNameValLbl = tkinter.Label(self.dataFrame, text=record[3], font = "Verdana 20")
        LastNameValLbl.grid(row=3, column=1)

        DateLbl = tkinter.Label(self.dataFrame, text="DOB:", font = "Verdana 20 bold")
        DateLbl.grid(row=4, column=0)

        DateValLbl = tkinter.Label(self.dataFrame, text=record[7], font = "Verdana 20")
        DateValLbl.grid(row=4, column=1)

        subPrefLbl = tkinter.Label(self.dataFrame, text = "Subject Preferences", font = "Verdana 20 bold")
        subPrefLbl.grid(row=0, column=4)

        testPrefLbl = tkinter.Label(self.dataFrame, text = "Test Preferences", font = "Verdana 20 bold")
        testPrefLbl.grid(row=0, column=5)

        sub1Lbl = tkinter.Label(self.dataFrame, text=record[8], font = "Verdana 20")
        sub1Lbl.grid(row=1, column=4)

        sub2Lbl = tkinter.Label(self.dataFrame, text=record[9], font = "Verdana 20")
        sub2Lbl.grid(row=2, column=4)

        sub3Lbl = tkinter.Label(self.dataFrame, text=record[10], font = "Verdana 20")
        sub3Lbl.grid(row=3, column=4)

        sub4Lbl = tkinter.Label(self.dataFrame, text=record[11], font = "Verdana 20")
        sub4Lbl.grid(row=4, column=4)

        sub5Lbl = tkinter.Label(self.dataFrame, text=record[12], font = "Verdana 20")
        sub5Lbl.grid(row=5, column=4)

        test1Lbl = tkinter.Label(self.dataFrame, text=record[13], font = "Verdana 20")
        test1Lbl.grid(row=1, column=5)

        test2Lbl = tkinter.Label(self.dataFrame, text=record[14], font = "Verdana 20")
        test2Lbl.grid(row=2, column=5)

        test3Lbl = tkinter.Label(self.dataFrame, text=record[15], font = "Verdana 20")
        test3Lbl.grid(row=3, column=5)

        test4Lbl = tkinter.Label(self.dataFrame, text=record[16], font = "Verdana 20")
        test4Lbl.grid(row=4, column=5)

        test5Lbl = tkinter.Label(self.dataFrame, text=record[17], font = "Verdana 20")
        test5Lbl.grid(row=5, column=5)

        tutorlookuplbl = tkinter.Label(self.frame1, text="Tutor Look-up!", font = "Verdana 20 bold")
        tutorlookuplbl.grid(row=9, column=0, columnspan=1)

        subjects = tkinter.Button(self.frame1, text = "By Subjects",bg = "RoyalBlue1", font = "Verdana 20 bold")
        subjects.grid(row=10, column=1, columnspan=2, sticky=tkinter.N+tkinter.S+tkinter.E+tkinter.W)

        test = tkinter.Button(self.frame1, text = "By tests",bg = "RoyalBlue1", font = "Verdana 20 bold")
        test.grid(row=10, column=3, columnspan=2, sticky=tkinter.N+tkinter.S+tkinter.E+tkinter.W)

        college = tkinter.Button(self.frame1, text = "By colleges",bg = "RoyalBlue1", font = "Verdana 20 bold")
        college.grid(row=10, column=5, columnspan=2, sticky=tkinter.N+tkinter.S+tkinter.E+tkinter.W)
        
        update = tkinter.Button(self.frame1, text = "Update",bg = "RoyalBlue1", command = updateprofile, font = "Verdana 20 bold")
        update.grid(row=0, column=8)

        update = tkinter.Button(self.frame1, text = "Sign out",bg = "RoyalBlue1", command = self.signout, font = "Verdana 20 bold")
        update.grid(row=1, column=8)

    def profilepic(self):
        pic1 = tkinter.PhotoImage(file="pig.png")
        pic2 = tkinter.PhotoImage(file="bear.png")
        pic3 = tkinter.PhotoImage(file="elephant.png")
        pic4 = tkinter.PhotoImage(file="horse.png")
        pic5 = tkinter.PhotoImage(file="dog.png")
        lst=[pic1, pic2, pic3, pic4, pic5]
        pic=random.choice(lst)
        return pic

    def signout(self):
        loginWindow(window)


window = tkinter.Tk()
window.title("Tutor Finder!")
loginWindow(window)
window.mainloop()
