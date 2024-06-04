#id_product, product_name, product_price,product_description
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

#clase de registro de opiniones
class RegisterProduct(FlaskForm):
    product_name = StringField('Nombre Producto', validators=[DataRequired(), Length(min=5, max=50)])
    product_price = StringField('Precio Producto', validators=[DataRequired()])
    product_description = TextAreaField('Descripción Producto', validators=[DataRequired(), Length(min=5, max=500)])
    submit = SubmitField('Registrar Producto')

class UpdateProduct(FlaskForm):
    product_name = StringField('Nombre Producto', validators=[DataRequired(), Length(min=5, max=50)])
    product_price = StringField('Precio Producto', validators=[DataRequired()])
    product_description = TextAreaField('Descripción Producto', validators=[DataRequired(), Length(min=5, max=500)])
    submit = SubmitField('Actualizar Producto')