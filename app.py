from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Database Configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="butterchicken1",
    database="BloodDonationDB"
)
cursor = db.cursor()

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Donor Registration
@app.route('/registerasdonor', methods=['GET', 'POST'])
def registerdonor():
    if request.method == 'POST':
        print(request.form)  # Debugging line to check received data
        
        # Safely retrieve form data
        name = request.form.get('name', '').strip()
        age = request.form.get('age', '').strip()
        blood_group = request.form.get('blood_group', '').strip().upper()
        contact = request.form.get('contact', '').strip()
        city = request.form.get('city', '').strip()

        # Fetch current date
        cursor.execute("SELECT NOW()")
        date = cursor.fetchone()[0]  # Fetch first column of first row (actual date)

        # Validate age
        if not age.isdigit() or not (18 <= int(age) <= 60):  
            return "Invalid age! Age must be between 18 and 60.", 400

        # Validate blood group
        valid_blood_groups = {'A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-'}
        if blood_group not in valid_blood_groups:
            return "Invalid blood group! Choose a valid blood type.", 400
        
        # Validate contact (should be 10-digit number)
        if not contact.isdigit() or len(contact) != 10:
            return "Invalid contact number! Must be a 10-digit number.", 400

        # Insert into database
        query = "INSERT INTO Donor (name, age, blood_group, contact, city, last_donation_date) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (name, age, blood_group, contact, city, date))
        db.commit()
        
        return redirect(url_for('donors'))  # Redirect to donor list page

    return render_template('registerdonor.html')

@app.route('/registerasreciever', methods=['GET', 'POST'])
def registerpatient():
    if request.method == 'POST':
        print(request.form)  # Debugging line to check received data
        
        # Safely retrieve form data
        name = request.form.get('name', '').strip()
        age = request.form.get('age', '').strip()
        blood_group = request.form.get('blood_group', '').strip().upper()
        hid = request.form.get('hid', '').strip()
        units = request.form.get('units', '').strip()

        # Fetch current date
        cursor.execute("SELECT NOW()")
        date = cursor.fetchone()[0]  # Fetch first column of first row (actual date)

        # Validate age
        if not age.isdigit() or not (18 <= int(age) <= 60):  
            return "Invalid age! Age must be between 18 and 60.", 400

        # Validate blood group
        valid_blood_groups = {'A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-'}
        if blood_group not in valid_blood_groups:
            return "Invalid blood group! Choose a valid blood type.", 400
        
        query = "INSERT INTO Patients (name, age, blood_group, hospital_id, units_needed, request_date) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (name, age, blood_group, hid, units, date))
        db.commit()
        
        return redirect(url_for('patients'))  # Redirect to donor list page

    return render_template('registerpatient.html')


# View Donors
@app.route('/donors')
def donors():
    cursor.execute("SELECT * FROM Donor")
    donors_list = cursor.fetchall()
    return render_template('donors.html', donors=donors_list)
@app.route('/patients')
def patients():
    cursor.execute("SELECT * FROM Patients")
    donors_list = cursor.fetchall()
    return render_template('patients.html', donors=donors_list)

# Blood Request
@app.route('/request_blood', methods=['GET', 'POST'])
def request_blood():
    if request.method == 'POST':
        hospital_id = request.form['hospital_id']
        blood_group = request.form['blood_group']
        units_required = request.form['units_required']

        query = "INSERT INTO BloodRequest (hospital_id, blood_group, units_required) VALUES (%s, %s, %s)"
        cursor.execute(query, (hospital_id, blood_group, units_required))
        db.commit()
        return redirect(url_for('blood_requests'))

    cursor.execute("SELECT * FROM Hospital")
    hospitals = cursor.fetchall()
    return render_template('request_blood.html', hospitals=hospitals)

# View Blood Requests
@app.route('/blood_requests')
def blood_requests():
    cursor.execute("""
        SELECT BloodRequest.request_id, Hospital.name, BloodRequest.blood_group, BloodRequest.units_required, BloodRequest.request_date 
        FROM BloodRequest 
        JOIN Hospital ON BloodRequest.hospital_id = Hospital.hospital_id
    """)
    requests_list = cursor.fetchall()
    return render_template('blood_requests.html', requests=requests_list)

if __name__ == '__main__':
    app.run(debug=True)
