from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_EditInfoWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 350)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        # Username
        self.label_username = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_username.setObjectName("label_username")
        self.verticalLayout.addWidget(self.label_username)

        self.lineEdit_username = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.verticalLayout.addWidget(self.lineEdit_username)

        # Email
        self.label_email = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_email.setObjectName("label_email")
        self.verticalLayout.addWidget(self.label_email)

        self.lineEdit_email = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.verticalLayout.addWidget(self.lineEdit_email)

        # Old Password
        self.label_old_password = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_old_password.setObjectName("label_old_password")
        self.verticalLayout.addWidget(self.label_old_password)

        self.lineEdit_old_password = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_old_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_old_password.setObjectName("lineEdit_old_password")
        self.verticalLayout.addWidget(self.lineEdit_old_password)

        # New Password
        self.label_new_password = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_new_password.setObjectName("label_new_password")
        self.verticalLayout.addWidget(self.label_new_password)

        self.lineEdit_new_password = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_new_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_new_password.setObjectName("lineEdit_new_password")
        self.verticalLayout.addWidget(self.lineEdit_new_password)

        # Confirm Password
        self.label_confirm_password = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_confirm_password.setObjectName("label_confirm_password")
        self.verticalLayout.addWidget(self.label_confirm_password)

        self.lineEdit_confirm_password = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_confirm_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_confirm_password.setObjectName("lineEdit_confirm_password")
        self.verticalLayout.addWidget(self.lineEdit_confirm_password)

        # Buttons layout
        self.buttonLayout = QtWidgets.QHBoxLayout()
        self.buttonLayout.setObjectName("buttonLayout")

        self.btnSave = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnSave.setObjectName("btnSave")
        self.buttonLayout.addWidget(self.btnSave)

        self.btnCancel = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnCancel.setObjectName("btnCancel")
        self.buttonLayout.addWidget(self.btnCancel)

        self.verticalLayout.addLayout(self.buttonLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Edit Info"))
        self.label_username.setText(_translate("MainWindow", "Username:"))
        self.label_email.setText(_translate("MainWindow", "Email:"))
        self.label_old_password.setText(_translate("MainWindow", "Old Password:"))
        self.label_new_password.setText(_translate("MainWindow", "New Password:"))
        self.label_confirm_password.setText(_translate("MainWindow", "Confirm New Password:"))
        self.btnSave.setText(_translate("MainWindow", "Save"))
        self.btnCancel.setText(_translate("MainWindow", "Cancel"))
