from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import Email, DataRequired, InputRequired

class AddMessage(FlaskForm):

    name = StringField('Name*', validators=[InputRequired("Name is required.")])
    email = StringField("Email*", validators=[Email(),
                                               DataRequired("Email address is required.")])
    message = TextAreaField('Message*', validators=[InputRequired("Message can't be empty.")])
    submit = SubmitField("Send Message")
