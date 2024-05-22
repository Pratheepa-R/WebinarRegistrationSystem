import mysql.connector as sq
con=sq.connect(host="localhost",user="root",passwd="srk123",database="webinar")
cursor=con.cursor()
'''cursor.execute("create table student(USER_ID varchar(4) primary key,NAME varchar(20),EMAIL_ID varchar(30),PASSWORD varchar(10),PHONE_NUMBER varchar(10))")
cursor.execute("create table Workshops(WORKSHOP_ID integer primary key,TITLE varchar(50),RESOURCE_PERSON varchar(30),DATE varchar(10),TIME varchar(10),MAXIMUM_ATTENDEES integer,CATEGORY varchar(20),FEES_PER_PERSON float(10,2))")
cursor.execute("create table Registration(WORKSHOP_ID integer,USER_ID integer,ATTENDEES integer)")
cursor.execute("create table Registered_Details(WORKSHOP_ID integer,USER_ID integer,ATTENDEES integer,USERNAME varchar(20),PHONE_NUMBER varchar(10))")'''
def addstdrec():
    n1=(userid.get())
    n2=(name.get())
    n3=(emailid.get())
    n4=(passwd.get())
    n5=(phone.get())
    global a
    a=n1
    from tkinter import messagebox
    l=[n1,n2,n3,n4,n5]
    for i in l:
        if len(i)==0:
            messagebox.showinfo("Sign Up Error","All Columns Need To Be Filled")
            break
        elif len(n1)!=4:
            messagebox.showinfo("Sign Up Error","UserID Should Have 4 Characters")
            break
        elif len(n5)!=10:
            messagebox.showinfo("Sign Up Error","Phone Number Should Have 10 Characters")
            break
    else:
        st="insert into student(USER_ID,NAME,EMAIL_ID,PASSWORD,PHONE_NUMBER) values(%s,%s,%s,%s,%s)"
        val=(n1,n2,n3,n4,n5)
        cursor.execute(st,val)
        con.commit()
        r1.destroy()
        main()
def unavailability():
    import tkinter as tk
    global r5
    r5=tk.Tk()
    r5.title("Places Unavailable")
    canvas=Canvas(r5,height=1900,width=1900,bg="#263D42")
    canvas.pack()
    frame=Frame(r5,bg="white")
    frame.place(relheight=1.0,relwidth=0.9,relx=0.05,rely=0)
    global rem
    if rem==0:
        tk.Label(frame,text="Sorry,All Places Are Booked For This Webinar",font=("algerian",40),bg="white",fg="blue").place(x=100,y=100)
    else:
        tk.Label(frame,text="Sorry,Only",font=("algerian",40),bg="white",fg="blue").place(x=100,y=100)
        tk.Label(frame,text=rem,font=("algerian",40),bg="white",fg="blue").place(x=425,y=100)
        tk.Label(frame,text="Place(s) Are Available",font=("algerian",40),bg="white",fg="blue").place(x=490,y=100)
