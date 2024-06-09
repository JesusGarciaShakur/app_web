#id_product, product_name, product_price,product_description
from flask_wtf import FlaskForm
from wtforms import FileField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileField, FileAllowed

#clase de registro de opiniones
class RegisterProduct(FlaskForm):
    product_name = StringField('Nombre Producto', validators=[DataRequired(), Length(min=5, max=50)])
    product_price = StringField('Precio Producto', validators=[DataRequired()])
    product_description = TextAreaField('Descripción Producto', validators=[DataRequired(), Length(min=5, max=500)])
    product_image = FileField('Imagen de Producto', validators=[ FileAllowed(['png'], 'Solo imágenes con extension png!')])
    submit = SubmitField('Registrar Producto')

class UpdateProduct(FlaskForm):
    product_name = StringField('Nombre Producto', validators=[DataRequired(), Length(min=5, max=50)])
    product_price = StringField('Precio Producto', validators=[DataRequired()])
    product_description = TextAreaField('Descripción Producto', validators=[DataRequired(), Length(min=5, max=500)])
    product_image = FileField('Imagen de Producto', validators=[ FileAllowed(['png'], 'Solo imágenes con extension png!')])
    submit = SubmitField('Actualizar Producto')