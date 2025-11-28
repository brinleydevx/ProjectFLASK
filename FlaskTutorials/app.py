from flask import Flask, render_template, url_for
from forms import LoginForm
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
import os

app = Flask(__name__)
csrf = CSRFProtect(app)

app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://3Jx1ZWvJxr4cwx5.root:XFlPRBe00aEsDGWS@gateway01.eu-central-1.prod.aws.tidbcloud.com:4000/users'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    # Form validation
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        return f"recieved: {username}, {password}"

    return render_template('login.html', form=form) 

if __name__ == "__main__":
    app.run(debug=True)