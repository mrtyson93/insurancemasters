from flask import Blueprint, render_template

faq = Blueprint(
    'faq', __name__, template_folder='templates')

@faq.route("/faq")
def faq_load():

    return render_template('faq.html')
