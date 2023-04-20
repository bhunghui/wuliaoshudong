import wtforms
from wtforms.validators import length, email, EqualTo


class LoginForm(wtforms.Form):
    username = wtforms.StringField(validators=[length(min=1, max=10)])
    passwd = wtforms.StringField(validators=[length(min=8, max=30)])


class RegisterForm(wtforms.Form):
    username = wtforms.StringField(validators=[length(min=1, max=10)])
    passwd = wtforms.StringField(validators=[length(min=8, max=30)])
    passwd_again = wtforms.StringField(validators=[EqualTo('passwd')])
    email = wtforms.StringField(validators=[email()])


class QaForm(wtforms.Form):
    title = wtforms.StringField(validators=[length(min=10, max=150)])
    content = wtforms.StringField(validators=[length(min=20, max=500)])


class CommentForm(wtforms.Form):
    content = wtforms.StringField(validators=[length(min=1, max=800)])