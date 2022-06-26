from flask import Blueprint, render_template, request
from website.extensions import db
from forms import EmployeesForm


org = Blueprint('org', __name__, template_folder='templates')


@org.route('/AddEmp')
def addEmp():
    form = EmployeesForm()
    if request.method == 'POST':
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        cellPhoneNumber = request.form.get('phoneNumber')
        emailAddress = request.form.get('emailAddress')
        birthday = request.form.get('birthday')
        new_emp = Employees(firstName=firstName, lastName=lastName, cellPhoneNumber=cellPhoneNumber, emailAddress=emailAddress, birthday=birthday)
        db.session.add(new_emp)
        db.session.commit()
    return render_template('employees.html')