def end():
    import tkinter as tk
    global r4
    r4=tk.Tk()
    r4.title("Registration Successfull")
    canvas=Canvas(r4,height=1900,width=1900,bg="#263D42")
    canvas.pack()
    frame=Frame(r4,bg="white")
    frame.place(relheight=1.0,relwidth=0.9,relx=0.05,rely=0)
    x=(wid.get())
    y=(nofatt.get())
    z=(userid.get())
    p=int(x)
    q=int(y)
    r=int(z)
    st="select * from workshops where workshop_id={}".format(p)
    cursor.execute(st)
    data=cursor.fetchall()
    for i in data:
        title=i[1]
        resource_person=i[2]
        date=i[3]
        time=i[4]
        category=i[6]
        tot_fees=i[7]*q
    tk.Label(frame,text="You Have Registered Successfully",font=("algerian",40),bg="white",fg="blue").place(x=400,y=100)
    tk.Label(frame,text="For The Webinar",font=("algerian",40),bg="white",fg="blue").place(x=600,y=150)
    tk.Label(frame,text="User ID",font=("arial black",20)).place(x=600,y=250)
    tk.Label(frame,text=r,font=("arial black",20)).place(x=1000,y=250)
    tk.Label(frame,text="Workshop ID",font=("arial black",20)).place(x=600,y=300)
    tk.Label(frame,text=p,font=("arial black",20)).place(x=1000,y=300)
    tk.Label(frame,text="Resource Person",font=("arial black",20)).place(x=600,y=350)
    tk.Label(frame,text=resource_person,font=("arial black",20)).place(x=1000,y=350)
    tk.Label(frame,text="Date",font=("arial black",20)).place(x=600,y=400)
    tk.Label(frame,text=date,font=("arial black",20)).place(x=1000,y=400)
    tk.Label(frame,text="Time",font=("arial black",20)).place(x=600,y=450)
    tk.Label(frame,text=time,font=("arial black",20)).place(x=1000,y=450)
    tk.Label(frame,text="Category",font=("arial black",20)).place(x=600,y=500)
    tk.Label(frame,text=category,font=("arial black",20)).place(x=1000,y=500)
    tk.Label(frame,text="No Of Attendees",font=("arial black",20)).place(x=600,y=550)
    tk.Label(frame,text=q,font=("arial black",20)).place(x=1000,y=550)
    tk.Label(frame,text="Total Fees",font=("arial black",20)).place(x=600,y=600)
    tk.Label(frame,text=tot_fees,font=("arial black",20)).place(x=1000,y=600)
def registration():
    x=(wid.get())
    y=(nofatt.get())
    p=int(x)
    q=int(y)
    totatt=0
    global u
    global name_extracted
    global phone_extracted
    z=[]
    from tkinter import messagebox
    l=[x,y]
    for i in l:
        if len(i)==0:
            messagebox.showinfo("Error","All columns have to be filled")
            break
    cursor.execute("select * from Workshops where (date>curdate()) or (date=curdate() and time>current_time())")
    data=cursor.fetchall()
    for i in data:
            a=i[0]
            z.append(a)
    if p in z:
        st="select * from workshops where workshop_id={}".format(p)
        cursor.execute(st)
        data=cursor.fetchall()
        for i in data:
            maxatt=i[5]
        st="select * from registration where workshop_id={}".format(p)
        cursor.execute(st)
        data=cursor.fetchall()
        for i in data:
            totatt=totatt+i[2]
        if q<=maxatt-totatt:
            st="insert into Registration(WORKSHOP_ID,USER_ID,ATTENDEES) values(%s,%s,%s)"
            val=(x,u,y)
            cursor.execute(st,val)
            con.commit()
            st="insert into Registered_Details(WORKSHOP_ID,USER_ID,ATTENDEES,USERNAME,PHONE_NUMBER) values(%s,%s,%s,%s,%s)"
            val=(x,u,y,name_extracted,phone_extracted)
            cursor.execute(st,val)
            con.commit()
            r3.destroy()
            end()
        else:
            global rem
            rem=maxatt-totatt
            unavailability()
    else:
        messagebox.showinfo("Error","Invalid Workshop ID")
