import sys
import mysql.connector
from mysql.connector import Error
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit

from register_and_login import Ui_MainWindow as HomeUI
from login_screen import Ui_MainWindow as LoginUI
from register_screen import Ui_MainWindow as RegisterUI
from movies import NowShowingScreen, Movie1Window, Movie2Window, Movie3Window
from seatplan_screen import SeatPlanScreen
from receipt_screen import Ui_ReceiptWindow as ReceiptUI
from edit_info_screen import Ui_EditInfoWindow

class EditInfoWindow(QMainWindow):
    def __init__(self, username, email, db_cursor, db_connection):
        super().__init__()
        self.ui = Ui_EditInfoWindow()
        self.ui.setupUi(self)
        self.db_cursor = db_cursor
        self.db = db_connection
        self.original_username = username

        # Prefill fields
        self.ui.lineEdit_username.setText(username)
        self.ui.lineEdit_email.setText(email)

        self.ui.btnSave.clicked.connect(self.save_info)
        self.ui.btnCancel.clicked.connect(self.close)

    def save_info(self):
        new_username = self.ui.lineEdit_username.text().strip()
        new_email = self.ui.lineEdit_email.text().strip()
        old_password = self.ui.lineEdit_old_password.text()
        new_password = self.ui.lineEdit_new_password.text()
        confirm_password = self.ui.lineEdit_confirm_password.text()

        if not new_username:
            QMessageBox.warning(self, "Input Error", "Username cannot be empty.")
            return

        if any([old_password, new_password, confirm_password]):
            if not old_password:
                QMessageBox.warning(self, "Input Error", "Please enter your old password to change password.")
                return
            self.db_cursor.execute("SELECT password FROM users WHERE username = %s", (self.original_username,))
            result = self.db_cursor.fetchone()
            if not result or result[0] != old_password:
                QMessageBox.warning(self, "Password Error", "Old password is incorrect.")
                return
            if new_password != confirm_password:
                QMessageBox.warning(self, "Password Error", "New password and confirmation do not match.")
                return
        else:
            new_password = None

        try:
            if new_password:
                self.db_cursor.execute(
                    "UPDATE users SET username = %s, email = %s, password = %s WHERE username = %s",
                    (new_username, new_email, new_password, self.original_username)
                )
            else:
                self.db_cursor.execute(
                    "UPDATE users SET username = %s, email = %s WHERE username = %s",
                    (new_username, new_email, self.original_username)
                )
            self.db.commit()
            QMessageBox.information(self, "Success", "Information updated.")
            self.close()
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Error", str(e))


