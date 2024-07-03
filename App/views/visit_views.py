from flask import make_response
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from flask import Blueprint, abort, jsonify, render_template, redirect, request, url_for, flash, session
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

from models.db import get_connection

mydb = get_connection()

visit_views = Blueprint('visit', __name__)

@visit_views.route('/')
def index():
    return render_template('pages/index.html')

@visit_views.route('/product', methods=['GET', 'POST'])
def product():
    form = OpinionForm()
    products = Product.get_all()
    form.id_product.choices = [(product.id_product, product.product_name) for product in products]
    
    page = request.args.get('page', 1, type=int)
    per_page = 5
    opinions, total_opinions = Opinion.get_paginated_comments(page, per_page)
    
    if 'user' in session:
        user = session['user']
        form.username_opinion.data = user.get('user_username')
        form.date_opinion.data = datetime.date.today()
    
    if request.method == 'POST':
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
            flash('Tu calificación ha sido registrada correctamente.', 'success')
            return redirect(url_for('visit.product'))
        else:
            flash('Error al registrar la calificación. Por favor, revisa los datos ingresados.', 'error')
    
    # En el caso de GET o si hay errores en el formulario, renderiza la plantilla con los datos necesarios.
        return render_template('pages/product.html', form=form, opinions=opinions, products=products, total_opinions=total_opinions, page=page, per_page=per_page)
    
    # En el caso de GET o si hay errores en el formulario, renderiza la plantilla con los datos necesarios.
    return render_template('pages/product.html', form=form, opinions=opinions, products=products)


@visit_views.route('/product_list', methods=['GET', 'POST'])
def product_list():
    form = RegisterSaleForm()
    user = User.get_all()
    products = Product.get_all()
    product_prices = {product.id_product: product.product_price for product in products}

    if 'user' in session:
        user = session['user']
        form.userName_sale.data = user.get('user_username')
        form.sale_date.data = datetime.date.today()
    
    if request.method == 'POST':
        if form.validate_on_submit():
            userName_sale = form.userName_sale.data
            id_product = request.form.get('id_product')
            product_name = request.form.get('product_name')
            sale_date = form.sale_date.data
            total_sale = form.total_sale.data
            pieces = form.pieces.data

            if form.use_new_address.data:
                direction = form.direction.data
            else:
                direction = user.get('user_direction')

            sale = Sale(
                userName_sale=userName_sale,
                product_name=product_name,
                sale_date=sale_date,
                total_sale=total_sale,
                direction=direction,
                pieces=pieces
            )
            sale.save()
                        # Enviar correo electrónico con la información del usuario
            user_info = {
                'user_name': user.get('user_name'),
                'user_lastname': user.get('user_lastname'),
                'user_email': user.get('user_email'),
                'user_phoneNumber': user.get('user_phoneNumber')
            }

            # Enviar correo electrónico
            send_email(userName_sale, product_name, sale_date, total_sale, direction, pieces, user_info)

            flash('Solicitud registrada correctamente, en breve nos pondremos en contacto con usted.', 'success')
            return redirect(url_for('visit.product_list'))
        else:
            flash('Error al registrar la venta. Por favor, revise los datos ingresados.', 'error')
    
    return render_template('pages/list_products.html', form=form, product_prices=product_prices, products=products, user=user)

def send_email(userName_sale, product_name, sale_date, total_sale, direction, pieces, user_info):
    try:
        # Configuración del servidor SMTP
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        smtp_username = 'meztlicode@gmail.com'
        smtp_password = 'bxpl scep qciv gaby'  # Usa la contraseña de aplicación generada

        # Configuración del mensaje
        msg = MIMEMultipart()
        msg['From'] = smtp_username
        msg['To'] = 'meztlicode@gmail.com'
        msg['Subject'] = 'Nueva Solicitud de Instalación'

        body = f'''
        Nueva solicitud de instalación registrada:

        Usuario: {userName_sale}
        Producto: {product_name}
        Fecha de venta: {sale_date}
        Total de la venta: ${total_sale}
        Dirección de instalación: {direction}
        Piezas solicitadas: {pieces}
        
        Información del Usuario:

        Nombre: {user_info['user_name']}
        Apellidos: {user_info['user_lastname']}
        Número de Teléfono: {user_info['user_phoneNumber']}
        Correo Electrónico: {user_info['user_email']}
        '''
        msg.attach(MIMEText(body, 'plain'))

        # Conexión y envío del correo
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(msg)
        server.quit()
    except Exception as e:
        print(f"Error al enviar el correo: {e}")
        
@visit_views.route('/contact', methods=['GET', 'POST'])
def contact():
    form = CommentForm()
    
    if 'user' in session:
        user = session['user']
        form.email_comment.data = user.get('user_email')
        form.date_comment.data = datetime.date.today()
        form.nameUser_comment.data = user.get('user_username')
    
    if request.method == 'POST':
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
            flash('Comentario enviado correctamente.', 'success')
            return redirect(url_for('visit.contact'))
        else:
            flash('Error al enviar el comentario. Por favor, revise los datos ingresados.', 'error')
    
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
        f = form.user_image.data
        if f:
            user.user_image = save_image(f, 'images/profiles', user.user_username)
        else:
            user.user_image = user.user_image  # Mantener valor existente si no hay imagen nueva
        user.update()
        return redirect(url_for('visit.profile'))

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
        user.update()
        return redirect(url_for('visit.profile'))
        # Actualiza los atributos del usuario con los datos ingresados
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

@visit_views.route('/get_comments')
def get_comments():
    page = request.args.get('page', 1, type=int)
    per_page = 5
    
    comments, total = Opinion.get_paginated_comments(page, per_page)
    
    comments_dict = [{
        'id_opinion': comment.id_opinion,
        'username_opinion': comment.username_opinion,
        'id_product': comment.id_product,
        'rating_product': comment.rating_product,
        'comment_opinion': comment.comment_opinion,
        'date_opinion': comment.date_opinion
    } for comment in comments]

    response = make_response(jsonify({'comments': comments_dict, 'total': total, 'page': page, 'per_page': per_page}))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response
