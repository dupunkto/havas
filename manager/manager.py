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
    articles = Article.query.order_by(Article.datetime_edited.desc()).all()

    return render_template("manager_index.html", articles=articles)


@manager_bp.route("/add_article")
def add_article():
    return redirect(url_for("manager.editor", id="new"))


@manager_bp.route("/editor")
def editor_apex():
    articles = Article.query.order_by(Article.datetime_edited.desc()).all()

    header_text = "Recently edited"

    return render_template(
        "manager_listing.html", articles=articles, header_text=header_text
    )


@manager_bp.route("/editor/<string:id>")
def editor(id):
    if id == "new":
        article = Article(
            title="Title",
            description="Description",
            content="Content",
            html="<p>Content</p>",
            datetime_made=datetime.now(timezone.utc),
            datetime_edited=datetime.now(timezone.utc),
        )
    else:
        article = Article.query.get(id)

    return render_template("manager_editor.html", article=article)


def build_HTML(markdown_input):
    return markdown.markdown(markdown_input)


@manager_bp.route("/save_api", methods=["POST"])
def save_api():
    article_id = request.form.get("id")
    article = Article.query.get(article_id)

    def split_and_clean(field):
        return [x for x in request.form.get(field, "").split(";") if x.strip()]

    if not article:
        flash("Made new article", "success")
        new_article = Article(
            title=request.form.get("title"),
            description=request.form.get("description"),
            content=request.form.get("content"),
            authors=split_and_clean("authors"),
            tags=split_and_clean("tags"),
            html=build_HTML(request.form.get("content")),
            datetime_made=datetime.now(timezone.utc),
            datetime_edited=datetime.now(timezone.utc),
        )
        db.session.add(new_article)
        db.session.commit()
        return redirect(url_for("manager.editor", id=new_article.id))
    else:
        article.title = request.form.get("title", article.title)
        article.description = request.form.get("description", article.description)
        article.content = request.form.get("content", article.content)
        authors = split_and_clean("authors")
        tags = split_and_clean("tags")
        if authors:
            article.authors = authors
        if tags:
            article.tags = tags
        article.html = build_HTML(request.form.get("content", article.content))
        article.datetime_edited = datetime.now(timezone.utc)

        db.session.commit()
        flash("Article saved", "success")
        return redirect(url_for("manager.editor", id=article.id))


@manager_bp.route("/delete/<string:id>", methods=["POST"])
def delete_article(id):
    article = Article.query.get(id)
    if article:
        db.session.delete(article)
        db.session.commit()
        flash("Article deleted", "success")
    else:
        flash("Article not found", "error")
    return redirect(url_for("manager.editor_apex"))

