# Scan2Hall

### Raspberry Pi-Based Examination Hall Navigation System

**Scan2Hall** is an academic mini project developed using a **Raspberry Pi** to help students quickly find their examination halls.

The system uses a **barcode/QR scanner** to identify a student. It then searches the local student database and displays the student's **assigned building, floor, and room**, along with a digital floor map showing the room location.

The system works locally and does not require an internet connection.

---

## 📌 How It Works

```text
Student scans ID
       ↓
Barcode / QR Scanner
       ↓
Raspberry Pi
       ↓
Student Database
       ↓
Building + Floor + Room
       ↓
Digital Floor Map
```

---

## ✨ Features

* Scan student ID using a barcode/QR scanner
* Automatically find the assigned examination room
* Display building and floor information
* Show the room on a digital floor map
* Works without internet
* Local Flask-based web application
* Simple CSV-based student and room database
* Admin options for updating student and room data

---

## 🛠️ Hardware Used

* Raspberry Pi 4 Model B
* USB Barcode/QR Scanner
* HDMI Display
* Raspberry Pi Power Supply

---

## 💻 Software Used

* Python
* Flask
* HTML/CSS/JavaScript
* CSV
* SVG
* Raspberry Pi OS

---

## 📂 Project Structure

```text
Scan2Hall/
│
├── app.py
├── student_data.csv
├── room_details.csv
├── templates/
├── static/
├── screenshots/
└── README.md
```

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/Scan2Hall.git
cd Scan2Hall
```

### 2. Install Flask

```bash
pip install flask
```

### 3. Connect the hardware

Connect the barcode/QR scanner and display to the Raspberry Pi.

### 4. Run the application

```bash
python3 app.py
```

Then open the local address shown by Flask, for example:

```text
http://127.0.0.1:5000
```

---

## 📷 Screenshots

### Main Screen

<img width="1912" height="1035" alt="Screenshot 2026-10-08 012537" src="https://github.com/user-attachments/assets/4fb55bd9-55ef-490d-bbbe-59d57278a056" />

### Student Result

<img width="1916" height="1035" alt="Screenshot 2026-10-08 012647" src="https://github.com/user-attachments/assets/12fc9f0e-c803-43cf-b882-35e83dc090e6" />

### Admin

<img width="1885" height="1032" alt="Screenshot 2026-10-08 012602" src="https://github.com/user-attachments/assets/09b5724d-0805-4062-95ff-735bbcec1ec6" />

<img width="1885" height="1025" alt="Screenshot 2026-10-08 012619" src="https://github.com/user-attachments/assets/bad74360-58cf-4299-b49a-456c0807fa82" />

---

## 🔮 Future Improvements

Some possible improvements are:

* Support for multiple buildings and floors
* Excel-based bulk student data import
* Use of a proper database such as SQLite
* Improved interactive floor maps
* Touchscreen support
* Better admin interface
* Support for multiple Scan2Hall kiosks

---

---

## 👥 Project Team

This project was developed as a team academic mini project.

* **Devadutt Priyan**
* **Kiran Alias Shaji**
* **Harisankar S**
* **Julia Sara Korah**

**B.Tech Electronics and Communication Engineering**
**Muthoot Institute of Technology & Science, Kerala**

---

## 📄 Note

This project was developed for academic and educational purposes.

For public repositories, use **dummy student information** instead of real student records.
