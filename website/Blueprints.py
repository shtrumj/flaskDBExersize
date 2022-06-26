from flask import Blueprint, render_template, request, url_for, redirect
from website.extensions import db
from website.forms import EmployeesForm


org = Blueprint('org', __name__, template_folder='templates')


@org.route('/AddEmp',methods=('GET','POST'))
def addEmp():
    form = EmployeesForm()
    if request.method == 'POST':
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        cellPhoneNumber = request.form.get('phoneNumber')
        emailAddress = request.form.get('emailAddress')
        birthday = request.form.get('birthday')
        from website.dbModel import Employees
        new_emp = Employees(firstName=firstName, lastName=lastName, cellPhoneNumber=cellPhoneNumber, emailAddress=emailAddress, birthday=birthday)
        db.session.add(new_emp)
        db.session.commit()
        return redirect(url_for('org.home'))
    return render_template('employees.html', form=form)


@org.route('/Menu', methods=('GET','POST'))
def home():
    return render_template('menu.html')

