import datetime
from flask import Blueprint, abort, render_template, redirect, request, url_for, flash, session
from forms.user_forms import UpdateUserVisitForm, UpdateProfileForm
from utils.file_handler import save_image
from models.comments import Comment
from models.opinions import Opinion
from models.products import Product
from models.sales import Sale
from models.users import Type, User
from forms.comment_forms import CommentForm
from forms.opinion_forms import OpinionForm
from forms.sales_forms import RegisterSaleForm


visit_views = Blueprint('visit', __name__)

@visit_views.route('/')
def index():
    return render_template('pages/index.html')

@visit_views.route('/product', methods=['GET', 'POST'])
def product():
    form = OpinionForm()
    products = Product.get_all()
    form.id_product.choices = [(product.id_product, product.product_name) for product in products]
    opinions = Opinion.get_all()
    product = Product.get_all()
    if 'user' in session:
        user = session['user']
        form.username_opinion.data = user.get('user_username')
        form.date_opinion.data = datetime.date.today()
    if form.validate_on_submit():
        username_opinion = form.username_opinion.data
        id_product = form.id_product.data
        rating_product = form.rating_product.data
        comment_opinion = form.comment_opinion.data
        date_opinion = form.date_opinion.data
        opinion = Opinion(username_opinion=username_opinion,
                        id_product=id_product,
                        rating_product=rating_product,
                        comment_opinion=comment_opinion,
                        date_opinion=date_opinion)
        opinion.save()
        return redirect(url_for('visit.product'))
    return render_template('pages/product.html', form=form, opinions=opinions, products=products)

@visit_views.route('/product_list', methods=['GET', 'POST'])
def product_list():
    form = RegisterSaleForm()
    products = Product.get_all()
    product_prices = {product.id_product: product.product_price for product in products}

    if 'user' in session:
        user = session['user']
        form.userName_sale.data = user.get('user_username')
        form.sale_date.data = datetime.date.today()
        form.direction.data = user.get('user_direction')

    if form.validate_on_submit():
        userName_sale = form.userName_sale.data
        id_product = request.form.get('id_product')  # Obtener el ID del producto del formulario
        product_name = request.form.get('product_name')
        sale_date = form.sale_date.data
        total_sale = form.total_sale.data  # Puedes calcularlo o actualizarlo según sea necesario
        direction = form.direction.data
        pieces = form.pieces.data
        sale = Sale(
            userName_sale=userName_sale,
            product_name=product_name,
            sale_date=sale_date,
            total_sale=total_sale,
            direction=direction,
            pieces=pieces
        )
        sale.save()
        return redirect(url_for('visit.product_list'))

    return render_template('pages/list_products.html', form=form, product_prices=product_prices, products=products)



@visit_views.route('/contact', methods=['GET', 'POST'])
def contact():
    form = CommentForm()
    if 'user' in session:
        user = session['user']
        form.email_comment.data = user.get('user_email')
        form.date_comment.data = datetime.date.today()
        form.nameUser_comment.data = user.get('user_username')
        
    if form.validate_on_submit():
        content_comment = form.content_comment.data
        email_comment = form.email_comment.data
        date_comment = form.date_comment.data
        nameUser_comment = form.nameUser_comment.data
        comentario = Comment(content_comment=content_comment,
                            email_comment=email_comment, 
                            date_comment=date_comment, 
                            nameUser_comment=nameUser_comment)
        comentario.save()
        return redirect(url_for('visit.contact'))
    
    return render_template('pages/contact.html', form=form)

@visit_views.route('/company')
def company():
    return render_template('pages/company.html')

@visit_views.route('/profile')
def profile():
    user = User.__get__(id_user=session['user']['id_user'])
    return render_template('pages/profile.html', user=user)


@visit_views.route('/users/<int:id_user>/update/info', methods=('GET', 'POST'))
def update_info(id_user):
    # Verifica si el ID del usuario en la sesión coincide con el ID en la URL
    logged_in_id_user = session['user']['id_user']
    if logged_in_id_user != id_user:
        abort(403)
    form = UpdateUserVisitForm()
    user = User.get(id_user)
    if form.validate_on_submit():
        user.user_name = form.user_name.data
        user.user_lastname = form.user_lastname.data
        user.user_direction = form.user_direction.data
        user.user_phoneNumber = form.user_phoneNumber.data
        user.update()
        return redirect(url_for('visit.index'))
        # Actualiza los atributos del usuario con los datos ingresados

    form.user_name.data = user.user_name
    form.user_lastname.data = user.user_lastname
    form.user_direction.data = user.user_direction
    form.user_phoneNumber.data = user.user_phoneNumber
    return render_template('pages/update_info.html', form=form, user=user)

@visit_views.route('/users/<int:id_user>/update/profile', methods=('GET', 'POST'))
def update_profile(id_user):
        # Verifica si el ID del usuario en la sesión coincide con el ID en la URL
    logged_in_id_user = session['user']['id_user']
    if logged_in_id_user != id_user:
        abort(403)
    form = UpdateProfileForm()
    types = Type.get_all()
    form.id_type.choices = [(type.id_type, type.type_name) for type in types]
    user = User.get(id_user)
    if form.validate_on_submit():
        user.id_type = form.id_type.data
        user.user_username = form.user_username.data
        user.user_email = form.user_email.data
        user.user_password = form.user_password.data
        f = form.user_image.data
        if f:
            user.user_image = save_image(f, 'images/profiles', user.user_username)
        else:
            user.user_image = user.user_image  # Mantener valor existente si no hay imagen nueva
        user.update()
        return redirect(url_for('visit.index'))
    else:
        # Imprimir errores de validación para depuración
        print(form.errors)
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"Error en el campo {field}: {error}", 'danger')

    form.id_type.data = user.id_type
    form.user_username.data = user.user_username
    form.user_email.data = user.user_email
    form.user_password.data = user.user_password
    return render_template('pages/update_profile.html', form=form, user=user)

@visit_views.route('/users/<int:id_user>/delete/', methods=['POST'])
def delete_profile(id_user):
    user = User.get(id_user)
    user.delete()
    return redirect(url_for('visit.index'))