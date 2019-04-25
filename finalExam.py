# Task 1
#def func1(s):
#    dict1 = dict()
#    list1 = s.split(',')
#    for ss in list1:
#        if ss not in dict1:
#            dict1[ss] = 1
#        else:
#            dict1[ss] +=1
#    return dict1
#print(func1('Rah, rah, ah, ah, ah, roma, roma, ma, Gaga, ooh, la, la, want, your, bad, romance'))

# Task 2
import pandas as pd
import matplotlib.pyplot as plt

df1=pd.read_excel('data.xlsx',sheet_name1='data1')
df2=pd.read_excel('data.xlsx',sheet_name2='data2')
df3=pd.read_excel('data.xlsx',sheet_name3='data3')


if df1.values[1,1] is not "data not available":
    temp = df1.values[:,1]

    time = df1.values[:,0]

    stdDev = df1.values[:,2]

    line, caps,bars=plt.errorbar(time, temp,yerr = stdDev,fmt = 'bs--',linewidth=3,
        elinewidth=0.5,ecolor='k',capsize=5,capthick=1)

    plt.title("Task 2", fontsize = 16)
    plt.xlabel('Time', fontweight='bold')
    plt.ylabel('Temperature(C)', fontweight='bold')
    plt.legend(["Error Bars"],numpoints=1,loc=("upper left"))
    plt.savefig('task2.png', dpi=600)
    plt.show()

elif df2.values[1,1] is not "data not available":
    temp = df1.values[:,1]

    time = df1.values[:,0]

    stdDev = df1.values[:,2]

    line, caps,bars=plt.errorbar(time, temp,yerr = stdDev,fmt = 'bs--',linewidth=3,
        elinewidth=0.5,ecolor='k',capsize=5,capthick=1)

    plt.legend(["Error Bars"],numpoints=1,loc=("upper left"))
    plt.savefig('task2.png', dpi=600)
    plt.show()

elif df3.values[1,1] is not "data not available":
    temp = df1.values[:,1]

    time = df1.values[:,0]

    stdDev = df1.values[:,2]

    line, caps,bars=plt.errorbar(time, temp,yerr = stdDev,fmt = 'bs--',linewidth=3,
        elinewidth=0.5,ecolor='k',capsize=5,capthick=1)

    plt.legend(["Error Bars"],numpoints=1,loc=("upper left"))
    plt.savefig('task2.png', dpi=600)
    plt.show()

# Task 3   
#class linkedList:
#    def __init__(self):
#        self.head = None
#        
#    def append(self, data):
#        newNode=Node(data)
#        if self.head==None:
#            self.head=newNode
#            return
#        else:
#            lastNode=self.head
#            while lastNode.next != None:
#                lastNode=lastNode.next
#            lastNode.next=newNode
#            
#    def print_list(self):
#        curNode=self.head
#        while curNode!= None:
#            print(curNode.data)
#            curNode=curNode.next
#            
#    def insterAtPos(self,data,pos):
#        newNode=Node(data)
#        curNode=self.head
#        if pos==0:
#            newNode.next=curNode.next
#            self.head.next=newNode
#            return
#        else:
#            cnt=0
#            prev=None
#            while curNode != None and cnt != pos:
#                prev=curNode
#                curNode=curNode.next
#                cnt+=1
#            if curNode==None:
#                print("The node doesn't exist")
#                return
#            else:
#                prev.next=newNode
#                newNode.next = curNode
#    def scndLastToFront(self):
#        curNode=self.head
#        while curNode.next.next != None:
#            prev=curNode
#            curNode=curNode.next
#        
#        prev.next=curNode.next
#        curNode.next = self.head
#        self.head = curNode
#
#class Node:
#    def __init__(self,data):
#        self.data=data
#        self.next = None

# Task 4
#from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtWidgets import QApplication, QToolTip, QPushButton, QWidget
##'''user code'''
##from PyQt5.QtWidgets import QMessageBox
##
##def btn_clicked():
##    
##'''user code'''
#
#class Ui_MainWindow(object):
#    def setupUi(self, MainWindow):
#        MainWindow.setObjectName("MainWindow")
#        MainWindow.resize(800, 600)
#        self.centralwidget = QtWidgets.QWidget(MainWindow)
#        self.centralwidget.setObjectName("centralwidget")
#        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
#        self.pushButton.setGeometry(QtCore.QRect(170, 210, 181, 91))
#        font = QtGui.QFont()
#        font.setPointSize(12)
#        self.pushButton.setFont(font)
#        self.pushButton.setObjectName("pushButton")
#        MainWindow.setCentralWidget(self.centralwidget)
#        self.statusbar = QtWidgets.QStatusBar(MainWindow)
#        self.statusbar.setObjectName("statusbar")
#        MainWindow.setStatusBar(self.statusbar)
#
#        self.retranslateUi(MainWindow)
#        QtCore.QMetaObject.connectSlotsByName(MainWindow)
#
#    def retranslateUi(self, MainWindow):
#        _translate = QtCore.QCoreApplication.translate
#        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
#        self.pushButton.setText(_translate("MainWindow", "Exit"))
#        self.pushButton.clicked.connect(QApplication.instance().quit)
#'''user code'''
#import sys
#app = QtWidgets.QApplication(sys.argv)
#MainWindow=QtWidgets.QMainWindow()
#ui=Ui_MainWindow()
#ui.setupUi(MainWindow)
#MainWindow.show()
##ex=Example()
#sys.exit(app.exec_())
#'''usr code'''
