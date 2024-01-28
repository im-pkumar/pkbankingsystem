from tkinter import *
from tkinter import messagebox
import time
from tkinter.ttk import Combobox
import sqlite3 as slite

win = Tk()
win.state("zoomed")
win.configure(bg="medium sea green")
win.resizable(width=False,height=False)

header = Label(win,text="PK BANKING SYSTEM",font=("broadway",60,'bold'),bg="medium sea green",fg="black")
header.pack()

date = Label(win,text=time.ctime(),font=("calibri",16,"bold"),bg="medium sea green",fg="pale green")
date.place(relx=0.82,rely=0.12)


#   database 
try:
    con = slite.connect(database="pkbankdb.sqlite3")
    cur = con.cursor()
    cur.execute("create table pkacnholder(acno integer primary key autoincrement,type text, name text not null, email varchar(50), mob integer not null, pas varcha(8) not null, sal float, opdate text)")
    con.commit()
    print("Table created successfuly!")
except:
    print("Something went wrong! Might be table already exists.")
con.close()

def mainscreen():
    frame = Frame(win)
    frame.configure(bg="light blue")
    frame.place(relx=0,rely=0.16,relwidth=1,relheight=0.855)    

    def reset():
            e_acno.delete(0,"end")
            e_pas.delete(0,"end")
            e_acno.focus()
            print("Reset Done!");

    def login():
        acn = e_acno.get()
        pas = e_pas.get()   

        if len(acn) == 0 or len(pas) == 0:
            messagebox.showerror(message="Invalid! Empty credentials not allowed.",title="Message")
        
        else:
            #database check
            conobj=slite.connect("pkbankdb.sqlite3")
            cur=conobj.cursor()
            cur.execute("select * from pkacnholder where acno=? and pas=?",(acn,pas))
            data=cur.fetchone()
            conobj.close()
             
            if data == None:    
                messagebox.showerror(message="Incorrect! Enter correct credentials.",title="Message")
                reset()
            else:
                print("Login successful!")
                global gacno,gname
                gacno=data[0]
                gname=data[2]
                frame.destroy()
                homescreen()

    def fp():
        frame.destroy() 
        forgetpassscreen()

    def signup():
        frame.destroy()
        acnopenscreen()

    l_acno = Label(frame,text="A/C No:",font=("Arial",18,"bold"),bg="light blue",fg="blue2")
    l_acno.place(relx=0.2,rely=0.15)

    l_pas = Label(frame,text="Password:",font=("Arial",18,"bold"),bg="light blue",fg="blue2")
    l_pas.place(relx=0.2,rely=0.3)

    e_acno = Entry(frame,width=40,font=("calibri",20,"bold"),bg="white",fg="blue2",bd=5)
    e_acno.place(relx=0.35,rely=0.15)

    e_pas = Entry(frame,width=40,font=("calibri",20,"bold"),bg="white",fg="blue2",bd=5,show="*")
    e_pas.place(relx=0.35,rely=0.3)

    b_login = Button(frame,text="Login",width=10,font=("Calibri",16,"bold"),fg="light cyan",bg="dark slate gray",bd=2,command=login)
    b_login.place(relx=0.4,rely=0.5)

    b_reset = Button(frame,text="Reset",width=10,font=("Calibri",16,"bold"),fg="light cyan",bg="dark slate gray",bd=2,command=reset)
    b_reset.place(relx=0.5,rely=0.5)

    b_ftpas = Button(frame,text="Forgot Password",width=20,font=("Calibri",16,"bold"),fg="light cyan",bg="dark slate gray",bd=2,command=fp)
    b_ftpas.place(relx=0.41,rely=0.60)

    b_signup = Button(frame,text="Open An Account",width=27,font=("Calibri",16,"bold"),fg="light cyan",bg="dark slate gray",bd=2,command=signup)
    b_signup.place(relx=0.38,rely=0.70)

