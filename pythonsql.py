
import mysql.connector as sql
import tkinter

con = sql.connect(host="localhost", user = "root", passwd = "Winter123!", database = "pythonproject")
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

def signupwindow1():
    frame1.destroy()
    frame12.destroy()
    frame2.destroy()

    frame3=tkinter.Frame(window)
    Emaillbl = tkinter.Label(frame3, text = "Email:", fg = "Blue4")
    Emaillbl.grid(row=0,column=0)
    global Email
    Email = tkinter.Entry(frame3)
    Email.grid(row=0,column=1)

    passwordlbl = tkinter.Label(frame3, text = "Password:", fg = "Blue4")
    passwordlbl.grid(row=1,column=0)
    global Password
    Password = tkinter.Entry(frame3, show = "*")
    Password.grid(row=1,column=1)

    firstnamelbl = tkinter.Label(frame3, text = "First Name:", fg = "Blue4")
    firstnamelbl.grid(row=2,column=0)
    global FirstName
    FirstName = tkinter.Entry(frame3)
    FirstName.grid(row=2,column=1)

    lastnamelbl = tkinter.Label(frame3, text = "Last Name:", fg = "Blue4")
    lastnamelbl.grid(row=3,column=0)
    global LastName
    LastName = tkinter.Entry(frame3)
    LastName.grid(row=3,column=1)
    
    Next=tkinter.Button(frame3, text = "Next",bg = "RoyalBlue1", command = lambda:[window.destroy(), signup1()])
    Next.grid(row=6,column=5)
    frame3.pack()
def signupwindow2():
    hslbl = tkinter.Label(frame3, text = "High School:", fg = "Blue4")
    hslbl.grid(row=4,column=0)
    global Highschool
    Highschool = tkinter.Entry(frame3)
    Highschool.grid(row=4,column=1)
    
    uglbl = tkinter.Label(frame3, text = "Undergraduate School:", fg = "Blue4")
    uglbl.grid(row=5,column=0)
    global Undergraduate
    Undergraduate = tkinter.Entry(frame3)
    Undergraduate.grid(row=5,column=1)

    glbl = tkinter.Label(frame3, text = "Graduate School:", fg = "Blue4")
    glbl.grid(row=6,column=0)
    global Graduate
    Graduate = tkinter.Entry(frame3)
    Graduate.grid(row=6,column=1)

    doblbl = tkinter.Label(frame3, text = "DOB:", fg = "Blue4")
    doblbl.grid(row=7,column=0)
    global DOB
    DOB = tkinter.Entry(frame3)
    DOB.grid(row=7,column=1)

    sub1lbl = tkinter.Label(frame3, text = "Subject 1:", fg = "Blue4")
    sub1lbl.grid(row=0,column=2)
    global Sub1
    Sub1 = tkinter.Entry(frame3)
    Sub1.grid(row=0,column=3)
    
    sub2lbl = tkinter.Label(frame3, text = "Subject 2:", fg = "Blue4")
    sub2lbl.grid(row=1,column=2)
    global Sub2
    Sub2 = tkinter.Entry(frame3)
    Sub2.grid(row=1,column=3)

    sub3lbl = tkinter.Label(frame3, text = "Subject 3:", fg = "Blue4")
    sub3lbl.grid(row=2,column=2)
    global Sub3
    Sub3 = tkinter.Entry(frame3)
    Sub3.grid(row=2,column=3)

    sub4lbl = tkinter.Label(frame3, text = "Subject 4:", fg = "Blue4")
    sub4lbl.grid(row=3,column=2)
    global Sub4
    Sub4 = tkinter.Entry(frame3)
    Sub4.grid(row=3,column=3)

    sub5lbl = tkinter.Label(frame3, text = "Subject 5:", fg = "Blue4")
    sub5lbl.grid(row=4,column=2)
    global Sub5
    Sub5 = tkinter.Entry(frame3)
    Sub5.grid(row=4,column=3)

    test1lbl = tkinter.Label(frame3, text = "Test 1:", fg = "Blue4")
    test1lbl.grid(row=0,column=4)
    global Test1
    Test1 = tkinter.Entry(frame3)
    Test1.grid(row=0,column=5)

    test2lbl = tkinter.Label(frame3, text = "Test 2:", fg = "Blue4")
    test2lbl.grid(row=1,column=4)
    global Test2
    Test2 = tkinter.Entry(frame3)
    Test2.grid(row=1,column=5)

    test3lbl = tkinter.Label(frame3, text = "Test 3:", fg = "Blue4")
    test3lbl.grid(row=2,column=4)
    global Test3
    Test3 = tkinter.Entry(frame3)
    Test3.grid(row=2,column=5)

    test4lbl = tkinter.Label(frame3, text = "Test 4:", fg = "Blue4")
    test4lbl.grid(row=3,column=4)
    global Test4
    Test4 = tkinter.Entry(frame3)
    Test4.grid(row=3,column=5)
    
    test5lbl = tkinter.Label(frame3, text = "Test 5:", fg = "Blue4")
    test5lbl.grid(row=4,column=4)
    global Test5
    Test5 = tkinter.Entry(frame3)
    Test5.grid(row=4,column=5)

    submit = tkinter.Button(frame3, text = "Sign up",bg = "RoyalBlue1", command = signup2)
    submit.grid(row=6,column=3)

    back=tkinter.Button(frame3, text = "Back",bg = "RoyalBlue1", command = lambda:[window.destroy(), signupwindow1()])
    back.grid(row=6,column=5)
    
    frame3.pack()
    
