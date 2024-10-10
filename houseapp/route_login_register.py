from houseapp import app, db, bcrypt
from flask import redirect, request, flash, session
from flask import url_for, render_template
from houseapp.models import Customer, Professional, User
from flask_login import login_user, logout_user

@app.route('/signup', methods = ['GET', 'POST'])
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
        username_exists = Customer.query.filter_by(user_email = email).first()
        if not username_exists:
            password = bcrypt.generate_password_hash(password).decode('utf-8')
            user = Customer(cust_email = email, cust_password = password, cust_fname = fullname,
                        cust_address = address, cust_phone = contact_no, cust_pincode = pincode)
            db.session.add(user)
            db.session.commit()
            flash('Your account has been created! You are now able to log in as User.', 'success')
            return redirect(url_for('login'))
        else:
            flash('User already exists, try with a different Email ID.', 'danger')
            return redirect(url_for('customer_signup'))
    return render_template('signup_customer.html')

@app.route('/psignup', methods = ['GET', 'POST'])
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
            password = bcrypt.generate_password_hash(password).decode('utf-8')
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

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('InputEmail1')
        password = request.form.get('InputPassword1')
        professional_ = request.form.get('flexSwitchCheck')
        
        if username == 'admin@admin':
            admin_password = 'admin'
            admin_password = bcrypt.generate_password_hash(admin_password).decode('utf-8')
            if bcrypt.check_password_hash(admin_password, password):
                admin = User('admin_admin', 'Admin', 'admin@admin.com', 'admin')
                login_user(admin, remember = True)
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for('admin_home'))
            flash('Mismatch in Admin Password, try again with correct one.', 'info')
            return redirect(url_for('login'))
        
        if not professional_:
            user = Customer.query.filter_by(cust_email = username).first()
            if user:
                if bcrypt.check_password_hash(user.cust_password, password):
                    user = User(f'customer_{user.cust_id}', user.cust_fname, user.cust_email, 'customer')
                    login_user(user, remember = True)
                    next_page = request.args.get('next')
                    return redirect(next_page) if next_page else redirect(url_for('customer_home'))
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
                    user = User(f'professional_{user.prof_id}', user.prof_fname, user.prof_email, 'professional')
                    login_user(user, remember = True)
                    next_page = request.args.get('next')
                    return redirect(next_page) if next_page else redirect(url_for('professional_home'))
                else:
                    flash('Mismatched Password, try again with correct password.', 'info')
                    return redirect(url_for('login'))
            else:
                flash('Professional is not registered yet, please register before trying login.', 'info')
                return redirect(url_for('professional_signup'))
    return render_template('login.html')

@app.route('/logout', methods = ['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('home'))