def forgetpassscreen():
    frame = Frame(win)
    frame.configure(bg="light blue")
    frame.place(relx=0,rely=0.16,relwidth=1,relheight=0.85)

    def fp_reset():
        e_fp_acno.delete(0,"end")
        e_fp_email.delete(0,"end")
        e_fp_mob.delete(0,"end")

    def fp_back():
        frame.destroy()
        mainscreen()

    def fp_submit():
        acn = e_fp_acno.get()
        mob = e_fp_mob.get()
        email = e_fp_email.get()

        #   databse
        conobj = slite.connect(database="pkbankdb.sqlite3")
        cur = conobj.cursor()
        cur.execute("select pas from pkacnholder where acno=? and mob=? and email=?",(acn,mob,email))
        fp_data = cur.fetchone()
        conobj.close()
        
        if fp_data == None:
            messagebox.showwarning(title="Warning",message="Wrong credentials! Enter correct data.")
        else:
            messagebox.showinfo(title="Message",message=f"Your Password for Account- {acn} is {fp_data[0]}")
            fp_reset()


    fp_acno = Label(frame,text="A/C No:",font=("Arial",18,"bold"),bg="light blue",fg="blue2")
    fp_acno.place(relx=0.2,rely=0.25)

    e_fp_acno = Entry(frame,width=40,font=("calibri",20,"bold"),bg="white",fg="blue2",bd=5)
    e_fp_acno.place(relx=0.35,rely=0.25)

    fp_mob = Label(frame,text="Mobile No:",font=("Arial",18,"bold"),bg="light blue",fg="blue2")
    fp_mob.place(relx=0.2,rely=0.35)

    e_fp_mob = Entry(frame,width=40,font=("calibri",20,"bold"),bg="white",fg="blue2",bd=5)
    e_fp_mob.place(relx=0.35,rely=0.35)

    fp_email = Label(frame,text="Email ID:",font=("Arial",18,"bold"),bg="light blue",fg="blue2")
    fp_email.place(relx=0.2,rely=0.45)

    e_fp_email = Entry(frame,width=40,font=("calibri",20,"bold"),bg="white",fg="blue2",bd=5)
    e_fp_email.place(relx=0.35,rely=0.45)

    b_fp_submit = Button(frame,text="Submit",width=20,font=("Calibri",16,"bold"),fg="light cyan",bg="dark slate gray",bd=2,command=fp_submit)
    b_fp_submit.place(relx=0.3,rely=0.60)

    b_fp_reset = Button(frame,text="Reset",width=20,font=("Calibri",16,"bold"),fg="light cyan",bg="dark slate gray",bd=2,command=fp_reset)
    b_fp_reset.place(relx=0.5,rely=0.60)

    b_fp_back = Button(frame,text="Back",width=5,font=("Arial",16,"bold"),fg="light cyan",bg="dark slate gray",bd=2,command=fp_back)
    b_fp_back.place(relx=0.0,rely=0.0)


