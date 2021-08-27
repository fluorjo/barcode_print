from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton, QDialog, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPdfWriter, QPagedPaintDevice, QPainter, QScreen, QPixmap
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog

import sys

import barcode
from barcode.writer import ImageWriter
from barcode import EAN13
from PIL import Image
#바코드를 EAN13형식으로 받음.
hr=barcode.get_barcode_class('ean13')

import tkinter
from math import *
from tkinter import *
from tkinter import ttk

window=tkinter.Tk()
#바코드 숫자를 입력받는 부분
a=StringVar()

window.title("바코드 입력창")
window.geometry("300x300")
window.resizable(False, False)

def bar(event):
    #이 j 값이 항상 숫자여야 한다면서, 저 'a'값을 받는 게 안 되는데... 
    #어떻게 해야 UI 내에서 받도록 할 수 있는지 모르겠습니다...! 
    j=EAN13(a.get("1.0","end"),writer=ImageWriter())
    j.save("barcode")   
    image = Image.open('C:/Users/fluor/barcode.png')
    resize_image = image.resize((400,400))
    resize_image.save('C:/Users/fluor/barcode1.png')

entry=tkinter.Entry(window)
entry.bind("<Return>", bar)
entry.pack()

label=tkinter.Label(window)
label.pack()

window.mainloop()