def signup1():
    Email1=Email.get()
    Password1=Password.get()
    FirstName1=FirstName.get()
    LastName1=LastName.get()
    Highschool1=Highschool.get()
    
    cursor=con.cursor()
    try:
        cursor.execute("INSERT INTO AccDetails values('{}','{}','{}','{}')".format(Email1, Password1, FirstName1, LastName1))
    except sql.Error as Err:
        print(Err)
    cursor.close()
    
def signup2():
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
        cursor.execute("INSERT INTO AccDetails values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(Highschool1, Undergraduate1, Graduate1, DOB1, S1, S2, S3, S4, S5, T1, T2, T3, T4, T5))
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
    frame2 = tkinter.Frame(frame12, bg = "alice blue")

    Emaillbl = tkinter.Label(frame2, text = "Email", bg = "alice blue", fg = "Blue4", font = "Verdana 20 bold")
    Emaillbl.pack(side=tkinter.TOP, expand=tkinter.YES)
    global Email
    Email = tkinter.Entry(frame2, bg = "PaleTurquoise2", font = "Verdana 15 bold")
    Email.pack(side=tkinter.TOP, expand=tkinter.YES)

    passwordlbl = tkinter.Label(frame2, text = "Password", bg = "alice blue", fg = "Blue4", font = "Verdana 20 bold")
    passwordlbl.pack(side=tkinter.TOP, expand=tkinter.YES)
    global password
    password = tkinter.Entry(frame2, bg = "PaleTurquoise2", show = "*", font = "Verdana 15 bold")
    password.pack(side=tkinter.TOP, expand=tkinter.YES)

    submit = tkinter.Button(frame2, text = "Login",bg = "RoyalBlue1", font = "Verdana 20 bold", command = login)
    submit.pack(side=tkinter.TOP, expand=tkinter.YES)

    signup = tkinter.Button(frame2, text = "Create new account",bg = "RoyalBlue1", font = "Verdana 20 bold", command = signupwindow1)
    signup.pack(side=tkinter.TOP, expand=tkinter.YES)

    frame2.place(relx =0.5, rely=0.5,anchor=tkinter.CENTER)
    frame1.place(relx = 0, relwidth = 0.7, relheight=1)
    frame12.place(relx = 0.7, relwidth = 0.3, relheight=1)

    window.mainloop()

main()