def acnopenscreen():
    frame = Frame(win)
    frame.configure(bg="light blue")
    frame.place(relx=0,rely=0.16,relwidth=1,relheight=0.850)

    def op_reset():
        e_op_name.delete(0,"end")
        e_op_email.delete(0,"end")
        e_op_mob.delete(0,"end")
        e_op_pas.delete(0,"end")
        e_op_type.current(0)

    def submit_chk():
        name = e_op_name.get()
        mob = e_op_mob.get()
        type = e_op_type.get()

        #   database
        conobj = slite.connect(database="pkbankdb.sqlite3")
        cur = conobj.cursor()
        cur.execute("select * from pkacnholder where type=? and mob=? and name=?",(type,mob,name))
        chkdata = cur.fetchone() 
        conobj.close()
        if chkdata == None:
            acopened()
        else:
            messagebox.showwarning(title="Message",message="Account Already exists!")
            op_reset()    

    def acopened():
        name = e_op_name.get()
        email = e_op_email.get()
        mob = e_op_mob.get()
        pas = e_op_pas.get()
        dt = time.ctime()
        type = e_op_type.get()
        bal = 0

        #   database
        conobj = slite.connect(database="pkbankdb.sqlite3")
        cur = conobj.cursor()
        cur.execute("insert into pkacnholder(type,name,email,mob,pas,sal,opdate) values(?,?,?,?,?,?,?)",(type,name,email,mob,pas,bal,dt))
        conobj.commit()
        conobj.close()

        conobj = slite.connect(database="pkbankdb.sqlite3")
        cur = conobj.cursor()
        cur.execute("select max(acno) from pkacnholder")
        data=cur.fetchone()
        conobj.close()
        messagebox.showinfo(title="Message",message=f"Account Opened A/C No. {data[0]} ")
        print("Successfully Opened!")
        mainscreen()

    def op_back():
        frame.destroy()
        mainscreen()

    l_op_name = Label(frame,text="Name:",font=("Arial",18,"bold"),bg="light blue",fg="blue2")
    l_op_name.place(relx=0.2,rely=0.15)

    e_op_name = Entry(frame,width=40,font=("calibri",20,"bold"),bg="white",fg="blue2",bd=5)
    e_op_name.place(relx=0.35,rely=0.15)

    l_op_email = Label(frame,text="Email ID:",font=("Arial",18,"bold"),bg="light blue",fg="blue2")
    l_op_email.place(relx=0.2,rely=0.25)

    e_op_email = Entry(frame,width=40,font=("calibri",20,"bold"),bg="white",fg="blue2",bd=5)
    e_op_email.place(relx=0.35,rely=0.25)

    l_op_mob = Label(frame,text="Mobile No:",font=("Arial",18,"bold"),bg="light blue",fg="blue2")
    l_op_mob.place(relx=0.2,rely=0.35)

    e_op_mob = Entry(frame,width=40,font=("calibri",20,"bold"),bg="white",fg="blue2",bd=5)
    e_op_mob.place(relx=0.35,rely=0.35)

    l_op_pas = Label(frame,text="Password:",font=("Arial",18,"bold"),bg="light blue",fg="blue2")
    l_op_pas.place(relx=0.2,rely=0.45)

    e_op_pas = Entry(frame,width=40,font=("calibri",20,"bold"),bg="white",fg="blue2",bd=5)
    e_op_pas.place(relx=0.35,rely=0.45)

    l_op_type = Label(frame,text="A/C Type:",font=("Arial",18,"bold"),bg="light blue",fg="blue2")
    l_op_type.place(relx=0.2,rely=0.55)

    e_op_type = Combobox(frame,width=20,font=("calibri",20,"bold"),values=['Savings','Current','Salary'])
    e_op_type.current(0)
    e_op_type.place(relx=0.35,rely=0.55)

    b_op_acn = Button(frame,text="Submit",width=20,font=("Calibri",16,"bold"),fg="light cyan",bg="dark slate gray",bd=2,command=submit_chk)
    b_op_acn.place(relx=0.3,rely=0.70)

    b_op_reset = Button(frame,text="Reset",width=20,font=("Calibri",16,"bold"),fg="light cyan",bg="dark slate gray",bd=2,command=op_reset)
    b_op_reset.place(relx=0.5,rely=0.70)

    b_op_back = Button(frame,text="Back",width=5,font=("Arial",16,"bold"),fg="light cyan",bg="dark slate gray",bd=2,command=op_back)
    b_op_back.place(relx=0.00,rely=0.0)

