import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, TextAreaField
from wtforms.validators import DataRequired, Length

# Clase para registro de comentarios
class CommentForm(FlaskForm):
    content_comment = TextAreaField('Comentario', validators=[DataRequired(), Length(min=1, max=300)])
    email_comment = StringField('Email', validators=[DataRequired(), Length(min=1, max=100)], render_kw={'readonly': True})
    date_comment = DateField('Fecha de Publicacion', validators=[DataRequired()], format='%Y-%m-%d', default=datetime.date.today, render_kw={'readonly': True})
    nameUser_comment = StringField('Nombre de Usuario', validators=[DataRequired(), Length(min=1, max=80)], render_kw={'readonly': True})
    submit = SubmitField('Enviar comentario')

class UpdateCommentForm(FlaskForm):
    content_comment = StringField('Comentario', validators=[DataRequired(), Length(min=1, max=300)])
    email_comment = StringField('Email', validators=[DataRequired(), Length(min=1, max=100)])
    date_comment = DateField('Fecha de Publicacion', validators=[DataRequired()], format='%Y-%m-%d')
    nameUser_comment = StringField('Nombre de Usuario', validators=[DataRequired(), Length(min=1, max=80)])
    submit = SubmitField('Actualizar comentario')