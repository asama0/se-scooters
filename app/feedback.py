from flask import render_template
from flask_mail import Message
#from app import mail

from .models import *
from .forms import *
from stripe_functions import *
from helper_functions import *








@app.route("/feedback", methods=['GET', 'POST'])
def register():

    form = feedbackForm()

    return render_template('feedback.html', title='feedback', form=form)