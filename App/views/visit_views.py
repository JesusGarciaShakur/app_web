from flask import Blueprint, render_template, session, abort

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

@visit_views.route('/legal')
def legal():
    return render_template('legal/legal_information.html')

@visit_views.route('/privacidad')
def privacidad():
    return render_template('legal/Privaci_Policy.html')
