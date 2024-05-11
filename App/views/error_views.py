from flask import Blueprint, render_template # type: ignore

error_views = Blueprint('error', __name__)

@error_views.app_errorhandler(404)
def not_found_error_404(error):
    return render_template('error/404.html')

@error_views.app_errorhandler(403)
def not_found_error_403(error):
    return render_template('error/403.html')