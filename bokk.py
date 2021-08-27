# %%
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
 
class bbbb(object):
    number=input()
    j=EAN13(number,writer=ImageWriter())
    j.save("kkkkk")   
    image = Image.open('C:/Users/fluor/kkkkk.png')
    resize_image = image.resize((400,400))
    resize_image.save('C:/Users/fluor/kkkkkk.png')

class Ui_Dialog(QWidget):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(542, 329)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridWidget = QtWidgets.QWidget(Dialog)
        self.gridWidget.setObjectName("gridWidget")
        self.label = QtWidgets.QLabel(self.gridWidget)
        self.label.setGeometry(QtCore.QRect(30, 140, 350, 50))
        self.label.setText("")
        self.label.setObjectName("label")
        a = QPixmap('C:/Users/fluor/kkkkkk.png')
        self.label.setPixmap(a)
        
        self.textEdit = QtWidgets.QTextEdit(self.gridWidget)
        self.textEdit.setGeometry(QtCore.QRect(30, 0, 350, 70))
        self.textEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.gridWidget)
        self.textEdit_2.setGeometry(QtCore.QRect(30, 60, 350, 70))
        self.textEdit_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayout.addWidget(self.gridWidget)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.btnClick)
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'HY헤드라인M\'; font-size:21pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'HY헤드라인M\'; font-size:18pt;\"></span></p></body></html>"))
        self.textEdit_2.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'HY견고딕\'; font-size:20pt;\">₩</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "프린트"))
        
        self.textEdit.setAlignment(Qt.AlignCenter)
        self.textEdit_2.setAlignment(Qt.AlignRight)
        self.label.setAlignment(Qt.AlignCenter)
    
        
    def btnClick(self):
        # 프린터 생성, 실행
        printer = QPrinter()
        dlg = QPrintDialog(printer, self)
        if dlg.exec() == QDialog.Accepted:
            # Painter 생성
            qp = QPainter()
            qp.begin(printer)        
 
            # 여백 비율
            wgap = printer.pageRect().width()
            hgap = printer.pageRect().height()
 
            # 화면 중앙에 위젯 배치
            xscale = (printer.pageRect().width()-wgap)
            yscale = (printer.pageRect().height()-hgap)
            scale = xscale if xscale < yscale else yscale               
 
            # 인쇄
            self.gridWidget.render(qp)

            qp.end()       

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()

    sys.exit(app.exec_())

