from dotenv import load_dotenv
from flask import Flask, render_template
import os
from python_logic import quoteYou, quoteBusiness, result, contact, quote, faq
# from quoteYou import quoteyou
# from quoteBusiness import quotebusiness
# from about import about
# from result import result
# from contact import contact



# Load environment
load_dotenv('.env')

# Initialize
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

app.register_blueprint(quoteYou.quoteyou)
app.register_blueprint(quoteBusiness.quotebusiness)
# app.register_blueprint(about)
app.register_blueprint(result.result)
app.register_blueprint(contact.contact)
app.register_blueprint(faq.faq)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
