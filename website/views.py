from flask import Blueprint, render_template, request, flash,url_for
from dbModel import Users
from forms import RegisterUsers
from website.extensions import db


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
        email = request.form.get('signupemail')
        new_user = Users(username=username, password=password, email=email)
        db.session.add(new_user)
        db.session.commit()

    return render_template('Login.html', form=form, error=error)

