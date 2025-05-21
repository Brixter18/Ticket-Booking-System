
from PyQt6 import QtWidgets, QtCore

class Ui_ReceiptWindow(object):
    def setupUi(self, ReceiptWindow):
        ReceiptWindow.setObjectName("ReceiptWindow")
        ReceiptWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(parent=ReceiptWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.titleLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(100, 20, 200, 30))
        self.titleLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")

        self.txtMovie = QtWidgets.QLabel(parent=self.centralwidget)
        self.txtMovie.setGeometry(QtCore.QRect(50, 70, 300, 20))
        self.txtMovie.setObjectName("txtMovie")

        self.txtSchedule = QtWidgets.QLabel(parent=self.centralwidget)
        self.txtSchedule.setGeometry(QtCore.QRect(50, 100, 300, 20))
        self.txtSchedule.setObjectName("txtSchedule")

        self.txtSeats = QtWidgets.QLabel(parent=self.centralwidget)
        self.txtSeats.setGeometry(QtCore.QRect(50, 130, 300, 20))
        self.txtSeats.setObjectName("txtSeats")

        self.txtTotal = QtWidgets.QLabel(parent=self.centralwidget)
        self.txtTotal.setGeometry(QtCore.QRect(50, 160, 300, 20))
        self.txtTotal.setObjectName("txtTotal")

        self.closeButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.closeButton.setGeometry(QtCore.QRect(150, 220, 100, 30))
        self.closeButton.setText("Close")
        self.closeButton.setObjectName("closeButton")

        ReceiptWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(ReceiptWindow)
        QtCore.QMetaObject.connectSlotsByName(ReceiptWindow)

    def retranslateUi(self, ReceiptWindow):
        _translate = QtCore.QCoreApplication.translate
        ReceiptWindow.setWindowTitle(_translate("ReceiptWindow", "Receipt"))
        self.titleLabel.setText(_translate("ReceiptWindow", "<b>BOOKING RECEIPT</b>"))
        self.txtMovie.setText(_translate("ReceiptWindow", "Movie:"))
        self.txtSchedule.setText(_translate("ReceiptWindow", "Schedule:"))
        self.txtSeats.setText(_translate("ReceiptWindow", "Seats:"))
        self.txtTotal.setText(_translate("ReceiptWindow", "Total:"))
