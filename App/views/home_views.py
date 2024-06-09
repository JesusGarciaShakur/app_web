from flask import Blueprint, render_template, redirect, url_for, flash, session, request
from models.users import User
from forms.user_forms import LoginForms

home_views = Blueprint('home', __name__)

@home_views.route('/signin', methods=['GET', 'POST'])
def signin():
    form = LoginForms()
    if form.validate_on_submit():
        user_username = form.user_username.data
        user_password = form.user_password.data
        print(f"Trying to authenticate user: {user_username}")
        user = User.get_by_password(user_username, user_password)
        if not user:
            flash('Verifica tus Datos')
            print("Authentication failed: Invalid username or password")
        else:
            session['user'] = {
                'id_user': user.id_user,
                'user_email': user.user_email,
                'user_username': user.user_username,
                'type': user.id_type
            }
            print(f"User authenticated: {user.user_username} with type: {user.id_type}")
            if user.id_type == 1:
                return redirect(url_for('admin.admin_users'))
            elif user.id_type == 2:
                return redirect(url_for('visit.index'))
            else:
                flash('No tienes un rol válido', 'error')
                print("Invalid user role")
    else:
        print("Form validation failed")

    return render_template('pages/signin.html', form=form)

@home_views.route('/logout/')
def logout():
    print('Cerrando sesión')
    session.clear()
    print(session)  # Remueve el ID del usuario de la sesión
    flash('Has cerrado sesión', 'success')
    return redirect(url_for('home.signin'))  # Redirige al formulario de inicio de sesión
