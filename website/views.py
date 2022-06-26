from flask import Blueprint, render_template, request, flash,url_for, redirect
from website.dbModel import Users
from website.forms import RegisterUsers
from website.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime



Myviews = Blueprint("Myviews", __name__, template_folder="../website/templates", static_folder="../website/static")


@Myviews.route('/', methods=['GET','POST'])
def Register():
    error=None
    form = RegisterUsers()
    if request.method == 'POST':
        if form.signinpassword.data:
            password = generate_password_hash(form.signinpassword.data, 'sha256')
            username = form.signinusername.data
            user = Users.query.filter_by(username=username).first()
            if user:
                formpass = form.signinpassword.data
                formhasedpass = generate_password_hash(form.signinpassword.data, 'sha256')
                dbpass =  user.password
                if check_password_hash(user.password, formpass):

                    return '<h1> All Good! </h1>'
                else:
                    #return '<h1> Password incorrect</h1>' ##+ user.password + ' ' + formhasedpass
                    error = "Password incorrect"
                    #return redirect(url_for('Register'))
        else:
             username = form.signupusername.data
             password = form.signuppassword.data
             password2 = form.signuppassword2.data
             user = Users.query.filter_by(username=username).first()
             if user:
                 if user.password == password:
                    error= 'Passwords do not match'

             else:
                 hashed_pass =  generate_password_hash(password, 'sha256')
                 email = request.form.get('signupemail')
                 new_user = Users(username=username, password=hashed_pass, email=email)
                 db.session.add(new_user)
                 db.session.commit()

    return render_template('Login.html', form=form, error=error)


# @Myviews.route('/employees', methods=['GET','POST'])
# def employees():
#     form = EmployeesForm()
#     if request.method == 'POST':
#         firstName = request.form.get('firstName')
#         lastName = request.form.get('lastName')
#         cellPhoneNumber = request.form.get('phoneNumber')
#         emailAddress = request.form.get('emailAddress')
#         birthday = request.form.get('birthday')
#         new_emp = Employees(firstName=firstName, lastName=lastName, cellPhoneNumber=cellPhoneNumber, emailAddress=emailAddress, birthday=birthday)
#         db.session.add(new_emp)
#         db.session.commit()
#     return render_template('employees.html', form=form )
