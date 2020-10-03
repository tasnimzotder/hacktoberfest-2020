from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
root=Tk()
root.title("DATABASE")
root.geometry("1350x750+0+0")
title=Label(root,text="STUDENT MANAGEMENT SYSTEM",font="TIMESNEWROMAN 15 bold",bg="white",fg="black",bd=2,relief="solid")
title.place(x=500,y=0)
frame1=Frame(root,bd=4,relief="ridge",width=550,height=600,bg="crimson")
frame1.place(x=20,y=40)
frame2=Frame(root,bd=4,relief="ridge",width=750,height=600,bg="crimson")
frame2.place(x=600,y=40)
title2=Label(root,text="MANAGE STUDENTS",font="TIMESNEWROMAN 12 bold",bg="white",fg="black",bd=2,relief="solid")
title2.place(x=220,y=50)
title2=Label(root,text="STUDENTS DETAILS",font="TIMESNEWROMAN 12 bold",bg="white",fg="black",bd=2,relief="solid")
title2.place(x=900,y=50)
label1=Label(root,text="NAME",font="TIMESNEWROMAN 10 bold",bg="crimson",fg="white")
label1.place(x=130,y=122)
def caps(event):
    NAME.set(NAME.get().upper())
NAME=StringVar()
entry1=Entry(root,textvariable=NAME,bd=3,relief="sunken",font="TIMESNEWROMAN 10 bold",width=30)
entry1.place(x=200,y=120)
entry1.bind("<KeyRelease>",caps)
label2=Label(root,text="ROLLNO",font="TIMESNEWROMAN 10 bold",bg="crimson",fg="white")
label2.place(x=130,y=182)
ROLLNO=StringVar()
#ROLLNO.set("")
entry2=Entry(root,textvariable=ROLLNO,bd=3,relief="sunken",font="TIMESNEWROMAN 10 bold",width=30)
entry2.place(x=200,y=182)
label3=Label(root,text="CLASS",font="TIMESNEWROMAN 10 bold",bg="crimson",fg="white")
label3.place(x=130,y=242)
CLASS=StringVar()
#CLASS.set("")
entry3=Entry(root,textvariable=CLASS,bd=3,relief="sunken",font="TIMESNEWROMAN 10 bold",width=30)
entry3.place(x=200,y=242)
label4=Label(root,text="SECTION",font="TIMESNEWROMAN 10 bold",bg="crimson",fg="white")
label4.place(x=120,y=302)
def caps(event):
    SECTION.set(SECTION.get().upper())
SECTION=StringVar()
entry4=Entry(root,textvariable=SECTION,bd=3,relief="sunken",font="TIMESNEWROMAN 10 bold",width=30)
entry4.place(x=200,y=302)
entry4.bind("<KeyRelease>",caps)
label5=Label(root,text="SEX",font="TIMESNEWROMAN 10 bold",bg="crimson",fg="white")
label5.place(x=120,y=360)
combo=ttk.Combobox(root,font="TIMESNEWROMAN 10 bold",width=28)
combo['values']=("MALE","FEMALE","OTHER")
combo.place(x=200,y=360)
combo.set("Select")
label6=Label(root,text="EMAIL_ID",font="TIMESNEWROMAN 10 bold",bg="crimson",fg="white")
label6.place(x=120,y=412)
def caps(event):
    EMAIL_ID.set(EMAIL_ID.get().lower())
EMAIL_ID=StringVar()
entry6=Entry(root,textvariable=EMAIL_ID,bd=3,relief="sunken",font="TIMESNEWROMAN 10 bold",width=35)
entry6.place(x=200,y=412)
entry6.bind("<KeyRelease>",caps)
label7=Label(frame2,text="SearchBy",font="TIMESNEWROMAN 10 bold",bg="crimson",fg="white")
label7.place(x=50,y=40)
global SearchBy,SearchTxt
SearchBy=StringVar()
comb=ttk.Combobox(frame2,textvariable=SearchBy,font="TIMESNEWROMAN 10 bold",width=20)
comb['values']=("ROLL_NO","CLASS","SEX")
comb.place(x=120,y=40)
comb.set("Select")
SearchTxt=StringVar()
txt=Entry(frame2,textvariable=SearchTxt,font="TIMESNEWROMAN 10 bold",width=20)
txt.place(x=320,y=40)
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<FUNCTIONS START FOR BUTTONS>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

global fetch_data,clear_data,get_cursor,update_data,delete_data,search_data
def add_students():
    if ROLLNO.get()=="" or NAME.get()=="" or CLASS.get()=="":
        messagebox.showerror("ERROR","ALL FIELDS ARE REQUIRED")
    else:
        conn=sqlite3.Connection("School.db")
        cur=conn.cursor()
        cur.execute("INSERT INTO STUDENTS VALUES(?,?,?,?,?,?)",(NAME.get(),ROLLNO.get(),CLASS.get(),SECTION.get(),combo.get(),EMAIL_ID.get()))
        conn.commit()
        fetch_data()
        clear_data()
        conn.close()
        messagebox.showinfo("SUCCESS","RECORDS HAVE BEEN INSERTED") 
global fetch    
def fetch_data():
    conn=sqlite3.Connection("School.db")
    cur=conn.cursor()
    cur.execute("select * from STUDENTS")
    rows=cur.fetchall()
    if len(rows)!=0:
        Student_table.delete(*Student_table.get_children())
        for row in rows:
            Student_table.insert('',END,values=row)
        conn.commit()   
    conn.close()    
