import os
from datetime import datetime
from houseapp import db, app, DB_NAME

# class Person(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False)
#     addresses = db.relationship('Address', backref='person', lazy=True)

# class Address(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(120), nullable=False)
#     person_id = db.Column(db.Integer, db.ForeignKey('person.id'),
#         nullable=False)
    
class User(db.Model):
    user_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    user_email = db.Column(db.String(50), unique = True, nullable = False)
    user_password = db.Column(db.String(60), nullable = False)
    user_fname = db.Column(db.String(50), nullable = False)
    user_address = db.Column(db.String(50), nullable = False)
    user_phone = db.Column(db.Integer, nullable = False)
    user_pincode = db.Column(db.Integer, nullable = False)
    user_action = db.Column(db.String(50), nullable = True, default = 'None')
    def __repr__(self):
        return f"User('{self.user_id}', '{self.user_email}', '{self.user_fname}', '{self.user_pincode}')"

class Professional(db.Model):
    prof_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    prof_email = db.Column(db.String(50), unique = True, nullable = False)
    prof_password = db.Column(db.String(60), nullable = False)
    prof_fname = db.Column(db.String(50), nullable = False)
    prof_experience = db.Column(db.Integer, nullable = False)
    prof_service = db.Column(db.String(50), nullable = False)
    prof_documents = db.Column(db.String(50), nullable = False)
    prof_address = db.Column(db.String(50), nullable = False)
    prof_phone = db.Column(db.Integer, nullable = False)
    prof_pincode = db.Column(db.Integer, nullable = False)
    prof_action = db.Column(db.String(50), nullable = True, default = 'None')
    def __repr__(self):
        return f"Professional('{self.prof_id}', '{self.prof_email}', '{self.prof_fname}', '{self.prof_service}', '{self.prof_experience}')"

class Services(db.Model):
    service_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    service_name = db.Column(db.String(50), unique = True, nullable = False)
    service_description = db.Column(db.String(50), nullable = False)
    service_price = db.Column(db.Integer, nullable = False)
    def __repr__(self):
        return f"Services('{self.service_id}', '{self.service_name}', '{self.service_price}')"




# os.remove(f'./instance/{DB_NAME}')
if not os.path.isfile(f'./instance/{DB_NAME}'):
    db.create_all()

# from houseapp import db
# from houseapp.models import User
# db.create_all()
# user = User(user_email = 'Jishnu', user_password = '12345', user_fname = 'Koliyadan', user_address = 'Cheeral', user_pincode = 6789)
# db.session.add(user)
# db.session.commit()
# User.query.all()
# User.query.first()