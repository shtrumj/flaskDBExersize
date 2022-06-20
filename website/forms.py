from wtforms import Form, StringField, validators,PasswordField, SubmitField


class RegisterUsers(Form):
    signupusername = StringField('Username', [validators.Length(min=4, max=25)])
    signupemail = StringField('Email',[validators.length(min=6, max=30)])
    signuppassword = PasswordField('Password')
    signuppassword2 = PasswordField('Password')
    signup = SubmitField()
