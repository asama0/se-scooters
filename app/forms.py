from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, TextAreaField, RadioField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from wtforms.fields import DateField, TelField, TimeField, SelectField
from wtforms_sqlalchemy.fields import QuerySelectField
from helper_functions import Unique
from .models import *


def get_time_periods():
    return Price.query.order_by('amount')

def get_scooters():
    return Scooter.query.order_by('id').all()


class registrationForm(FlaskForm):
    # string field to write username
    name = StringField('Name', validators=[DataRequired()])
    # string field to write email
    email = StringField('Email',
                        validators=[
                            Email(message='Error, Enter a valid email'),
                            DataRequired(),
                            Unique(User, User.email)
                        ]
                        )
    # password field to write user password
    # length, min=8,max=25

    password = PasswordField('Password',
                             validators=[
                                 Length(
                                     min=8, max=25, message='Error, password must be between 8-25 charecter '),
                                 DataRequired()
                             ]
                             )
    # password field to re-write user password for confirmation

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
    password = PasswordField('Password',validators=[DataRequired()])

    submit = SubmitField('Login')


class BookingForm(FlaskForm):

    pickup_date = StringField(validators=[DataRequired()])

    pickup_time = StringField(validators=[DataRequired()])

    time_period = QuerySelectField(
        validators=[DataRequired()],
        query_factory=get_time_periods
    )

    pickup_parking_id = IntegerField(validators=[DataRequired()])

    submit = SubmitField('Submit')


class AdminBookingForm(FlaskForm):

    user_email = StringField(validators=[
                                 Email(message='Error, Enter a valid email'),
                                 DataRequired()
                             ]
                             )

    pickup_date = DateField(validators=[DataRequired()])

    pickup_time = TimeField(validators=[DataRequired()])

    time_period = QuerySelectField(
        validators=[DataRequired()],
        query_factory=get_time_periods
    )

    scooter_id = QuerySelectField(
        validators=[DataRequired()],
        query_factory=get_scooters
    )

    submit = SubmitField('Submit')


class forgotPasswordForm(FlaskForm):
    email = StringField('Email',
                        validators=[
                            Email(),
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
    password2 = PasswordField('Confirm Password',
                              validators=[
                                  EqualTo(
                                      'password', message='passwords does not match'),
                                  DataRequired()
                              ]
                              )
    submit = SubmitField('change password')


class feedbackForm(FlaskForm):
    experience = RadioField(choices=["Excellent", "Good", "Average", "Bad", "Very bad"],
                            validators=[DataRequired()])
    feedback = TextAreaField(
        validators=[
            DataRequired(), Length(min=0, max=10000, message='please provide a feedback')
        ]
    )
    submit = SubmitField('Submit')


class editProfileForm(FlaskForm):
    # string field to write username
    name = StringField('Name', validators=[DataRequired()])

    birth_date = DateField('Date of Birth', validators=[DataRequired()])

    phone = TelField('Phone Number', validators=[DataRequired()])

    # submit field to submit user info
    submit = SubmitField('Update')


class TicketForm(FlaskForm):
    new_dutration = QuerySelectField(
        validators=[DataRequired()], query_factory=get_time_periods)
    extend = SubmitField('Extend')
    booking_id = IntegerField(validators=[DataRequired()])
    refund = SubmitField('Refund')
    activate = SubmitField('Activate')


class NotAvailableDurationsForm(FlaskForm):
    booking_id = IntegerField(validators=[DataRequired()])