import mysql.connector as sql
import tkinter
from tkinter import ttk
import copy
import datetime

global testList
testList = ["SAT", "TOEFL", "IELTS", "SAT Maths 2", "SAT Maths 1", "SAT Literature", "SAT Philosophy", "SAT Japanese", "SAT US History", "SAT World History", "JLPTN1", "JLPTN2", "JLPTN3", "JLPTN4", "JLPTN5"]
global subjectList
subjectList = ["Maths", "Physics", "Chemistry", "English", "Biology", "History", "Economics", "Entrepreneurship", "Accounting", "Computer Science", "Psychology"]

con = sql.connect(host="localhost", user = "root", passwd = "root", database = "tfdb")
if (con.is_connected()):
    print("Connection is successfull!!")
else:
    print("Not connected!")

def getAllYears():
    yearList = []
    yearNow = datetime.datetime.now().year
    for i in range(yearNow - 100, yearNow+1,1):
        yearList.append(i)
    return yearList

def getAllDays():
    dayList = []
    if Month.get() == "Feb":
        if int(Year.get()) % 4 == 0:
            for i in range(1,30,1):
                dayList.append(i)
        else:
            for i in range(1,29,1):
                dayList.append(i)
    elif Month.get() in ["Apr", "Jun", "Sep", "Nov"]:
        for i in range(1,31,1):
                dayList.append(i)
    else:
        for i in range(1,32,1):
            dayList.append(i)
    return dayList

def monthToNum(month):
    monthDict = {"Jan" : "1", "Feb" : "2", "Mar" : "3", "Apr" : "4", "May" : "5", "Jun" : "6", "Jul" : "7", "Aug" : "8", "Sep" : "9", "Oct" : "10", "Nov" : "11", "Dec" : "12"}
    return monthDict[month]

