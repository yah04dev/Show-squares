# -*- coding: UTF-8 -*-
import tkinter as tk  
from functools import partial  
import sys, string, os
root = tk.Tk()  
def bi( q1,hg,wd,mc,cl):  
    q1 = (q1.get()) 
    hg = (hg.get()) 
    wd = (wd.get()) 
    mc = (mc.get()) 
    cl = (cl.get()) 
    
    c=0
    r=2
    
    for i in range(0,q1):
    

         l=tk.Label(root, text=i,background=cl,height=hg,width=wd).grid(row=r, column=c) 
         c=c+1
         i=i+1

         if c==mc:
             c=0
             r=r+1
        


root.title('box emulator')

  
i1 = tk.IntVar()  
i2 = tk.IntVar()
i3 = tk.IntVar()
i4 = tk.IntVar()
i5 = tk.StringVar()

 

 
  
  
entryNum1 = tk.Entry(root, textvariable=i1).grid(row=0, column=0)  
en = tk.Entry(root, textvariable=i2).grid(row=0, column=1)  
ent = tk.Entry(root, textvariable=i3).grid(row=0, column=2)  
entr = tk.Entry(root, textvariable=i4).grid(row=0, column=3)  
entry = tk.Entry(root, textvariable=i5).grid(row=0, column=4)  
tk.Label(root, text="n of box").grid(row=1, column=0) 
tk.Label(root, text="hight of box").grid(row=1, column=1) 
tk.Label(root, text="width of box").grid(row=1, column=2) 
tk.Label(root, text="max of column").grid(row=1, column=3) 
tk.Label(root, text="color of box").grid(row=1, column=4) 
  
bi = partial(bi, i1,i2,i3,i4,i5)  
buttonCal = tk.Button(root, text="emulate", command=bi).grid(row=0, column=5)  
root.mainloop()  



