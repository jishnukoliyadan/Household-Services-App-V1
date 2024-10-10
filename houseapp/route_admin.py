from houseapp import app, db
from flask import render_template, url_for
from flask import request, flash, redirect
from houseapp.models import Services, Professional
from flask_login import login_required, current_user

@app.route('/admin',methods = ["GET","POST"])
@login_required
def admin_home():
    if current_user.role != 'admin':
        flash(f'Logged out successfully! Admin page is not accessible if logged in as {current_user.role.title()}', 'warning')
        return redirect(url_for('logout'))
    services = Services.query.all()
    professionals = Professional.query.filter_by(prof_action = 'None').all()
    return render_template('dashboard_admin.html', title = 'Admin', services = services, professionals = professionals)

@app.route('/admin/new',methods = ["GET","POST"])
@login_required
def new_service():
    if current_user.role != 'admin':
        flash(f'Logged out successfully! Admin page is not accessible if logged in as {current_user.role.title()}', 'warning')
        return redirect(url_for('logout'))
    if request.method == 'POST':
        service_name = request.form.get('inputSName')
        service_description = request.form.get('inputDescription')
        service_price = request.form.get('inputBasePrice')
        service_image = request.form.get('formImage')
        service_exists = Services.query.filter_by(service_name = service_name,
                                                  service_description = service_description,
                                                  service_price = service_price).first()
        if not service_exists:
            service = Services(service_name = service_name,
                               service_description = service_description,
                               service_price = service_price,
                               service_image = service_image)
            db.session.add(service)
            db.session.commit()
            flash('New service has been created!', 'success')
            return redirect(url_for('admin_home'))
        else:
            flash('The service with same details already exists, try creating a new one.', 'info')
        return redirect(url_for('new_service'))
    return render_template('new_service.html', title = 'Admin', alias = 'sampleA')