from tkinter import *
import time
from tkinter import ttk

root = Tk()
root.geometry('1366x768+0+0')
root.title('Hotel Billing System')

#====================== Window Partition ==========================================
tops = Frame(root, width=1366, height=100, bg='blue', relief=SUNKEN)
tops.pack(side=TOP)

f1= Frame(root, width=800, height=10, bg='green', relief=SUNKEN)
f1.pack(side=LEFT)

f2= Frame(root, width=400, height=10, bg='red', relief=SUNKEN)
f2.pack(side=RIGHT)

f3= Frame(root, width=30, height=10, bg='blue', relief=SUNKEN)
f3.pack(side=LEFT)

f4= Frame(root, width=100, height=10, bg='orange', relief=SUNKEN)
f4.pack(side=LEFT)

#======================== Main Screen =============================================
txt_ip= StringVar(value = 'Welcome to HBS......')
Display = Entry(tops, font=('arial',50,'bold'), fg='white', bg='blue', bd=30, justify='center',textvariable=txt_ip)
Display.grid(columnspan=4)

#================= Program init execute =========================================
root.mainloop()