import os
from datetime import datetime
from houseapp import db, app, DB_NAME, login_manager
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, fname, email, role):
        self.id = id
        self.email = email
        self.name = fname
        self.role = role

@login_manager.user_loader
def load_user(user_role_id):
    role, user_id = user_role_id.split('_')
    if role == 'customer':
        customer = Customer.query.get(int(user_id))
        if customer:
            return User(customer.cust_id, customer.cust_fname, customer.cust_email, 'customer')
    if role == 'professional':
        professional = Professional.query.get(int(user_id))
        if professional:
            return User(professional.prof_id, professional.prof_fname, professional.prof_email, 'professional')
    if role == 'admin':
        if user_id == 'admin':
            return User('admin', 'Admin', 'admin@admin.com', 'admin')
    return None

class Customer(db.Model):
    cust_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    cust_email = db.Column(db.String(100), unique = True, nullable = False)
    cust_password = db.Column(db.String(60), nullable = False)
    cust_fname = db.Column(db.String(20), nullable = False)
    cust_address = db.Column(db.String(100), nullable = False)
    cust_phone = db.Column(db.Integer, nullable = False)
    cust_pincode = db.Column(db.Integer, nullable = False)
    cust_action = db.Column(db.String(20), nullable = True, default = 'None')
    def __repr__(self):
        return f"User('{self.cust_id}', '{self.cust_email}', '{self.cust_fname}', '{self.cust_pincode}')"

class Professional(db.Model):
    prof_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    prof_email = db.Column(db.String(100), unique = True, nullable = False)
    prof_password = db.Column(db.String(60), nullable = False)
    prof_fname = db.Column(db.String(20), nullable = False)
    prof_experience = db.Column(db.Integer, nullable = False)
    prof_service = db.Column(db.String(20), nullable = False)
    prof_documents = db.Column(db.String(150), nullable = False)
    prof_address = db.Column(db.String(100), nullable = False)
    prof_phone = db.Column(db.Integer, nullable = False)
    prof_pincode = db.Column(db.Integer, nullable = False)
    prof_action = db.Column(db.String(20), nullable = True, default = 'None')
    def __repr__(self):
        return f"Professional('{self.prof_id}', '{self.prof_email}', '{self.prof_fname}', '{self.prof_service}', '{self.prof_experience}')"

class Services(db.Model):
    service_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    service_name = db.Column(db.String(20), unique = False, nullable = False)
    service_description = db.Column(db.String(150), nullable = False)
    service_price = db.Column(db.Integer, nullable = False)
    service_image = db.Column(db.String(20), nullable = True, default = 'no_image.jpg')
    def __repr__(self):
        return f"Services('{self.service_id}', '{self.service_name}', '{self.service_price}')"




# os.remove(f'./instance/{DB_NAME}')
if not os.path.isfile(f'./instance/{DB_NAME}'):
    db.create_all()
# from houseapp import create_db