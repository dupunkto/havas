from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    make_response,
    abort,
    jsonify,
)

from db.models import Article, db

from datetime import datetime, timezone
import markdown
import json

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

    if not article:
        abort(404)

    return render_template("manager_editor.html", article=article)


def build_HTML(markdown_input):
    # Can/will be extended in the future
    return markdown.markdown(
        markdown_input,
        extensions=[
            "tables",
            "fenced_code",
            "codehilite",
            "toc",
            "sane_lists",
            "nl2br",
            "smarty",
        ],
    )


@manager_bp.route("/build-HTML", methods=["POST"])
def build_HTML_api():
    data = request.get_json()
    html = build_HTML(data.get("content", ""))

    return jsonify({"result": html})


@manager_bp.route("/save_api", methods=["POST"])
def save_api():
    article_id = request.form.get("id")
    article = Article.query.get(article_id)

    def split_and_clean(field):
        return [x for x in request.form.get(field, "").split(";") if x.strip()]

    if not article:
        new_article = Article(
            title=request.form.get("title"),
            description=request.form.get("description"),
            content=request.form.get("content"),
            cover_image_id=request.form.get("cover_image_id"),
            authors=split_and_clean("authors"),
            tags=split_and_clean("tags"),
            html=build_HTML(request.form.get("content")),
            datetime_made=datetime.now(timezone.utc),
            datetime_edited=datetime.now(timezone.utc),
        )

        if (
            new_article.title == "Title"
            or new_article.description == "Description"
            or new_article.content == "Content"
            or new_article.html == "<p>Content</p>"
        ):
            flash("Enter an title, description and content.", "error")
            return redirect(
                url_for("manager.editor_apex")
            )  # todo(gijs): Don't return to the apex, return to the form on /editor/new (filled in form)

        db.session.add(new_article)
        db.session.commit()
        flash(
            f"New article <b>{new_article.title}</b> created successfully.", "success"
        )
        return redirect(url_for("manager.editor", id=new_article.id))

    article.title = request.form.get("title", article.title)
    article.description = request.form.get("description", article.description)
    article.content = request.form.get("content", article.content)
    article.cover_image_id = request.form.get("cover_image_id", article.cover_image_id)
    authors = split_and_clean("authors")
    tags = split_and_clean("tags")
    if authors:
        article.authors = authors
    if tags:
        article.tags = tags
    article.html = build_HTML(request.form.get("content", article.content))
    article.datetime_edited = datetime.now(timezone.utc)

    db.session.commit()
    flash(f"Changes to article <b>{article.title}</b> have been saved.", "success")
    return redirect(url_for("manager.editor", id=article.id))


@manager_bp.route("/delete/<string:id>", methods=["POST"])
def delete_article(id):
    article = Article.query.get(id)
    if article:
        db.session.delete(article)
        db.session.commit()
        flash(
            f"Article <b>{article.title}</b> (ID: {article.id}) has been deleted.",
            "success",
        )
    else:
        flash(f"Article with ID <b>{id}</b> not found. Nothing was deleted.", "error")
    return redirect(url_for("manager.editor_apex"))


@manager_bp.route("/reset_dates/<string:id>", methods=["POST"])
def reset_dates(id):
    article = Article.query.get(id)
    if not article:
        flash(f"Article with ID <b>{id}</b> not found. Dates were not reset.", "error")
    else:
        now = datetime.now(timezone.utc)
        article.datetime_made = now
        article.datetime_edited = now
        db.session.commit()
        flash(
            f"Timestamps for article <b>{article.title}</b> have been reset to now.",
            "success",
        )
    return redirect(url_for("manager.editor", id=id))


@manager_bp.route("/toggle_archive/<string:id>", methods=["POST"])
def toggle_archive(id):
    article = Article.query.get(id)
    if not article:
        flash(
            f"Article with ID <b>{id}</b> not found. Archive status unchanged.", "error"
        )
    else:
        article.archived = not getattr(article, "archived", False)
        db.session.commit()
        status = "archived" if article.archived else "unarchived"
        flash(f"Article <b>{article.title}</b> has been {status}.", "success")
    return redirect(url_for("manager.editor", id=id))


@manager_bp.route("/export_json/<string:id>", methods=["GET"])
def export_json(id):
    article = Article.query.get(id)
    if not article:
        flash(f"Article with ID <b>{id}</b> not found. Export failed.", "error")
        return redirect(url_for("manager.editor_apex"))
    data = {
        "id": article.id,
        "title": article.title,
        "description": article.description,
        "content": article.content,
        "html": article.html,
        "authors": article.authors,
        "tags": article.tags,
        "datetime_made": article.datetime_made.isoformat(),
        "datetime_edited": article.datetime_edited.isoformat(),
        "cover_image_id": article.cover_image_id,
        "archived": getattr(article, "archived", False),
    }
    response = make_response(json.dumps(data, indent=2))
    response.headers["Content-Disposition"] = (
        f"attachment; filename=article_{article.id}.json"
    )
    response.mimetype = "application/json"
    return response


@manager_bp.route("/regen_html/<string:id>", methods=["POST"])
def regen_html(id):
    article = Article.query.get(id)
    if not article:
        flash(
            f"Article with ID <b>{id}</b> not found. HTML was not regenerated.", "error"
        )
    else:
        article.html = build_HTML(article.content)
        db.session.commit()
        flash(
            f"HTML for article <b>{article.title}</b> has been regenerated from its content.",
            "success",
        )
    return redirect(url_for("manager.editor", id=id))


@manager_bp.route("/regen_html_all", methods=["POST"])
def regen_html_all():
    articles = Article.query.all()
    for article in articles:
        article.html = build_HTML(article.content)
    db.session.commit()
    flash("HTML for all articles has been regenerated from their content.", "success")
    return redirect(url_for("manager.editor_apex"))
