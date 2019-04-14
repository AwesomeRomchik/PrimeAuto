from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDateTime, QDate, QTime, Qt
import sqlite3
import sys
import os
from datetime import datetime

class Ui_Dialog(object):
    def mechanicsdisplay(self):
        self.mechanicsWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.mechanicsWindow)
        self.mechanicsWindow.show()
    def loginCheck(self):
        #store the login and password inputs in variables
        global username
        username = self.loginField.text()
        global password
        password = self.passwordField.text()
        #connect to database to check for details
        connection = sqlite3.connect("logindatabase.db")
        result = connection.execute("SELECT * FROM USERS WHERE USERNAME = ? and PASSWORD = ?",(username,password))
        global fullname
        fullname = Ui_MainWindow.getfullname()
        #print(fullname)
        global workrole
        #fetching all data from the DB to check the login details
        if ( len(result.fetchall()) > 0):
            #print("User found")
            #print(datetime.date(datetime.now()))
            self.mechanicsdisplay()
            self.label.setText('')
        else:
            #print("User not found")
            self.label.setText("Incorrect username or password")


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(436, 380)
        self.password = QtWidgets.QLabel(Dialog)
        self.password.setGeometry(QtCore.QRect(70, 120, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.password.setFont(font)
        self.password.setObjectName("password")
        self.loginInfo = QtWidgets.QLabel(Dialog)
        self.loginInfo.setGeometry(QtCore.QRect(40, 290, 361, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.loginInfo.setFont(font)
        self.loginInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.loginInfo.setWordWrap(True)
        self.loginInfo.setObjectName("loginInfo")
        #password input
        self.passwordField = QtWidgets.QLineEdit(Dialog)
        self.passwordField.setGeometry(QtCore.QRect(190, 125, 151, 25))
        self.passwordField.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordField.setObjectName("passwordField")
        self.loginField = QtWidgets.QLineEdit(Dialog)
        self.loginField.setGeometry(QtCore.QRect(190, 50, 151, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        #login input
        self.loginField.setFont(font)
        self.loginField.setText("")
        self.loginField.setObjectName("loginField")
        self.login = QtWidgets.QLabel(Dialog)
        self.login.setGeometry(QtCore.QRect(70, 50, 71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        self.login.setFont(font)
        self.login.setObjectName("login")
        #login button
        self.loginButton = QtWidgets.QPushButton(Dialog)
        self.loginButton.setGeometry(QtCore.QRect(170, 190, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.loginButton.setFont(font)
        self.loginButton.setObjectName("loginButton")
        ################## Button event ###################
        self.loginButton.clicked.connect(self.loginCheck)
        ###################################################
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 250, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 0, 0)")
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def closeIt(self):
        self.close()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Login"))
        self.password.setText(_translate("Dialog", "Password"))
        self.loginInfo.setText(_translate("Dialog", "Your login details are issued by the administrator! Contact them for the details. You can not register on your own."))
        self.login.setText(_translate("Dialog", "Login"))
        self.loginButton.setText(_translate("Dialog", "Login"))

class Ui_MainWindow(object):
    def __init__(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_label)
        self.time = QtCore.QTime(0, 0, 0)
        self.totalworkedtime = QtCore.QTime(0, 0, 0)
        self.Dialog2 = QtWidgets.QDialog()
        self.ui = EndDialog()
        self.ui.setupUi(self.Dialog2)
        #self.Dialog2.show()


    def getfullname():
        connection = sqlite3.connect("logindatabase.db")
        fullname = connection.execute("SELECT FULLNAME FROM USERS WHERE USERNAME = ? and PASSWORD = ?",(username,password))
        for row in fullname:
            return (row[0])
        connection.commit()

    def getworkrole(self):
        connection = sqlite3.connect("logindatabase.db")
        workrole = connection.execute("SELECT WORK FROM USERS WHERE USERNAME = ? and PASSWORD = ?",(username,password))
        self.workroleValue = workrole.fetchall()[0][0]
        #self.workroleValue = str(self.workroleValue)
        connection.commit()
        return self.workroleValue

    def comboBoxValues(self):
        self.getworkrole()
        connection = sqlite3.connect("logindatabase.db")
        options_list = []
        workroleValue = self.getworkrole()
        if self.workroleValue == "bodyshop":
            worktype = connection.execute("SELECT * FROM BODYSHOP")
            options_list = worktype.fetchall()
            connection.commit()
            self.combo_box_options = [x[0] for x in options_list]
            #print(self.combo_box_options)
        elif self.workroleValue == "locksmithshop":
            worktype = connection.execute("SELECT * FROM LOCKSMITHSHOP")
            options_list = worktype.fetchall()
            connection.commit()
            self.combo_box_options = [x[0] for x in options_list]
            #print(self.combo_box_options)
        elif self.workroleValue == "tuning":
            worktype = connection.execute("SELECT * FROM TUNING")
            options_list = worktype.fetchall()
            connection.commit()
            self.combo_box_options = [x[0] for x in options_list]
            #print(self.combo_box_options)
        else:
            self.combo_box_options = []
        
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(745, 503)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.comboBoxValues()
        
        #Logged as display
        self.loggedasLabel = QtWidgets.QLabel(self.centralwidget)
        self.loggedasLabel.setGeometry(QtCore.QRect(10, 10, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.loggedasLabel.setFont(font)
        self.loggedasLabel.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
        self.loggedasLabel.setObjectName("loggedasLabel")
        #Logged as end

        #login name start
        self.fullname = QtWidgets.QLabel(self.centralwidget)
        self.fullname.setGeometry(QtCore.QRect(140, 10, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        #displays login name
        self.fullname.setFont(font)
        self.fullname.setText(fullname)
        self.fullname.setObjectName("fullname")
        #login name end
        
        #logout button
        self.logoutbutton = QtWidgets.QPushButton(self.centralwidget)
        self.logoutbutton.setGeometry(QtCore.QRect(300, 10, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.logoutbutton.setFont(font)
        self.logoutbutton.setObjectName("logoutbutton")
        self.logoutbutton.clicked.connect(self.logout)
        #logout button end

        #display current date
        self.date = QtWidgets.QLabel(self.centralwidget)
        self.date.setGeometry(QtCore.QRect(10, 50, 50, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.date.setFont(font)
        self.date.setObjectName("date")
        self.dateActual = QtWidgets.QLabel(self.centralwidget)
        self.dateActual.setGeometry(QtCore.QRect(70, 50, 131, 21))
        self.dateActual.setObjectName("actualDate")
        date = str(datetime.date(datetime.now()))
        self.dateActual.setFont(font)
        self.dateActual.setText(date)
        #end date display

        #display table
        #combo_box_options = ["Option 1","Option 2","Option 3"]
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 90, 721, 161))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        #self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        #table end

        #add work button
        self.AddWork = QtWidgets.QPushButton(self.centralwidget)
        self.AddWork.setGeometry(QtCore.QRect(310, 270, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.AddWork.setFont(font)
        self.AddWork.setObjectName("AddWork")
        self.AddWork.clicked.connect(self.add_work)
        #add work end

        #timer start button
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(320, 360, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.start.setFont(font)
        self.start.setObjectName("start")
        self.start.clicked.connect(self.update_label)
        self.start.setEnabled(False)
        #timer start button end

        #pause button
        self.Pause = QtWidgets.QPushButton(self.centralwidget)
        self.Pause.setGeometry(QtCore.QRect(460, 360, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Pause.setFont(font)
        self.Pause.setObjectName("Pause")
        self.Pause.clicked.connect(self.stop_timer)
        self.Pause.setEnabled(False)
        #pause button end

        #Submit button
        self.EndSubmit = QtWidgets.QPushButton(self.centralwidget)
        self.EndSubmit.setGeometry(QtCore.QRect(270, 440, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.EndSubmit.setFont(font)
        self.EndSubmit.setObjectName("EndSubmit")
        self.EndSubmit.clicked.connect(self.submit)
        #submit button end

        #time elapsed label
        self.timeelapsedLabel = QtWidgets.QLabel(self.centralwidget)
        self.timeelapsedLabel.setGeometry(QtCore.QRect(10, 360, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.timeelapsedLabel.setFont(font)
        self.timeelapsedLabel.setObjectName("timeelapsedLabel")
        #time elapsed end

        #total time worked label
        self.totalWorkedLabel = QtWidgets.QLabel(self.centralwidget)
        self.totalWorkedLabel.setGeometry(QtCore.QRect(10, 410, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.totalWorkedLabel.setFont(font)
        self.totalWorkedLabel.setObjectName("totalWorkedLabel")
        #total time worked label end

        #total time worked actual number label
        self.totalWorkedLabelActual = QtWidgets.QLabel(self.centralwidget)
        self.totalWorkedLabelActual.setGeometry(QtCore.QRect(145, 422, 94, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.totalWorkedLabelActual.setFont(font)
        self.totalWorkedLabelActual.setObjectName("totalWorkedLabelActual")
        #total time worked actual number label end

        #finish button
        self.finish = QtWidgets.QPushButton(self.centralwidget)
        self.finish.setGeometry(QtCore.QRect(600, 360, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.finish.setFont(font)
        self.finish.setObjectName("finish")
        self.finish.clicked.connect(self.reset_timer)
        self.finish.setEnabled(False)
        #finish button end

        #timer label
        self.timerLabel = QtWidgets.QLabel(self.centralwidget)
        self.timerLabel.setGeometry(QtCore.QRect(150, 370, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.timerLabel.setFont(font)
        self.timerLabel.setObjectName("timerLabel")
        #timer label end
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loggedasLabel.setText(_translate("MainWindow", "Logged in as:"))
        self.logoutbutton.setText(_translate("MainWindow", "LogOut"))
        self.date.setText(_translate("MainWindow", "Date:"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Work type"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Work duration"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Order number"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", ""))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.AddWork.setText(_translate("MainWindow", "Add work"))
        self.start.setText(_translate("MainWindow", "Start"))
        self.Pause.setText(_translate("MainWindow", "Pause"))
        self.EndSubmit.setText(_translate("MainWindow", "End shift and submit"))
        self.timeelapsedLabel.setText(_translate("MainWindow", "Time elapsed:"))
        self.finish.setText(_translate("MainWindow", "Finish"))
        self.timerLabel.setText(_translate("MainWindow", "00:00:00"))
        self.totalWorkedLabel.setText(_translate("MainWindow", "Total worked:"))
        self.totalWorkedLabelActual.setText(_translate("MainWindow", "00:00:00"))

    def update_label(self):
        self.timer.start(1000)
        self.time = self.time.addSecs(1)
        self.Pause.setEnabled(True)
        self.finish.setEnabled(True)
        self.timerLabel.setText(self.time.toString("hh:mm:ss"))
        #print(self.timerLabel.text())
        self.counting = True
        if self.counting == True:
            self.Pause.setText("Pause")
        self.getworkrole()

    def stop_timer(self):
        self.timer.stop()
        if self.counting == True:
            self.Pause.setText("Resume")
        if self.counting == False:
            self.Pause.setText("Pause")
            self.update_label()
        self.counting = False

    def reset_timer(self):
        self.timer.stop()
        self.rowPosition = self.tableWidget.rowCount() - 1
        self.tableWidget.item(self.rowPosition, 1).setText(self.timerLabel.text())
        self.timerLabel.setText("00:00:00")
        self.total_worked()
        self.time = QtCore.QTime(0, 0, 0)
        self.Pause.setText("Pause")

    def total_worked(self):
        self.totalworkedtime = self.totalworkedtime.addSecs(self.time.second())
        self.totalworkedtime = self.totalworkedtime.addSecs(self.time.minute() * 60)
        self.totalworkedtime = self.totalworkedtime.addSecs(self.time.hour() * 3600)
        #print(self.totalworkedtime)
        self.totalWorkedLabelActual.setText(self.totalworkedtime.toString("hh:mm:ss"))


    def add_work(self):
        self.rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(self.rowPosition)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(self.rowPosition, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(self.rowPosition, 1, item)
        combo = QtWidgets.QComboBox()
        for t in self.combo_box_options:
            combo.addItem(t)
        self.tableWidget.setCellWidget(self.rowPosition,0,combo)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(self.rowPosition, 1, item)
        self.deleteButton = QtWidgets.QPushButton(self.tableWidget)
        self.tableWidget.setCellWidget(self.rowPosition, 3, self.deleteButton)
        self.deleteButton.setText("Delete")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.deleteButton.setFont(font)
        self.deleteButton.clicked.connect(self.removeRow)
        self.start.setEnabled(True)

    def add_delete_button(self):
        self.rowPosition = self.tableWidget.rowCount()
        self.buttonDelete = QtWidgets.QPushButton(self.centralwidget)
        self.buttonDelete.setGeometry(QtCore.QRect(310, 270, 125, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.buttonDelete.setFont(font)
        self.buttonDelete.setObjectName("DeleteButton")
        self.tableWidget.setCellWidget(self.rowPosition, 3, self.buttonDelete)
        
    def removeRow(self):
        self.tableWidget.removeRow(self.tableWidget.currentRow())

    def logout(self):
        sys.exit()

    def submit(self):
        self.Dialog2.show()

        

class EndDialog(object):
    
        
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(451, 200)
        self.topLabel = QtWidgets.QLabel(Dialog)
        self.topLabel.setGeometry(QtCore.QRect(90, 10, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.topLabel.setFont(font)
        self.topLabel.setLineWidth(1)
        self.topLabel.setMidLineWidth(0)
        self.topLabel.setTextFormat(QtCore.Qt.AutoText)
        self.topLabel.setScaledContents(False)
        self.topLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.topLabel.setWordWrap(True)
        self.topLabel.setObjectName("topLabel")

        #OK button
        self.ok = QtWidgets.QPushButton(Dialog)
        self.ok.setGeometry(QtCore.QRect(180, 120, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ok.setFont(font)
        self.ok.setObjectName("Pause")
        self.ok.clicked.connect(self.closeIt)
        #OK button end

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.topLabel.setText(_translate("Dialog", "Your work has been submitted! Thank you for using the program."))
        self.ok.setText(_translate("Dialog", "OK"))

        
    def closeIt(self): 
        sys.exit()
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