def main():
    import tkinter as tk
    global r3
    r3=tk.Tk()
    r3.title("Register For A Webinar")
    canvas=Canvas(r3,height=1900,width=1900,bg="#263D42")
    canvas.pack()
    frame=Frame(r3,bg="white")
    frame.place(relheight=1.0,relwidth=0.9,relx=0.05,rely=0)
    cursor.execute("select * from student")
    data=cursor.fetchall()
    for i in data:
        global a
        global u
        global name_extracted
        global phone_extracted
        u=a
        if a==i[0]:
            name=i[1]
            phone_no=i[4]
            name_extracted=name
            phone_extracted=phone_no
            break
    cursor.execute("select * from Workshops where (date>curdate()) or(date=curdate() and time>current_time())")
    data=cursor.fetchall()
    if len(data)==0:
        tk.Label(frame,text="Sorry",font=("arial black",25),bg="white",fg="blue").place(x=700,y=100)
        tk.Label(frame,text=name,font=("arial black",25),bg="white",fg="blue").place(x=810,y=100)
        tk.Label(frame,text="There are no upcoming webinars",font=("arial black",25),bg="white",fg="blue").place(x=500,y=150)
    else:
        tk.Label(frame,text="Welcome",font=("arial black",15),bg="white",fg="blue").place(x=10,y=25)
        tk.Label(frame,text=name,font=("arial black",15),bg="white",fg="blue").place(x=115,y=25)
        tk.Label(frame,text="Here is the list of upcomimg webinars:",font=("arial black",15)).place(x=10,y=70)
        tk.Label(frame,text="ID",font=("arial black",15)).place(x=10,y=150)
        tk.Label(frame,text="TOPIC",font=("arial black",15)).place(x=100,y=150)
        tk.Label(frame,text="RESOURCE PERSON",font=("arial black",15)).place(x=400,y=150)
        tk.Label(frame,text="DATE",font=("arial black",15)).place(x=675,y=150)
        tk.Label(frame,text="TIME",font=("arial black",15)).place(x=875,y=150)
        tk.Label(frame,text="MAX ATTENDEES",font=("arial black",15)).place(x=1000,y=150)
        tk.Label(frame,text="CATEGORY",font=("arial black",15)).place(x=1250,y=150)
        tk.Label(frame,text="FEES",font=("arial black",15)).place(x=1450,y=150)
        a=10
        b=200
        for i in data:
            for j in range(len(i)):
                if j==len(i)-1:
                    l=tk.Label(frame,text=i[j],font=("arial black",15)).place(x=a,y=b)
                    a=10
                elif j==1:
                    l=tk.Label(frame,text=i[j],font=("arial black",15)).place(x=100,y=b)
                    a=450
                else:
                    l=tk.Label(frame,text=i[j],font=("arial black",15)).place(x=a,y=b)
                    a=a+200
            b=b+50
        global wid
        global nofatt
        wid=tk.StringVar()
        nofatt=tk.StringVar()
        tk.Label(frame,text="Workshop ID:",font=("arial black",15)).place(x=100,y=800)
        tk.Entry(frame,textvariable=wid,width=20,bd=3).place(x=400,y=800)
        tk.Label(frame,text="Number Of Attendees:",font=("arial black",15)).place(x=100,y=850)
        tk.Entry(frame,textvariable=nofatt,width=20,bd=3).place(x=400,y=850)
        tk.Button(frame,text="REGISTER",font=("arial black",20),bg="blue",fg="white",command=registration).place(x=600,y=900)
def checksignin():
    n1=(userid.get())
    n2=(passwd.get())
    cursor.execute("select * from student")
    data=cursor.fetchall()
    from tkinter import messagebox
    for i in data:
        if len(n1)==0 or len(n2)==0:
            messagebox.showinfo("Sign In Error","All Columns Need To Be Filled")
            break
        x=i[0]
        y=i[3]
        if (n1,n2)==(x,y):
            global a
            a=n1
            r2.destroy()
            main()
            break
    else:
        messagebox.showinfo("Account Not Found","Invalid UserID OR Password")
def clicked2():
    root.destroy()
    import tkinter as tk
    global r2
    r2=tk.Tk()
    r2.title("Sign In Page")
    canvas=Canvas(r2,height=1900,width=1900,bg="#263D42")
    canvas.pack()
    frame=Frame(r2,bg="white")
    frame.place(relheight=0.3,relwidth=0.3,relx=0.35,rely=0.3)
    global userid
    global passwd
    userid=tk.StringVar()
    passwd=tk.StringVar()
    tk.Label(frame,text="SIGN IN",font=("algerian",50)).pack()
    tk.Label(frame,text="USER ID",font=("arial black",20)).place(x=50,y=100)
    tk.Entry(frame,textvariable=userid,width=20,bd=3).place(x=300,y=100)
    tk.Label(frame,text="PASSWORD",font=("arial black",20)).place(x=50,y=180)
    tk.Entry(frame,textvariable=passwd,show="*",width=20,bd=3).place(x=300,y=180)
    tk.Button(frame,text="LOGIN",font=("arial black",20),bg="blue",fg="white",command=checksignin).place(x=200,y=250)
