#id_opinion, username_opcion, id_product, rating_product, comment_opinion, date_opinion
import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, DateField
from wtforms.validators import DataRequired, Length

#Clase de registro de opiniones
class OpinionForm(FlaskForm):
    username_opinion = StringField('Nombre de Usuario', validators=[DataRequired(), Length(min=2, max=80)], render_kw={'readonly': True})
    id_product = SelectField('Producto', coerce=int, validators=[DataRequired()], choices=[])
    rating_product = StringField('Calificacion', validators=[DataRequired()])
    comment_opinion = TextAreaField('Opinion', validators=[DataRequired(), Length(min=2, max=200)])
    date_opinion = DateField('Fecha', validators=[DataRequired()], format='%Y-%m-%d', default=datetime.date.today, render_kw={'readonly': True})
    submit = SubmitField('Enviar')

class UpdateOpinionForm(FlaskForm):
    username_opcion = StringField('Nombre de Usuario', validators=[DataRequired(), Length(min=2, max=80)])
    id_product = SelectField('Producto', coerce=int ,validators=[DataRequired()], choices=[])
    rating_product = SelectField('Calificacion', validators=[DataRequired()])
    comment_opinion = TextAreaField('Opinion', validators=[DataRequired(), Length(min=2, max=200)])
    date_opinion = DateField('Fecha', validators=[DataRequired()], format='%Y-%m-%d')
    submit = SubmitField('Actualizar')
