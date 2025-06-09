import sys
import mysql.connector
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QTableWidget, QTableWidgetItem, QLineEdit
from datetime import datetime

class GISDataManager(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Simple GIS Data Manager")
        self.setGeometry(200, 200, 600, 400)

        self.layout = QVBoxLayout()

        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sohan",
            database="gis_data"
        )
        self.curs = self.conn.cursor()

        self.upload_button = QPushButton('Upload Image')
        self.upload_button.setEnabled(False)
        self.upload_button.clicked.connect(self.upload_image)
        self.layout.addWidget(self.upload_button)

        self.search_box = QLineEdit(self)
        self.search_box.setPlaceholderText("Search by Image Name or Date")
        self.layout.addWidget(self.search_box)

        self.search_button = QPushButton('Search')
        self.search_button.clicked.connect(self.search_image)
        self.layout.addWidget(self.search_button)

        self.table = QTableWidget(self)
        self.layout.addWidget(self.table)

        self.coordinate_input = QLineEdit(self)
        self.coordinate_input.setPlaceholderText("Enter Coordinates (lat, long)")
        self.layout.addWidget(self.coordinate_input)

        self.selected_image = None

        self.select_button = QPushButton('Select Image')
        self.select_button.clicked.connect(self.select_image)
        self.layout.addWidget(self.select_button)

        self.setLayout(self.layout)

    def select_image(self):
        options = QFileDialog.Options()
        file, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.jpg *.bmp)", options=options)
        
        if file:
            self.selected_image = file
            self.upload_button.setEnabled(True)

    def upload_image(self):
        if not self.selected_image:
            return
        
        coordinates_text = self.coordinate_input.text()

        if not coordinates_text.strip():
            coordinates_text = "0.0, 0.0"  # Default coordinates

        date = datetime.now().strftime("%Y-%m-%d")
        name = self.selected_image.split("/")[-1]
        location = "Unknown"

        self.curs.execute("INSERT INTO images (name, path, date, location, coordinates) VALUES (%s, %s, %s, %s, %s)",
                          (name, self.selected_image, date, location, coordinates_text))
        self.conn.commit()

        self.upload_button.setEnabled(False)
        self.selected_image = None

    def search_image(self):
        search_query = self.search_box.text()
        self.curs.execute("SELECT * FROM images WHERE name LIKE %s OR date LIKE %s", 
                          ('%' + search_query + '%', '%' + search_query + '%'))
        results = self.curs.fetchall()

        self.table.setRowCount(len(results))
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["ID", "Name", "Location", "Date", "Coordinates"])

        for row_idx, result in enumerate(results):
            for col_idx, item in enumerate(result):
                self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(item)))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GISDataManager()
    window.show()
    sys.exit(app.exec_())
