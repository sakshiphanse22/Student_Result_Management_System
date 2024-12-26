#making GUI in python
#we will use 1 intermodule for GUI which is pre inbuilt libraray in that there are different classes like label,combobox,antifields are widgets.
#work on course
# work on buttons in course file, for that we will make one db file and will import new library in it.
#work on student file 
#work on result files
#work on view students results files

#command=self.add_course

from tkinter import* #in tkinter there are many widgets, to use that widgets ny their names directly we have use library tkinter
from PIL import Image,ImageTk #pip install pillow
from course import CourseClass #want to import courseclass to access this in add course
from student import studentClass
from result import resultClass
from report import reportClass
#want to import studentclass to access this in add student
from tkinter import messagebox
import os

from tkinter import*
from PIL import Image,ImageTk,ImageDraw #pip install pilllow
from datetime import*
import time
from math import*
import sqlite3
import os
from tkinter import messagebox

class RMS:     #class helps us to define structured way

  def __init__(self,root):
    #pass # to live body  blank(by removing pass we will write code here)
    #for title in fault constructor
    self.root=root #root reinitialised
    self.root.title("Students Result Management System")#with the help of self.root we will access all the features
    self.root.geometry("1350x700+0+0")#for define width we will use geometry function (width is 1350, heigght is 700, placed where we want to prinnt title margin from top and left)
    # self.root.config(bg="white")#for background color
    
    #----icons--(import library,install library in cmd using pip install --user Pillow)
    self.logo_dash=ImageTk.PhotoImage(file="allimages/IMAGE1.jpg")

    #---title---
    title=Label(self.root,text="Students Result Management System",padx=10,compound=LEFT,image=self.logo_dash,font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=1,y=1,relwidth=1,height=75)#title is object for the class label(in bracket all are widgets,compounf is for there place at left, pad is for gap betn name and logo)
    
    M_Frame=LabelFrame(self.root,text="Menu",font=("times new roman",15),bg="white")#for menu
    M_Frame.place(x=8,y=70,width=1260,height=80)#define m frame with .place`
    
    btn_course=Button(M_Frame,text="course",font=("goudy old style",15,"bold"),bg="black",fg="white",cursor="hand2",command=self.add_course).place(x=15,y=5,width=130,height=40)
    # button style,place for where we want to place that button,but for cursor we have used cursor=hand2, add 220 to 20
    
    btn_student=Button(M_Frame,text="student",font=("goudy old style",15,"bold"),bg="black",fg="white",cursor="hand2",command=self.add_student).place(x=235,y=5,width=130,height=40)#add 240
    
    btn_result=Button(M_Frame,text="result",font=("goudy old style",15,"bold"),bg="black",fg="white",cursor="hand2",command=self.add_result).place(x=455,y=5,width=130,height=40)#add 460
    
    btn_view=Button(M_Frame,text="view",font=("goudy old style",15,"bold"),bg="black",fg="white",cursor="hand2",command=self.add_report).place(x=675,y=5,width=130,height=40)
    
    btn_logout=Button(M_Frame,text="logout",font=("goudy old style",15,"bold"),bg="black",fg="white",cursor="hand2",command=self.logout).place(x=895,y=5,width=130,height=40)
    
    btn_exit=Button(M_Frame,text="exit",font=("goudy old style",15,"bold"),bg="black",fg="white",cursor="hand2",command=self.exit_).place(x=1115,y=5,width=130,height=40)
    
    #----content-window---
    self.bg_img=Image.open("allimages/image4.jpg")
    self.bg_img=self.bg_img.resize((920,450))
    self.bg_img=ImageTk.PhotoImage(self.bg_img)
    
    self.lbl_bg=Label(self.root,image=self.bg_img).place(x=400,y=180,width=920,height=350) #main background image
    
    #--update-details--
  
    self.lbl_course=Label(self.root,text="Total Course\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#e43b06",fg="white");self.lbl_course.place(x=400,y=530,width=250,height=100)
    
    self.lbl_student=Label(self.root,text="Total Student\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="green",fg="white");
    self.lbl_student.place(x=710,y=530,width=250,height=100) #add 400
    
    self.lbl_result=Label(self.root,text="Total Result\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="blue",fg="white");
    self.lbl_result.place(x=1020,y=530,width=250,height=100)
    
    #---clock-----
    self.lbl=Label(self.root,text="\nWebCode Clock",font=("Book Antique",25,"bold"),fg="white",compound=BOTTOM,bg="#081923",bd=0)
    self.lbl.place(x=10,y=180,height=450,width=350)
    
    self.working()
    
    
    #----footer---
    footer=Label(self.root,text="SRMS-Students Result Management System\nContact us for any Technical Issue: 906xxxxx46",font=("goudy old style",12),bg="black",fg="white").pack(side=BOTTOM)
    self.update_details()
    
  #========================  
  
  def update_details(self):
    con=sqlite3.connect(database="rms.db")
    cur=con.cursor()
    try:
      cur.execute("select * from course")
      cr=cur.fetchall()
      self.lbl_course.config(text=f"Total Courses\n[{str(len(cr))}]")
      
      cur.execute("select * from student")
      cr=cur.fetchall()
      self.lbl_student.config(text=f"Total Student\n[{str(len(cr))}]")
      
      cur.execute("select * from result")
      cr=cur.fetchall()
      self.lbl_result.config(text=f"Total Result\n[{str(len(cr))}]")
      
    except Exception as ex:
      messagebox.showerror("Error",f"Error due to {str(ex)}") 
      
  
  
  def working(self):
    h=datetime.now().time().hour
    m=datetime.now().time().minute
    s=datetime.now().time().second
    
    hr=(h/12)*360
    min_=(m/60)*360
    sec_=(s/60)*360
    
    self.clock_image(hr,min_,sec_)
    self.img=ImageTk.PhotoImage(file="images/clock.jpg")
    self.lbl.config(image=self.img)
    self.lbl.after(200,self.working)
    #-----
    
  def clock_image(self,hr,min_,sec_):
    clock=Image.new("RGB",(400,400),(8,25,35))
    draw=ImageDraw.Draw(clock)
    
    #------for clock image-----
    bg=Image.open("images/clock1.jpg")
    bg=bg.resize((300,300))
    clock.paste(bg,(50,50))
    
    #clock.show()
    
    #-----Hour line image--
    origin=200,200
    draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill="black",width=4)
    
    # #-----  Min line image---
    origin=200,200
    draw.line((origin,200+80*sin(radians(min_)),200-80*cos(radians(min_))),fill="blue",width=3)
    
    #----sec line image---
    origin=200,200
    draw.line((origin,200+100*sin(radians(sec_)),200-100*cos(radians(sec_))),fill="green",width=2)
    draw.ellipse((195,195,210,210),fill="black")
    clock.save("images/clock.jpg")
    
    #-----
    
  def add_course(self): #we have created one object that we will pass later, call this function in button
    self.new_win=Toplevel(self.root)   #top of the dashboard
    self.new_obj=CourseClass(self.new_win)
    
  def add_student(self): 
    self.new_win=Toplevel(self.root)  
    self.new_obj=studentClass(self.new_win)
    
  def add_result(self): 
    self.new_win=Toplevel(self.root)  
    self.new_obj=resultClass(self.new_win)
    
  def add_report(self): 
    self.new_win=Toplevel(self.root)  
    self.new_obj=reportClass(self.new_win)
  
  def logout(self):
    op=messagebox.askyesno("Confirm","Do you really want to logout?",parent=self.root)
    if op==True:
      self.root.destroy()
      os.system("python login.py")
      
  def exit_(self):
    op=messagebox.askyesno("Confirm","Do you really want to Exit?",parent=self.root)
    if op==True:
      self.root.destroy()
      
      
  
  
if __name__=="__main__":   #we are dealing with multipe files we have used this method
  root=Tk()#tkinter class ka object
  obj=RMS(root)
  root.mainloop()
