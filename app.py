from flask import Flask
import os

from db.models import db

from frontend.frontend import frontend_bp
from manager.manager import manager_bp
from db.media import media_bp

import filters

app = Flask(__name__)
app.secret_key = os.urandom(30)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///havas.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.register_blueprint(frontend_bp)
app.register_blueprint(manager_bp)
app.register_blueprint(media_bp)

app.jinja_env.filters["capit"] = filters.capit

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
