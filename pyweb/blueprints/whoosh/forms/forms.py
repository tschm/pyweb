from flask_wtf import FlaskForm
from wtforms import StringField

class SearchForm(FlaskForm):
    search = StringField(u'Search')
    #submit = SubmitField('Submit')