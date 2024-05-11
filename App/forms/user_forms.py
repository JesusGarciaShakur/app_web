# Importaciones
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField, EmailField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo, Length
#from models.


class RegisterForm(FlaskForm):
    username = StringField('Nombre de Usuario', validators = [DataRequired(), Length(min=4, max=25)])



    #Validar correo electronico unico

    def validate_email(self, field):
        if User.checkusername(field.data):
            raise ValidationError('El correo ya esta en uso')

    #Validar username unico
    def validate_username(self, field):
        if User.check_username(field.data):
            raise ValidationError('El username ya esta en uso')
        
#Clase para login
class LoginForms(FlaskForm):
    username = StringField('Nombre de Usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Ingresar')

class UpdaeProfileForm(FlaskForm):
    username = StringField('Nombre de Usuario', validators = [DataRequired(), Length(min=4, max=25)])