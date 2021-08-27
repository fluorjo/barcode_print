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
hr=barcode.get_barcode_class('ean13')

import tkinter
from math import *

window=tkinter.Tk()
window.title("바코드 입력창")
window.geometry("200x50")
window.resizable(False, False)

def calc(event):
    number=input()
    j=EAN13(number,writer=ImageWriter())
    j.save("barcode")   
    image = Image.open('C:/Users/fluor/barcode.png')
    resize_image = image.resize((400,400))
    resize_image.save('C:/Users/fluor/barcode1.png')

entry=tkinter.Entry(window)
entry.bind("<Return>", calc)
entry.pack()

label=tkinter.Label(window)
label.pack()

window.mainloop()