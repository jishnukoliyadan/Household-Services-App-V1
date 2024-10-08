from flask import render_template, url_for
from flask import request, flash, redirect
from houseapp import app, db, bcrypt
from houseapp.models import User, Professional





@app.route('/', methods = ['GET'])
def home():
    return render_template('home.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('InputEmail1')
        password = request.form.get('InputPassword1')
        professional_ = request.form.get('flexSwitchCheck')
        if username == 'admin@admin':
            admin_password = 'admin'
            admin_password = bcrypt.generate_password_hash(admin_password)
            if bcrypt.check_password_hash(admin_password, password):
                return redirect(url_for('admin_home'))
            flash('Mismatch in Admin Password, try again with correct one.', 'info')
            return redirect(url_for('login'))
        if not professional_:
            user = User.query.filter_by(user_email = username).first()
            if user:
                if bcrypt.check_password_hash(user.user_password, password):
                    return redirect(url_for('customer_home'))
                else:
                    flash('Mismatched Password, try again with correct password.', 'info')
                    return redirect(url_for('login'))
            else:
                flash('User is not registered yet, please register before trying login.', 'info')
                return redirect(url_for('customer_signup'))
        else:
            user = Professional.query.filter_by(prof_email = username).first()
            if user:
                if bcrypt.check_password_hash(user.prof_password, password):
                    return redirect(url_for('professional_home'))
            else:
                flash('Professional is not registered yet, please register before trying login.', 'info')
                return redirect(url_for('professional_signup'))
    return render_template('login.html')

@app.route('/c_signup', methods = ['GET', 'POST'])
def customer_signup():
    if request.method == 'POST':
        email = request.form.get('inputEmail3')
        password = request.form.get('inputPassword3')
        fullname = request.form.get('inputFName')
        address = request.form.get('inputAddress')
        contact_no = request.form.get('inputContactNo')
        pincode = request.form.get('inputPincode')
        if email == 'admin@admin':
            flash('Restricted Email, choose a different one to register.', 'info')
            return redirect(url_for('customer_signup'))
        username_exists = User.query.filter_by(user_email = email).first()
        if not username_exists:
            password = bcrypt.generate_password_hash(password)
            user = User(user_email = email, user_password = password, user_fname = fullname,
                        user_address = address, user_phone = contact_no, user_pincode = pincode)
            db.session.add(user)
            db.session.commit()
            flash('Your account has been created! You are now able to log in as User.', 'success')
            return redirect(url_for('login'))
        else:
            flash('User already exists, try with a different Email ID.', 'danger')
            return redirect(url_for('customer_signup'))
    return render_template('signup_customer.html')

@app.route('/p_signup', methods = ['GET', 'POST'])
def professional_signup():
    if request.method == 'POST':
        email = request.form.get('inputEmail3')
        password = request.form.get('inputPassword3')
        fullname = request.form.get('inputFName')
        service_name = request.form.get('inputServiceName')
        experience = request.form.get('inputExperience')
        doc_file = request.form.get('formFile')
        address = request.form.get('inputAddress')
        contact_no = request.form.get('inputContactNo')
        pincode = request.form.get('inputPincode')
        if email == 'admin@admin':
            flash('Restricted Email, choose a different one to register.', 'danger')
            return redirect(url_for('professional_signup'))
        username_exists = Professional.query.filter_by(prof_email = email).first()
        if not username_exists:
            password = bcrypt.generate_password_hash(password)
            prof = Professional(prof_email = email, prof_password = password, prof_fname = fullname,
                            prof_experience = experience, prof_service = service_name,
                            prof_documents = doc_file, prof_address = address,
                            prof_phone = contact_no, prof_pincode = pincode)
            db.session.add(prof)
            db.session.commit()
            flash('Your account has been created! You are now able to log in as Professional.', 'success')
            return redirect(url_for('login'))
        else:
            flash('User already exists, try with a different Email ID.', 'danger')
            return redirect(url_for('professional_signup'))
    return render_template('signup_professional.html')

@app.route('/admin',methods = ["GET","POST"])
def admin_home():
    return render_template('dashboard_admin.html', title = 'Admin', alias = 'sampleA')

@app.route('/cust',methods = ["GET","POST"])
def customer_home():
    return render_template('dashboard_customer.html', title = 'Customer', alias = 'sampleC')

@app.route('/prof',methods = ["GET","POST"])
def professional_home():
    return render_template('dashboard_professional.html', title = 'Professional', alias = 'sampleP')


@app.route('/admin/new',methods = ["GET","POST"])
def new_service():
    return render_template('new_service.html', title = 'Admin', alias = 'sampleA')