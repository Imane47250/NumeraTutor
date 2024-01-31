import os
print("Current Working Directory:", os.getcwd())

from flask import Flask, render_template, redirect, url_for
from forms import LoginForm, SignInForm
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from flask import Flask, render_template, redirect, url_for, flash, session


import uuid



# Initialize Flask app
app = Flask(__name__)

#secret key
app.secret_key = 'wa9afa_7imaRo_juhha_fl3gbA'

# Configure SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return f'<User {self.email}>'


# Routes





@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    form = SignInForm()
    if form.validate_on_submit():
        print("Form submitted successfully.")
        print("Email:", form.email.data)
        # Hash the password
        hashed_password = generate_password_hash(form.password.data)

        # Create a new user instance
        new_user = User(email=form.email.data, password_hash=hashed_password)

        # Add the new user to the database session and commit
        db.session.add(new_user)
        db.session.commit()

    else:
        print("Form data:", form.data)
        print("Form errors:", form.errors)
    return render_template('signin.html', form=form)



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            session['id'] = user.id  
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password')
    return render_template('login.html', form=form)



@app.route('/dashboard')
def dashboard():
    # Check if the user is logged in
    if 'id' in session:
        return render_template('dashboard.html')
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    # Clear the user's session
    session.clear()
    # Redirect to the home page or login page
    return redirect(url_for('home'))

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
