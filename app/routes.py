from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/login')
def login():
    return render_template('login.html')