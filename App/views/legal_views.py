from flask import Blueprint, render_template

legal_views = Blueprint('legal', __name__)

@legal_views.route('/legal_information')
def legal_information():
    return render_template('legal/legal_information.html')

@legal_views.route('/privacy_policy')
def privacy_policy():
    return render_template('legal/privacy_policy.html')

@legal_views.route('/terms_of_service')
def terms_of_service():
    return render_template('legal/terms_of_service.html')