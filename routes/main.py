# routes/main.py
from flask import Blueprint, render_template, request
import json

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')



@main.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.form
        print(f"Message from {data['name']} ({data['email']}): {data['message']}")
    return render_template('index.html')
