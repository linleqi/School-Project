
import mysql.connector as sql
import tkinter
from tkinter import ttk

global testsList
testsList = ["SAT", "TOEFL", "IELTS", "SAT Maths 2", "SAT Maths 1", "SAT Literature", "SAT Philosophy", "SAT Japanese", "SAT US History", "SAT World History", "JLPTN1", "JLPTN2", "JLPTN3", "JLPTN4", "JLPTN5"]
global subjectList
subjectList = ["Maths", "Physics", "Chemistry", "English", "Biology", "History", "Economics", "Entrepreneurship", "Accounting", "Computer Science", "Psychology"]

con = sql.connect(host="localhost", user = "root", passwd = "grade12", database = "pythonproject")
if (con.is_connected()):
    print("Connection is successfull!!")
else:
    print("Not connected!")

def login():
    username = Email.get()
    password1 = password.get()
    cursor=con.cursor()
    cursor.execute("SELECT * FROM AccDetails WHERE Email='"+str(username)+"'AND Password='"+str(password1)+"';")
    records=cursor.fetchall()
    if len(records)==1:
        print("Login Successfull!")
    else:
        print("Incorrect Email or Password. Please try again.")
    cursor.close()

def signupwindow():
    global subList
    subList = subjectList
    global testList
    testList = testsList
    frame1.destroy()
    frame12.destroy()
    frame2.destroy()

    frame3=tkinter.Frame(window)
    
    Emaillbl = tkinter.Label(frame3, text = "Email:", fg = "Blue4", font = "Verdana 15 bold")
    Emaillbl.grid(row=0,column=0)
    global Email
    Email = tkinter.Entry(frame3)
    Email.grid(row=0,column=1)

    passwordlbl = tkinter.Label(frame3, text = "Password:", fg = "Blue4", font = "Verdana 15 bold")
    passwordlbl.grid(row=1,column=0)
    global Password
    Password = tkinter.Entry(frame3, show = "*")
    Password.grid(row=1,column=1)

    firstnamelbl = tkinter.Label(frame3, text = "First Name:", fg = "Blue4", font = "Verdana 15 bold")
    firstnamelbl.grid(row=2,column=0)
    global FirstName
    FirstName = tkinter.Entry(frame3)
    FirstName.grid(row=2,column=1)

    lastnamelbl = tkinter.Label(frame3, text = "Last Name:", fg = "Blue4", font = "Verdana 15 bold")
    lastnamelbl.grid(row=3,column=0)
    global LastName
    LastName = tkinter.Entry(frame3)
    LastName.grid(row=3,column=1)

    back=tkinter.Button(frame3, text = "Back", bg = "RoyalBlue1", font = "Verdana 15 bold", command = lambda:[window.destroy(), main()])
    back.grid(row=6,column=5)
    
    next1=tkinter.Button(frame3, text = "Next", bg = "RoyalBlue1", font = "Verdana 15 bold", command = lambda:[frame3.place_forget(),frame4.place(relx =0.5, rely=0.5,anchor=tkinter.CENTER)])
    next1.grid(row=6,column=6)

    frame3.place(relx =0.5, rely=0.5,anchor=tkinter.CENTER)

    global frame4
    frame4=tkinter.Frame(window)

    hslbl = tkinter.Label(frame4, text = "High School:", fg = "Blue4", font = "Verdana 15 bold")
    hslbl.grid(row=0,column=0)
    global Highschool
    Highschool = tkinter.Entry(frame4)
    Highschool.grid(row=0,column=1)
    
    uglbl = tkinter.Label(frame4, text = "Undergraduate School:", fg = "Blue4", font = "Verdana 15 bold")
    uglbl.grid(row=1,column=0)
    global Undergraduate
    Undergraduate = tkinter.Entry(frame4)
    Undergraduate.grid(row=1,column=1)

    glbl = tkinter.Label(frame4, text = "Graduate School:", fg = "Blue4", font = "Verdana 15 bold")
    glbl.grid(row=2,column=0)
    global Graduate
    Graduate = tkinter.Entry(frame4)
    Graduate.grid(row=2,column=1)

    doblbl = tkinter.Label(frame4, text = "DOB:", fg = "Blue4", font = "Verdana 15 bold")
    doblbl.grid(row=3,column=0)
    global DOB
    DOB = tkinter.Entry(frame4)
    DOB.grid(row=3,column=1)

    sub1lbl = tkinter.Label(frame4, text = "Subject 1:", fg = "Blue4", font = "Verdana 15 bold")
    sub1lbl.grid(row=0,column=2)
    global Sub1
    Sub1 = ttk.Combobox(frame4, values = ["None"]+subList)
    Sub1.current(0)
    Sub1.grid(row=0,column=3)
    Sub1.bind("<<ComboboxSelected>>", changeSubList)
    
    sub2lbl = tkinter.Label(frame4, text = "Subject 2:", fg = "Blue4", font = "Verdana 15 bold")
    sub2lbl.grid(row=1,column=2)
    global Sub2
    Sub2 = ttk.Combobox(frame4, values = ["None"]+subList)
    Sub2.current(0)
    Sub2.grid(row=1,column=3)
    Sub2.bind("<<ComboboxSelected>>", changeSubList)

    sub3lbl = tkinter.Label(frame4, text = "Subject 3:", fg = "Blue4", font = "Verdana 15 bold")
    sub3lbl.grid(row=2,column=2)
    global Sub3
    Sub3 = ttk.Combobox(frame4, values = ["None"]+subList)
    Sub3.current(0)
    Sub3.grid(row=2,column=3)
    Sub3.bind("<<ComboboxSelected>>", changeSubList)

    sub4lbl = tkinter.Label(frame4, text = "Subject 4:", fg = "Blue4", font = "Verdana 15 bold")
    sub4lbl.grid(row=3,column=2)
    global Sub4
    Sub4 = ttk.Combobox(frame4, values = ["None"]+subList)
    Sub4.current(0)
    Sub4.grid(row=3,column=3)
    Sub4.bind("<<ComboboxSelected>>", changeSubList)

    sub5lbl = tkinter.Label(frame4, text = "Subject 5:", fg = "Blue4", font = "Verdana 15 bold")
    sub5lbl.grid(row=4,column=2)
    global Sub5
    Sub5 = ttk.Combobox(frame4, values = ["None"]+subList)
    Sub5.current(0)
    Sub5.grid(row=4,column=3)
    Sub5.bind("<<ComboboxSelected>>", changeSubList)

    test1lbl = tkinter.Label(frame4, text = "Test 1:", fg = "Blue4", font = "Verdana 15 bold")
    test1lbl.grid(row=0,column=4)
    global Test1
    Test1 = ttk.Combobox(frame4, values = ["None"]+testList)
    Test1.current(0)
    Test1.grid(row=0,column=5)
    Test1.bind("<<ComboboxSelected>>", changeTestList)

    test2lbl = tkinter.Label(frame4, text = "Test 2:", fg = "Blue4", font = "Verdana 15 bold")
    test2lbl.grid(row=1,column=4)
    global Test2
    Test2 = ttk.Combobox(frame4, values = ["None"]+testList)
    Test2.current(0)
    Test2.grid(row=1,column=5)
    Test2.bind("<<ComboboxSelected>>", changeTestList)

    test3lbl = tkinter.Label(frame4, text = "Test 3:", fg = "Blue4", font = "Verdana 15 bold")
    test3lbl.grid(row=2,column=4)
    global Test3
    Test3 = ttk.Combobox(frame4, values = ["None"]+testList)
    Test3.current(0)
    Test3.grid(row=2,column=5)
    Test3.bind("<<ComboboxSelected>>", changeTestList)

    test4lbl = tkinter.Label(frame4, text = "Test 4:", fg = "Blue4", font = "Verdana 15 bold")
    test4lbl.grid(row=3,column=4)
    global Test4
    Test4 = ttk.Combobox(frame4, values = ["None"]+testList)
    Test4.current(0)
    Test4.grid(row=3,column=5)
    Test4.bind("<<ComboboxSelected>>", changeTestList)
    
    test5lbl = tkinter.Label(frame4, text = "Test 5:", fg = "Blue4", font = "Verdana 15 bold")
    test5lbl.grid(row=4,column=4)
    global Test5
    Test5 = ttk.Combobox(frame4, values = ["None"]+testList)
    Test5.current(0)
    Test5.grid(row=4,column=5)
    Test5.bind("<<ComboboxSelected>>", changeTestList)

    resetSubs=tkinter.Button(frame4, text = "Reset Subjects",bg = "RoyalBlue1", font = "Verdana 15 bold", command = lambda:[frame4.place_forget(), frame3.place(relx =0.5, rely=0.5,anchor=tkinter.CENTER)])
    back.grid(row=6,column=3)

    resetTests=tkinter.Button(frame4, text = "Reset Tests",bg = "RoyalBlue1", font = "Verdana 15 bold", command = lambda:[frame4.place_forget(), frame3.place(relx =0.5, rely=0.5,anchor=tkinter.CENTER)])
    back.grid(row=6,column=5)
    
    back=tkinter.Button(frame4, text = "Back",bg = "RoyalBlue1", font = "Verdana 15 bold", command = lambda:[frame4.place_forget(), frame3.place(relx =0.5, rely=0.5,anchor=tkinter.CENTER)])
    back.grid(row=7,column=3)
    
    submit = tkinter.Button(frame4, text = "Sign up",bg = "RoyalBlue1", font = "Verdana 15 bold", command = signup)
    submit.grid(row=7,column=5)

