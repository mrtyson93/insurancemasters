from flask import Blueprint, render_template

quoteyou = Blueprint(
    'quoteyou', __name__, template_folder='templates')


@quoteyou.route("/quoteaboutyou", methods=['POST'])
def quoteyou_load():

    return render_template('quoteyou.html')
