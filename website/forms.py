from wtforms import StringField, validators,PasswordField, SubmitField, DateField
from wtforms.fields import DateField, DateTimeField
from flask_wtf import FlaskForm



class RegisterUsers(FlaskForm):
    signinusername = StringField('Username', [validators.Length(min=4, max=25)])
    signinpassword = PasswordField('Password')
    signupusername = StringField('Username', [validators.Length(min=4, max=25)])
    signupemail = StringField('Email',[validators.length(min=6, max=30)])
    signuppassword = PasswordField('Password')
    signuppassword2 = PasswordField('Password')
    signup = SubmitField()


class EmployeesForm(FlaskForm):
    firstName = StringField('First name', [validators.length(min=3, max=10)])
    lastName = StringField('Last name', [validators.length(min=3, max=10)])
    emailAddress = StringField('email address', [validators.length(min=3, max=25)])
    birthday = DateField('Your Birthday', [validators.length(max=20)])
    phoneNumber = StringField('Phone Number', [validators.length(max=11)])
    submit = SubmitField('Create a new Employee')
