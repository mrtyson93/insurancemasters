from dotenv import load_dotenv
from flask import Flask, render_template
import os
from python_logic.quoteYou import quoteyou
from python_logic.quoteBusiness import quotebusiness
from python_logic.about import about
from python_logic.stateselection import stateselection
from python_logic.result import result

# Load environment
load_dotenv('.env')

# Initialize
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

app.register_blueprint(quoteyou)
app.register_blueprint(quotebusiness)
app.register_blueprint(about)
app.register_blueprint(stateselection)
app.register_blueprint(result)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
