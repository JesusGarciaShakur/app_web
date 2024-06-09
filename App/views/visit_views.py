import datetime
from flask import Blueprint, render_template, redirect, url_for, flash, session
from models.comments import Comment
from models.opinions import Opinion
from models.products import Product
from forms.comment_forms import CommentForm
from forms.opinion_forms import OpinionForm

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
