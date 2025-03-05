#Blood Donation Management System

📌 Overview

The Blood Donation Management System is a web-based application that helps hospitals and blood donors manage blood donation records efficiently. It allows donors to register, hospitals to request blood, and records to be maintained in a MySQL database.

🚀 Features

Donor Registration: Donors can register with their details.

Hospital Management: Hospitals can request blood units.

Blood Request Handling: Track blood requests from hospitals.

Donation Records: Maintain donation history.

Database Integration: Uses MySQL for efficient data management.

🛠️ Tech Stack

Backend: Flask (Python)

Database: MySQL

Frontend: HTML, CSS

📂 Project Structure

├── app.py                 # Main Flask application
├── blood_donation.sql      # Database schema
├── templates/
│   ├── index.html         # Home page
│   ├── register.html      # Donor registration form
│   ├── hospitals.html     # Hospital list
│   ├── blood_requests.html # Blood request tracking
├── static/
│   ├── styles.css         # CSS files
├── README.md              # Project documentation

🏗️ Setup and Installation

1️⃣ Prerequisites

Python 3.x installed

MySQL installed

Flask installed (pip install flask)

2️⃣ Database Setup

CREATE DATABASE BloodDonationDB;
USE BloodDonationDB;

-- Create tables and insert sample data
SOURCE blood_donation.sql;

3️⃣ Running the Flask App

python app.py

Then, open the browser and go to:

http://127.0.0.1:5000/

🔗 Endpoints

Endpoint

Method

Description

/

GET

Home Page

/register

GET/POST

Donor Registration

/hospitals

GET

View Hospitals

/blood_requests

GET

View Blood Requests

📌 Troubleshooting

Error: KeyError: 'blood_group'

Ensure the form in register.html has a field named blood_group.

Debug using print(request.form) inside app.py.

📜 License

This project is open-source and free to use. Modify as needed! 🚀

Made with ❤️ using Flask and MySQL
