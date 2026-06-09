from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

# Usuario temporal para pruebas
class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

def create_app():
    app = Flask(__name__, template_folder='templates')

    app.config['SECRET_KEY'] = 'mi_clave_secreta'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bd_equipo.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = '123456789'

    db.init_app(app)
    migrate.init_app(app, db)

    # Inicializar Flask-Login
    login_manager.init_app(app)
    login_manager.login_view = 'bp_auth.login'

    # Blueprints
    from blueprintapp.miembros.routes import bp_miembro
    from blueprintapp.core.routes import bp_core
    from blueprintapp.tareas.routes import bp_tarea
    from blueprintapp.auth.routes import bp_auth

    app.register_blueprint(bp_auth, url_prefix="/auth")
    app.register_blueprint(bp_miembro, url_prefix="/miembros")
    app.register_blueprint(bp_core, url_prefix="/")
    app.register_blueprint(bp_tarea, url_prefix="/tareas")

    return app