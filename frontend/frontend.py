from flask import Blueprint, render_template, abort

from db.models import Article


frontend_bp = Blueprint(
    "frontend",
    __name__,
    template_folder="templates/",
    static_folder="static/",
    static_url_path="/static/frontend",
)


@frontend_bp.route("/")
def index():
    articles = Article.query.all()
    tags = set([tag for a in articles for tag in a.tags])

    return render_template("frontend_listing.html", articles=articles, tags=tags)


@frontend_bp.route("/tag/<string:tag>")
def tagpage(tag):
    articles = Article.query.all()
    filtered = [a for a in articles if tag in a.tags]
    tags = set([tag for a in articles for tag in a.tags])

    return render_template("frontend_listing.html", articles=filtered, tags=tags, this_page_tag=tag)


@frontend_bp.route("/article/<string:id>")
def view_article(id):
    article = Article.query.get(id)
    if article:
        return render_template("frontend_article.html", article=article)

    abort(404)
