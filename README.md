# Face-Recognition-Attendance-Management-System
# 🎓 Face Recognition Based Attendance Management System

This project automates student attendance using face recognition. The system captures real-time facial data, matches it against pre-registered images, and records attendance with timestamps into both CSV files and a database. It eliminates the need for manual attendance while providing a secure, contactless, and efficient solution for institutions.

---

## 📌 Project Summary

- **Objective:** Automatically recognize students' faces and mark attendance in real time using a webcam.
- **Technology Stack:**
  - Python 3.7+
  - OpenCV, NumPy, Pandas
  - face_recognition / LBPH Face Recognizer
  - Tkinter (GUI)
  - MySQL / CSV for attendance logging
  - PIL / Pillow for image handling

---

## 🧠 Features

-  Face detection and recognition using OpenCV
-  Real-time webcam integration
-  Auto-generation of CSV attendance sheets
-  Manual attendance option via GUI
-  Admin login panel to view registered student data
-  GUI built with Tkinter
-  Database connectivity using PyMySQL
-  Face training and dataset storage system
-  Attendance export and viewing in tabular format

---

## 🛠 Installation & Setup

### ✅ Requirements:
- Python 3.7+
- Webcam
- MySQL Server (for DB storage)
- Required Python packages:
```bash
pip install opencv-python numpy pandas pillow mysql-connector-python

---
🔧 Setup Steps:
Clone or download this repo.

Run the attendance.py or main.py script.

Use the GUI to:

Register a new face (Take Images)

Train the model (Train Images)

Start attendance capture (Automatic Attendance)

Or manually enter attendance (Manual Fill)

Attendance will be saved in both CSV format and MySQL tables.
