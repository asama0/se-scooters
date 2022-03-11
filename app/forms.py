from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from wtforms.fields import DateField,TelField, TimeField
from wtforms_sqlalchemy.fields import QuerySelectField

from .models import Price, Parking

def hours_to_words(hours_arg):
    hours = int(round(hours_arg))

    words = ''
    count = 0 # counts how many weeks or days or hours..

    if hours < 24:
        count = hours
        words = f'{hours} hour'
    elif hours < 168:
        count = int(round(hours//24))
        words = f'{count} day'
    elif hours < 730.001:
        count = int(round(hours//168))
        words = f'{count} day'
    elif hours < 8760.0024:
        count = int(round(hours//730.001))
        words = f'{count} month'
    else:
        count = int(round(hours//8760.0024))
        words = f'{count} year'

    return words + 's' if count == 1 else ''

def get_time_periods():
    return Price.query.order_by('duration')

def get_parkings():
    return Parking.query.filter(Parking.scooters.any()).order_by('location')

class registrationForm(FlaskForm):
    # string field to write username
    # no limitations yet
    name = StringField('Name', validators=[DataRequired()])
    # string field to write email
    # validator used from wtforms.validators is  Email
    # error message provided
    email = StringField('Email',
                        validators=[
                            Email(message='Error, Enter a valid email'),
                            DataRequired()
                        ]
                        )
    # password field to write user password
    # limitations: length, min=8,max=25
    # error message provided
    password = PasswordField('Password',
                             validators=[
                                 Length(
                                     min=8, max=25, message='Error, password must be between 8-25 charecter '),
                                 DataRequired()
                             ]
                             )
    # password field to re-write user password
    # error message provided
    password2 = PasswordField('Confirm Password',
                              validators=[
                                  EqualTo(
                                      'password', message='passwords does not match'),
                                  DataRequired()
                              ]
                              )
    birth_date = DateField('Date of Birth',
                            validators=[
                                DataRequired()
                            ]
                            )

    phone = TelField('Phone Number',
                            validators=[
                                DataRequired()
                            ]
                            )
    # user phone number and user birth-date to be added in registrationForm class
    # limitation should be disscussed
    # changes to the error messages needed
    # submit field to submit user info
    submit = SubmitField('register')

# user must complete registration to login otherwise user will be rejected with suitable error messages


class loginForm(FlaskForm):
    email = StringField('Email',
                        validators=[
                            Email(message='Error, Enter a valid email'),
                            DataRequired()
                        ]
                        )
    password = PasswordField('Password',
                             validators=[
                                 Length(min=8, max=25,
                                        message='Wrong password '),
                                 DataRequired()
                             ]
                             )
    submit = SubmitField('Login')


class BookingForm(FlaskForm):

    pickup_date = DateField(validators=[DataRequired()])

    pickup_time = TimeField(validators=[DataRequired()])

    time_period = QuerySelectField(
        validators=[DataRequired()],
        query_factory=get_time_periods
    )

    pickup_location = QuerySelectField(
        validators=[DataRequired()],
        query_factory=get_parkings
    )

    submit = SubmitField('submit')

    class forgotPasswordForm(FlaskForm):
    email = StringField('Email',
                        validators=[
                            Email()
                            ,
                            DataRequired()
                        ]
                        )    
    submit = SubmitField('send email')
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('no account found .')

class resetPasswordForm(FlaskForm):
    password = PasswordField('Password',
                            validators=[
                                Length(
                                    min=8, max=25, message='Error, password must be between 8-25 charecter '),
                                DataRequired()
                            ]
                            )
    # password field to re-write user password
    # error message provided
    password2 = PasswordField('Confirm Password',
                            validators=[
                                EqualTo(
                                    'password', message='passwords does not match'),
                                DataRequired()
                            ]
                            )
    submit = SubmitField('change password')





