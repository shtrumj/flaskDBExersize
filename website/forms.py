from wtforms import StringField, validators,PasswordField, SubmitField
from wtforms.fields import DateField, DateTimeField
from flask_wtf import FlaskForm


class RegisterUsers(FlaskForm):
    signupusername = StringField('Username', [validators.Length(min=4, max=25)])
    signupemail = StringField('Email',[validators.length(min=6, max=30)])
    signuppassword = PasswordField('Password')
    signuppassword2 = PasswordField('Password')
    signup = SubmitField()


class Employees(FlaskForm):
    firstName = StringField('First name', [validators.length(min=3, max=10)])
    lastName = StringField('Last name', [validators.length(min=3, max=10)])
    birthday = DateField('Your Birthday', format='%d/%m/%y')
    phoneNumber = StringField('Phone Number',[validators.length(max=11)])
    submit = SubmitField('Create a new Employee')