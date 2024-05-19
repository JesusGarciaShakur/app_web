import datetime
from flask import Blueprint, render_template, redirect, url_for, flash, session
from models.comments import Comment
from models.users import User
from forms.comment_forms import CommentForm

visit_views = Blueprint('visit', __name__)

@visit_views.route('/')
def index():
    return render_template('pages/index.html')

@visit_views.route('/product')
def product():
    return render_template('pages/product.html')

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
