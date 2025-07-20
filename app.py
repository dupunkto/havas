from flask import Flask, render_template
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


@app.errorhandler(404)
def page_not_found(e):
    return render_template("error/404.html"), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template("error/500.html"), 500


if __name__ == "__main__":
    app.run(debug=True)
