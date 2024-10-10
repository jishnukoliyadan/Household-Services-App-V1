from flask import render_template, url_for
from flask import request, flash, redirect
from houseapp import app, db, bcrypt
from houseapp.models import Customer, Professional, Services
from flask_login import login_required, logout_user, current_user

from houseapp import route_admin
from houseapp import route_login_register

@app.route('/', methods = ['GET'])
def home():
    services = Services.query.all()
    return render_template('home.html', services = services)

@app.route('/cust',methods = ["GET","POST"])
@login_required
def customer_home():
    if current_user.role != 'customer':
        flash(f'Logged out successfully! Customer page is not accessible if logged in as {current_user.role.title()}', 'warning')
        return redirect(url_for('logout'))
    services = Services.query.all()
    return render_template('dashboard_customer.html', title = 'Customer', alias = 'sampleC', services = services)

@app.route('/prof',methods = ["GET","POST"])
@login_required
def professional_home():
    if current_user.role != 'professional':
        flash(f'Logged out successfully! Professional page is not accessible if logged in as {current_user.role.title()}', 'warning')
        return redirect(url_for('logout'))
    return render_template('dashboard_professional.html', title = 'Professional', alias = 'sampleP')