def homescreen():
    frame = Frame(win)
    frame.configure(bg="pale turquoise")
    frame.place(relx=0,rely=0.16,relwidth=1,relheight=0.85)
    gflag = True

    def title(t):
        t_frame = Frame(frame)
        t_frame.configure(bg="pale turquoise")
        t_frame.place(relx=0.25,rely=0.05,relheight=0.1,relwidth=0.5)

        upd_title = Label(t_frame,text=t,bg="pale turquoise",font=("Arial",22,"normal","underline"),fg="black")
        upd_title.place(relx=0.35,rely=0.4)

    def hs_logout():
        global gname,gacno
        gname=""
        gacno=""
        frame.destroy()
        mainscreen()

    def hs_back():
        if mainscreen.gflag == True:
            res = messagebox.askquestion(message="You pressed Back! Want to Logout?",title="Warning")
            if res == 'yes':
                frame.destroy()
                mainscreen()
            else:
                pass;
        else:
            profile()

    welcome = f"Welcome! {gname}"
    l_welcm = Label(frame,text=welcome,font=("Calibri",16,""),fg="black",bg="pale turquoise")
    l_welcm.place(relx=0.8,rely=0.01)

    def profile():
        
        mainscreen.gflag = True
        #   database extraction
        conobj = slite.connect(database="pkbankdb.sqlite3")
        cur = conobj.cursor()
        cur.execute("select * from pkacnholder where acno=? and name=?",(gacno,gname))
        data = cur.fetchone()
        conobj.close()

        p_frame = Frame(frame)
        p_frame.configure(bg="azure",bd=5)
        p_frame.place(relx=0.188,rely=0.15,relwidth=0.6,relheight=0.6)

        t = "Account Details"
        title(t)

        l_hs_acno = Label(p_frame,text="Account No.:",fg="black",bg="azure",font=("Arial",18,""))
        l_hs_acno.place(relx=0.25,rely=0.1)

        hs_acno = Label(p_frame,text=f"{gacno}",fg="blue",bg="azure",font=("Calibri",16,"italic"))
        hs_acno.place(relx=0.5,rely=0.1)

        l_hs_type = Label(p_frame,text="A/C Type:",fg="black",bg="azure",font=("Arial",18,""))
        l_hs_type.place(relx=0.25,rely=0.2)

        hs_type = Label(p_frame,text=data[1],fg="blue",bg="azure",font=("Calibri",16,"italic"))
        hs_type.place(relx=0.5,rely=0.2)

        l_hs_name = Label(p_frame,text="Name:",fg="black",bg="azure",font=("Arial",18,""))
        l_hs_name.place(relx=0.25,rely=0.3)

        hs_name = Label(p_frame,text=data[2],fg="blue",bg="azure",font=("Calibri",16,"italic"))
        hs_name.place(relx=0.5,rely=0.3)

        l_hs_email = Label(p_frame,text="Email ID:",fg="black",bg="azure",font=("Arial",18,""))
        l_hs_email.place(relx=0.25,rely=0.4)

        hs_acno = Label(p_frame,text=data[3],fg="blue",bg="azure",font=("Calibri",16,"italic"))
        hs_acno.place(relx=0.5,rely=0.4)

        l_hs_mob = Label(p_frame,text="Mobile No:",fg="black",bg="azure",font=("Arial",18,""))
        l_hs_mob.place(relx=0.25,rely=0.5)

        hs_mob = Label(p_frame,text=f"{data[4]}",fg="blue",bg="azure",font=("Calibri",16,"italic"))
        hs_mob.place(relx=0.5,rely=0.5)

        l_hs_pas = Label(p_frame,text="Password:",fg="black",bg="azure",font=("Arial",18,""))
        l_hs_pas.place(relx=0.25,rely=0.6)

        hs_pas = Label(p_frame,text=data[5],fg="blue",bg="azure",font=("Calibri",16,"italic"))
        hs_pas.place(relx=0.5,rely=0.6)

        l_hs_opdate = Label(p_frame,text="Opening Date:",fg="black",bg="azure",font=("Arial",18,""))
        l_hs_opdate.place(relx=0.25,rely=0.7)

        hs_opdate = Label(p_frame,text=data[7],fg="blue",bg="azure",font=("Calibri",16,"italic"))
        hs_opdate.place(relx=0.5,rely=0.7)

    profile()

    def updatedetail():
        print("This is update!")
        
        mainscreen.gflag = False
        upd_frame = Frame(frame)
        upd_frame.configure(bg="azure",bd=5)
        upd_frame.place(relx=0.188,rely=0.15,relwidth=0.6,relheight=0.6)

        t = "Update Account Details"
        title(t)

        def upd_submit():
            email = e_upd_email.get()
            mob = e_upd_mob.get()
            name = e_upd_name.get()
            pas = e_upd_pas.get()

            #   database updatation       
                                                                                              
            conobj = slite.connect(database="pkbankdb.sqlite3")
            cur = conobj.cursor()
            cur.execute("update pkacnholder set name=?, email=?, mob=?, pas=? where acno=?",(name,email,int(mob),pas,gacno))
            conobj.commit()
            conobj.close()
            messagebox.showinfo("Message","Account details Updated successfully!")
            global gname
            gname = name
            upd_frame.destroy()
            profile()

        l_upd_name = Label(upd_frame,text="Name",fg="black",bg="azure",font=("Arial",16,""))
        l_upd_name.place(relx=0.09,rely=0.12)

        e_upd_name = Entry(upd_frame,width=25,font=("calibri",18,""),fg="sea green",bd=1)
        e_upd_name.place(relx=0.095,rely=0.2)

        l_upd_email = Label(upd_frame,text="Email ID",fg="black",bg="azure",font=("Arial",16,""))
        l_upd_email.place(relx=0.55,rely=0.12)

        e_upd_email = Entry(upd_frame,width=25,font=("calibri",18,""),fg="sea green",bd=1)
        e_upd_email.place(relx=0.555,rely=0.2)

        l_upd_mob = Label(upd_frame,text="Mobile No.",fg="black",bg="azure",font=("Arial",16,""))
        l_upd_mob.place(relx=0.09,rely=0.48)

        e_upd_mob = Entry(upd_frame,width=25,font=("calibri",18,""),fg="sea green",bd=1)
        e_upd_mob.place(relx=0.095,rely=0.56)

        l_upd_pas = Label(upd_frame,text="Password",fg="black",bg="azure",font=("Arial",16,""))
        l_upd_pas.place(relx=0.55,rely=0.48)

        e_upd_pas = Entry(upd_frame,width=25,font=("calibri",18,""),fg="sea green",bd=1)
        e_upd_pas.place(relx=0.555,rely=0.56)

        b_upd_submit = Button(upd_frame,text="Submit",width =10,font=("calibri",16,"bold"),fg="blue",bg="light grey",bd=2,command=upd_submit)
        b_upd_submit.place(relx=0.4,rely=0.8)

        
        #   database extraction
        conobj = slite.connect(database="pkbankdb.sqlite3")
        cur = conobj.cursor()
        cur.execute("select name,mob,email,pas from pkacnholder where acno=? and name=?",(gacno,gname))
        data = cur.fetchone()
        conobj.close()

        e_upd_name.insert(0,data[0])
        e_upd_mob.insert(0,data[1])
        e_upd_email.insert(0,data[2])
        e_upd_pas.insert(0,data[3])


    def transfer():
        t = "Transfer Amount to Account "
        title(t)
        mainscreen.gflag = False
        print("Transfer Accessed!")
        tnsfr_frame = Frame(frame)
        tnsfr_frame.configure(bg="azure",bd=5)
        tnsfr_frame.place(relx=0.188,rely=0.15,relwidth=0.6,relheight=0.6)

        l_t_2acn = Label(tnsfr_frame,text="To Account:",fg="black",font=("Arial",18,""),bg="azure")
        l_t_2acn.place(relx=0.2,rely=0.2)

        e_t_2acn = Entry(tnsfr_frame,width=25,font=("calibri",18,""),bd=4,fg="sea green")
        e_t_2acn.place(relx=0.45,rely=0.2)
        
        l_t_2name = Label(tnsfr_frame,text="To Name:",fg="black",font=("Arial",18,""),bg="azure")
        l_t_2name.place(relx=0.2,rely=0.325)

        e_t_2name = Entry(tnsfr_frame,width=25,font=("calibri",18,""),bd=4,fg="sea green")
        e_t_2name.place(relx=0.45,rely=0.325)

        l_t_amt = Label(tnsfr_frame,text="Amount",fg="black",font=("Arial",18,""),bg="azure")
        l_t_amt.place(relx=0.2,rely=0.45)
        
        e_t_amt = Entry(tnsfr_frame,width=25,font=("calibri",18,""),bd=4,fg="sea green")
        e_t_amt.place(relx=0.45,rely=0.45)

        def t_submit():
            acn2 = e_t_2acn.get()
            name2 = e_t_2name.get()
            amt = e_t_amt.get()

            #   database updation
            conobj = slite.connect(database="pkbankdb.sqlite3")
            cur = conobj.cursor()
            cur.execute("select acno,name from pkacnholder where acno=? and name=?",(acn2,name2))
            data2 = cur.fetchone()
            conobj.close()

            if data2 == None:
                messagebox.showerror("Error",f"{acn2} doesnot exists under {name2}. Please enter correct credentials!")
            else:            
                #   database updation
                conobj = slite.connect(database="pkbankdb.sqlite3")
                cur = conobj.cursor()
                cur.execute("update pkacnholder set sal=sal-? where acno=? and name=?",(amt,gacno,gname))
                cur.execute("update pkacnholder set sal=sal+? where acno=? and name=?",(amt,acn2,name2))
                conobj.commit()
                conobj.close()
                messagebox.showinfo("Message",f"Transfer to {acn2} of Rs.{amt} completed successfully!")

                tnsfr_frame.destroy()
                profile()

        b_t_submit = Button(tnsfr_frame,text="Submit",width =10,font=("calibri",16,"bold"),fg="blue",bg="light grey",bd=2,command=t_submit)
        b_t_submit.place(relx=0.4,rely=0.75)

    def withdraw():
        mainscreen.gflag = False
        t = "Withdraw Amount"
        title(t)

        wdw_frame = Frame(frame)
        wdw_frame.configure(bg="azure")
        wdw_frame.place(relx=0.188,rely=0.15,relwidth=0.6,relheight=0.6)

        def wdw_submit():
            amt = e_wdw_amt.get()

            #   database extraction
            conobj = slite.connect(database="pkbankdb.sqlite3")
            cur = conobj.cursor()
            cur.execute("select sal from pkacnholder where acno=? and name=?",(gacno,gname))
            data = cur.fetchone()
            conobj.close()
                        
            if len(amt) == 0:
                messagebox.showwarning("Invalid! Enter Amount!")
            elif float(amt) > data[0]:
                messagebox.showinfo("Message","You don't sufficient amount to withdraw.")
            elif float(amt) <= data[0]:
                #   database updation
                conobj = slite.connect(database="pkbankdb.sqlite3")
                cur = conobj.cursor()
                cur.execute("update pkacnholder set sal=sal-? where acno=? and name=?",(float(amt),gacno,gname))
                conobj.commit()
                conobj.close()
                messagebox.showinfo("Message",f"Withdrawal of Rs.{amt} Successful!")
                wdw_frame.destroy()
                profile()

        l_wdw_amt = Label(wdw_frame,text="Amount:",font=("Arial",18,"normal"),fg="black",bg="azure")
        l_wdw_amt.place(relx=0.2,rely=0.2)

        e_wdw_amt = Entry(wdw_frame,width=25,font=("Calibri",18,""),fg="sea green",bd=4)
        e_wdw_amt.place(relx=0.45,rely=0.2)

        b_wdw_submit = Button(wdw_frame,text="Submit",font=("Calibri",16,"bold"),width=10,fg="blue",bg="light grey",bd=2,command=wdw_submit)
        b_wdw_submit.place(relx=0.4,rely=0.75)

    def chkbal():
        mainscreen.gflag = False
        t = "Balance Details"
        title(t)

        bal_frame = Frame(frame)
        bal_frame.configure(bg = "azure")
        bal_frame.place(relx=0.188,rely=0.15,relwidth=0.6,relheight=0.6)

        #   database extraction
        conobj = slite.connect(database="pkbankdb.sqlite3")
        cur = conobj.cursor()
        cur.execute("select type,sal from pkacnholder where acno=? and name=?",(gacno,gname))
        data = cur.fetchone()
        con.close()

        l_bal_acn = Label(bal_frame,text=f"A/C No.:\t{gacno}",font=("Calibri",16,"normal"),fg="black",bg="azure")
        l_bal_acn.place(relx=0.15,rely=0.25)
        
        l_bal_type = Label(bal_frame,text=f"A/C Type:\t{data[0]}",font=("Calibri",16,"normal"),fg="black",bg="azure")
        l_bal_type.place(relx=0.15,rely=0.4)
        
        l_bal_name = Label(bal_frame,text=f"Name:\t{gname}",font=("Calibri",16,"normal"),fg="black",bg="azure")
        l_bal_name.place(relx=0.15,rely=0.55)

        
        l_bal_h = Label(bal_frame,text="Balance",font=("Arial",18,"bold"),fg="black",bg="azure")
        l_bal_h.place(relx=0.65,rely=0.25)

        l_bal = Label(bal_frame,text=f"{data[1]}",font=("Arial",40,"bold"),fg="sea green",bg="azure")
        l_bal.place(relx=0.6,rely=0.35)


    def deposit():
        mainscreen.gflag = False
        t = "Deposit Amount"
        title(t)

        dep_frame = Frame(frame)
        dep_frame.configure(bg = "azure")
        dep_frame.place(relx=0.188,rely=0.15,relwidth=0.6,relheight=0.6)

        def dep_submit():
            amt = e_dep_amt.get()
            #   database updation
            if len(amt) == 0:
                messagebox.showerror(message="Invalid! Enter Amount (x500)")
            elif int(amt) < 500:
                messagebox.showwarning(message="Entered amount less than Rs.500.")
            else:
                conobj = slite.connect(database="pkbankdb.sqlite3")
                cur = conobj.cursor()
                cur.execute("update pkacnholder set sal=sal+? where acno=? and name=?",(float(amt),gacno,gname))
                conobj.commit()
                conobj.close()
                messagebox.showinfo("Message",f"Amount {amt} deposited successfully in A/C No. {gacno}. **Thank You**")
                dep_frame.destroy()
                profile()

        
        l_dep_amt = Label(dep_frame,text="Amount:",font=("Arial",18,"normal"),fg="black",bg="azure")
        l_dep_amt.place(relx=0.2,rely=0.2)

        e_dep_amt = Entry(dep_frame,width=25,font=("Calibri",18,""),fg="sea green",bd=4)
        e_dep_amt.place(relx=0.45,rely=0.2)

        b_wdw_submit = Button(dep_frame,text="Submit",font=("Calibri",16,"bold"),width=10,fg="blue",bg="light grey",bd=2,command=dep_submit)
        b_wdw_submit.place(relx=0.4,rely=0.75)

    
    b_hs_logout = Button(frame,text="Logout",width=6,font=("Arial",16,"bold"),fg="light cyan",bg="dark slate gray",bd=2,command=hs_logout)
    b_hs_logout.place(relx=0.935,rely=0.0)

    b_hs_back = Button(frame,text="Back",width=5,font=("Arial",16,"bold"),fg="light cyan",bg="dark slate gray",bd=2,command=hs_back)
    b_hs_back.place(relx=0.00,rely=0.0)


    hs_b_frame = Frame(frame)
    hs_b_frame.configure(bg="pale turquoise")
    hs_b_frame.place(relx=0.23,rely=0.84,relheight=0.15,relwidth=0.7)

    b_hs_update = Button(hs_b_frame,text="Update",width=10,font=("Calibri",16,"bold"),fg="blue2",bg="light grey",bd=2,command=updatedetail)
    b_hs_update.grid(row=0,column=0,padx=10)
    
    b_hs_dpst = Button(hs_b_frame,text="Deposit",width=10,font=("Calibri",16,"bold"),fg="blue2",bg="light grey",bd=2,command=deposit)
    b_hs_dpst.grid(row=0,column=1,padx=10)

    b_hs_wdw = Button(hs_b_frame,text="Withdraw",width=10,font=("Calibri",16,"bold"),fg="blue2",bg="light grey",bd=2,command=withdraw)
    b_hs_wdw.grid(row=0,column=2,padx=10)

    b_hs_tnsfr = Button(hs_b_frame,text="Transfer",width=10,font=("Calibri",16,"bold"),fg="blue2",bg="light grey",bd=2,command=transfer)
    b_hs_tnsfr.grid(row=0,column=3,padx=10)

    b_hs_ckbal = Button(hs_b_frame,text="Balance",width=10,font=("Calibri",16,"bold"),fg="blue2",bg="light grey",bd=2,command=chkbal)
    b_hs_ckbal.grid(row=0,column=4,padx=10)




mainscreen()
win.mainloop()