from flask import Blueprint, render_template, redirect, url_for, flash, session
from models.users import User
from forms.user_forms import LoginForms

home_views = Blueprint('home', __name__)

@home_views.route('/signin', methods=['GET', 'POST'])
def signin():
    form = LoginForms()
    if form.validate_on_submit():
        user_username = form.user_username.data
        user_password = form.user_password.data
        user = User.get_by_password(user_username, user_password)
        if not user:
            flash('Verifica tus Datos')
        else:
            session['user'] = {'user_username': user.user_username, 'role': user.id_type}  # Almacenamos el ID del usuario en la sesión
            if user.id_type == 1:
                # Redireccionar a la vista de administrador
                return redirect(url_for('admin.sesion_admin'))
            elif user.id_type == 2:
                # Redireccionar a la vista de empleado
                return redirect(url_for('entry.sesion_empleado'))
            else:
                flash('No tienes un rol válido', 'error')
    return render_template('pages/signin.html', form=form)

@home_views.route('/logout/')
def logout():
    print('Cerrando session')
    session.clear()
    print(session)  # Remueve el ID del usuario de la sesión
    flash('Has cerrado sesión', 'success')
    return redirect(url_for('home.login'))  # Redirige al formulario de inicio de sesión