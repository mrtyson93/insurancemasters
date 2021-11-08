from dotenv import load_dotenv
from flask import Flask, render_template
import os

# Load environment
load_dotenv('.env')

# Initialize
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')
