from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo


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
    # user phone number and user birth-date to be added in registrationForm class
    # limitation should be disscussed
    # changes to the error messages needed
    # submit field to submit user info
    submit = SubmitField('register')

# user must complete registration to login otherwise user will be rejected with suitable error messages


class loginForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
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