def changeSubList(*args):
    if Sub1.get() in subList:
        subList.remove(Sub1.get())
        Sub1["values"] = ["None"]+subList
        Sub2["values"] = ["None"]+subList
        Sub3["values"] = ["None"]+subList
        Sub4["values"] = ["None"]+subList
        Sub5["values"] = ["None"]+subList
        Sub1["state"] = "disabled"
    if Sub2.get() in subList:
        subList.remove(Sub2.get())
        Sub1["values"] = ["None"]+subList
        Sub2["values"] = ["None"]+subList
        Sub3["values"] = ["None"]+subList
        Sub4["values"] = ["None"]+subList
        Sub5["values"] = ["None"]+subList
        Sub2["state"] = "disabled"
    if Sub3.get() in subList:
        subList.remove(Sub3.get())
        Sub1["values"] = ["None"]+subList
        Sub2["values"] = ["None"]+subList
        Sub3["values"] = ["None"]+subList
        Sub4["values"] = ["None"]+subList
        Sub5["values"] = ["None"]+subList
        Sub3["state"] = "disabled"
    if Sub4.get() in subList:
        subList.remove(Sub4.get())
        Sub1["values"] = ["None"]+subList
        Sub2["values"] = ["None"]+subList
        Sub3["values"] = ["None"]+subList
        Sub4["values"] = ["None"]+subList
        Sub5["values"] = ["None"]+subList
        Sub4["state"] = "disabled"
    if Sub5.get() in subList:
        subList.remove(Sub5.get())
        Sub1["values"] = ["None"]+subList
        Sub2["values"] = ["None"]+subList
        Sub3["values"] = ["None"]+subList
        Sub4["values"] = ["None"]+subList
        Sub5["values"] = ["None"]+subList
        Sub5["state"] = "disabled"

