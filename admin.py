import sys
import logging
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
from admin_screen import Ui_MainWindow
import mysql.connector
from mysql.connector import Error

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s:%(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)

class AdminWindow(QMainWindow):
    def __init__(self):
        logging.debug("Initializing AdminWindow...")
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        logging.debug("Attempting to connect to MySQL...")
        try:
            self.db = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="",
                database="ticket_universe",
                port=3306,
                connection_timeout=5,
                autocommit=True,
                use_pure=True
            )
            self.cursor = self.db.cursor()
            logging.debug("MySQL connection established.")
        except Error as e:
            logging.error(f"MySQL connection error: {e}")
            QMessageBox.critical(self, "Database Connection Error", str(e))
            sys.exit(1)

        self.load_users()
        self.ui.deleteBtn.clicked.connect(self.delete_user)

    def load_users(self):
        logging.debug("Loading users from database...")
        try:
            self.cursor.execute("SELECT username, email, password FROM users")
            users = self.cursor.fetchall()
            self.ui.tableWidget.setRowCount(0)
            for row_index, row_data in enumerate(users):
                self.ui.tableWidget.insertRow(row_index)
                for col_index, col_data in enumerate(row_data):
                    self.ui.tableWidget.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))
            logging.debug("Users loaded successfully.")
        except Error as e:
            logging.error(f"Failed to load users: {e}")
            QMessageBox.critical(self, "Load Error", f"Failed to load users:\n{e}")

    def delete_user(self):
        logging.debug("Delete button clicked.")
        selected = self.ui.tableWidget.currentRow()
        if selected >= 0:
            username_item = self.ui.tableWidget.item(selected, 0)
            if username_item:
                username = username_item.text()
                try:
                    self.cursor.execute("DELETE FROM users WHERE username = %s", (username,))
                    self.db.commit()
                    self.ui.tableWidget.removeRow(selected)
                    QMessageBox.information(self, "Deleted", f"User '{username}' deleted.")
                    logging.debug(f"User '{username}' deleted successfully.")
                except Error as e:
                    logging.error(f"Failed to delete user: {e}")
                    QMessageBox.critical(self, "Delete Error", f"Failed to delete user:\n{e}")
            else:
                QMessageBox.warning(self, "Error", "No user selected.")
                logging.warning("No user item found in selected row.")
        else:
            QMessageBox.warning(self, "Error", "Please select a user to delete.")
            logging.warning("No row selected for deletion.")

if __name__ == "__main__":
    logging.debug("Starting application...")
    app = QApplication(sys.argv)
    window = AdminWindow()
    window.show()
    sys.exit(app.exec())
