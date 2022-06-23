from flask import Blueprint, render_template, request, flash,url_for, redirect
from website.dbModel import Users, Employees
from website.forms import RegisterUsers, EmployeesForm
from website.extensions import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


Myviews = Blueprint("Myviews", __name__, template_folder="../website/templates", static_folder="../website/static")


@Myviews.route('/', methods=['GET','POST'])
def Register():
    error=None
    form = RegisterUsers()
    if request.method == 'POST':
        username = request.form.get('signupusername')
        password = request.form.get('signuppassword')
        password2 = request.form.get('signuppassword2')
        if password != password2:
            error= 'Passwords do not match'
            redirect({{ url_for('Register')}})


        email = request.form.get('signupemail')
        new_user = Users(username=username, password=password, email=email)
        db.session.add(new_user)
        db.session.commit()

    return render_template('Login.html', form=form, error=error)


@Myviews.route('/employees', methods=['GET','POST'])
def employees():
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
    return render_template('employees.html', form=form )
