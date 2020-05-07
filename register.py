# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import sqlite3
import cv2, sys, numpy, os
import hashlib


class Ui_MainWindow(object):
    def openWindow(self):
        self.ui = Ui_MainWindowLogin()
        self.ui.setupUi(MainWindow2)
        MainWindow.hide()
        MainWindow2.showMaximized()

    def save_data(self):
        print("I am inside save Data")
        name = self.lineEdit.text()
        email = self.lineEdit_2.text()
        contact = self.lineEdit_3.text()
        dob = self.dateEdit.text()
        aadhar = self.lineEdit_4.text()
        address = self.plainTextEdit.toPlainText()
        if len(aadhar) != 0 and ".com" in email and len(contact) != 0:
            conn = sqlite3.connect('db.db')
            conn.execute("INSERT INTO REGISTER (NAME,EMAIL,CONTACT,DOB,AADHAR,ADDRESS) VALUES (?,?,?,?,?,?)",
                         (name, email, str(contact), str(dob), str(aadhar), address))
            ran = numpy.random.random_integers(100,25000)
            os.mkdir('datasets/' + str(ran))

            haar_file = 'haarcascade_frontalface_default.xml'

            # All the faces data will be
            #  present this folder
            datasets = 'datasets'

            # These are sub data sets of folder,
            # for my faces I've used my name you can
            # change the label here
            sub_data = str(ran)

            path = os.path.join(datasets, sub_data)
            if not os.path.isdir(path):
                os.mkdir(path)

            # defining the size of images
            (width, height) = (130, 100)

            # '0' is used for my webcam,
            # if you've any other camera
            #  attached use '1' like this
            face_cascade = cv2.CascadeClassifier(haar_file)
            webcam = cv2.VideoCapture(0)

            # The program loops until it has 30 images of the face.
            count = 1
            while count < 30:
                (_, im) = webcam.read()
                gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.3, 4)
                for (x, y, w, h) in faces:
                    cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    face = gray[y:y + h, x:x + w]
                    face_resize = cv2.resize(face, (width, height))
                    cv2.imwrite('% s/% s.png' % (path, count), face_resize)
                count += 1

                cv2.imshow('OpenCV', im)
                key = cv2.waitKey(10)
                if key == 27:
                    break
            webcam.release()
            conn.commit()
            conn.close()
            QtWidgets.QMessageBox.information(MainWindow, "Message", "Voter Created Successfully")
            self.openWindow()
        else:
            QtWidgets.QMessageBox.information(MainWindow, "Message", "Please Fill All Values")

    def save_images(self):
        haar_file = 'haarcascade_frontalface_default.xml'

        # All the faces data will be
        #  present this folder
        datasets = 'datasets'

        # These are sub data sets of folder,
        # for my faces I've used my name you can
        # change the label here
        sub_data = 'vivek'

        path = os.path.join(datasets, sub_data)
        if not os.path.isdir(path):
            os.mkdir(path)

            # defining the size of images
        (width, height) = (130, 100)

        # '0' is used for my webcam,
        # if you've any other camera
        #  attached use '1' like this
        face_cascade = cv2.CascadeClassifier(haar_file)
        webcam = cv2.VideoCapture(0)

        # The program loops until it has 30 images of the face.
        count = 1
        while count < 30:
            (_, im) = webcam.read()
            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 4)
            for (x, y, w, h) in faces:
                cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
                face = gray[y:y + h, x:x + w]
                face_resize = cv2.resize(face, (width, height))
                cv2.imwrite('% s/% s.png' % (path, count), face_resize)
            count += 1

            cv2.imshow('OpenCV', im)
            key = cv2.waitKey(10)
            if key == 27:
                break

    def clear(self):
        name = self.lineEdit.clear()
        email = self.lineEdit_2.clear()
        contact = self.lineEdit_3.clear()
        dob = self.dateEdit.clear()
        aadhar = self.lineEdit_4.clear()
        address = self.plainTextEdit.clear()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1360, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1361, 61))
        font = QtGui.QFont()
        font.setFamily("Monaco")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(17, 168, 198);\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(410, 90, 551, 611))
        self.frame.setStyleSheet("background-color: rgb(211, 220, 207);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(86, 52, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(180, 40, 271, 51))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(3, 3, 3);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 110, 271, 51))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(3, 3, 3);")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(86, 122, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 190, 271, 51))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(3, 3, 3);")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(76, 202, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(76, 282, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.dateEdit = QtWidgets.QDateEdit(self.frame)
        self.dateEdit.setGeometry(QtCore.QRect(180, 270, 271, 61))
        self.dateEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(3, 3, 3);")
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(184, 360, 271, 51))
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(3, 3, 3);")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(80, 372, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(80, 442, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.frame)
        self.plainTextEdit.setGeometry(QtCore.QRect(190, 440, 261, 71))
        self.plainTextEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(3, 3, 3);")
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(190, 530, 121, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.save_data)

        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 530, 111, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.openWindow)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1360, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Register"))
        self.label_2.setText(_translate("MainWindow", "Name: "))
        self.label_3.setText(_translate("MainWindow", "Email: "))
        self.label_4.setText(_translate("MainWindow", "Contact No.: "))
        self.label_5.setText(_translate("MainWindow", "D.O.B : "))
        self.label_6.setText(_translate("MainWindow", "Aadhar No.: "))
        self.label_12.setText(_translate("MainWindow", "Address: "))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.pushButton_2.setText(_translate("MainWindow", "Login"))


