from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb

GUI = Tk()
GUI.title('new project')
GUI.geometry('800x400')

L1 = Label(GUI,text='Welcome to my store',font=('Angsana New',30))
L1.pack()

n1 = 0
n2 = 0

photo1 = tk.PhotoImage(file="x.png")
photo1 = photo1.subsample(5,5)

photo2 = tk.PhotoImage(file="y.png")
photo2 = photo2.subsample(5,5)

img1 = tk.Label(GUI, image=photo1)
img1.place(x = 70 , y = 50)

img2 = tk.Label(GUI, image=photo2)
img2.place(x = 300 , y = 85)

def bt1():
    global n1
    n1 += 1
    text = 'คุณต้องการสั้ง x จำนวน '
    mb.showinfo('รายการ',text + str(n1) + ' ชิ้น' )
    
def bt2():
    global n1
    n1 -= 1
    if n1 < 0:
        n1 = 0
        text = 'ยกเลิกคำสั่งซื้อ x คงเหลือ ' 
        mb.showinfo('รายการ',text + str(n1) + ' ชิ้น')
    else:
        text = 'ยกเลิกคำสั่งซื้อ x คงเหลือ '
        mb.showinfo('รายการ',text + str(n1) + ' ชิ้น')
        
def bt3():
    global n2
    n2 += 1
    text = 'คุณต้องการสั้ง y จำนวน '
    mb.showinfo('รายการ',text + str(n2) + ' ชิ้น ')
def bt4():
    global n2
    n2 -= 1
    if n2 < 0:
        n2 = 0
        text = 'ยกเลิกคำสั่งซื้อ y คงเหลือ '
        mb.showinfo('รายการ',text + str(n2) + ' ชิ้น')
    else:
        text = 'ยกเลิกคำสั่งซื้อ y คงเหลือ '
        mb.showinfo('รายการ',text + str(n2) + ' ชิ้น')

def bt5():
    global n1
    global n2
    text1 ='คุณได้สั่งซื้อของ ชนิด x เป็นจำนวน '
    text2 ='คุณได้สั่งซื้อของ ชนิด y เป็นจำนวน '
    p = n1*200 + n2*100
    mb.showinfo('ยอดรวมรายการสินค้า',text1 + str(n1) + ' ชิ้น' + '\n' + text2 + str(n2) + ' ชิ้น' + '\n' + 'คิดเป็นเงิน ' + str(p) + ' บาท')
    
    
FB1 = Frame(GUI)
FB1.place(x = 40,y = 220)
B1 = ttk.Button(FB1,text='BUY',command = bt1)
B1.pack()

FB2 = Frame(GUI)
FB2.place(x = 150,y = 220)
B1 = ttk.Button(FB2,text='CANCEL',command = bt2)
B1.pack()

FB3 = Frame(GUI)
FB3.place(x = 270,y = 220)
B3 = ttk.Button(FB3,text='BUY',command = bt3)
B3.pack()

FB4 = Frame(GUI)
FB4.place(x = 380,y = 220)
B4 = ttk.Button(FB4,text='CANCEL',command = bt4)
B4.pack()

FB5 = Frame(GUI)
FB5.place(x = 190,y = 260)
B5 = ttk.Button(FB5,text='ENTER',command = bt5)
B5.pack(ipadx=20,ipady=10)






















