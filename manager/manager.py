from flask import Blueprint, render_template

from db.models import Article


manager_bp = Blueprint(
    "manager",
    __name__,
    url_prefix="/manager",
    template_folder="templates/",
    static_folder="static/",
)


@manager_bp.route("/")
def index():
    articles = Article.query.all()

    return render_template("manager_index.html", articles=articles)


@manager_bp.route("/add_article")
def add_article():
    return "", 200


@manager_bp.route("/editor/<string:id>")
def editor(id):
    article = Article.query.get(id)

    return render_template("manager_editor.html", article=article)


@manager_bp.route("/save_api", methods=["POST"])
def save_api():
    return "", 200
