from flask import Flask

# Importar views
from views.admin_views import admin_views
from views.visit_views import visit_views


app = Flask(__name__)
app.config['SECRET_KEY'] = 'My Secret Key'

#Registrar views
app.register_blueprint(admin_views)
app.register_blueprint(visit_views)

if __name__ == '__main__':
    app.run(debug=True)