def changeTestList(*args):
    if Test1.get() in testList:
        testList.remove(Test1.get())
        Test1["values"] = ["None"]+testList
        Test2["values"] = ["None"]+testList
        Test3["values"] = ["None"]+testList
        Test4["values"] = ["None"]+testList
        Test5["values"] = ["None"]+testList
        Test1["state"] = "disabled"
    if Test2.get() in testList:
        testList.remove(Test2.get())
        Test1["values"] = ["None"]+testList
        Test2["values"] = ["None"]+testList
        Test3["values"] = ["None"]+testList
        Test4["values"] = ["None"]+testList
        Test5["values"] = ["None"]+testList
        Test2["state"] = "disabled"
    if Test3.get() in testList:
        testList.remove(Test3.get())
        Test1["values"] = ["None"]+testList
        Test2["values"] = ["None"]+testList
        Test3["values"] = ["None"]+testList
        Test4["values"] = ["None"]+testList
        Test5["values"] = ["None"]+testList
        Test3["state"] = "disabled"
    if Test4.get() in testList:
        testList.remove(Test4.get())
        Test1["values"] = ["None"]+testList
        Test2["values"] = ["None"]+testList
        Test3["values"] = ["None"]+testList
        Test4["values"] = ["None"]+testList
        Test5["values"] = ["None"]+testList
        Test4["state"] = "disabled"
    if Test5.get() in testList:
        testList.remove(Test5.get())
        Test1["values"] = ["None"]+testList
        Test2["values"] = ["None"]+testList
        Test3["values"] = ["None"]+testList
        Test4["values"] = ["None"]+testList
        Test5["values"] = ["None"]+testList
        Test5["state"] = "disabled"
    
