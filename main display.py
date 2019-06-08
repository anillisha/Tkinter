from tkinter import*
import random
import time

root=Tk()
root.geometry("1800x1000+0+0")
root.title("ALISHA EMBSOFT")
text_Input=StringVar()


Tops =Frame(root,width=100,height=50,bg="RED",relief=SUNKEN)
Tops.pack(side=TOP)

bottom =Frame(root,width=100,height=100,bg="blue",relief=RIDGE)
bottom.pack(side=BOTTOM)

f1 =Frame(root,width=700,height=450,bg="RED",relief=SUNKEN)
f1.pack(side=LEFT)

f2 =Frame(root,width=700,height=450,bg="BLUE",relief=SUNKEN)
f2.pack(side=RIGHT)


localtime=time.asctime(time.localtime(time.time()))
lbinfo=Label(Tops,font=('arial',50,'bold'),text="ALISHA EMBSOFT SYSTEM",fg="RED",bd=10,anchor='w')
lbinfo.grid(row=0,column=0)

lbinfo=Label(Tops,padx=0,pady=10,font=('arial',20,'bold'),text=localtime,fg="BLACK",bd=10,anchor='w')
lbinfo.grid(row=1,column=0)


bottominfo=Label(bottom,font=('arial',20,'bold'),padx=0,pady=0,text="POWERED BY ALISHA COMPANY",fg="RED",bd=10,anchor='w')
bottominfo.grid(row=0,column=0)

c_f1 =Frame(f1,width=600,height=600,bg="BLACK",relief=RAISED)
c_f1.pack(side=TOP)


c1_f1=Label(c_f1,font=('arial',60,'bold'),padx=0,pady=0,text="Counter-1",fg="BLACK",bd=10,anchor='w',relief=RIDGE)
c1_f1.grid(row=0,column=0)
c1_f1=Label(c_f1,font=('arial',60,'bold'),padx=20,pady=20,fg="BLACK",bd=10,anchor='w')
c1_f1.grid(row=0,column=1)
c1_f1=Label(c_f1,font=('arial',60,'bold'),padx=20,pady=20,text="100",fg="BLACK",bd=10,anchor='w',relief=RIDGE)
c1_f1.grid(row=0,column=2)

c2_f1=Label(c_f1,font=('arial',60,'bold'),padx=0,pady=0,text="Counter-2",fg="BLACK",bd=10,anchor='w',relief=RIDGE)
c2_f1.grid(row=1,column=0)
c2_f1=Label(c_f1,font=('arial',60,'bold'),padx=20,pady=20,fg="BLACK",bd=10,anchor='w')
c2_f1.grid(row=1,column=1)
c2_f1=Label(c_f1,font=('arial',60,'bold'),padx=20,pady=20,text="022",fg="BLACK",bd=10,anchor='w',relief=RIDGE)
c2_f1.grid(row=1,column=2)

c3_f1=Label(c_f1,font=('arial',60,'bold'),padx=0,pady=0,text="Counter-3",fg="BLACK",bd=10,anchor='w',relief=RIDGE)
c3_f1.grid(row=2,column=0)
c3_f1=Label(c_f1,font=('arial',60,'bold'),padx=20,pady=20,fg="BLACK",bd=10,anchor='w')
c3_f1.grid(row=2,column=1)
c3_f1=Label(c_f1,font=('arial',60,'bold'),padx=20,pady=20,text="233",fg="BLACK",bd=10,anchor='w',relief=RIDGE)
c3_f1.grid(row=2,column=2)


c_f2 =Frame(f2,width=600,height=600,bg="BLACK",relief=RAISED)
c_f2.pack(side=TOP)


c1_f2=Label(c_f2,font=('arial',60,'bold'),padx=0,pady=0,text="Counter-4",fg="BLACK",bd=10,anchor='w',relief=RIDGE)
c1_f2.grid(row=0,column=0)
c1_f2=Label(c_f2,font=('arial',60,'bold'),padx=20,pady=20,fg="BLACK",bd=10,anchor='w')
c1_f2.grid(row=0,column=1)
c1_f2=Label(c_f2,font=('arial',60,'bold'),padx=20,pady=20,text="999",fg="BLACK",bd=10,anchor='w',relief=RIDGE)
c1_f2.grid(row=0,column=2)

c2_f2=Label(c_f2,font=('arial',60,'bold'),padx=0,pady=0,text="Counter-5",fg="BLACK",bd=10,anchor='w',relief=RIDGE)
c2_f2.grid(row=1,column=0)
c2_f2=Label(c_f2,font=('arial',60,'bold'),padx=20,pady=20,fg="BLACK",bd=10,anchor='w')
c2_f2.grid(row=1,column=1)
c2_f2=Label(c_f2,font=('arial',60,'bold'),padx=20,pady=20,text="200",fg="BLACK",bd=10,anchor='w',relief=RIDGE)
c2_f2.grid(row=1,column=2)

c3_f2=Label(c_f2,font=('arial',60,'bold'),padx=0,pady=0,text="Counter-6",fg="BLACK",bd=10,anchor='w',relief=RIDGE)
c3_f2.grid(row=2,column=0)
c3_f2=Label(c_f2,font=('arial',60,'bold'),padx=20,pady=20,fg="BLACK",bd=10,anchor='w')
c3_f2.grid(row=2,column=1)
c3_f2=Label(c_f2,font=('arial',60,'bold'),padx=20,pady=20,text="500",fg="BLACK",bd=10,anchor='w',relief=RIDGE)
c3_f2.grid(row=2,column=2)






