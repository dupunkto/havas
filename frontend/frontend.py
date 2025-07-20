from flask import Blueprint, render_template, abort, request

from db.models import Article


frontend_bp = Blueprint(
    "frontend",
    __name__,
    template_folder="templates/",
    static_folder="static/",
    static_url_path="/static/frontend",
)


@frontend_bp.context_processor
def inject_tags():
    articles = Article.query.all()
    tags = set(tag for a in articles for tag in a.tags)
    return dict(tags=tags)


@frontend_bp.route("/")
def index():
    articles = Article.query.order_by(Article.datetime_made.desc()).all()

    return render_template("frontend_listing.html", articles=articles)


@frontend_bp.route("/tag/<string:tag>")
def tagpage(tag):
    articles = Article.query.order_by(Article.datetime_made.desc()).all()
    filtered = [a for a in articles if tag in a.tags]
    return render_template(
        "frontend_listing.html", articles=filtered, this_page_tag=tag
    )


@frontend_bp.route("/article/<string:id>")
def view_article(id):
    article = Article.query.get(id)
    if article:
        return render_template("frontend_article.html", article=article)

    abort(404)


@frontend_bp.route("/search")
def search_article():
    search_term = request.args.get("q", "")
    query = search_term.lower()
    articles = (
        Article.query.filter(Article.title.ilike(f"%{query}%"))
        .order_by(Article.datetime_made.desc())
        .all()
    )
    return render_template(
        "frontend_searchresult.html", articles=articles, search_term=search_term
    )
