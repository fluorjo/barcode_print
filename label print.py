from PyQt5 import QtCore, QtGui, QtWidgets, QtPrintSupport
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton, QDialog, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPdfWriter, QPagedPaintDevice, QPainter, QScreen, QPixmap
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog


from tkinter import *
from win32gui import FindWindow, GetWindowRect
import pygetwindow as gw
import PIL
from PIL import ImageGrab

import numpy
import sys

import barcode
from barcode.writer import ImageWriter
from barcode import EAN13
from PIL import Image, ImageTk
hr=barcode.get_barcode_class('ean13')
 
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import Label, PhotoImage

#엑셀파일 열기
import openpyxl
da =  openpyxl.load_workbook('C:/Users/fluor/2x.xlsx')
sheet = da.active


#검색기능
import operator
import pr4
from pr4 import *


#검색 결과값 저장 list
o=['0']
p=['0']

#바코드 입력창

import sys
 
def ilaya1():
    current_func_name = sys._getframe().f_code.co_name
    print ("The current running function name : {}".format(current_func_name))
 

bw=tk.Tk()
bw.title("바코드 입력창")
bw.geometry("400x100")
bw.resizable(True, True)
a = tk.Entry(bw, width = 30, bg = 'white')
a.pack(pady = 15)


def search():
    x=int(o[0])
    for i in sheet.rows:
        if(operator.eq(i[0].value,x)): 
            for j in range(1,3):
                    p.insert(0,i[j].value)
        else:
            p.insert(0,'없음')
            p.insert(1,'없음')
    


class barcode:
    def bar(event):    
        b=a.get()
        c=EAN13(b,writer=ImageWriter())
        c.save('C:/Users/fluor/bgg')  
        img = PIL.Image.open('C:/Users/fluor/bgg.png')
        img_resize = img.resize((350, 60), PIL.Image.LANCZOS)
        img_resize.save('C:/Users/fluor/bgggg.png')
        del o[0]
        o.insert(0,b)
        search()  
    
        cw=tk.Tk()
        cw.title("x")
        
        cw.geometry("340x220")
        cw.resizable(True, True)
        
        wa = tk.Entry(cw)
        wa.pack()
        wa.insert(INSERT,p[1])
        wa.configure(font=("HY헤드라인M", 42,),justify='center')
        
        wb = tk.Entry(cw)
        wb.insert(INSERT,p[0])
        wb.configure(font=("HY견고딕", 48, "bold"),justify='center')
        
        wb.pack()
        
        img=tk.PhotoImage(file="C:/Users/fluor/bgggg.png", master=cw)
        la=tk.Label(cw, image=img, width = 320, height = 30)
        la.pack()
        button = tk.Button(cw, text="print", width=50, height =20,command=pr4.App)
        button.pack()
       
        
        def ss():
            win = gw.getWindowsWithTitle("x")[0]
            winleft = win.left+9
            wintop = win.top +32 #change 38 to 7 to not capture the titlebar
            winright = win.right-9
            winbottom = win.bottom-73
            final_rect = (winleft,wintop,winright,winbottom)
            img = ImageGrab.grab(final_rect)
            img.save('requi.png')
            #making the tkinter window
            
            
        cw.after(1000,ss)
        cw.mainloop()
        

            
        
    bw.bind('<Return>', bar)
    bw.mainloop()


#8801043450690
