# Importaciones
from flask import Blueprint, redirect, render_template, session, abort, url_for
from models.users import User
from models.type import Type
from models.comments import Comment
from models.products import Product
from models.sales import Sale
from forms.user_forms import RegisterForm, UpdateUserForm
from forms.products_forms import RegisterProduct, UpdateProduct
from utils.file_handler import save_image
from flask import request
from flask import make_response
from flask import jsonify

admin_views = Blueprint('admin', __name__)

@admin_views.route('/admin/users')
def admin_users():
    if session.get('user') and session.get('user')['type'] == 1:
        page = request.args.get('page', 1, type=int)
        per_page = 1
        users, total = User.get_paginated_users(page, per_page)
        total_pages = (total + per_page - 1) // per_page
        
        return render_template('admin/users_admin.html', users=users, page=page, total_pages=total_pages)
    else:
        abort(403)

@admin_views.route('/get_users')
def get_users():
    page = request.args.get('page', 1, type=int)
    per_page = 10
    users, total = User.get_paginated_users(page, per_page)

    users_dict = [
        {
            'id_user': user.id_user,
            'id_type': user.id_type,
            'user_username': user.user_username,
            'user_name': user.user_name,
            'user_lastname': user.user_lastname,
            'user_email': user.user_email,
            'user_direction': user.user_direction,
            'user_phoneNumber': user.user_phoneNumber
        }
        for user in users
    ]

    response = make_response(jsonify({'users':users_dict, 'total': total, 'page': page, 'per_page': per_page}))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@admin_views.route('/admin/sales')
def admin_sales():
    if session.get('user') and session.get('user')['type'] == 1:
        sales = Sale.get_all()
        return render_template('admin/sales_admin.html', sales=sales)
    else:
        abort(403)

@admin_views.route('/admin/comments')
def admin_comments():
    if session.get('user') and session.get('user')['type'] == 1:
        comments = Comment.get_all()
        return render_template('admin/comments_admin.html', comments=comments)
    else:
        abort(403)

@admin_views.route('/admin/products')
def admin_products():
    if session.get('user') and session.get('user')['type'] == 1:
        products = Product.get_all()
        return render_template('admin/products_admin.html', products=products)
    else:
        abort(403)

@admin_views.route('/admin/register/products', methods=('GET', 'POST'))
def admin_register_products():
    if session.get('user') and session.get('user')['type'] == 1:
        form = RegisterProduct()
        if form.validate_on_submit():
            product_name = form.product_name.data
            product_price = form.product_price.data
            product_description = form.product_description.data
            f = form.product_image.data
            
            # Crear el producto primero
            product = Product(product_name=product_name, product_price=product_price, product_description=product_description)
            
            # Si hay una imagen, guardarla después de crear el producto
            if f:
                product.product_image = save_image(f, 'images/products', product.product_name)
            
            # Guardar el producto en la base de datos
            product.save()
            return redirect(url_for('admin.admin_products'))
        
        for field, errors in form.errors.items():
            for error in errors:
                print(f"Error en el campo '{field}': {error}")
        return render_template('admin/register_product.html', form=form)
    else:
        abort(403)

@admin_views.route('/admin/products/<int:id_product>/update', methods=('GET', 'POST'))
def admin_update_products(id_product):
    if session.get('user') and session.get('user')['type'] == 1:
        form = UpdateProduct()
        product = Product.get(id_product)
        if form.validate_on_submit():
            product.product_name = form.product_name.data
            product.product_price = form.product_price.data
            product.product_description = form.product_description.data
            f = form.product_image.data
            if f:
                product.product_image = save_image(f, 'images/products', product.product_name)
            else:
                product.product_image = product.product_image  # Mantener valor existente si no hay imagen nueva
            
            product.update()
            return redirect(url_for('admin.admin_products'))
        
        form.product_name.data = product.product_name
        form.product_price.data = product.product_price
        form.product_description.data = product.product_description

        return render_template('admin/update_product.html', form=form, product=product)

@admin_views.route('/admin/products/<int:id_product>/delete', methods=['POST'])
def admin_delete_products(id_product):
    if session.get('user') and session.get('user')['type'] == 1:
        product = Product.get(id_product)
        product.delete()
        return redirect(url_for('admin.admin_products'))
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
            f = form.user_image.data
            # Crear el usuario primero
            user = User(id_type=id_type, user_username=user_username, user_name=user_name, user_lastname=user_lastname, 
                        user_email=user_email, user_password=user_password, 
                        user_direction=user_direction, user_phoneNumber=user_phoneNumber)
            # Si hay una imagen, guardarla después de crear el usuario
            if f:
                user.user_image = save_image(f, 'images/profiles', user.user_username)
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
        form = UpdateUserForm()
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
            f = form.user_image.data
            if f:
                user.user_image = save_image(f, 'images/profiles', user.user_username)
            else:
                user.user_image = user.user_image  # Mantener valor existente si no hay imagen nueva
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