from flask import Blueprint, render_template, session, abort
from models.users import User

admin_views = Blueprint('admin', __name__)

# @admin_views.route('/')
# def index():
#     return render_template('pages/index.html')
