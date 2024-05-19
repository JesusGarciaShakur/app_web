# Importaciones
from flask import Blueprint, render_template, session, abort
from models.users import User

admin_views = Blueprint('admin', __name__)

@admin_views.route('/admin/sales')
def admin_sales():
    if session.get('user') and session.get('user')['type'] == 1:
        return render_template('admin/sales.html')
    else:
        abort(403)

@admin_views.route('/admin/users')
def admin_users():
    if session.get('user') and session.get('user')['type'] == 1:
        users = User.get_all()
        return render_template('admin/users.html', users=users)
    else:
        abort(403)