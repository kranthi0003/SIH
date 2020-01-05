from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_wtf.file import FileField
from wtforms.validators import InputRequired, Length

class UploadForm(FlaskForm):
    file = FileField()
    submit = SubmitField('Submit')

class QuesSearchForm(FlaskForm):
	search = StringField('Search', validators = [InputRequired()])
	index = StringField('Index', validators = [InputRequired()])
	submit = SubmitField('Search')
    
class EntryForm(FlaskForm):
	#filename = StringField('File Path', validators = [InputRequired()])
	index = StringField('Index', validators = [InputRequired()])
	enter = SubmitField('Enter')

class SearchForm(FlaskForm):
	index = StringField('Index', validators = [InputRequired()])
	query = StringField('Query', validators = [InputRequired()])
	submit = SubmitField('Submit')