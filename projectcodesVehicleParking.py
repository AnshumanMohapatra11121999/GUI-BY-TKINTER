from  tkinter import *
from tkinter import ttk

m=Tk()

ml1=Label(m,text="Parking Management System",font=("hellvetica",18),bd=1,relief="sunken" )
ml1.pack(pady=30)
l1=Label(m,text="Username",bg="yellow")
l1.place(relx=0.4,rely=0.2)
e1=Entry(m,bd=5,bg="blue")
e1=e1.place(relx=0.55,rely=0.2)
l2=Label(m,text="Pass number",bg="yellow")
l2.place(relx=0.4,rely=0.3)
e2=Entry(m,bd=5,bg="blue")
e2=e2.place(relx=0.55,rely=0.3)
ls=Label(m,text="Request Type",bg="yellow")
ls.place(relx=0.4,rely=0.4)
rt=["Exit","Entry","Any Other Request"]
cmb1=ttk.Combobox(m,values=rt,width=20)
cmb1.place(relx=0.55,rely=0.4)
ls2=Label(m,text=" NO OF DAYS",bg="yellow")
ls2.place(relx=0.4,rely=0.5)
rt2=["Intraday","More than 1 day","Any Other Request"]
cmb2=ttk.Combobox(m,values=rt2,width=20)
cmb2.place(relx=0.55,rely=0.5)
l3=Label(m,text="Vehicle number",bg="yellow")
l3.place(relx=0.4,rely=0.6)
e3=Entry(m,bd=5,bg="blue")
e3=e3.place(relx=0.55,rely=0.6)
l4=Label(m,text="ENTRY DATE",bg="yellow")
l4.place(relx=0.2,rely=0.7)
e4=Entry(m,bd=5,bg="blue")
e4=e4.place(relx=0.3,rely=0.7)
l5=Label(m,text="EXIT DATE",bg="yellow")
l5.place(relx=0.5,rely=0.7)
e5=Entry(m,bd=5,bg="blue")
e5=e5.place(relx=0.6,rely=0.7)
b1=Button(m,text="Get Confirmation Ticket",command="Parking slot alloted",bg="green")
b1.place(relx=0.6,rely=0.8)
b2=Button(m,text="Place a  Request",command="Parking slot alloted",bg="green")
b2.place(relx=0.3,rely=0.8)

m.mainloop()