def clear_data():
    NAME.set("")
    ROLLNO.set("")
    CLASS.set("")
    SECTION.set("")
    combo.set("")
    EMAIL_ID.set("")
    SearchBy.set("")
    SearchTxt.set("")
def get_cursor(ev):
    cursor_row=Student_table.focus()
    course=Student_table.item(cursor_row)
    row=course['values']
    NAME.set(row[0])
    ROLLNO.set(row[1])
    CLASS.set(row[2])
    SECTION.set(row[3])
    combo.set(row[4])
    EMAIL_ID.set(row[5])
def update_data():
    if  NAME.get()=="" or CLASS.get()=="":
        messagebox.showerror("ERROR","ALL FIELDS ARE REQUIRED")
    else:
        conn=sqlite3.Connection("School.db")
        cur=conn.cursor()
        cur.execute("update STUDENTS SET NAME=?,CLASS=?,SECTION=?,SEX=?,EMAIL_ID=? WHERE ROLL_NO=?",(NAME.get(),CLASS.get(),SECTION.get(),combo.get(),EMAIL_ID.get(),ROLLNO.get()))
        conn.commit()
        fetch_data()
        clear_data()
        conn.close() 
        messagebox.showinfo("SUCCESS","RECORDS HAVE BEEN UPDATED")            
def delete_data():
    if  ROLLNO.get()=="":
        messagebox.showerror("ERROR","ALL FIELDS ARE REQUIRED")
    else:
        msg=messagebox.askyesno('Delete','DELETE RECORD?')
    if msg>0:
        conn=sqlite3.Connection("School.db")
        cur=conn.cursor()
        cur.execute("delete from students where ROLL_NO=?",(ROLLNO.get(),))
        conn.commit()
        conn.close()
        fetch_data()
        clear_data()
def search_data():
    if SearchBy.get()=="Select":
        messagebox.showerror("ERROR","PLEASE ENTER THE TYPE FOR SEARCH")
        SearchBy.set("Select")
        SearchTxt.set("") 
    elif SearchTxt.get()=="": 
        messagebox.showerror("ERROR","PLEASE ENTER THE DATA FOR SEARCH")
        SearchBy.set("Select")
        SearchTxt.set("") 
    if True:
        conn=sqlite3.Connection("School.db")
        cur=conn.cursor()
        cur.execute("SELECT * from STUDENTS WHERE "+(SearchBy.get())+" LIKE '%"+(SearchTxt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            Student_table.delete(*Student_table.get_children())
            for row in rows:
                Student_table.insert('',END,values=row)
        SearchBy.set("")
        SearchTxt.set("")       
        conn.commit()
        conn.close()
button=Button(root,text="ADD",bg="white",fg="black",font="TIMESNEWROMAN 10 bold",bd=4,relief="sunken",command=add_students,padx=20,pady=5)
button.place(x=50,y=590)
button=Button(root,text="UPDATE",bg="white",fg="black",font="TIMESNEWROMAN 10 bold",bd=4,relief="sunken",command=update_data,padx=20,pady=5)
button.place(x=160,y=590)
button=Button(root,text="DELETE",bg="white",fg="black",font="TIMESNEWROMAN 10 bold",bd=4,relief="sunken",command=delete_data,padx=20,pady=5)
button.place(x=290,y=590)
button=Button(root,text="CLEAR",bg="white",fg="black",font="TIMESNEWROMAN 10 bold",bd=4,relief="sunken",command=clear_data,padx=20,pady=5)
button.place(x=420,y=590)
but=Button(frame2,text="SEARCH",bg="white",fg="black",width=10,command=search_data)
but.place(x=480,y=35)



con=sqlite3.Connection("School.db")
cur=con.cursor()
cur.execute("""
CREATE TABLE STUDENTS
(
    NAME TEXT,
    ROLL_NO VARCHAR PRIMARY KEY,
    CLASS INT,
    SECTION TEXT,
    SEX TEXT,
    EMAIL_ID TEXT
)""")
con.commit()
con.close()
frame3=Frame(frame2,bd=4,relief="ridge",bg="white")
frame3.place(x=0,y=70,width=720,height=500)
scroll_x=Scrollbar(frame3,orient=HORIZONTAL)
scroll_y=Scrollbar(frame3,orient=VERTICAL)
Student_table=ttk.Treeview(frame3,columns=("NAME","RollNO","CLASS","SECTION","SEX","EMAIL_ID"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=Student_table.xview)
scroll_y.config(command=Student_table.yview)
Student_table.heading("NAME",text="NAME")
Student_table.heading("RollNO",text="ROLL_NO")
Student_table.heading("CLASS",text="CLASS")
Student_table.heading("SECTION",text="SECTION")
Student_table.heading("SEX",text="SEX")
Student_table.heading("EMAIL_ID",text="EMAIL_ID")
Student_table['show']='headings'
Student_table.column("NAME",width=150)
Student_table.column("RollNO",width=150)
Student_table.column("CLASS",width=150)
Student_table.column("SECTION",width=150)
Student_table.column("SEX",width=150)
Student_table.column("EMAIL_ID",width=150)
Student_table.pack(fill=BOTH,expand=1)
Student_table.bind("<ButtonRelease-1>",get_cursor)
fetch_data()   
BU=Button(frame2,text="SHOWALL",bg="white",fg="black",width=10,command=fetch_data)
BU.place(x=590,y=35)
root.mainloop()