def signupwindow():
    frame1.destroy()
    frame12.destroy()
    frame2.destroy()

    window.configure(bg = "Blue")

    # FRAME 3
    global frame3
    frame3 = tkinter.Frame(window, bg = "PaleTurquoise2", borderwidth = "1", padx = "25", pady = "35", relief = tkinter.GROOVE)
    font1 = ("Verdana", 15, "bold")
    font2 = ("Comic Sans MS", 15, "bold")

    Emaillbl = tkinter.Label(frame3, text = "Email:", bg = "PaleTurquoise1", fg = "Blue4", font = font1)
    Emaillbl.grid(row=0,column=0)
    global Email
    Email = tkinter.Entry(frame3, font = font2)
    Email.grid(row=0,column=1)

    passwordlbl = tkinter.Label(frame3, text = "Password:", bg = "PaleTurquoise1", fg = "Blue4", font = font1)
    passwordlbl.grid(row=1,column=0)
    global Password
    Password = tkinter.Entry(frame3, show = "*", font = font2)
    Password.grid(row=1,column=1)

    firstnamelbl = tkinter.Label(frame3, text = "First Name:", bg = "PaleTurquoise1", fg = "Blue4", font = font1)
    firstnamelbl.grid(row=2,column=0)
    global FirstName
    FirstName = tkinter.Entry(frame3, font = font2)
    FirstName.grid(row=2,column=1)

    lastnamelbl = tkinter.Label(frame3, text = "Last Name:", bg = "PaleTurquoise1", fg = "Blue4", font = font1)
    lastnamelbl.grid(row=3,column=0)
    global LastName
    LastName = tkinter.Entry(frame3, font = font2)
    LastName.grid(row=3,column=1)

    cancel1=tkinter.Button(frame3, text = "Cancel", bg = "RoyalBlue1", font = font1, command = cancelBtnFunc)
    cancel1.grid(row=4,column=0)
    
    next1=tkinter.Button(frame3, text = "Next", bg = "RoyalBlue1", font = font1, command = nextBtnFunc1)
    next1.grid(row=4,column=1)

    global lblx
    lblx = tkinter.Label(window, bg = "blue", fg = "red")

    frame3.place(relx =0.5, rely=0.5,anchor=tkinter.CENTER)

    # FRAME 4
    global frame4
    frame4=tkinter.Frame(window, bg = "PaleTurquoise2", borderwidth = "1", padx = "15", pady = "15", relief = tkinter.GROOVE)

    hslbl = tkinter.Label(frame4, text = "High School:", bg = "PaleTurquoise1", fg = "Blue4", font = font1)
    hslbl.grid(row=0,column=0)
    global Highschool
    Highschool = tkinter.Entry(frame4, font = font2)
    Highschool.grid(row=0,column=1)
    
    uglbl = tkinter.Label(frame4, text = "Undergraduate School:", bg = "PaleTurquoise1", fg = "Blue4", font = font1)
    uglbl.grid(row=1,column=0)
    global Undergraduate
    Undergraduate = tkinter.Entry(frame4, font = font2)
    Undergraduate.grid(row=1,column=1)

    glbl = tkinter.Label(frame4, text = "Graduate School:", bg = "PaleTurquoise1", fg = "Blue4", font = font1)
    glbl.grid(row=2,column=0)
    global Graduate
    Graduate = tkinter.Entry(frame4, font = font2)
    Graduate.grid(row=2,column=1)

    doblbl = tkinter.Label(frame4, text = "DOB:-", bg = "PaleTurquoise1", fg = "Blue4", font = font1)
    doblbl.grid(row=3,column=0)
    
    yearlbl = tkinter.Label(frame4, text = "Year:", bg = "PaleTurquoise1", fg = "Blue4", font = "Verdana 15")
    yearlbl.grid(row=4, column=0)
    global Year
    Year = ttk.Combobox(frame4, values = getAllYears())
    Year.grid(row=4,column=1)
    Year.bind("<<ComboboxSelected>>", disableYear)
    monthlbl = tkinter.Label(frame4, text = "Month:", bg = "PaleTurquoise1", fg = "Blue4", font = "Verdana 15")
    monthlbl.grid(row=5, column=0)
    global Month
    Month = ttk.Combobox(frame4, values = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
    Month["state"] = "disabled"
    Month.grid(row=5,column=1)
    Month.bind("<<ComboboxSelected>>", disableMonth)
    daylbl = tkinter.Label(frame4, text = "Day:", bg = "PaleTurquoise1", fg = "Blue4", font = "Verdana 15")
    daylbl.grid(row=6, column=0)
    global Day
    Day = ttk.Combobox(frame4, values = [])
    Day["state"]="disabled"
    Day.grid(row=6,column=1)
    resetDOBBtn=tkinter.Button(frame4, text = "Reset DOB",bg = "RoyalBlue1", font = font1, command = resetDOB)
    resetDOBBtn.grid(row=7,column=1)

    headinglbl = tkinter.Label(frame4, text = "Select subjects and tests you want to TEACH:", font = font1)
    headinglbl.grid(row=0,column=2, columnspan=4)

    sub1lbl = tkinter.Label(frame4, text = "Subject 1:", bg = "PaleTurquoise1", fg = "Blue4", font = font1)
    sub1lbl.grid(row=1,column=2)
    global Sub1
    Sub1 = ttk.Combobox(frame4, values = ["None"]+subjectList)
    Sub1.current(0)
    Sub1["state"] = "disbaled"
    Sub1.grid(row=1,column=3)
    Sub1.bind("<<ComboboxSelected>>", disableSub1)
    
    sub2lbl = tkinter.Label(frame4, text = "Subject 2:", bg = "PaleTurquoise1", fg = "Blue4", font = font1)
    sub2lbl.grid(row=2,column=2)
    global Sub2
    Sub2 = ttk.Combobox(frame4, values = [])
    Sub2["state"] = "disabled"
    Sub2.grid(row=2,column=3)
    Sub2.bind("<<ComboboxSelected>>", disableSub2)

    sub3lbl = tkinter.Label(frame4, text = "Subject 3:", bg = "PaleTurquoise1", fg = "Blue4", font = font1)
    sub3lbl.grid(row=3,column=2)
    global Sub3
    Sub3 = ttk.Combobox(frame4, values = [])
    Sub3["state"] = "disabled"
    Sub3.grid(row=3,column=3)
    Sub3.bind("<<ComboboxSelected>>", disableSub3)

    sub4lbl = tkinter.Label(frame4, text = "Subject 4:", bg = "PaleTurquoise1", fg = "Blue4", font = font1)
    sub4lbl.grid(row=4,column=2)
    global Sub4
    Sub4 = ttk.Combobox(frame4, values = [])
    Sub4["state"] = "disabled"
    Sub4.grid(row=4,column=3)
    Sub4.bind("<<ComboboxSelected>>", disableSub4)

    sub5lbl = tkinter.Label(frame4, text = "Subject 5:", bg = "PaleTurquoise1", fg = "Blue4", font = font1)
    sub5lbl.grid(row=5,column=2)
    global Sub5
    Sub5 = ttk.Combobox(frame4, values = [])
    Sub5["state"] = "disabled"
    Sub5.grid(row=5,column=3)

    test1lbl = tkinter.Label(frame4, text = "Test 1:", bg = "PaleTurquoise1", fg = "Blue4", font = font1)
    test1lbl.grid(row=1,column=4)
    global Test1
    Test1 = ttk.Combobox(frame4, values = ["None"]+testList)
    Test1.current(0)
    Test1.grid(row=1,column=5)
    Test1.bind("<<ComboboxSelected>>", disableTest1)

    test2lbl = tkinter.Label(frame4, text = "Test 2:", bg = "PaleTurquoise1", fg = "Blue4", font = font1)
    test2lbl.grid(row=2,column=4)
    global Test2
    Test2 = ttk.Combobox(frame4, values = [])
    Test2["state"] = "disabled"
    Test2.grid(row=2,column=5)
    Test2.bind("<<ComboboxSelected>>", disableTest2)

    test3lbl = tkinter.Label(frame4, text = "Test 3:", bg = "PaleTurquoise1", fg = "Blue4", font = font1)
    test3lbl.grid(row=3,column=4)
    global Test3
    Test3 = ttk.Combobox(frame4, values = [])
    Test3["state"] = "disabled"
    Test3.grid(row=3,column=5)
    Test3.bind("<<ComboboxSelected>>", disableTest3)

    test4lbl = tkinter.Label(frame4, text = "Test 4:", bg = "PaleTurquoise1", fg = "Blue4", font = font1)
    test4lbl.grid(row=4,column=4)
    global Test4
    Test4 = ttk.Combobox(frame4, values = [])
    Test4["state"] = "disabled"
    Test4.grid(row=4,column=5)
    Test4.bind("<<ComboboxSelected>>", disableTest4)
    
    test5lbl = tkinter.Label(frame4, text = "Test 5:", bg = "PaleTurquoise1", fg = "Blue4", font = font1)
    test5lbl.grid(row=5,column=4)
    global Test5
    Test5 = ttk.Combobox(frame4, values = [])
    Test5["state"] = "disabled"
    Test5.grid(row=5,column=5)

    resetSubsBtn=tkinter.Button(frame4, text = "Reset Subjects",bg = "RoyalBlue1", font = font1, command = resetSubjects)
    resetSubsBtn.grid(row=6,column=3)

    resetTestsBtn=tkinter.Button(frame4, text = "Reset Tests",bg = "RoyalBlue1", font = font1, command = resetTests)
    resetTestsBtn.grid(row=6,column=5)
    
    cancel2=tkinter.Button(frame4, text = "Cancel",bg = "RoyalBlue1", font = font1, command = cancelBtnFunc)
    cancel2.grid(row=9,column=3)
    
    submit = tkinter.Button(frame4, text = "Sign up",bg = "RoyalBlue1", font = font1, command = checksignup)
    submit.grid(row=9,column=5)

    global lblx2
    lblx2 = tkinter.Label(window, bg = "blue", fg = "red")

def nextBtnFunc1():
    if Email.get() == "":
        lblx.configure(text = "*Email not entered*")
        lblx.pack()
    elif Password.get() == "":
        lblx.configure(text = "*Password not entered*")
        lblx.pack()
    elif FirstName.get() == "":
        lblx.configure(text = "*First name not entered*")
        lblx.pack()
    elif LastName.get() == "":
        lblx.configure(text = "*Last name not entered*")
        lblx.pack()
    else:
        lblx.pack_forget()
        frame3.place_forget()
        frame4.place(relx =0.5, rely=0.5,anchor=tkinter.CENTER)

def cancelBtnFunc():
    window.destroy()
    main()

def disableYear(*args):
    Year["state"] = "disabled"
    Month["state"] = "normal"

def disableMonth(*args):
    Month["state"] = "disabled"
    Day["state"] = "normal"
    Day["values"] = getAllDays()

def disableSub1(*args):
    Sub1["state"] = "disabled"
    Sub2["state"] = "normal"
    Sub2["values"] = ["None"]+changeSubList()
    Sub2.current(0)

def disableSub2(*args):
    Sub2["state"] = "disabled"
    Sub3["state"] = "normal"
    Sub3["values"] = ["None"]+changeSubList()
    Sub3.current(0)

def disableSub3(*args):
    Sub3["state"] = "disabled"
    Sub4["state"] = "normal"
    Sub4["values"] = ["None"]+changeSubList()
    Sub4.current(0)

def disableSub4(*args):
    Sub4["state"] = "disabled"
    Sub5["state"] = "normal"
    Sub5["values"] = ["None"]+changeSubList()
    Sub5.current(0)

def disableTest1(*args):
    Test1["state"] = "disabled"
    Test2["state"] = "normal"
    Test2["values"] = ["None"]+changeTestList()
    Test2.current(0)

def disableTest2(*args):
    Test2["state"] = "disabled"
    Test3["state"] = "normal"
    Test3["values"] = ["None"]+changeTestList()
    Test3.current(0)

def disableTest3(*args):
    Test3["state"] = "disabled"
    Test4["state"] = "normal"
    Test4["values"] = ["None"]+changeTestList()
    Test4.current(0)

def disableTest4(*args):
    Test4["state"] = "disabled"
    Test5["state"] = "normal"
    Test5["values"] = ["None"]+changeTestList()
    Test5.current(0)

def changeSubList():
    subList = copy.deepcopy(subjectList)
    if Sub1.get() in subjectList:
        subList.remove(Sub1.get())
    if Sub2.get() in subjectList:
        subList.remove(Sub2.get())
    if Sub3.get() in subjectList:
        subList.remove(Sub3.get())
    if Sub4.get() in subjectList:
        subList.remove(Sub4.get())
    if Sub5.get() in subjectList:
        subList.remove(Sub5.get())
    return subList

def changeTestList(*args):
    tList = copy.deepcopy(testList)
    if Test1.get() in tList:
        tList.remove(Test1.get())
    if Test2.get() in tList:
        tList.remove(Test2.get())
    if Test3.get() in tList:
        tList.remove(Test3.get())
    if Test4.get() in tList:
        tList.remove(Test4.get())
    if Test5.get() in tList:
        tList.remove(Test5.get())
    return tList
    
def resetSubjects():
    Sub1["values"] = ["None"]+subjectList
    Sub1["state"] = "normal"
    Sub2["state"] = "disabled"
    Sub3["state"] = "disabled"
    Sub4["state"] = "disabled"
    Sub5["state"] = "disabled"
    Sub1.current(0)
    Sub2.set("")
    Sub3.set("")
    Sub4.set("")
    Sub5.set("")

def resetTests():
    Test1["values"] = ["None"]+testList
    Test1["state"] = "normal"
    Test2["state"] = "disabled"
    Test3["state"] = "disabled"
    Test4["state"] = "disabled"
    Test5["state"] = "disabled"
    Test1.current(0)
    Test2.set("")
    Test3.set("")
    Test4.set("")
    Test5.set("")

def resetDOB():
    Year["state"]="normal"
    Month["state"]="disabled"
    Day["state"]="disabled"
    Month.set("")
    Day.set("")

def checksignup():
    if Year.get() == "":
        lblx2.configure(text = "Year not entered")
        lblx2.pack()
    elif Month.get() == "":
        lblx2.configure(text = "Month not entered")
        lblx2.pack()
    elif Day.get() == "":
        lblx2.configure(text = "Day not entered")
        lblx2.pack()
    else:
        Highschool1=Highschool.get()
        if Highschool1 == "":
            Highschool1 = None
        Undergraduate1=Undergraduate.get()
        if Undergraduate1 == "":
            Undergraduate1 = None
        Graduate1=Graduate.get()
        if Graduate1 == "":
            Graduate1 = None

        DOB1 = Year.get()+"-"+monthToNum(Month.get())+"-"+Day.get()

        S1=Sub1.get()
        if S1 == "None" or S1 == "":
            S1 = None
        S2=Sub2.get()
        if S2 == "None" or S2 == "":
            S2 = None
        S3=Sub3.get()
        if S3 == "None" or S3 == "":
            S3 = None
        S4=Sub4.get()
        if S4 == "None" or S4 == "":
            S4 = None
        S5=Sub5.get()
        if S5 == "None" or S5 == "":
            S5 = None

        T1=Test1.get()
        if T1 == "None" or T1 == "":
            T1 = None
        T2=Test2.get()
        if T2 == "None" or T2 == "":
            T2 = None
        T3=Test3.get()
        if T3 == "None" or T3 == "":
            T3 = None
        T4=Test4.get()
        if T4 == "None" or T4 == "":
            T4 = None
        T5=Test5.get()
        if T5 == "None" or T5 == "":
            T5 = None

        signup(Email.get(), Password.get(), FirstName.get(), LastName.get(), Highschool1, Undergraduate1, Graduate1, DOB1, S1, S2, S3, S4, S5, T1, T2, T3, T4, T5)
    
def signup(Email, Password, FirstName, LastName, Highschool, Undergraduate, Graduate, DOB, Sub1, Sub2, Sub3, Sub4, Sub5, Test1, Test2, Test3, Test4, Test5):
    print(Sub1)
    cursor=con.cursor()
    try:
        cursor.execute("INSERT INTO AccDetails values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(Email, Password, FirstName, LastName, Highschool, Undergraduate, Graduate, DOB, Sub1, Sub2, Sub3, Sub4, Sub5, Test1, Test2, Test3, Test4, Test5))
        con.commit()
    except sql.Error as Err:
        print(Err)


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

def login():
    username = Email.get()
    password1 = password.get()
    cursor=con.cursor()
    cursor.execute("SELECT * FROM AccDetails WHERE Email='"+str(username)+"'AND Password='"+str(password1)+"';")
    records=cursor.fetchall()
    if len(records)==1:
        loginErrlbl.pack_forget()
        print("Login Successfull!")
    else:
        loginErrlbl.configure(text="*Incorrect Email or Password. Please try again.*")
        loginErrlbl.pack()
    cursor.close()

def main():
    global window
    global frame1
    global frame12
    global frame2

    window = tkinter.Tk()
    window.geometry("1000x500")
    window.title("Tutor Finder!")

    frame1 = tkinter.Frame(window)
    frame12 = tkinter.Frame(window, bg = "PaleTurquoise1")
    frame2 = tkinter.Frame(frame12, bg = "PaleTurquoise2", borderwidth = "1", padx = "5", pady = "5", relief = tkinter.GROOVE)

    frame1.place(relx = 0, relwidth = 0.7, relheight=1)
    frame2.place(relx =0.5, rely=0.5,anchor=tkinter.CENTER)
    frame12.place(relx = 0.7, relwidth = 0.3, relheight=1)

    # Frame 1
    canvas1 = tkinter.Canvas(frame1, bg="blue")
    canvas1.pack(fill="both", expand=True)
    canvas1.update()
    welcomeText1 = canvas1.create_text(canvas1.winfo_width()//2, 500, text = "Welcome To", fill="White", font = "Verdana 50 bold")
    welcomeText2 = canvas1.create_text(canvas1.winfo_width()//2, 555, text = "Tutor Finder!", fill="White", font = "Verdana 50 bold")
    xinc = 0
    yinc = -10
    
    while True:
        canvas1.move(welcomeText1, xinc, yinc)
        canvas1.move(welcomeText2, xinc, yinc)
        canvas1.update()

        y = canvas1.bbox(welcomeText1)[1]
        if y < 50:
            break

    # Frame 2
    font1 = ("Verdana", 20, "bold")
    font2 = ("Comic Sans MS", 15, "bold")
    Emaillbl = tkinter.Label(frame2, text = "Email", bg = "PaleTurquoise1", fg = "Blue4", font = font1)
    Emaillbl.pack()
    global Email
    Email = tkinter.Entry(frame2, bg = "alice blue", font = font2)
    Email.pack()

    passwordlbl = tkinter.Label(frame2, text = "Password", bg = "PaleTurquoise1", fg = "Blue4", font = font1)
    passwordlbl.pack()
    global password
    password = tkinter.Entry(frame2, bg = "alice blue", show = "*", font = font2)
    password.pack()

    submit = tkinter.Button(frame2, text = "Login",bg = "RoyalBlue1", font = font1, command = login)
    submit.pack(side=tkinter.TOP)
    
    signup = tkinter.Button(frame2, text = "Create new account",bg = "RoyalBlue1", font = font1, command = signupwindow)
    signup.pack(side=tkinter.TOP)

    global loginErrlbl
    loginErrlbl = tkinter.Label(frame12, bg = "PaleTurquoise1", fg = "red", font = "Verdana 15", wraplength=frame12.winfo_width()-10)

    # Adding bubles in frame1
    #bbl1 = tkinter.Canvas.create_oval(canvas1.winfo_height)
    window.mainloop()

main()