from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_NowShowingScreen(object):
    def setupUi(self, NowShowingScreen):
        NowShowingScreen.setObjectName("NowShowingScreen")
        NowShowingScreen.resize(631, 512)
        self.centralwidget = QtWidgets.QWidget(parent=NowShowingScreen)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 50, 151, 31))
        self.label.setObjectName("label")

        self.movie1 = QtWidgets.QFrame(parent=self.centralwidget)
        self.movie1.setGeometry(QtCore.QRect(20, 120, 171, 271))
        self.movie1.setAutoFillBackground(True)
        self.movie1.setObjectName("movie1")

        self.btnReserveMovie1 = QtWidgets.QPushButton(parent=self.movie1)
        self.btnReserveMovie1.setGeometry(QtCore.QRect(30, 230, 111, 24))
        self.btnReserveMovie1.setObjectName("btnReserveMovie1")

        self.label_2 = QtWidgets.QLabel(parent=self.movie1)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 151, 181))
        self.label_2.setPixmap(QtGui.QPixmap("image/logo.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(parent=self.movie1)
        self.label_3.setGeometry(QtCore.QRect(40, 10, 91, 16))
        self.label_3.setObjectName("label_3")

        self.movie2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.movie2.setGeometry(QtCore.QRect(230, 120, 171, 271))
        self.movie2.setAutoFillBackground(True)
        self.movie2.setObjectName("movie2")

        self.btnReserveMovie2 = QtWidgets.QPushButton(parent=self.movie2)
        self.btnReserveMovie2.setGeometry(QtCore.QRect(30, 230, 111, 24))
        self.btnReserveMovie2.setObjectName("btnReserveMovie2")

        self.label_4 = QtWidgets.QLabel(parent=self.movie2)
        self.label_4.setGeometry(QtCore.QRect(10, 40, 151, 181))
        self.label_4.setPixmap(QtGui.QPixmap("image/uhuh.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(parent=self.movie2)
        self.label_5.setGeometry(QtCore.QRect(60, 10, 51, 16))
        self.label_5.setObjectName("label_5")

        self.movie3 = QtWidgets.QFrame(parent=self.centralwidget)
        self.movie3.setGeometry(QtCore.QRect(440, 120, 171, 271))
        self.movie3.setAutoFillBackground(True)
        self.movie3.setObjectName("movie3")

        self.btnReserveMovie3 = QtWidgets.QPushButton(parent=self.movie3)
        self.btnReserveMovie3.setGeometry(QtCore.QRect(30, 230, 111, 24))
        self.btnReserveMovie3.setObjectName("btnReserveMovie3")

        self.label_6 = QtWidgets.QLabel(parent=self.movie3)
        self.label_6.setGeometry(QtCore.QRect(10, 40, 151, 181))
        self.label_6.setPixmap(QtGui.QPixmap("image/yes.jpg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(parent=self.movie3)
        self.label_7.setGeometry(QtCore.QRect(50, 10, 71, 16))
        self.label_7.setObjectName("label_7")

        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 631, 31))
        self.frame.setAutoFillBackground(True)
        self.frame.setObjectName("frame")

        self.btnLogout = QtWidgets.QPushButton(parent=self.frame)
        self.btnLogout.setGeometry(QtCore.QRect(560, 0, 75, 31))
        self.btnLogout.setObjectName("btnLogout")

        self.pushButton_5 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 0, 75, 31))
        self.pushButton_5.setObjectName("pushButton_5")

        # THIS IS THE MISSING EDIT INFO BUTTON
        self.btnEditInfo = QtWidgets.QPushButton(parent=self.frame)
        self.btnEditInfo.setGeometry(QtCore.QRect(270, 0, 81, 31))
        self.btnEditInfo.setObjectName("btnEditInfo")

        NowShowingScreen.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=NowShowingScreen)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 631, 22))
        NowShowingScreen.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(parent=NowShowingScreen)
        NowShowingScreen.setStatusBar(self.statusbar)

        self.retranslateUi(NowShowingScreen)
        QtCore.QMetaObject.connectSlotsByName(NowShowingScreen)

    def retranslateUi(self, NowShowingScreen):
        _translate = QtCore.QCoreApplication.translate
        NowShowingScreen.setWindowTitle(_translate("NowShowingScreen", "MainWindow"))
        self.label.setText(_translate("NowShowingScreen", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">NOW SHOWING</span></p></body></html>"))
        self.btnReserveMovie1.setText(_translate("NowShowingScreen", "RESERVE TICKETS"))
        self.label_3.setText(_translate("NowShowingScreen", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">seat at the sea</span></p></body></html>"))
        self.btnReserveMovie2.setText(_translate("NowShowingScreen", "RESERVE TICKETS"))
        self.label_5.setText(_translate("NowShowingScreen", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">call me</span></p></body></html>"))
        self.btnReserveMovie3.setText(_translate("NowShowingScreen", "RESERVE TICKETS"))
        self.label_7.setText(_translate("NowShowingScreen", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">swagapino</span></p></body></html>"))
        self.btnLogout.setText(_translate("NowShowingScreen", "Logout"))
        self.pushButton_5.setText(_translate("NowShowingScreen", "Home"))
        self.btnEditInfo.setText(_translate("NowShowingScreen", "EDIT INFO"))
