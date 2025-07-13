from flask import Blueprint, render_template, request, redirect, url_for, flash

from db.models import Article, db

from datetime import datetime, timezone
import markdown

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


def build_HTML(markdown_input):
    return markdown.markdown(markdown_input)


@manager_bp.route("/save_api", methods=["POST"])
def save_api():
    article_id = request.form.get("id")
    article = Article.query.get(article_id)
    if not article:
        flash("Article not found", "error")
        return redirect(url_for("manager.index"))

    article.title = request.form.get("title", article.title)
    article.description = request.form.get("description", article.description)
    article.content = request.form.get("content", article.content)
    article.html = build_HTML(request.form.get("content", article.content))
    article.datetime_edited = datetime.now(timezone.utc)

    db.session.commit()
    flash("Article saved", "success")
    return redirect(url_for("manager.editor", id=article.id))