class MainApp:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.current_user = None

        try:
            self.db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="ticket_universe"
            )
            self.cursor = self.db.cursor()
            print("✅ Connected to MySQL")
        except Error as e:
            print("❌ Database connection failed:", e)
            QMessageBox.critical(None, "Database Error", str(e))
            sys.exit()

        self.setup_home()
        self.setup_login()
        self.setup_register()
        self.setup_now_showing()

        self.home_window.show()
        sys.exit(self.app.exec())

    def setup_home(self):
        self.home_window = QMainWindow()
        self.home_ui = HomeUI()
        self.home_ui.setupUi(self.home_window)
        self.home_ui.pushButton_2.clicked.connect(self.show_register_screen)
        self.home_ui.pushButton_3.clicked.connect(self.show_login_screen)

    def setup_login(self):
        self.login_window = QMainWindow()
        self.login_ui = LoginUI()
        self.login_ui.setupUi(self.login_window)
        self.login_ui.textEdit_2.setEchoMode(QLineEdit.EchoMode.Password)
        self.login_ui.pushButton.clicked.connect(self.login_user)
        if hasattr(self.login_ui, "backButton"):
            self.login_ui.backButton.clicked.connect(self.back_to_home)

    def setup_register(self):
        self.register_window = QMainWindow()
        self.register_ui = RegisterUI()
        self.register_ui.setupUi(self.register_window)
        self.register_ui.textEdit_2.setEchoMode(QLineEdit.EchoMode.Password)
        self.register_ui.pushButton.clicked.connect(self.register_user)
        if hasattr(self.register_ui, "backButton"):
            self.register_ui.backButton.clicked.connect(self.back_to_home)

    def setup_now_showing(self):
        self.now_showing_window = NowShowingScreen()
        self.now_showing_window.ui.btnLogout.clicked.connect(self.logout)
        self.now_showing_window.ui.btnReserveMovie1.clicked.connect(lambda: self.open_movie_window(1))
        self.now_showing_window.ui.btnReserveMovie2.clicked.connect(lambda: self.open_movie_window(2))
        self.now_showing_window.ui.btnReserveMovie3.clicked.connect(lambda: self.open_movie_window(3))
        if hasattr(self.now_showing_window.ui, "btnEditInfo"):
            self.now_showing_window.ui.btnEditInfo.clicked.connect(self.open_edit_info_window)

    def back_to_home(self):
        self.login_window.close()
        self.register_window.close()
        self.home_window.show()

    def show_login_screen(self):
        self.login_window.show()
        self.home_window.close()

    def show_register_screen(self):
        self.register_window.show()
        self.home_window.close()

    def register_user(self):
        username = self.register_ui.textEdit.text().strip()
        email = self.register_ui.textEdit_3.text().strip()
        password = self.register_ui.textEdit_2.text().strip()

        if not username or not password:
            QMessageBox.warning(self.register_window, "Input Error", "Username and Password are required.")
            return

        try:
            self.cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
                                (username, email, password))
            self.db.commit()
            QMessageBox.information(self.register_window, "Success", "Registration successful!")
            self.register_window.close()
            self.login_window.show()
        except mysql.connector.errors.IntegrityError:
            QMessageBox.warning(self.register_window, "Error", "Username already exists. Try another one.")

    def login_user(self):
        username = self.login_ui.textEdit.text().strip()
        password = self.login_ui.textEdit_2.text().strip()

        self.cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        result = self.cursor.fetchone()

        if result:
            self.current_user = username
            QMessageBox.information(self.login_window, "Login Success", f"Welcome, {username}!")
            self.login_window.close()
            self.now_showing_window.show()
        else:
            QMessageBox.warning(self.login_window, "Login Failed", "Invalid username or password.")

    def logout(self):
        self.current_user = None
        self.now_showing_window.close()
        self.home_window.show()

    def open_movie_window(self, movie_number):
        if movie_number == 1:
            self.active_movie_window = Movie1Window(self.now_showing_window)
            self.active_movie_title = "Seat at the Sea"
        elif movie_number == 2:
            self.active_movie_window = Movie2Window(self.now_showing_window)
            self.active_movie_title = "Call Me"
        elif movie_number == 3:
            self.active_movie_window = Movie3Window(self.now_showing_window)
            self.active_movie_title = "Swagapino"
        else:
            return

        self.active_movie_price = 300
        self.active_movie_window.ui.pushButton.clicked.connect(lambda: self.prepare_seat_selection(movie_number))
        self.active_movie_window.ui.pushButton_6.clicked.connect(self.active_movie_window.close)
        self.active_movie_window.show()
        self.now_showing_window.hide()

    def prepare_seat_selection(self, movie_number):
        ui = self.active_movie_window.ui
        schedule = None
        if hasattr(ui, 'checkBox') and ui.checkBox.isChecked():
            schedule = ui.checkBox.text().strip().split()
        elif hasattr(ui, 'checkBox_2') and ui.checkBox_2.isChecked():
            schedule = ui.checkBox_2.text().strip().split()

        if not schedule or len(schedule) < 4:
            QMessageBox.warning(self.active_movie_window, "No Schedule", "Please select a schedule.")
            return

        start_time, end_time, date = schedule[0], schedule[2], schedule[3]

        # Fixed: pass username argument as required by SeatPlanScreen
        self.seatplan_window = SeatPlanScreen(username=self.current_user)
        self.seatplan_window.movie_title = self.active_movie_title
        self.seatplan_window.movie_price = self.active_movie_price
        self.seatplan_window.schedule = (start_time, end_time, date)

        self.seatplan_window.btnConfirm.clicked.connect(self.finalize_booking)
        self.seatplan_window.show()
        self.active_movie_window.close()

    def finalize_booking(self):
        seats = self.seatplan_window.selected_seats
        movie = self.seatplan_window.movie_title
        start, end, date = self.seatplan_window.schedule
        price = self.seatplan_window.movie_price

        if not seats:
            QMessageBox.warning(self.seatplan_window, "No Seats", "Please select at least one seat.")
            return

        for seat in seats:
            self.cursor.execute(
                "SELECT * FROM bookings WHERE movie_title = %s AND seat_number = %s",
                (movie, seat)
            )
            if not self.cursor.fetchone():
                self.cursor.execute(
                    "INSERT INTO bookings (username, movie_title, seat_number) VALUES (%s, %s, %s)",
                    (self.current_user, movie, seat)
                )
        self.db.commit()

        self.receipt_window = QMainWindow()
        self.receipt_ui = ReceiptUI()
        self.receipt_ui.setupUi(self.receipt_window)

        self.receipt_ui.txtMovie.setText(f"Movie: {movie}")
        self.receipt_ui.txtSchedule.setText(f"Schedule: {start} - {end} on {date}")
        self.receipt_ui.txtSeats.setText("Seats: " + ", ".join(seats))
        self.receipt_ui.txtTotal.setText(f"Total: ₱{price * len(seats)}.00")
        self.receipt_ui.closeButton.clicked.connect(self.receipt_window.close)

        self.receipt_window.show()
        self.seatplan_window.close()

    def open_edit_info_window(self):
        if not self.current_user:
            QMessageBox.warning(None, "Error", "No user logged in.")
            return

        self.cursor.execute("SELECT email FROM users WHERE username = %s", (self.current_user,))
        email_result = self.cursor.fetchone()
        current_email = email_result[0] if email_result else ""

        self.edit_info_window = EditInfoWindow(self.current_user, current_email, self.cursor, self.db)
        self.edit_info_window.show()


if __name__ == "__main__":
    MainApp()
