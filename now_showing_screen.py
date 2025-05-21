from PyQt6 import QtWidgets
from now_showing_screen_ui import Ui_NowShowingScreen

class NowShowingScreen(QtWidgets.QMainWindow):
    def __init__(self, username=None):
        super().__init__()
        self.ui = Ui_NowShowingScreen()
        self.ui.setupUi(self)

        self.username = username  # store username for later use if needed

        # Example: you can now access self.username anywhere in this class
        # For example, if you want to display the username somewhere, you can add it here
        # self.ui.someLabel.setText(f"Welcome, {self.username}")

# If you want to test this file directly, you can add:
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = NowShowingScreen("test_user")
    window.show()
    sys.exit(app.exec())
