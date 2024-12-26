from tkinter import*
from PIL import Image,ImageTk,ImageDraw #pip install pilllow
from datetime import*
import time
from math import*
import sqlite3
#import pymysql #pip install pymysql, we will connect databse with the help of this library
import os
from tkinter import messagebox
class Login_window:
  def __init__(self,root):
    self.root=root
    self.root.title("GUI Analog Clock")
    self.root.geometry("1350x700+0+0")
    self.root.config(bg="#021e2f")
    #---------background colors---
    left_lbl=Label(self.root,bg="lightblue",bd=0)
    left_lbl.place(x=0,y=0,relheight=1,width=600)
    
    right_lbl=Label(self.root,bg="#031F3C",bd=0)
    right_lbl.place(x=600,y=0,relheight=1,relwidth=1)
    
    # #---frames---
    login_frame=Frame(self.root,bg="white")
    login_frame.place(x=250,y=100,width=800,height=500)
    
    title=Label(login_frame,text="LOGIN HERE",font=("times new roman",30,"bold"),bg="white",fg="#08A3D2").place(x=250,y=50)
    
    email=Label(login_frame,text="EMAIL ADDRESS",font=("times new roman",17,"bold"),bg="white",fg="black").place(x=250,y=150)
    self.txt_email=Entry(login_frame,font=("times new roman",15),bg="lightgray",fg="black")
    self.txt_email.place(x=250,y=190,width=350,height=35)
    
    pass_=Label(login_frame,text="PASSWORD",font=("times new roman",17,"bold"),bg="white",fg="black").place(x=250,y=250)
    self.txt_pass_=Entry(login_frame,font=("times new roman",15),bg="lightgray",fg="black")
    self.txt_pass_.place(x=250,y=280,width=350,height=35)
    
    btn_reg=Button(login_frame,cursor="hand2",command=self.register_window,text="Register New Account?",font=("times new roman",14),bg="white",bd=0,fg="#800857").place(x=250,y=320)
    
    btn_login=Button(login_frame,text="Login",command=self.login,font=("times new roman",20),fg="white",bg="#800857",cursor="hand2").place(x=250,y=380,width=180,height=40) #with the help of command we will call to the function login
    
    #---clock-----
    self.lbl=Label(self.root,text="\nWebCode Clock",font=("Book Antique",25,"bold"),fg="white",compound=BOTTOM,bg="#081923",bd=0)
    self.lbl.place(x=90,y=120,height=450,width=350)
    
    self.working()
  def register_window(self):
    # we will connect register file just import that file name
    self.root.destroy()
    import register
    
  def login(self):
    if self.txt_email.get()=="" or self.txt_pass_.get()=="":
      messagebox.showerror("Error","All Fields are Required",parent=self.root)
      #error gives icon,info gives data msg
    else:#link database
      try:
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        cur.execute("select * from employee where email=? and password=?",(self.txt_email.get(),self.txt_pass_.get()))
        #cursor helps in execution of the querries
        row=cur.fetchone()
        #print(row)
        if row==None:
          messagebox.showerror("Error","Invalid USERNAME & PASSWORD",parent=self.root)
          
        else:
          messagebox.showinfo("Success",f"Welcome: {self.txt_email.get()}",parent=self.root)
          self.root.destroy()
          os.system("python dashboard1.py")
        con.close()
      except Exception as es:
        messagebox.showerror("Error",f"Error Due to: {str(es)}",parent=self.root)
      
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
    
root=Tk()
obj=Login_window(root)
root.mainloop()

    
    