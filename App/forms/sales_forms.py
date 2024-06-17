import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, BooleanField
from wtforms.validators import DataRequired, Length, Optional

class RegisterSaleForm(FlaskForm):
    product_name = StringField('Producto', validators=[DataRequired()], render_kw={'readonly': True})
    userName_sale = StringField('Nombre de Usuario', validators=[DataRequired(), Length(min=1, max=80)], render_kw={'readonly': True})
    sale_date = DateField('Fecha', validators=[DataRequired()], format='%Y-%m-%d', default=datetime.date.today, render_kw={'readonly': True})
    total_sale = StringField('Total de venta', validators=[DataRequired(), Length(min=1, max=10)], render_kw={'readonly': True})
    direction = StringField('Dirección', validators=[Optional(), Length(min=4, max=50)])
    pieces = StringField('Piezas', validators=[DataRequired(), Length(min=1, max=10)])
    use_new_address = BooleanField('Usar nueva dirección')
    submit = SubmitField('Registrar Venta')