class Ui_MainWindowLogin(object):
    def openWindow(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        MainWindow2.hide()
        MainWindow.showMaximized()

    def openWindow2(self):
        self.ui = Ui_MainWindowVote()
        self.ui.setupUi(MainWindow3)
        MainWindow2.hide()
        MainWindow3.showMaximized()



    def authenticate_aadhar(self):
        print("I am inside aadhar authentication")
        self.lineEdit.setVisible(True)
        self.pushButton_3.setVisible(True)
        self.pushButton.setVisible(True)
        self.pushButton_2.setVisible(True)

    def check(self):
        aadhar_list = []
        name_list = []
        aadhar = self.lineEdit.text()
        print("I am inside check")
        conn = sqlite3.connect('db.db')
        data = conn.execute('''Select * from Register''')
        for row in data:
            aadhar_list.append(row[5])
            name_list.append(row[1])

        if aadhar in aadhar_list:
            self.openWindow2()

        else:
            QtWidgets.QMessageBox.information(MainWindow, "Message", "No Records Found")


    def open_camera(self):
        capture = cv2.VideoCapture(0)

        while (True):

            ret, frame = capture.read()

            cv2.imshow('video', frame)

            if cv2.waitKey(1) == 27:
                break

        capture.release()
        cv2.destroyAllWindows()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1360, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(410, 90, 551, 300))
        self.frame.setStyleSheet("background-color: rgb(211, 220, 207);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")


        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(140, 80, 300, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.authenticate_aadhar)
        self.pushButton.setStyleSheet("background-color: rgb(17, 168, 198);\n"
                                 "color: rgb(255, 255, 255);")

        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 150, 300, 41))
        self.pushButton_2.setObjectName("pushButton")
        self.pushButton_2.clicked.connect(self.openWindow)
        self.pushButton_2.setStyleSheet("background-color: rgb(17, 168, 198);\n"
                                      "color: rgb(255, 255, 255);")
        self.pushButton_2.setText("Register")

        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(140, 80, 300, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText('Enter Aadhar Number')
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "color: rgb(0, 0, 0);")
        self.lineEdit.setVisible(False)
        self.lineEdit.returnPressed.connect(self.check)


        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 150, 300, 41))
        self.pushButton_3.setObjectName("pushButton")
        self.pushButton_3.setStyleSheet("background-color: rgb(17, 168, 198);\n"
                                        "color: rgb(255, 255, 255);")
        self.pushButton_3.setText("Submit Aadhar")
        self.pushButton_3.setVisible(False)
        self.pushButton_3.clicked.connect(self.check)


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1361, 61))
        font = QtGui.QFont()
        font.setFamily("Monaco")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(17, 168, 198);\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1360, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.pushButton.setText(_translate("MainWindow", "Login"))
        self.label.setText(_translate("MainWindow", "Login"))


class Ui_MainWindowVote(object):
    def openWindow(self):
        self.ui = Ui_MainWindowLogin()
        self.ui.setupUi(MainWindow)
        MainWindow3.hide()
        MainWindow.showMaximized()

    def authenticate_aadhar(self):
        print("I am inside aadhar authentication")
        self.lineEdit.setVisible(True)
        self.pushButton_3.setVisible(True)
        self.pushButton.setVisible(True)
        self.pushButton_2.setVisible(True)

    def check(self):
        aadhar_list = []
        name_list = []
        print("I am inside check")
        conn = sqlite3.connect('db.db')
        data = conn.execute('''Select * from Register''')
        for row in data:
            aadhar_list.append(row[5])
            name_list.append(row[1])

        print(aadhar_list)
        print(name_list)


    def vote(self):
        conn = sqlite3.connect("db.db")
        cursor = conn.execute("SELECT ID, HASHBLOCK FROM VOTETABLE")
        conn.commit()
        for row in cursor:
            id = row[0]
            previous_block = row[1]

        # Creating new block and hashing it
        hash_block = str(previous_block) + str(id + 1)
        hash_object = hashlib.md5(hash_block.encode()).hexdigest()

        conn = sqlite3.connect("db.db")

        # Storing new block
        conn.execute("INSERT INTO VOTETABLE (HASHBLOCK,PREVIOUSBLOCK,VOTE,AADHAR) VALUES (?,?,?,?)",
            (str(hash_object), str(previous_block), self.comboBox.currentIndex(), "123456789"))
        conn.commit()
        self.openWindow()
        QtWidgets.QMessageBox.information(MainWindow, "Message", "Vote Casted")



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1360, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(410, 90, 551, 300))
        self.frame.setStyleSheet("background-color: rgb(211, 220, 207);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")


        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(140, 80, 300, 41))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setStyleSheet("background-color: rgb(17, 168, 198);\n"
                                 "color: rgb(255, 255, 255);")
        self.comboBox.addItem('Candidate 1')
        self.comboBox.addItem('Candidate 2')
        self.comboBox.addItem('Candidate 3')
        self.comboBox.addItem('Candidate 4')




        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 150, 300, 41))
        self.pushButton_2.setObjectName("pushButton")
        self.pushButton_2.clicked.connect(self.vote)
        self.pushButton_2.setStyleSheet("background-color: rgb(17, 168, 198);\n"
                                      "color: rgb(255, 255, 255);")
        self.pushButton_2.setText("Submit")




        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1361, 61))
        font = QtGui.QFont()
        font.setFamily("Monaco")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(17, 168, 198);\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1360, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Caste Vote"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow2 = QtWidgets.QMainWindow()
    MainWindow3 = QtWidgets.QMainWindow()



    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    sys.exit(app.exec_())

