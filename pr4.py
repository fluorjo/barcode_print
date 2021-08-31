import sys

from PyQt5 import QtGui, QtWidgets, QtPrintSupport
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
import tkinter as tk
from tkinter import *
from tkinter import ttk


class App(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()  
        # Create some widgets
        self.setGeometry(500, 500, 600, 600)
        self.editor = QtWidgets.QLabel(self)

        a = QPixmap('C:/Users/fluor/requi.png')
        self.editor.setPixmap(a)
        self.editor.setGeometry(65, 20, 340, 280)
        # Create printer
        printer = QtPrintSupport.QPrinter()
        # Create painter
        painter = QtGui.QPainter()
        # Start painter
        painter.begin(printer)
        # Grab a widget you want to print
        screen = self.editor.grab()
        # Draw grabbed pixmap
        painter.scale(0.5, 0.5);
        painter.drawPixmap(-10, -60, screen)
        
        # End painting
        painter.end()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = App()
    gui.show()
    app.exec_()
    app.end()