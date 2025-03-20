from flask import Flask, render_template, request, redirect, url_for,session
import mysql.connector
import os
app = Flask(__name__)
app.secret_key="hello123"
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
    return render_template('main.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/index2')
def hospital_dashboard():
    if 'hospital_id' not in session:
        return redirect(url_for('login'))  # Redirect to login if not logged in

    hospital_id = session['hospital_id']

    # Fetch blood bank data only for the logged-in hospital
    cursor.execute("SELECT * FROM BloodBank WHERE hospital_id = %s", (hospital_id,))
    blood_data = cursor.fetchall()

    # Fetch blood requests only for the logged-in hospital
    cursor.execute("""
        SELECT request_id, blood_group, units_required, request_date 
        FROM BloodRequest WHERE hospital_id = %s
    """, (hospital_id,))
    requests_list = cursor.fetchall()

    return render_template('index2.html', blood_data=blood_data, requests=requests_list)


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
        query=f"UPDATE bloodbank AS b1 JOIN (SELECT hospital_id FROM bloodbank ORDER BY `{blood_group}` LIMIT 1) AS b2 ON b1.hospital_id = b2.hospital_id SET b1.`{blood_group}` = b1.`{blood_group}` + 1;"
        cursor.execute(query)
        db.commit()
        cursor.execute(f"select hospital_id FROM BLOODBANK ORDER BY `{blood_group}` LIMIT 1;")
        id=cursor.fetchone()
        id=id[0]
        cursor.execute(f"select name from hospital where hospital_id={id};")
        hos=cursor.fetchone()
        message=f"Your blood has been donated to blood bank of {hos}" # Store the message temporarily
        return redirect(url_for('donors',message=message))
    return render_template('registerdonor.html')

@app.route('/registeraspatient', methods=['GET', 'POST'])
def registerpatient():
    if request.method == 'POST':
        print(request.form)  # Debugging line to check received data
        
        # Safely retrieve form data
        patientid = request.form.get('patientid', '').strip()
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
        
        query = "INSERT INTO Patients (patient_id,name, age, blood_group, hospital_id, units_needed, request_date) VALUES (%s,%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (patientid,name, age, blood_group, hid, units, date))
        db.commit()
        return redirect(url_for('available', blood_group=blood_group,units=units,patientid=patientid))
        
    return render_template('registerpatient.html')
# View Donors
@app.route('/donors')
def donors():
    message = request.args.get('message', '')
    cursor.execute("SELECT * FROM Donor")
    donors_list = cursor.fetchall()
    return render_template('donors.html', donors=donors_list,message=message)
@app.route('/patients')
def patients():
    cursor.execute("SELECT * FROM Patients WHERE RECIEVED='NO';")
    donors_list = cursor.fetchall()
    return render_template('patients.html', donors=donors_list)
@app.route('/available', methods=['GET', 'POST'])
def available():
    blood_group = request.args.get('blood_group', '').strip().upper()
    patientid = request.args.get('patientid', '').strip().upper()
    print(f"Extracted Blood Group: {blood_group}")
    units = request.args.get('units', '').strip().upper()
    # Validate blood group
    valid_blood_groups = {'A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-'}
    if blood_group not in valid_blood_groups:
        return "Invalid blood group!", 400

    # Fetch available hospitals
    query = f"SELECT b.hospital_id, h.Name, h.City, h.Contact, `{blood_group}` FROM hospital h, bloodbank b WHERE b.hospital_id = h.hospital_id and `{blood_group}`>{units} ORDER BY `{blood_group}` DESC;"
    cursor.execute(query)
    available_hospitals = cursor.fetchall()
    # Process form submission
    message = None
    if request.method == 'POST':
        hospital_id = request.form.get('hospital_id', '').strip()
        if available_hospitals:
            if hospital_id:
                message = f"You have recieved {units} units from Hospital ID {hospital_id}."
            query=f"update bloodbank set `{blood_group}`=`{blood_group}`-{units} where hospital_id={hospital_id};"
            cursor.execute(query)
            db.commit()
            cursor.execute(f"update patients set recieved='Yes' where patient_id={patientid};" )
            db.commit()
        else:
            message=f"There are no hospitals available for {units} units of blood group {blood_group}. You have sent a request."
            cursor.execute(f"update patients set recieved='NO' where patient_id={patientid};" )
            db.commit()
    return render_template('availablehospitals.html', blood_group=blood_group, available_hospitals=available_hospitals, message=message)

@app.route('/hospitallogin',methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        hospital_id = request.form['hospital_id']
        password = request.form['password']

        cursor.execute("SELECT COUNT(*) FROM passwords WHERE hospital_id=%s AND password=%s;", (hospital_id, password))
        result = cursor.fetchone()

        if result[0] == 1:
            session['hospital_id'] = hospital_id  # Store hospital ID in session
            return redirect(url_for('hospital_dashboard'))
        else:
            return "Invalid Credentials", 401

    return render_template('hospitallogin.html')
@app.route('/logout')
def logout():
    session.pop('hospital_id', None)  # Clear session
    return redirect(url_for('login'))  # Redirect to login page


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
        SELECT BloodRequest.request_id, Hospital.name, BloodRequest.blood_group, BloodRequest.units_required, BloodRequest.request_date, Bloodrequest.units_required, Bloodrequest.request_date 
        FROM BloodRequest 
        JOIN Hospital ON BloodRequest.hospital_id = Hospital.hospital_id
    """)
    requests_list = cursor.fetchall()
    return render_template('blood_requests.html', requests=requests_list)
@app.route('/hospitals')
def hospitals():
    cursor.execute("SELECT * FROM HOSPITAL;")
    hospitals=cursor.fetchall()
    return render_template('hospitals.html',hospitals=hospitals)
@app.route('/bloodbank')
def bloodbank():
    cursor.execute("SELECT * FROM bloodbank;")
    hospitals=cursor.fetchall()
    return render_template('bloodbank.html',hospitals=hospitals)
if __name__ == '__main__':
    app.run(debug=True)
