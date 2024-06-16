import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField
from wtforms.validators import DataRequired, Length

class RegisterSaleForm(FlaskForm):
    userName_sale =  StringField('Nombre de Usuario', validators=[DataRequired(), Length(min=1, max=80)], render_kw={'readonly': True})
    id_product = SelectField('Producto', coerce=int, validators=[DataRequired()], choices=[])
    sale_date = DateField('Fecha', validators=[DataRequired()], format='%Y-%m-%d', default=datetime.date.today, render_kw={'readonly': True})
    total_sale = StringField('Total de venta', validators=[DataRequired(), Length(min=1, max=10)])
    direction = StringField('Dirección', validators=[DataRequired(), Length(min=4, max=50)])
    pieces = StringField('Piezas', validators=[DataRequired(), Length(min=1, max=10)])
    submit = SubmitField('Register Sale')