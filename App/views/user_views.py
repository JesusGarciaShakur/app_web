# user_views.py
from flask import Blueprint, render_template, redirect, url_for # type: ignore
from models.users import User, Type
from forms.user_forms import RegisterForm, UpdateProfileForm
# Importaciones comments
from models.comments import Comment
from forms.comment_forms import CommentForm, UpdateCommentForm

user_views = Blueprint('user', __name__)

@user_views.route('/user/register/', methods=('GET', 'POST'))
def register():
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
        user = User(id_type = id_type ,user_username = user_username, user_name=user_name, user_lastname=user_lastname, user_email=user_email, user_password=user_password, user_direction=user_direction, user_phoneNumber=user_phoneNumber)
        user.save()

        return redirect(url_for('visit.index'))
    for field, errors in form.errors.items():
        for error in errors:
            print(f"Error en el campo '{field}': {error}")

    return render_template('pages/signup.html', form=form)

@user_views.route('/users/<int:id_user>/update/', methods=('GET', 'POST'))
def update(id_user):
    form = UpdateProfileForm()
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
        return redirect(url_for('visit.index'))
        # Actualiza los atributos del usuario con los datos ingresados
    form.id_type.data = user.id_type
    form.user_username.data = user.user_username
    form.user_name.data = user.user_name
    form.user_lastname.data = user.user_lastname
    form.user_email.data = user.user_email
    form.user_password.data = user.user_password
    form.user_direction.data = user.user_direction
    form.user_phoneNumber.data = user.user_phoneNumber
    return render_template('pages/signup.html', form=form, user=user)

@user_views.route('/users/<int:id_user>/delete/', methods=['POST'])
def delete(id_user):
    user = User.get(id_user)
    user.delete()
    return redirect(url_for('visit.index'))

#id_comment, content_comment, email_comment, 
#date_comment, nameUser_comment
@user_views.route('/comment/register/', methods=('GET', 'POST'))
def realize_comment():
    form = CommentForm()
    if form.validate_on_submit():
        content_comment = form.content_comment.data
        email_comment = form.email_comment.data
        date_comment = form.date_comment.data
        nameUser_comment = form.nameUser_comment.data
        comment = Comment(content_comment = content_comment, email_comment=email_comment, date_comment=date_comment, nameUser_comment=nameUser_comment)
        comment.save()

        return redirect(url_for('visit.index'))
    for field, errors in form.errors.items():
        for error in errors:
            print(f"Error en el campo '{field}': {error}")

    return render_template('pages/contact.html', form=form)

@user_views.route('/comment/<int:id_user>/update/', methods=('GET', 'POST'))
def update_comment(id_comment):
    form = UpdateCommentForm()
    comment = Comment.get(id_comment)
    if form.validate_on_submit():
        comment.content_comment = form.content_comment.data
        comment.email_comment = form.email_comment.data
        comment.date_comment = form.date_comment.data
        comment.nameUser_comment = form.nameUser_comment.data
        comment.update()
        return redirect(url_for('visit.index'))
        # Actualiza los atributos del usuario con los datos ingresados
    form.content_comment.data = comment.content_comment
    form.email_comment.data = comment.email_comment
    form.date_comment.data = comment.date_comment
    form.nameUser_comment.data = comment.nameUser_comment
    return render_template('pages/contact.html', form=form, comment=comment)

@user_views.route('/comment/<int:id_user>/delete/', methods=['POST'])
def delete_comment(id_comment):
    comment = Comment.get(id_comment)
    comment.delete()
    return redirect(url_for('visit.index'))