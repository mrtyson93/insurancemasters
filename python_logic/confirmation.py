from flask import Blueprint, render_template, request, session
from datetime import datetime
import random
import string
from .helper import *

confirmation = Blueprint(
    'confirmation', __name__, template_folder='templates')


@confirmation.route("/confirmation",  methods=['POST', 'GET'])
def confirmation_load():
    #default value
    cc_name = ""
    cc_number = ""
    cc_expiry = ""
    cc_cvv = ""
    cc_amount = ""
    if request.method == 'POST':
        if "name" in request.form:
            session['cc_name'] = request.form['name']
            cc_name = request.form['name']
        if "cardnumber" in request.form:
            session['cc_number'] = request.form['cardnumber']
            cc_number = request.form['cardnumber']

    if 'final_quote' in session:
        cc_amount = Helper.format_currency(float(session['final_quote']))

    now = datetime.now()
    letters = string.digits
    return render_template('confirmation.html', cc_name=cc_name, cc_number=cc_number[-4:],
                           cc_date=now.strftime("%m/%d/%Y"), cc_time=now.strftime("%H:%M:%S"),
                           cc_auth_code=''.join(random.choice(letters) for i in range(10)),
                           cc_amount=cc_amount)