def clicked1():
    root.destroy()
    import tkinter as tk
    global r1
    r1=tk.Tk()
    r1.title("Sign Up Page")
    canvas=Canvas(r1,height=1900,width=1900,bg="#263D42")
    canvas.pack()
    frame=Frame(r1,bg="white")
    frame.place(relheight=0.6,relwidth=0.4,relx=0.3,rely=0.2)
    global userid
    global name
    global emailid
    global passwd
    global phone
    userid=tk.StringVar()
    name=tk.StringVar()
    emailid=tk.StringVar()
    passwd=tk.StringVar()
    phone=tk.StringVar()
    tk.Label(frame,text="SIGN UP",font=("algerian",50)).pack()
    tk.Label(frame,text="USER ID",font=("arial black",20)).place(x=100,y=100)
    tk.Entry(frame,textvariable=userid,width=20,bd=3).place(x=500,y=100)
    tk.Label(frame,text="NAME",font=("arial black",20)).place(x=100,y=180)
    tk.Entry(frame,textvariable=name,width=20,bd=3).place(x=500,y=180)
    tk.Label(frame,text="EMAIL-ID",font=("arial black",20)).place(x=100,y=260)
    tk.Entry(frame,textvariable=emailid,width=20,bd=3).place(x=500,y=260)
    tk.Label(frame,text="PASSWORD",font=("arial black",20)).place(x=100,y=340)
    tk.Entry(frame,textvariable=passwd,show="*",width=20,bd=3).place(x=500,y=340)
    tk.Label(frame,text="PHONE NUMBER",font=("arial black",20)).place(x=100,y=420)
    tk.Entry(frame,textvariable=phone,width=20,bd=3).place(x=500,y=420)
    tk.Button(frame,text="SUBMIT",font=("arial black",20),bg="blue",fg="white",command=addstdrec).place(x=300,y=500)
def addingweb():
    from tkinter import messagebox
    a=(workid.get())
    b=(title.get())
    c=(person.get())
    d=(date.get())
    e=(time.get())
    f=(maxatt.get())
    g=(category.get())
    h=(fees.get())
    l=[a,b,c,d,e,f,g,h]
    for i in l:
        if len(i)==0:
            messagebox.showinfo("Error","All Columns Need To Be Filled")
            break
    else:
        st="insert into Workshops(WORKSHOP_ID,TITLE,RESOURCE_PERSON,DATE,TIME,MAXIMUM_ATTENDEES,CATEGORY,FEES_PER_PERSON) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        val=(a,b,c,d,e,f,g,h)
        cursor.execute(st,val)
        con.commit()
        messagebox.showinfo("Added","Workshop Added Successfully")
def removingweb():
    from tkinter import messagebox
    w=(wid.get())
    a=int(w)
    cursor.execute("select * from workshops")
    data=cursor.fetchall()
    for i in data:
        if i[0]==a:
              st="delete from workshops where workshop_id={}".format(a)
              cursor.execute(st)
              con.commit()
              messagebox.showinfo("Removed","Workshop Removed Successfully")
              break
    else:
        messagebox.showinfo("NOT FOUND","Workshop Does Not Exist")
def alter():
    from tkinter import messagebox
    altworkid=int(w)
    a=(alttitle.get())
    b=(altperson.get())
    c=(altdate.get())
    d=(alttime.get())
    e=(altmaxatt.get())
    f=(altcategory.get())
    g=(altfees.get())
    l=[a,b,c,d,e,f,g]
    for i in l:
        if len(i)==0:
            messagebox.showinfo("Error","All Columns Need To Be Filled")
            break
    else:
        st1="update Workshops set TITLE='%s' where WORKSHOP_ID=%s" %(a,altworkid)
        cursor.execute(st1)
        st2="update Workshops set RESOURCE_PERSON='%s' where WORKSHOP_ID=%s" %(b,altworkid)
        cursor.execute(st2)
        st3="update Workshops set DATE='%s' where WORKSHOP_ID=%s" %(c,altworkid)
        cursor.execute(st3)
        st4="update Workshops set TIME='%s' where WORKSHOP_ID=%s" %(d,altworkid)
        cursor.execute(st4)
        st5="update Workshops set MAXIMUM_ATTENDEES=%s where WORKSHOP_ID=%s" %(e,altworkid)
        cursor.execute(st5)
        st6="update Workshops set CATEGORY='%s' where WORKSHOP_ID=%s" %(f,altworkid)
        cursor.execute(st5)
        st7="update Workshops set FEES_PER_PERSON=%s where WORKSHOP_ID=%s" %(g,altworkid)
        cursor.execute(st7)
        con.commit()
        messagebox.showinfo("Altered","Workshop Altered Successfully")
