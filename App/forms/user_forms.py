# Importaciones
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, EmailField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo, Length
from models.users import User

#Clase para registro
class RegisterForm(FlaskForm):
    id_type = SelectField('Tipo de Usuario', coerce=int, validators=[DataRequired()], choices=[])
    user_username = StringField('Nombre de Usuario', validators = [DataRequired(), Length(min=4, max=25)])
    user_name = StringField('Nombre(s)', validators = [DataRequired(), Length(min=4, max=25)])
    user_lastname = StringField('Apellido(s)', validators = [DataRequired(), Length(min=4, max=25)])
    user_email = EmailField('Correo Electrónico', validators = [DataRequired(), Email()])
    user_password = PasswordField('Contraseña', validators = [DataRequired(), Length(min=8)])
    user_password_confirm = PasswordField('Confirmar contraseña', validators=[DataRequired(), EqualTo('user_password')])
    user_direction = StringField('Dirección', validators = [DataRequired(), Length(min=4, max=100)])
    user_phoneNumber = StringField('Teléfono', validators = [DataRequired(),Length(min=10, max=10)])
    submit = SubmitField('Registrarse')

    #Validar correo electrónico único
    def validate_user_email(self, field):
        if User.check_email(field.data):
            raise ValidationError('El correo ya esta en uso')
        

    #Validar username único
    def validate_user_username(self, field):
        if User.check_username(field.data):
            raise ValidationError('El username ya esta en uso')
        
#Clase para login
class LoginForms(FlaskForm):
    user_username = StringField('Nombre de Usuario', validators=[DataRequired()])
    user_password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Ingresar')

#Clase para actualizar perfil
class UpdateProfileForm(FlaskForm):
    id_type = SelectField('Tipo de Usuario', coerce=int, validators=[DataRequired()], choices=[])
    user_username = StringField('Nombre de Usuario', validators = [DataRequired(), Length(min=4, max=25)])
    user_name = StringField('Nombre(s)', validators = [DataRequired(), Length(min=4, max=25)])
    user_lastname = StringField('Apellido(s)', validators = [DataRequired(), Length(min=4, max=25)])
    user_email = EmailField('Correo Electrónico', validators = [DataRequired(), Email()])
    user_password = PasswordField('Contraseña', validators = [DataRequired(), Length(min=8)])
    user_password_confirm = PasswordField('Confirmar contraseña', validators=[DataRequired(), EqualTo('user_password')])
    user_direction = StringField('Dirección', validators = [DataRequired(), Length(min=4, max=100)])
    user_phoneNumber = StringField('Teléfono', validators = [DataRequired(),Length(min=10, max=10)])
    submit = SubmitField('Actualizar información')