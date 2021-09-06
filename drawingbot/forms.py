from flask_wtf import FlaskForm
from wtforms import SubmitField

class ConfirmForm(FlaskForm):
    """Creates a flask form used to submit user choice. This form will be used
    to determine if the models prediction was indeed correct.
    """
    submit = SubmitField('Yes')


