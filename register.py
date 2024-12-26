#we are designing register page which is link to the database.
#we have used pymysql for connect the database to XAMPP  control panel and we will fetch all the data which we will create on my database xampp

from tkinter import* #module, root will become the object of tk module
from tkinter import ttk,messagebox
from PIL import Image,ImageTk#(to deal with jpg file)#pip install pillow
#import pymysql #pip install pymysql
import sqlite3
import os
class Register: #by working in class we will get security and it will enhanced further coding also.
  def __init__(self,root):
    self.root=root #initializing of root
    self.root.title("Registration window")
    self.root.geometry("1350x700+0+0")
    self.root.config(bg="white")
    
    #=========Bg Image======
    self.bg=ImageTk.PhotoImage(file="images/backimg2.jpg")#variable for the image, this bg is object of class
    bg=Label(self.root,image=self.bg,bg="lightblue").place(x=250,y=0,relwidth=1,relheight=1)#relwidth takes a value between 0 and 1, representing a fraction of the parent container's width. 
    #object f root window
    

    #=========LEFT Image======
    self.left=ImageTk.PhotoImage(file="images/sideimg.jpg")#variable for the image, this bg is object of class
    left=Label(self.root,image=self.left).place(x=80,y=100,width=400,height=500)#object f root window
    
    #--------------Register Frame------------
    frame1=Frame(self.root,bg="white")
    frame1.place(x=400,y=100,width=700,height=500)
    
    title=Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="black").place(x=50,y=30)
    #-----------row1
    # self.var_fname=StringVar()
    f_name=Label(frame1,text="First Name",font=("times new roman",15,"bold"),fg="black").place(x=50,y=100)
    self.txt_fname=Entry(frame1,font=("times new roman",15),bg="lightgray")
    self.txt_fname.place(x=50,y=130,width=250)
    
    l_name=Label(frame1,text="Last Name",font=("times new roman",15,"bold"),fg="black").place(x=370,y=100)
    self.txt_lname=Entry(frame1,font=("times new roman",15),bg="lightgray")#to make it object add self.to the first name
    self.txt_lname.place(x=370,y=130,width=250)
    #------------row2
    contact_no=Label(frame1,text="Contact Number",font=("times new roman",15,"bold"),fg="black").place(x=50,y=170)
    self.txt_ContactNo=Entry(frame1,font=("times new roman",15),bg="lightgray")
    self.txt_ContactNo.place(x=50,y=200,width=250)
    
    email_name=Label(frame1,text="Email",font=("times new roman",15,"bold"),fg="black").place(x=370,y=170)
    self.txt_emailname=Entry(frame1,font=("times new roman",15),bg="lightgray")
    self.txt_emailname.place(x=370,y=200,width=250)
    
    #---------row3 
    question=Label(frame1,text="Security Question",font=("times new roman",15,"bold"),fg="black").place(x=50,y=240)
    
    self.cmb_quest=ttk.Combobox(frame1,font=("times new roman",13),state='readonly',justify='center')
    self.cmb_quest['values']=("select","your first pet name","your birth place","your Best friend")
    self.cmb_quest.place(x=50,y=270,width=250)
    self.cmb_quest.current(0)
    #we want combo box for selecting the option
    
    answer=Label(frame1,text="Answer",font=("times new roman",15,"bold"),fg="black").place(x=370,y=240)
    self.txt_answer=Entry(frame1,font=("times new roman",15),bg="lightgray")
    self.txt_answer.place(x=370,y=270,width=250)
    
    #--------------
    Password=Label(frame1,text="Password",font=("times new roman",15,"bold"),fg="black").place(x=50,y=310)
    self.txt_Password=Entry(frame1,font=("times new roman",15),bg="lightgray")
    self.txt_Password.place(x=50,y=340,width=250)
    
    cPassword=Label(frame1,text="Confirm Password",font=("times new roman",15,"bold"),fg="black").place(x=370,y=310)
    self.txt_cPassword=Entry(frame1,font=("times new roman",15),bg="lightgray")
    self.txt_cPassword.place(x=370,y=340,width=250)
    
    #----Terms----
    self.var_chk=IntVar()
    chk=Checkbutton(frame1,text="I Agree The Terms & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,font=("times new roman",12)).place(x=50,y=380)
    
    self.btn_img=ImageTk.PhotoImage(file="images/reg5.jpg")
    btn=Button(frame1,image=self.btn_img,bd=0,cursor="hand2",command=self.register_data).place(x=0,y=415,width=275,height=80)
  
    btn_login=Button(self.root,text="Sign In",command=self.login_window,font=("times new roman",20),bd=0,cursor="hand2").place(x=200,y=460,width=180)
    
  def login_window(self):
    # we will connect register file just import that file name
    self.root.destroy()
    #import login
    os.system("python login.py")
    
# now we will fetch the data 
# there are two types of fetching the data 1. create variavles and pass them in antri and fetch the data, 2.we will fetch the data with the help of antri field object
  def clear(self):
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_ContactNo.delete(0,END)
    self.txt_emailname.delete(0,END)
    self.txt_answer.delete(0,END)
    self.txt_Password.delete(0,END)
    self.txt_cPassword.delete(0,END)
    self.cmb_quest.current(0)
    
  def register_data(self):
    if self.txt_fname.get()==""or self.txt_lname.get()=="" or self.txt_ContactNo.get()=="" or self.txt_emailname.get=="" or self.cmb_quest.get()=="select" or self.txt_answer.get()=="" or self.txt_Password.get()=="" or self.txt_cPassword.get()=="":
      messagebox.showerror("Error","All Fields Are Required",parent=self.root)
    elif self.txt_Password.get()!=self.txt_cPassword.get():
      messagebox.showerror("Error","Password and Confirm Password should be same",parent=self.root)
    elif self.var_chk.get()==0:
      messagebox.showinfo("Error","Please Agree our Terms and Conditions",parent=self.root)
    else: #to connect databse to python we have used this try and except
      try: #connection to connect sql file, #connect to call function, we need to give 4 parameters to it
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor() #now we have one cursor to execute cross queries
        cur.execute("select * from employee where email=?", (self.txt_emailname.get(),))
        row=cur.fetchone()
        #print(row)
        if row!=None:
          messagebox.showinfo("Error","User already Exist,Please try with another email",parent=self.root)
        else:
          cur.execute("insert into employee(fname,lname,contact,email,question,answer,password)values(?,?,?,?,?,?,?)",
                    (self.txt_fname.get(),
                     self.txt_lname.get(),
                     self.txt_ContactNo.get(),
                     self.txt_emailname.get(),
                     self.cmb_quest.get(),
                     self.txt_answer.get(),
                     self.txt_Password.get()
                    ))
        con.commit()
        con.close()
        messagebox.showinfo("Success","Register Successfull",parent=self.root)
        self.clear()
        self.login_window()
      
      except Exception as es:
        messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
        
      
      
      
          
          
      
root=Tk()
obj=Register(root)
root.mainloop()