def resetSubjects():
    Sub1["values"] = ["None"]+subjectList
    Sub2["values"] = ["None"]+subjectList
    Sub3["values"] = ["None"]+subjectList
    Sub4["values"] = ["None"]+subjectList
    Sub5["values"] = ["None"]+subjectList

def resetTests():
    Test1["values"] = ["None"]+testsList
    Test2["values"] = ["None"]+testsList
    Test3["values"] = ["None"]+testsList
    Test4["values"] = ["None"]+testsList
    Test5["values"] = ["None"]+testsList

def signup():
    Email1=Email.get()
    Password1=Password.get()
    FirstName1=FirstName.get()
    LastName1=LastName.get()
    Highschool1=Highschool.get()
    Undergraduate1=Undergraduate.get()
    Graduate1=Graduate.get()
    DOB1=DOB.get()
    S1=Sub1.get()
    S2=Sub2.get()
    S3=Sub3.get()
    S4=Sub4.get()
    S5=Sub5.get() 
    T1=Test1.get()
    T2=Test2.get()
    T3=Test3.get()
    T4=Test4.get()
    T5=Test5.get()
    cursor=con.cursor()
    try:
        cursor.execute("INSERT INTO AccDetails values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(Email1, Password1, FirstName1, LastName1, Highschool1, Undergraduate1, Graduate1, DOB1, S1, S2, S3, S4, S5, T1, T2, T3, T4, T5))
        con.commit()
    except sql.Error as Err:
        print(Err)
    cursor.close()

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

def main():
    global window
    global frame1
    global frame12
    global frame2

    window = tkinter.Tk()
    window.geometry("1000x500")
    window.title("Tutor Finder!")

    frame1 = tkinter.Frame(window, bg = "azure")
    frame12 = tkinter.Frame(window, bg = "PaleTurquoise2")
    frame2 = tkinter.Frame(frame12, bg = "blue", borderwidth = "1")

    Emaillbl = tkinter.Label(frame2, text = "Email", bg = "PaleTurquoise2", fg = "Blue4", font = "Verdana 20 bold")
    #Emaillbl.pack(side=tkinter.TOP, expand=tkinter.YES)
    Emaillbl.pack()
    global Email
    Email = tkinter.Entry(frame2, bg = "alice blue", font = "Verdana 15 bold")
    #Email.pack(side=tkinter.TOP, expand=tkinter.YES)
    Email.pack()

    passwordlbl = tkinter.Label(frame2, text = "Password", bg = "PaleTurquoise2", fg = "Blue4", font = "Verdana 20 bold")
    #passwordlbl.pack(side=tkinter.TOP, expand=tkinter.YES)
    passwordlbl.pack()
    global password
    password = tkinter.Entry(frame2, bg = "alice blue", show = "*", font = "Verdana 15 bold")
    password.pack()
    #password.pack(side=tkinter.TOP, expand=tkinter.YES)

    submit = tkinter.Button(frame2, text = "Login",bg = "RoyalBlue1", font = "Verdana 15 bold", command = login)
    #submit.pack(side=tkinter.TOP, expand=tkinter.YES)
    submit.pack(side=tkinter.TOP)
    
    signup = tkinter.Button(frame2, text = "Create new account",bg = "RoyalBlue1", font = "Verdana 15 bold", command = signupwindow)
    #signup.pack(side=tkinter.TOP, expand=tkinter.YES)
    signup.pack(side=tkinter.TOP)

    frame2.place(relx =0.5, rely=0.5,anchor=tkinter.CENTER)
    frame1.place(relx = 0, relwidth = 0.7, relheight=1)
    frame12.place(relx = 0.7, relwidth = 0.3, relheight=1)

    window.mainloop()

main()
