from tkinter import* #in tkinter there are many widgets, to use that widgets ny their names directly we have use library tkinter
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk,messagebox
import sqlite3 

class studentClass:     #class helps us to define structured way
  def __init__(self,root):
    #pass # to live body  blank(by removing pass we will write code here)
    #for title in fault constructor
    self.root=root #root reinitialised
    self.root.title("Students Result Management System")#with the help of self.root we will access all the features
    self.root.geometry("1200x480+80+170")#for define width we will use geometry function (width is 1200, height is 480, placed where we want to prinnt title margin from top and left)
    self.root.config(bg="white")#for background color
    self.root.focus_force()
    
    #---title---
    title=Label(self.root,text="Manage Student Details",font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=10,y=15,width=1180,height=35)
    
    #----variables---
    self.var_roll=StringVar()
    self.var_name=StringVar()
    self.var_email=StringVar()
    self.var_gender=StringVar()
    self.var_dob=StringVar()
    self.var_contact=StringVar()
    self.var_course=StringVar()
    self.var_a_date=StringVar()
    self.var_state=StringVar()
    self.var_city=StringVar()
    self.var_pin=StringVar()
    
    
    #-----widgets----
    #-----column 1--------------
    lbl_roll=Label(self.root,text="Roll No.",font=("goudy old style",15,'bold'),bg="grey",fg="white").place(x=10,y=60) #add 40 to y-axis
    
    lbl_Name=Label(self.root,text="Name",font=("goudy old style",15,'bold'),bg="grey",fg="white").place(x=10,y=100)
    
    lbl_Email=Label(self.root,text="Email",font=("goudy old style",15,'bold'),bg="grey",fg="white").place(x=10,y=140)
    
    lbl_gender=Label(self.root,text="Gender",font=("goudy old style",15,'bold'),bg="grey",fg="white").place(x=10,y=180)
    
    lbl_state=Label(self.root,text="state",font=("goudy old style",15,'bold'),bg="grey",fg="white").place(x=10,y=220)
    
    txt_state=Entry(self.root,textvariable=self.var_state,font=("goudy old style",15,'bold'),bg="lightBlue",fg="black").place(x=150,y=220,width=150) 
    
    
    lbl_city=Label(self.root,text="city",font=("goudy old style",15,'bold'),bg="grey",fg="white").place(x=310,y=220)
    
    txt_city=Entry(self.root,textvariable=self.var_city,font=("goudy old style",15,'bold'),bg="lightBlue",fg="black").place(x=380,y=220,width=100) 
    
    
    lbl_pin=Label(self.root,text="pin",font=("goudy old style",15,'bold'),bg="grey",fg="white").place(x=500,y=220)
    
    txt_pin=Entry(self.root,textvariable=self.var_pin,font=("goudy old style",15,'bold'),bg="lightBlue",fg="black").place(x=560,y=220,width=120) 
    
    lbl_address=Label(self.root,text="Address",font=("goudy old style",15,'bold'),bg="grey",fg="white").place(x=10,y=260)
    
    
    #for define variables, whatever data we write here that will be stored in variables section
    
    #---Entry Fields---
    self.txt_roll=Entry(self.root,textvariable=self.var_roll,font=("goudy old style",15,'bold'),bg="lightBlue",fg="black")
    self.txt_roll.place(x=150,y=60,width=200) #add 40 to y-axis
    
    
    txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15,'bold'),bg="lightBlue",fg="black").place(x=150,y=100,width=200)
    
    txt_email=Entry(self.root,textvariable=self.var_email,font=("goudy old style",15,'bold'),bg="lightBlue",fg="black").place(x=150,y=140,width=200)
    
    #with the help of ttk we will make combo box
    self.txt_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female","other"),font=("goudy old style",15,'bold'),state='readonly',justify=CENTER)
    
    self.txt_gender.place(x=150,y=180,width=200)
    self.txt_gender.current(0)
    
    
    
    #--------column 2 -------
    
    lbl_dob=Label(self.root,text="D.O.B",font=("goudy old style",15,'bold'),bg="grey",fg="white").place(x=360,y=60) #add 40 to y-axis
    
    lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15,'bold'),bg="grey",fg="white").place(x=360,y=100)
    
    lbl_address=Label(self.root,text="Admission",font=("goudy old style",15,'bold'),bg="grey",fg="white").place(x=360,y=140)
    
    lbl_course=Label(self.root,text="Course",font=("goudy old style",15,'bold'),bg="grey",fg="white").place(x=360,y=180)
    
    #---Entry Fields 2---
    
    self.course_list=[]
    #function_call to update the list
    self.fetch_course()
    txt_dob=Entry(self.root,textvariable=self.var_dob,font=("goudy old style",15,'bold'),bg="lightBlue",fg="black").place(x=460,y=60,width=200) #add 40 to y-axis
    
    
    txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15,'bold'),bg="lightBlue",fg="black").place(x=460,y=100,width=200)
    
    txt_admission=Entry(self.root,textvariable=self.var_a_date,font=("goudy old style",15,'bold'),bg="lightBlue",fg="black").place(x=460,y=140,width=200)
    
    #with the help of ttk we will make combo box
    self.txt_course=ttk.Combobox(self.root,textvariable=self.var_course,values=self.course_list,font=("goudy old style",15,'bold'),state='readonly',justify=CENTER)
    
    self.txt_course.place(x=460,y=180,width=200)
    self.txt_course.set("Select")
    
    
    #-------Text Address----------
    
    self.txt_address=Text(self.root,font=("goudy old style",15,'bold'),bg="lightBlue",fg="black")
    
    self.txt_address.place(x=150,y=260,width=540,height=100) #we have take Text here cause we have to write long messages using enter also ,it is accessible using Text
    
    #----Buttons---
    self.btn_add=Button(self.root,text='Add',font=("goudy old style",15,"bold"),bg="blue",fg="white",cursor="hand2",command=self.add)
    self.btn_add.place(x=150,y=400,width=110,height=40)
    
    self.btn_update=Button(self.root,text='Update',font=("goudy old style",15,"bold"),bg="orange",fg="white",cursor="hand2",command=self.update)
    self.btn_update.place(x=270,y=400,width=110,height=40)
    
    self.btn_delete=Button(self.root,text='Delete',font=("goudy old style",15,"bold"),bg="green",fg="white",cursor="hand2",command=self.delete)
    self.btn_delete.place(x=390,y=400,width=110,height=40)
    
    self.btn_clear=Button(self.root,text='Clear',font=("goudy old style",15,"bold"),bg="purple",fg="white",cursor="hand2",command=self.clear)
    self.btn_clear.place(x=510,y=400,width=110,height=40)
    
    #---search panel------
    
    self.var_search=StringVar()
  
    lbl_search_roll=Label(self.root,text="Roll No.",font=("goudy old style",15,'bold'),bg="white",fg="black").place(x=690,y=60,width=200) 
    
    txt_search_roll=Entry(self.root,textvariable=self.var_search,font=("goudy old style",15,'bold'),bg="lightBlue",fg="black").place(x=870,y=60,width=180) #add 40 to y-axis
    
    btn_search=Button(self.root,text='Search',font=("goudy old style",15,"bold"),bg="blue",fg="white",cursor="hand2",command=self.search).place(x=1070,y=60,width=120,height=28)
    
    #----Content----
    self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
    self.C_Frame.place(x=720,y=100,width=470,height=340)
    
    scrollx = Scrollbar(self.C_Frame,orient=VERTICAL)
    scrolly = Scrollbar(self.C_Frame,orient=HORIZONTAL)
    
    
    #for displaing details in table form
    self.CourseTable=ttk.Treeview(self.C_Frame,columns=("roll","name","email","gender","dob","contact","admission","course","state","city","pin","address"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
    
    scrollx.pack(side=BOTTOM,fill=X)
    scrolly.pack(side=RIGHT,fill=Y)
    scrollx.config(command=self.CourseTable.xview)
    scrolly.config(command=self.CourseTable.yview)
    
    self.CourseTable.heading("roll",text="Roll No.")
    self.CourseTable.heading("name",text="Name")
    self.CourseTable.heading("email",text="Email")
    self.CourseTable.heading("gender",text="Gender")
    self.CourseTable.heading("dob",text="D.O.B")
    self.CourseTable.heading("contact",text="Contact")
    self.CourseTable.heading("admission",text="Admission")
    self.CourseTable.heading("course",text="Course")
    self.CourseTable.heading("state",text="State")
    self.CourseTable.heading("city",text="City")
    self.CourseTable.heading("pin",text="Pin")
    self.CourseTable.heading("address",text="Address")
    
    self.CourseTable["show"]='headings'
    
    self.CourseTable.column("roll",width=100)
    self.CourseTable.column("name",width=100)
    self.CourseTable.column("email",width=100)
    self.CourseTable.column("gender",width=100)
    self.CourseTable.column("dob",width=100)
    self.CourseTable.column("contact",width=100)
    self.CourseTable.column("admission",width=100)
    self.CourseTable.column("course",width=100)
    self.CourseTable.column("state",width=100)
    self.CourseTable.column("city",width=100)
    self.CourseTable.column("pin",width=100)
    self.CourseTable.column("address",width=200)
    
    
    self.CourseTable.pack(fill=BOTH,expand=1)
    self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
    self.show()
    
#----------------------------------------------------------
  #all buttons features
  def clear(self):
    self.show()
    self.var_roll.set("")
    self.var_roll.set(""),
    self.var_name.set(""),
    self.var_email.set(""),
    self.var_gender.set(""),
    self.var_dob.set(""),
    self.var_contact.set(""),
    self.var_a_date.set(""),
    self.var_course.set(""),
    self.var_state.set(""),
    self.var_city.set(""),
    self.var_pin.set(""),
            
    self.txt_address.delete("1.0",END)
    self.txt_roll.config(state=NORMAL)
    self.var_search.set("")
    
  
  def delete(self):
    con=sqlite3.connect(database="rms.db")
    cur=con.cursor()
    try:
      if self.var_roll.get()=="":
        messagebox.showerror("Error","Roll No. should be required",parent=self.root)
      else:
        cur.execute("select * from student where roll=?",(self.var_roll.get(),))
        row=cur.fetchone()
        if row==None:
          messagebox.showerror("Error","please select student from the list first",parent=self.root)
        else:
          op=messagebox.askyesno("confirm","Do you really want to delete?",parent=self.root)
          if op==True:
            cur.execute("delete from student where roll =?",(self.var_roll.get(),))
            con.commit()
            messagebox.showinfo("delete","student deleted succesfully",parent=self.root)
            self.clear()
      
    except Exception as ex:
      messagebox.showerror("Error",f"Error due to {str(ex)}") 
    
  def get_data(self,ev):
    self.txt_roll.config(state='readonly')
    self.txt_roll
    r=self.CourseTable.focus()
    content=self.CourseTable.item(r)
    row=content["values"]
    self.var_roll.set(row[0]),
    self.var_name.set(row[1]),
    self.var_email.set(row[2]),
    self.var_gender.set(row[3]),
    self.var_dob.set(row[4]),
    self.var_contact.set(row[5]),
    self.var_a_date.set(row[6]),
    self.var_course.set(row[7]),
    self.var_state.set(row[8]),
    self.var_city.set(row[9]),
    self.var_pin.set(row[10]),
            
    self.txt_address.delete("1.0",END)
    self.txt_address.insert(END,row[11])   
    
    
    
  def add(self):
    con=sqlite3.connect(database="rms.db")
    cur=con.cursor()
    try:
      if self.var_roll.get()=="":
        messagebox.showerror("Error","Roll No. should be required",parent=self.root)
      else:
        cur.execute("select * from student where roll=?",(self.var_roll.get(),))
        row=cur.fetchone()
        if row!=None:
          messagebox.showerror("Error","Roll No. is already present",parent=self.root)
        else:
          cur.execute("insert into student (roll,name,email,gender,dob,contact,admission,course,state,city,pin,address) values(?,?,?,?,?,?,?,?,?,?,?,?)",(
            self.var_roll.get(),
            self.var_name.get(),
            self.var_email.get(),
            self.var_gender.get(),
            self.var_dob.get(),
            self.var_contact.get(),
            self.var_a_date.get(),
            self.var_course.get(),
            self.var_state.get(),
            self.var_city.get(),
            self.var_pin.get(),
            
            self.txt_address.get("1.0",END)
          ))
          con.commit()
          messagebox.showinfo("success","student Added successfully",parent=self.root)
          self.show()
        
    except Exception as ex:
      messagebox.showerror("Error",f"Error due to {str(ex)}") 
      
  def update(self):
    con=sqlite3.connect(database="rms.db")
    cur=con.cursor()
    try:
      if self.var_roll.get()=="":
        messagebox.showerror("Error","Roll No. should be required",parent=self.root)
      else:
        cur.execute("select * from student where roll=?",(self.var_roll.get(),))
        row=cur.fetchone()
        if row==None:
          messagebox.showerror("Error","select student from list",parent=self.root)
        else:
          cur.execute("update student set name=?,email=?,gender=?,dob=?,contact=?,admission=?,course=?,state=?,city=?,pin=?,address=? where roll=?",(
            self.var_roll.get(),
            self.var_name.get(),
            self.var_email.get(),
            self.var_gender.get("select"),
            self.var_dob.get(),
            self.var_contact.get(),
            self.var_a_date.get(),
            self.var_course.get("select"),
            self.var_state.get(),
            self.var_city.get(),
            self.var_pin.get(),
            self.txt_address.get("1.0",END),self.var_roll.get(),
          ))
          con.commit()
          messagebox.showinfo("success","student update successfully",parent=self.root)
          self.show()
        
    except Exception as ex:
      messagebox.showerror("Error",f"Error due to {str(ex)}") 
    
  def show(self):
    con=sqlite3.connect(database="rms.db")
    cur=con.cursor()
    try:
        cur.execute("select * from student")
        rows=cur.fetchall()
        self.CourseTable.delete(*self.CourseTable.get_children())
        for row in rows:
          self.CourseTable.insert('',END, values=row)
    except Exception as ex:
      messagebox.showerror("Error",f"Error due to {str(ex)}") 
  
  def fetch_course(self):
    con=sqlite3.connect(database="rms.db")
    cur=con.cursor()
    try:
        cur.execute("select name from course")
        rows=cur.fetchall()
        if len(rows)>0:
          for row in rows:
            self.course_list.append(row[0])
    except Exception as ex:
      messagebox.showerror("Error",f"Error due to {str(ex)}") 
      
      
  
      
  def search(self):
    con=sqlite3.connect(database="rms.db")
    cur=con.cursor()
    try:
        cur.execute("select * from student where roll=?",(self.var_search.get(),))
        row=cur.fetchone()
        if row!=None:
          self.CourseTable.delete(*self.CourseTable.get_children())
          self.CourseTable.insert('',END, values=row)
        else:
          messagebox.showerror("Error","No record found",parent=self.root)
          
    except Exception as ex:
      messagebox.showerror("Error",f"Error due to {str(ex)}") 
      
      
if __name__=="__main__":   #we are dealing with multipe files we have used this method
  root=Tk()#tkinter class ka object
  obj=studentClass(root)
  root.mainloop()