def alteringweb():
    root5.destroy()
    import tkinter as tk
    global root6
    root6=Tk()
    root6.title("Admin Page")
    canvas=Canvas(root6,height=1900,width=1900,bg="#263D42")
    canvas.pack()
    frame=Frame(root6,bg="white")
    frame.place(relheight=0.6,relwidth=0.5,relx=0.25,rely=0.1)
    global alttitle
    global altperson
    global altdate
    global alttime
    global altmaxatt
    global altcategory
    global altfees
    alttitle=tk.StringVar()
    altperson=tk.StringVar()
    altdate=tk.StringVar()
    alttime=tk.StringVar()
    altmaxatt=tk.StringVar()
    altcategory=tk.StringVar()
    altfees=tk.StringVar()
    tk.Label(frame,text="Enter New Details",font=("algerian",30)).pack()
    tk.Label(frame,text="Title",font=("arial black",20)).place(x=100,y=150)
    tk.Entry(frame,textvariable=alttitle,width=20,bd=3).place(x=400,y=150)
    tk.Label(frame,text="Resource Person",font=("arial black",20)).place(x=100,y=200)
    tk.Entry(frame,textvariable=altperson,width=20,bd=3).place(x=400,y=200)
    tk.Label(frame,text="Date",font=("arial black",20)).place(x=100,y=250)
    tk.Label(frame,text="YYYY/MM/DD",font=("arial black",10)).place(x=100,y=300)
    tk.Entry(frame,textvariable=altdate,width=20,bd=3).place(x=400,y=280)
    tk.Label(frame,text="Time",font=("arial black",20)).place(x=100,y=350)
    tk.Entry(frame,textvariable=alttime,width=20,bd=3).place(x=400,y=350)
    tk.Label(frame,text="Max Attendees",font=("arial black",20)).place(x=100,y=400)
    tk.Entry(frame,textvariable=altmaxatt,width=20,bd=3).place(x=400,y=400)
    tk.Label(frame,text="Category",font=("arial black",20)).place(x=100,y=450)
    tk.Entry(frame,textvariable=altcategory,width=20,bd=3).place(x=400,y=450)
    tk.Label(frame,text="Fees",font=("arial black",20)).place(x=100,y=500)
    tk.Entry(frame,textvariable=altfees,width=20,bd=3).place(x=400,y=500)
    tk.Button(frame,text="ALTER",font=("arial black",20),bg="blue",fg="white",command=alter).place(x=200,y=550)
def chkalteringweb():
    from tkinter import messagebox
    global w
    w=(wid.get())
    a=int(w)
    cursor.execute("select * from workshops")
    data=cursor.fetchall()
    for i in data:
        if i[0]==a:
            alteringweb()
            global alteringwid
            alteringwid=a
            break
    else:
        messagebox.showinfo("NOT FOUND","Workshop Does Not Exist")
def remweb():
     root2.destroy()
     import tkinter as tk
     global root4
     root4=Tk()
     root4.title("Admin Page")
     canvas=Canvas(root4,height=1900,width=1900,bg="#263D42")
     canvas.pack()
     frame=Frame(root4,bg="white")
     frame.place(relheight=0.4,relwidth=0.5,relx=0.25,rely=0.25)
     tk.Label(frame,text="Enter Workshop ID To Be Removed",font=("algerian",30)).place(x=125,y=100)
     global wid
     wid=tk.StringVar()
     tk.Entry(frame,textvariable=wid,width=30,bd=3).place(x=375,y=200)
     tk.Button(frame,text="REMOVE",font=("arial black",20),bg="blue",fg="white",command=removingweb).place(x=395,y=275)
