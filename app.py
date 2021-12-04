from dotenv import load_dotenv
from flask import Flask, render_template, session
import os
from python_logic import quoteYou, quoteBusiness, result, contact, quote, faq, payment, confirmation, certificate

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
app.register_blueprint(payment.payment)
app.register_blueprint(confirmation.confirmation)
app.register_blueprint(certificate.certificate)

@app.route('/')
@app.route('/index')
def index():
    selected_state = 'CA'
    if 'insured_state' in session:
        selected_state = session['insured_state']

    return render_template('index.html', selected_state=selected_state)
