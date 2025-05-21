from PyQt6 import QtWidgets, uic
import mysql.connector

class SeatPlanScreen(QtWidgets.QMainWindow):
    def __init__(self, username):
        super().__init__()
        uic.loadUi("seatplan_screen.ui", self)

        self.username = username
        self.selected_seats = []
        self.cancel_mode = False

        self.seat_buttons = {
            'A1': self.findChild(QtWidgets.QPushButton, "btnA1"),
            'A2': self.findChild(QtWidgets.QPushButton, "btnA2"),
            'A3': self.findChild(QtWidgets.QPushButton, "btnA3"),
            'A4': self.findChild(QtWidgets.QPushButton, "btnA4"),
            'A5': self.findChild(QtWidgets.QPushButton, "btnA5"),
            'B1': self.findChild(QtWidgets.QPushButton, "btnB1"),
            'B2': self.findChild(QtWidgets.QPushButton, "btnB2"),
            'B3': self.findChild(QtWidgets.QPushButton, "btnB3"),
            'B4': self.findChild(QtWidgets.QPushButton, "btnB4"),
            'B5': self.findChild(QtWidgets.QPushButton, "btnB5"),
            'C1': self.findChild(QtWidgets.QPushButton, "btnC1"),
            'C2': self.findChild(QtWidgets.QPushButton, "btnC2"),
            'C3': self.findChild(QtWidgets.QPushButton, "btnC3"),
            'C4': self.findChild(QtWidgets.QPushButton, "btnC4"),
            'C5': self.findChild(QtWidgets.QPushButton, "btnC5"),
        }

        for seat_name, btn in self.seat_buttons.items():
            if btn:
                btn.setCheckable(True)
                btn.toggled.connect(lambda checked, s=seat_name: self.on_seat_toggled(s, checked))

        if hasattr(self, "btnConfirm") and self.btnConfirm:
            self.btnConfirm.clicked.connect(self.confirm_selection)
        if hasattr(self, "pushButton_6") and self.pushButton_6:
            self.pushButton_6.clicked.connect(self.go_back)
        if hasattr(self, "pushButton_5") and self.pushButton_5:
            self.pushButton_5.clicked.connect(self.go_home)
        if hasattr(self, "btnCancel") and self.btnCancel:
            self.btnCancel.clicked.connect(self.toggle_cancel_mode)

        self.setup_database()
        self.load_booked_seats()

    def setup_database(self):
        try:
            self.db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="ticket_universe"
            )
            self.cursor = self.db.cursor()
        except mysql.connector.Error as err:
            QtWidgets.QMessageBox.critical(self, "Database Error", f"Failed to connect:\n{err}")
            self.close()

    def load_booked_seats(self):
        try:
            self.cursor.execute("SELECT seat_number, username FROM bookings")
            all_bookings = self.cursor.fetchall()

            for seat_name, btn in self.seat_buttons.items():
                if btn:
                    btn.setEnabled(True)
                    btn.setStyleSheet("")
                    btn.setChecked(False)

            for seat, booked_by in all_bookings:
                if seat in self.seat_buttons:
                    btn = self.seat_buttons[seat]
                    if btn:
                        if booked_by == self.username:
                            btn.setEnabled(False)
                            btn.setStyleSheet("background-color: red")
                        else:
                            btn.setEnabled(False)
                            btn.setStyleSheet("background-color: darkred")
        except mysql.connector.Error as err:
            QtWidgets.QMessageBox.warning(self, "Warning", f"Failed to load booked seats:\n{err}")

    def on_seat_toggled(self, seat_name, checked):
        if checked:
            if seat_name not in self.selected_seats:
                self.selected_seats.append(seat_name)
        else:
            if seat_name in self.selected_seats:
                self.selected_seats.remove(seat_name)

    def confirm_selection(self):
        if self.cancel_mode:
            if not self.selected_seats:
                QtWidgets.QMessageBox.warning(self, "No Selection", "Please select your booked seats to cancel.")
                return
            try:
                for seat in self.selected_seats:
                    self.cursor.execute(
                        "DELETE FROM bookings WHERE seat_number = %s AND username = %s",
                        (seat, self.username)
                    )
                self.db.commit()
            except mysql.connector.Error as err:
                QtWidgets.QMessageBox.critical(self, "Database Error", f"Failed to cancel booking:\n{err}")
                return
            QtWidgets.QMessageBox.information(self, "Cancelled", "Your bookings have been cancelled.")
            self.selected_seats.clear()
            self.cancel_mode = False
            self.btnCancel.setText("Cancel Booking")
            self.btnConfirm.setText("Confirm")
            self.load_booked_seats()
        else:
            if not self.selected_seats:
                QtWidgets.QMessageBox.warning(self, "No Selection", "Please select at least one seat.")
                return
            try:
                for seat in self.selected_seats:
                    self.cursor.execute(
                        "INSERT INTO bookings (seat_number, username) VALUES (%s, %s)",
                        (seat, self.username)
                    )
                self.db.commit()
            except mysql.connector.Error as err:
                QtWidgets.QMessageBox.critical(self, "Database Error", f"Failed to save:\n{err}")
                return
            QtWidgets.QMessageBox.information(self, "Success", "Booking confirmed.")
            self.go_back()

    def toggle_cancel_mode(self):
        if not self.cancel_mode:
            self.cancel_mode = True
            self.btnCancel.setText("Exit Cancel Mode")
            self.btnConfirm.setText("Confirm Cancel")
            self.selected_seats.clear()

            for seat, btn in self.seat_buttons.items():
                if btn:
                    btn.setChecked(False)
                    if btn.styleSheet() == "background-color: red":
                        btn.setEnabled(True)
                    else:
                        btn.setEnabled(False)
        else:
            self.cancel_mode = False
            self.btnCancel.setText("Cancel Booking")
            self.btnConfirm.setText("Confirm")
            self.selected_seats.clear()
            self.load_booked_seats()

    def go_back(self):
        from now_showing_screen import NowShowingScreen
        self.close()
        self.now_showing_window = NowShowingScreen(self.username)
        self.now_showing_window.show()

    def go_home(self):
        self.go_back()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # Replace with actual login logic
    logged_in_username = "example_user"
    window = SeatPlanScreen(logged_in_username)
    window.show()
    sys.exit(app.exec())
