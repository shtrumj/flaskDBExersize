from flask import Blueprint, render_template, request
from website.forms import RegisterUsers


Myviews = Blueprint("Myviews", __name__)


@Myviews.route('/', methods=['GET','POST'])
def myroute():
    form = RegisterUsers()
    if request.method =='POST' and form.validate():
        from website import db
        username = form.signupusername.data
        password = form.signuppassword.data
        password2 = form.signuppassword2.data
        email = form.signupemail.data
        new_user = Users(username=username, password=password, email=email)
        db.session.add(new_user)
        db.session.commit()
        return 'Daaa'

    return render_template('Login.html', form=form)

