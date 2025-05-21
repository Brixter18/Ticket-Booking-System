import sys
from PyQt6.QtWidgets import QApplication, QMainWindow

from now_showing_screen import Ui_NowShowingScreen
from movie1 import Ui_Movie1
from movie2 import Ui_Movie2
from movie3 import Ui_Movie3


class NowShowingScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_NowShowingScreen()
        self.ui.setupUi(self)

        # Connect RESERVE buttons
        self.ui.btnReserveMovie1.clicked.connect(self.open_movie1)
        self.ui.btnReserveMovie2.clicked.connect(self.open_movie2)
        self.ui.btnReserveMovie3.clicked.connect(self.open_movie3)

    def open_movie1(self):
        self.movie1_window = Movie1Window(self)
        self.movie1_window.show()
        self.hide()

    def open_movie2(self):
        self.movie2_window = Movie2Window(self)
        self.movie2_window.show()
        self.hide()

    def open_movie3(self):
        self.movie3_window = Movie3Window(self)
        self.movie3_window.show()
        self.hide()


class Movie1Window(QMainWindow):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = Ui_Movie1()
        self.ui.setupUi(self)

        # Connect Back button
        self.ui.pushButton_6.clicked.connect(self.go_back)

    def go_back(self):
        self.close()
        self.parent.show()


class Movie2Window(QMainWindow):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = Ui_Movie2()
        self.ui.setupUi(self)

        # Connect Back button
        self.ui.pushButton_6.clicked.connect(self.go_back)

    def go_back(self):
        self.close()
        self.parent.show()


class Movie3Window(QMainWindow):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = Ui_Movie3()
        self.ui.setupUi(self)

        # Connect Back button
        self.ui.pushButton_6.clicked.connect(self.go_back)

    def go_back(self):
        self.close()
        self.parent.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NowShowingScreen()
    window.show()
    sys.exit(app.exec())