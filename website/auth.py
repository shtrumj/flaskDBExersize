from flask import Blueprint, render_template, request

auth = Blueprint("auth", __name__, template_folder="../website/templates", static_folder="../website/static")


@auth.route('/reg', methods=['GET','POST'])
def register():
    return render_template('Register.html')