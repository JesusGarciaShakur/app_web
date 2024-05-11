# user_views.py
from flask import Blueprint, render_template, redirect, url_for # type: ignore
from models.users import User, Position, Role
from forms.user_forms import RegisterForm, UpdateProfileForm

user_views = Blueprint('user', __name__)

@user_views.route('/user/register/', methods=('GET', 'POST'))
def register():
    form = RegisterForm()
    positions = Position.get_all()
    form.id_position.choices = [(p.id_position, p.name_position) for p in positions]
    roles = Role.get_all()
    form.id_role.choices = [(r.id_role, r.name_role) for r in roles]

    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        ape_mat = form.ape_mat.data
        ape_pat = form.ape_pat.data
        name = form.name.data
        direction = form.direction.data
        id_position = form.id_position.data
        id_role = form.id_role.data
        user = User(ape_mat=ape_mat, ape_pat=ape_pat, direction=direction, email=email, id_position=id_position, id_role=id_role, name=name, password=password, username=username)
        user.save()

        return redirect(url_for('admin.usuario'))
    for field, errors in form.errors.items():
        for error in errors:
            print(f"Error en el campo '{field}': {error}")

    return render_template('users/register.html', form=form)

@user_views.route('/users/<int:id_user>/update/', methods=('GET', 'POST'))
def update(id_user):
    form = UpdateProfileForm()
    positions = Position.get_all()
    form.id_position.choices = [(p.id_position, p.name_position) for p in positions]
    roles = Role.get_all()
    form.id_role.choices = [(r.id_role, r.name_role) for r in roles]
    user = User.get(id_user)
    if form.validate_on_submit():
        user.ape_mat = form.ape_mat.data
        user.ape_pat = form.ape_pat.data
        user.name = form.name.data
        user.direction = form.direction.data
        user.id_position = form.id_position.data
        user.id_role = form.id_role.data
        user.update()
        return redirect(url_for('admin.usuario'))
        # Actualiza los atributos del usuario con los datos ingresados
    form.ape_mat.data = user.ape_mat
    form.ape_pat.data = user.ape_pat
    form.name.data = user.name
    form.direction.data = user.direction
    form.id_position.data = user.id_position
    form.id_role.data = user.id_role
    return render_template('users/update.html', form=form, user=user)

@user_views.route('/users/<int:id_user>/delete/', methods=['POST'])
def delete(id_user):
    user = User.get(id_user)
    user.delete()
    return redirect(url_for('admin.usuario'))