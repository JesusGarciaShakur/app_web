# Importaciones
from flask import Blueprint, redirect, render_template, session, abort, url_for
from models.users import User
from models.type import Type
from forms.user_forms import RegisterForm, UpdateProfileForm

admin_views = Blueprint('admin', __name__)

@admin_views.route('/admin/sales')
def admin_sales():
    if session.get('user') and session.get('user')['type'] == 1:
        return render_template('admin/sales.html')
    else:
        abort(403)

@admin_views.route('/admin/users')
def admin_users():
    if session.get('user') and session.get('user')['type'] == 1:
        users = User.get_all()
        return render_template('admin/users_admin.html', users=users)
    else:
        abort(403)

@admin_views.route('/admin/register/users', methods=('GET', 'POST'))
def admin_register_users():
    if session.get('user') and session.get('user')['type'] == 1:
        form = RegisterForm()
        types = Type.get_all()
        form.id_type.choices = [(type.id_type, type.type_name) for type in types]

        if form.validate_on_submit():
            id_type = form.id_type.data
            user_username = form.user_username.data
            user_name = form.user_name.data
            user_lastname = form.user_lastname.data
            user_email = form.user_email.data
            user_password = form.user_password.data
            user_direction = form.user_direction.data
            user_phoneNumber = form.user_phoneNumber.data
            user = User(id_type=id_type, user_username=user_username, user_name=user_name, user_lastname=user_lastname, user_email=user_email, user_password=user_password, user_direction=user_direction, user_phoneNumber=user_phoneNumber)
            user.save()

            return redirect(url_for('admin.admin_users'))

        for field, errors in form.errors.items():
            for error in errors:
                print(f"Error en el campo '{field}': {error}")

        return render_template('admin/register_user.html', form=form)
    else:
        abort(403)

@admin_views.route('/admin/users/<int:id_user>/update', methods=('GET', 'POST'))
def admin_update_users(id_user):
    if session.get('user') and session.get('user')['type'] == 1:
        form = UpdateProfileForm()
        types = Type.get_all()
        form.id_type.choices = [(type.id_type, type.type_name) for type in types]
        user = User.get(id_user)
        if form.validate_on_submit():
            user.id_type = form.id_type.data
            user.username = form.user_username.data
            user.user_name = form.user_name.data
            user.user_lastname = form.user_lastname.data
            user.user_email = form.user_email.data
            user.user_password = form.user_password.data
            user.user_direction = form.user_direction.data
            user.user_phoneNumber = form.user_phoneNumber.data
            user.update()
            return redirect(url_for('admin.admin_users'))
        
        form.id_type.data = user.id_type
        form.user_username.data = user.user_username
        form.user_name.data = user.user_name
        form.user_lastname.data = user.user_lastname
        form.user_email.data = user.user_email
        form.user_password.data = user.user_password
        form.user_direction.data = user.user_direction
        form.user_phoneNumber.data = user.user_phoneNumber
        return render_template('admin/update_user.html', form=form, user=user)

@admin_views.route('/admin/users/<int:id_user>/delete', methods=['POST'])
def admin_delete_users(id_user):
    if session.get('user') and session.get('user')['type'] == 1:
        user = User.get(id_user)
        user.delete()
        return redirect(url_for('admin.admin_users'))
    else:
        abort(403)