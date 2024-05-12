from flask import Blueprint, render_template, redirect, url_for, flash, session
from models.users import User
from forms.user_forms import LoginForms
visit_views = Blueprint('visit', __name__)

@visit_views.route('/')
def index():
    return render_template('pages/index.html')

@visit_views.route('/product')
def product():
    return render_template('pages/product.html')

@visit_views.route('/contact')
def contact():
    return render_template('pages/contact.html')

@visit_views.route('/company')
def company():
    return render_template('pages/company.html')

