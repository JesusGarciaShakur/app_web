from flask import Flask

# Importar views
from views.admin_views import admin_views
from views.visit_views import visit_views
from views.user_views import user_views
from views.legal_views import legal_views
from views.home_views import home_views
from views.error_views import error_views


app = Flask(__name__)
app.config['SECRET_KEY'] = 'My Secret Key'

#Registrar views
app.register_blueprint(admin_views)
app.register_blueprint(visit_views)
app.register_blueprint(user_views)
app.register_blueprint(legal_views)
app.register_blueprint(home_views)
app.register_blueprint(error_views)

if __name__ == '__main__':
    app.run(debug=True)