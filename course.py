from tkinter import* #in tkinter there are many widgets, to use that widgets ny their names directly we have use library tkinter
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk,messagebox
import sqlite3 

class CourseClass:     #class helps us to define structured way
  def __init__(self,root):
    #pass # to live body  blank(by removing pass we will write code here)
    #for title in fault constructor
    self.root=root #root reinitialised
    self.root.title("Students Result Management System")#with the help of self.root we will access all the features
    self.root.geometry("1200x480+80+170")#for define width we will use geometry function (width is 1200, height is 480, placed where we want to prinnt title margin from top and left)
    self.root.config(bg="white")#for background color
    self.root.focus_force()
    
    #---title---
    title=Label(self.root,text="Manage Course Details",font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=10,y=15,width=1180,height=35)
    
    #----variables---
    self.var_course=StringVar()
    self.var_duration=StringVar()
    self.var_charges=StringVar()
    
    #-----widgets----
    lbl_courseName=Label(self.root,text="Course Name",font=("goudy old style",15,'bold'),bg="grey",fg="white").place(x=10,y=60) #add 40 to y-axis
    
    lbl_duration=Label(self.root,text="Duration",font=("goudy old style",15,'bold'),bg="grey",fg="white").place(x=10,y=100)
    
    lbl_charges=Label(self.root,text="Charges",font=("goudy old style",15,'bold'),bg="grey",fg="white").place(x=10,y=140)
    
    lbl_Description=Label(self.root,text="Description",font=("goudy old style",15,'bold'),bg="grey",fg="white").place(x=10,y=180)
    
    
    #for define variables, whatever data we write here that will be stored in variables section
    
    #---Entry Fields---
    self.txt_courseName=Entry(self.root,textvariable=self.var_course,font=("goudy old style",15,'bold'),bg="lightBlue",fg="black")
    self.txt_courseName.place(x=150,y=60,width=200) #add 40 to y-axis
    
    
    txt_duration=Entry(self.root,textvariable=self.var_duration,font=("goudy old style",15,'bold'),bg="lightBlue",fg="black").place(x=150,y=100,width=200)
    
    txt_charges=Entry(self.root,textvariable=self.var_charges,font=("goudy old style",15,'bold'),bg="lightBlue",fg="black").place(x=150,y=140,width=200)
    
    self.txt_description=Text(self.root,font=("goudy old style",15,'bold'),bg="lightBlue",fg="black")
    self.txt_description.place(x=150,y=180,width=500,height=130) #we have take Text here cause we have to write long messages using enter also ,it is accessible using Text
    
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
    lbl_search_courseName=Label(self.root,text="Course Name",font=("goudy old style",15,'bold'),bg="white",fg="black").place(x=690,y=60,width=200) 
    
    txt_search_courseName=Entry(self.root,textvariable=self.var_search,font=("goudy old style",15,'bold'),bg="lightBlue",fg="black").place(x=870,y=60,width=180) #add 40 to y-axis
    
    btn_search=Button(self.root,text='Search',font=("goudy old style",15,"bold"),bg="blue",fg="white",cursor="hand2",command=self.search).place(x=1070,y=60,width=120,height=28)
    
    #----Content----
    self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
    self.C_Frame.place(x=720,y=100,width=470,height=340)
    
    scrollx = Scrollbar(self.C_Frame,orient=VERTICAL)
    scrolly = Scrollbar(self.C_Frame,orient=HORIZONTAL)
    
    
    #for displaing details in table form
    self.CourseTable=ttk.Treeview(self.C_Frame,columns=("cid","name","duration","charges","description"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
    
    scrollx.pack(side=BOTTOM,fill=X)
    scrolly.pack(side=RIGHT,fill=Y)
    scrollx.config(command=self.CourseTable.xview)
    scrolly.config(command=self.CourseTable.yview)
    
    self.CourseTable.heading("cid",text="course ID")
    self.CourseTable.heading("name",text="course Name")
    self.CourseTable.heading("duration",text="course Duration")
    self.CourseTable.heading("charges",text="course Charges")
    self.CourseTable.heading("description",text="course Description")
    
    self.CourseTable["show"]='headings'
    
    self.CourseTable.column("cid",width=50)
    self.CourseTable.column("name",width=100)
    self.CourseTable.column("duration",width=100)
    self.CourseTable.column("charges",width=100)
    self.CourseTable.column("description",width=150)
    
    self.CourseTable.pack(fill=BOTH,expand=1)
    self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
    self.show()
#----------------------------------------------------------
  #all buttons features
  def clear(self):
    self.show()
    self.var_course.set("")
    self.var_duration.set("")
    self.var_charges.set("")
    self.var_search.set("")
    self.txt_description.delete('1.0',END)
    self.txt_courseName.config(state=NORMAL)
  
  def delete(self):
    con=sqlite3.connect(database="rms.db")
    cur=con.cursor()
    try:
      if self.var_course.get()=="":
        messagebox.showerror("Error","Course name should be required",parent=self.root)
      else:
        cur.execute("select * from course where name=?",(self.var_course.get(),))
        row=cur.fetchone()
        if row==None:
          messagebox.showerror("Error","please select course from the list first",parent=self.root)
        else:
          op=messagebox.askyesno("confirm","Do you really want to delete?",parent=self.root)
          if op==True:
            cur.execute("delete from course where name =?",(self.var_course.get(),))
            con.commit()
            messagebox.showinfo("delete","course deleted succesfully",parent=self.root)
            self.clear()
      
    except Exception as ex:
      messagebox.showerror("Error",f"Error due to {str(ex)}") 
    
  def get_data(self,ev):
    self.txt_courseName.config(state='readonly')
    self.txt_courseName
    r=self.CourseTable.focus()
    content=self.CourseTable.item(r)
    row=content["values"]
    #print(row)
    self.var_course.set(row[1])
    self.var_duration.set(row[2])
    self.var_charges.set(row[3])
    #self.var_course.set(row[4])
    self.txt_description.delete('1.0',END)
    self.txt_description
    
  def add(self):
    con=sqlite3.connect(database="rms.db")
    cur=con.cursor()
    try:
      if self.var_course.get()=="":
        messagebox.showerror("Error","Course name should be required",parent=self.root)
      else:
        cur.execute("select * from course where name=?",(self.var_course.get(),))
        row=cur.fetchone()
        if row!=None:
          messagebox.showerror("Error","course Name already present",parent=self.root)
        else:
          cur.execute("insert into course (name,duration,charges,description)values(?,?,?,?)",(
            self.var_course.get(),
            self.var_duration.get(),
            self.var_charges.get(),
            self.txt_description.get("1.0",END)
          ))
          con.commit()
          messagebox.showinfo("success","course Added successfully",parent=self.root)
          self.show()
        
    except Exception as ex:
      messagebox.showerror("Error",f"Error due to {str(ex)}") 
      
  def update(self):
    con=sqlite3.connect(database="rms.db")
    cur=con.cursor()
    try:
      if self.var_course.get()=="":
        messagebox.showerror("Error","Course name should be required",parent=self.root)
      else:
        cur.execute("select * from course where name=?",(self.var_course.get(),))
        row=cur.fetchone()
        if row==None:
          messagebox.showerror("Error","select course from list",parent=self.root)
        else:
          cur.execute("update  course duration=?,charges=?,description=? where name=?",(
            
            
            self.var_duration.get(),
            self.var_charges.get(),
            self.txt_description.get("1.0",END),
            self.var_course.get(),
          ))
          con.commit()
          messagebox.showinfo("success","course update successfully",parent=self.root)
          self.show()
        
    except Exception as ex:
      messagebox.showerror("Error",f"Error due to {str(ex)}") 
    
  def show(self):
    con=sqlite3.connect(database="rms.db")
    cur=con.cursor()
    try:
        cur.execute("select * from course")
        rows=cur.fetchall()
        self.CourseTable.delete(*self.CourseTable.get_children())
        for row in rows:
          self.CourseTable.insert('',END, values=row)
    except Exception as ex:
      messagebox.showerror("Error",f"Error due to {str(ex)}") 
      
      
  def search(self):
    con=sqlite3.connect(database="rms.db")
    cur=con.cursor()
    try:
        cur.execute(f"select * from course where name LIKE '%{self.var_search.get()}%'")
        rows=cur.fetchall()
        self.CourseTable.delete(*self.CourseTable.get_children())
        for row in rows:
          self.CourseTable.insert('',END, values=row)
    except Exception as ex:
      messagebox.showerror("Error",f"Error due to {str(ex)}") 
      
      
if __name__=="__main__":   #we are dealing with multipe files we have used this method
  root=Tk()#tkinter class ka object
  obj=CourseClass(root)
  root.mainloop()