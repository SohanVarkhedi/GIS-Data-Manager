🗺️ Simple GIS Data Manager
A lightweight desktop application built with Python and PyQt5 that allows users to upload, store, and search satellite or geographic images in a MySQL database. Ideal for quick image metadata management in GIS workflows.

📸 Features
📁 Upload Images: Add geotagged or non-geotagged images with coordinates.

🔍 Search Functionality: Search by image name or upload date.

🌐 Coordinate Input: Tag each image with latitude and longitude.

📅 Auto Date Logging: Automatically records upload date.

🧮 MySQL Integration: Stores all image metadata in a structured MySQL database.

🧊 PyQt5 GUI: Intuitive and simple interface.

🚀 Getting Started
📦 Prerequisites
Python 3.x

MySQL Server

Pip packages:

bash
Copy
Edit
pip install pyqt5 mysql-connector-python
🛠️ Database Setup
Before running the app, ensure you have a MySQL database set up:

Create a database called gis_data.

Inside it, create a table:

sql
Copy
Edit
CREATE TABLE images (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    path TEXT,
    date DATE,
    location VARCHAR(255),
    coordinates VARCHAR(255)
);
💻 Running the Application
bash
Copy
Edit
python gis.py
Make sure your MySQL server is running and the connection credentials in the script are correct.

🧱 Tech Stack
Python 3

PyQt5

MySQL

datetime module

📂 File Structure
bash
Copy
Edit
├── gis.py             # Main application file
└── README.md          # Project documentation
⚠️ Security Note
Do not expose real credentials in production. The password="sohan" in the script is for demo/testing. Use environment variables or configuration files instead.

🙌 Contributing
Pull requests are welcome. For major changes, open an issue first to discuss what you would like to change.

📃 License
This project is open-source. Choose a license or insert your own.
