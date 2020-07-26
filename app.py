from tkinter import *
import time
from tkinter import ttk

root = Tk()
root.geometry('1600x800+0+0')
root.title('Hotel Billing System')

#====================== Window Partition ==========================================
tops = Frame(root,width=1600, height=100, bg='blue', relief=SUNKEN)
tops.pack(side=TOP)

f1= Frame(root, width=800, height=300, relief=SUNKEN)
f1.pack(side=LEFT)

f2= Frame(root, width=400, height=300, relief=SUNKEN)
f2.pack(side=RIGHT)

f3= Frame(root, width=30, height=10, relief=SUNKEN)
f3.pack(side=LEFT)

f4= Frame(root, width=100, height=10, relief=SUNKEN)
f4.pack(side=LEFT)

#========================== Main Screen =============================================
txt_ip= StringVar(value = 'Welcome to Hotel Bill System .....')
Display = Entry(tops, font=('arial',30,'bold'), fg='white', bg='blue', bd=20, justify='right',textvariable=txt_ip)
Display.grid(columnspan=16)

#================================= Time ====================================================
localtime = time.asctime(time.localtime(time.time()))
tstamp = Label(f2,font=('arial',20,'bold'),fg='dark blue',bd=20, text=localtime, anchor=W)
tstamp.grid(row=0,column=0,columnspan=4)

#================================ Calculator Buttons =================================================
but7 = Button(f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='7').grid(row=1,column=0)
but8 = Button(f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='8').grid(row=1,column=1)
but9 = Button(f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='9').grid(row=1,column=2)
butC = Button(f2,padx=13,pady=5,bd=8,font=('arial',20,'bold'),text='C').grid(row=1,column=3)
but4 = Button(f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='4').grid(row=2,column=0)
but5 = Button(f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='5').grid(row=2,column=1)
but6 = Button(f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='6').grid(row=2,column=2)
butP = Button(f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='+').grid(row=2,column=3)
but1 = Button(f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='1').grid(row=3,column=0)
but2 = Button(f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='2').grid(row=3,column=1)
but3 = Button(f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='3').grid(row=3,column=2)
butS = Button(f2,padx=18,pady=5,bd=8,font=('arial',20,'bold'),text='-').grid(row=3,column=3)
but0 = Button(f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='0').grid(row=4,column=0)
butDot = Button(f2,padx=19,pady=5,bd=8,font=('arial',20,'bold'),text='.').grid(row=4,column=1)
butDiv = Button(f2,padx=19,pady=5,bd=8,font=('arial',20,'bold'),text='/').grid(row=4,column=2)
butMul = Button(f2,padx=18,pady=5,bd=8,font=('arial',20,'bold'),text='*').grid(row=4,column=3)
butEq = Button(f2,padx=16,pady=5,bd=8,font=('arial',20,'bold'),text='=').grid(row=5,column=0)
butLB = Button(f2,padx=18,pady=5,bd=8,font=('arial',20,'bold'),text='(').grid(row=5,column=1)
butRB = Button(f2,padx=19,pady=5,bd=8,font=('arial',20,'bold'),text=')').grid(row=5,column=2)
butNone = Button(f2,padx=20,pady=5,bd=8,font=('arial',20,'bold'),text=' ').grid(row=5,column=3)


#================= Program init execute =========================================
root.mainloop()