def addweb():
    root2.destroy()
    import tkinter as tk
    global root3
    root3=Tk()
    root3.title("Admin Page")
    canvas=Canvas(root3,height=1900,width=1900,bg="#263D42")
    canvas.pack()
    frame=Frame(root3,bg="white")
    frame.place(relheight=0.6,relwidth=0.5,relx=0.25,rely=0.1)
    global workid
    global title
    global person
    global date
    global time
    global maxatt
    global category
    global fees
    workid=tk.StringVar()
    title=tk.StringVar()
    person=tk.StringVar()
    date=tk.StringVar()
    time=tk.StringVar()
    maxatt=tk.StringVar()
    category=tk.StringVar()
    fees=tk.StringVar()
    tk.Label(frame,text="Enter Details Of Webinar",font=("algerian",30)).pack()
    tk.Label(frame,text="Workshop ID",font=("arial black",20)).place(x=100,y=100)
    tk.Entry(frame,textvariable=workid,width=20,bd=3).place(x=400,y=100)
    tk.Label(frame,text="Title",font=("arial black",20)).place(x=100,y=150)
    tk.Entry(frame,textvariable=title,width=20,bd=3).place(x=400,y=150)
    tk.Label(frame,text="Resource Person",font=("arial black",20)).place(x=100,y=200)
    tk.Entry(frame,textvariable=person,width=20,bd=3).place(x=400,y=200)
    tk.Label(frame,text="Date",font=("arial black",20)).place(x=100,y=250)
    tk.Label(frame,text="YYYY/MM/DD",font=("arial black",10)).place(x=100,y=300)
    tk.Entry(frame,textvariable=date,width=20,bd=3).place(x=400,y=280)
    tk.Label(frame,text="Time",font=("arial black",20)).place(x=100,y=350)
    tk.Entry(frame,textvariable=time,width=20,bd=3).place(x=400,y=350)
    tk.Label(frame,text="Max Attendees",font=("arial black",20)).place(x=100,y=400)
    tk.Entry(frame,textvariable=maxatt,width=20,bd=3).place(x=400,y=400)
    tk.Label(frame,text="Category",font=("arial black",20)).place(x=100,y=450)
    tk.Entry(frame,textvariable=category,width=20,bd=3).place(x=400,y=450)
    tk.Label(frame,text="Fees",font=("arial black",20)).place(x=100,y=500)
    tk.Entry(frame,textvariable=fees,width=20,bd=3).place(x=400,y=500)
    tk.Button(frame,text="ADD",font=("arial black",20),bg="blue",fg="white",command=addingweb).place(x=200,y=550)
def altweb():
    root2.destroy()
    import tkinter as tk
    global root5
    root5=Tk()
    root5.title("Admin Page")
    canvas=Canvas(root5,height=1900,width=1900,bg="#263D42")
    canvas.pack()
    frame=Frame(root5,bg="white")
    frame.place(relheight=0.4,relwidth=0.5,relx=0.25,rely=0.25)
    tk.Label(frame,text="Enter Workshop ID To Be Altered",font=("algerian",30)).place(x=125,y=100)
    global wid
    wid=tk.StringVar()
    tk.Entry(frame,textvariable=wid,width=30,bd=3).place(x=375,y=200)
    tk.Button(frame,text="ALTER",font=("arial black",20),bg="blue",fg="white",command=chkalteringweb).place(x=395,y=275)
def listofatt():
    root2.destroy()
    import tkinter as tk
    global root6
    root6=Tk()
    root6.title("List Of Attendees")
    canvas=Canvas(root6,height=1900,width=1900,bg="#263D42")
    canvas.pack()
    frame=Frame(root6,bg="white")
    frame.place(relheight=1.0,relwidth=0.9,relx=0.05,rely=0)
    tk.Label(frame,text="Here is the list of attendees:",font=("arial black",15)).place(x=10,y=70)
    tk.Label(frame,text="WORKSHOP ID",font=("arial black",15)).place(x=10,y=150)
    tk.Label(frame,text="USER ID",font=("arial black",15)).place(x=250,y=150)
    tk.Label(frame,text="ATTENDEES",font=("arial black",15)).place(x=450,y=150)
    tk.Label(frame,text="USERNAME",font=("arial black",15)).place(x=850,y=150)
    tk.Label(frame,text="PHONE NUMBER",font=("arial black",15)).place(x=1250,y=150)
    cursor.execute("select * from registered_details")
    data=cursor.fetchall()
    b=200
    for i in data:
        for j in range(len(i)):
            if j==0:
                tk.Label(frame,text=i[j],font=("arial black",15)).place(x=60,y=b)
            elif j==1:
                tk.Label(frame,text=i[j],font=("arial black",15)).place(x=270,y=b)
            elif j==2:
                tk.Label(frame,text=i[j],font=("arial black",15)).place(x=500,y=b)
            elif j==3:
                tk.Label(frame,text=i[j],font=("arial black",15)).place(x=850,y=b)
            elif j==4:
                tk.Label(frame,text=i[j],font=("arial black",15)).place(x=1250,y=b)
        b=b+50
