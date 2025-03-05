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
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        print(request.form)  # Debugging line to check received data
        
        # Safely retrieve form data
        name = request.form.get('name', '').strip()
        age = request.form.get('age', '').strip()
        blood_group = request.form.get('blood_group', '').strip()
        contact = request.form.get('contact', '').strip()
        city = request.form.get('city', '').strip()

        if not name or not age or not blood_group or not contact or not city:
            return "Missing fields! Please fill all fields.", 400

        query = "INSERT INTO Donor (name, age, blood_group, contact, city, last_donation_date) VALUES (%s, %s, %s, %s, %s, NULL)"
        cursor.execute(query, (name, age, blood_group, contact, city))
        db.commit()
        return redirect(url_for('donors'))
    
    return render_template('register.html')


# View Donors
@app.route('/donors')
def donors():
    cursor.execute("SELECT * FROM Donor")
    donors_list = cursor.fetchall()
    return render_template('donors.html', donors=donors_list)

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