def click3():
    root1.destroy()
    import tkinter as tk
    global root2
    root2=Tk()
    root2.title("Admin Page")
    canvas=Canvas(root2,height=1900,width=1900,bg="#263D42")
    canvas.pack()
    frame=Frame(root2,bg="white")
    frame.place(relheight=0.5,relwidth=0.5,relx=0.25,rely=0.1)
    b1=tk.Button(frame,text="Add A Webinar",font=("arial black",20),padx=20,bg="blue",fg="white",command=addweb).place(x=100,y=100)
    b2=tk.Button(frame,text="Alter A Webinar",font=("arial black",20),padx=20,bg="blue",fg="white",command=altweb).place(x=100,y=200)
    b3=tk.Button(frame,text="Remove A Webinar",font=("arial black",20),padx=20,bg="blue",fg="white",command=remweb).place(x=100,y=300)
    b4=tk.Button(frame,text="List Of Attendees",font=("arial black",20),padx=20,bg="blue",fg="white",command=listofatt).place(x=100,y=400)
def click2():
    r.destroy()
    import tkinter as tk
    global root
    root=Tk()
    root.title("Webinar Registration")
    canvas=Canvas(root,height=1900,width=1900,bg="#263D42")
    canvas.pack()
    frame=Frame(root,bg="white")
    frame.place(relheight=0.5,relwidth=0.5,relx=0.25,rely=0.1)
    label=Label(frame,text="WEBINAR REGISTRATION",font=("algerian",50))
    label.pack()
    l1=Label(frame,text="Don't Have An Account? Sign Up",font=("arial black",15)).place(x=300,y=125)
    l2=Label(frame,text="Already Have An Account? Sign In",font=("arial black",15)).place(x=300,y=250)
    signup=Button(frame,text="Sign Up",font=("arial black",20),padx=15,bg="blue",fg="white",command=clicked1).place(x=400,y=170)
    signin=Button(frame,text="Sign In",font=("arial black",20),padx=20,bg="blue",fg="white",command=clicked2).place(x=400,y=300)
def admchk():
    from tkinter import messagebox
    a=(password.get())
    if a=="webreg537":
        click3()
    else:
        messagebox.showinfo("Login Error","Incorrect Password")
def click1():
    r.destroy()
    import tkinter as tk
    global root1
    root1=tk.Tk()
    root1.title("Admin Page")
    canvas=Canvas(root1,height=1900,width=1900,bg="#263D42")
    canvas.pack()
    frame=Frame(root1,bg="white")
    frame.place(relheight=0.3,relwidth=0.5,relx=0.25,rely=0.3)
    tk.Label(frame,text="Enter Password",font=("algerian",40)).place(x=250,y=10)
    global password
    password=tk.StringVar()
    tk.Entry(frame,textvariable=password,width=40,bd=3,show="*").place(x=350,y=125)
    tk.Button(frame,text="Login",font=("arial black",20),padx=30,bg="blue",fg="white",command=admchk).place(x=390,y=200)
from tkinter import *
global r
r=Tk()
r.title("Webinar Registration")
canvas=Canvas(r,height=1900,width=1900,bg="#263D42")
canvas.pack()
frame=Frame(r,bg="white")
frame.place(relheight=0.5,relwidth=0.5,relx=0.25,rely=0.1)
label=Label(frame,text="WEBINAR REGISTRATION",font=("algerian",50))
label.pack()
b1=Button(frame,text="Admin",font=("arial black",20),padx=15,bg="blue",fg="white",command=click1).place(x=400,y=170)
b2=Button(frame,text="User",font=("arial black",20),padx=30,bg="blue",fg="white",command=click2).place(x=400,y=300)




