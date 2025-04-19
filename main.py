from flask import Flask, render_template, abort, request, flash, redirect, session, make_response
from datetime import datetime, timedelta
from urllib.parse import urlparse
import pytz
import commonmark
import yaml
import os
import re


from modules import load_modules

app = Flask(__name__)

app.secret_key = os.urandom(30)

for module, module_name in load_modules():
    try:
        app.register_blueprint(module, url_prefix=f"/{module_name}")
    except Exception as e:
        print(f"An error occured while trying to load {module} as a blueprint: {e}")


BASE_DIR = os.path.abspath(os.path.dirname(__file__))


@app.context_processor
def inject_globals():
    return {"global": {"compname": "Barium"}}



@app.route("/")
def homepage():
    article_list = []

    def format_date(dt_input):
        now = datetime.now(pytz.timezone("Europe/Amsterdam"))
        if dt_input.date() == now.date():
            formatted = f"Today, {dt_input.strftime('%H:%M')}"
        elif dt_input.date() == (now.date() - timedelta(days=1)):
            formatted = f"Yesterday, {dt_input.strftime('%H:%M')}"
        else:
            if dt_input.year == now.year:
                formatted = dt_input.strftime("%a %d %b, %H:%M")
            else:
                formatted = dt_input.strftime("%a %d %b %Y, %H:%M")
        return formatted

    for article in os.listdir(os.path.join(BASE_DIR, "articles", "news")):
        article_id = article.removesuffix(".md")
        with open(os.path.join(BASE_DIR, "articles", "news", article), encoding="utf-8") as file:
            article_content = file.read().strip()
        extract = re.match(r"^---\n(.*?)\n---\n", article_content, re.DOTALL)
        article_data = yaml.safe_load(extract.group(1))

        dt_obj = datetime.fromisoformat(str(article_data["datetime"]))
        article_data["datetime_obj"] = dt_obj
        article_data["datetime_formatted"] = format_date(dt_obj)

        img_id = article_data.get("cover", "fallback")

        article_data["cover"] = f"/media/api/get_image/{img_id}"
        article_data["url"] = f"/article/{article_id}"

        article_list.append(article_data)

    article_list.sort(key=lambda x: x["datetime_obj"], reverse=True)

    return render_template("index.html", article_list = article_list)


@app.route("/article/<string:slug>")
def article(slug):
    file_name = slug + ".md"
    try:
        with open(os.path.join(BASE_DIR, "articles", "news", file_name), encoding="utf-8") as file:
            file_content = file.read().strip()
    except FileNotFoundError:
        abort(404) 

    extract = re.match(r"^---\n(.*?)\n---\n", file_content, re.DOTALL)
    article_data = yaml.safe_load(extract.group(1))

    file_content_clean = re.sub(r"^---\s*\n.*?\n---\s*\n", "", file_content, flags=re.DOTALL)

    dt_input = datetime.fromisoformat(str(article_data["datetime"]))

    now = datetime.now(pytz.timezone("Europe/Amsterdam"))

    if dt_input.date() == now.date():
        formatted = f"Today, {dt_input.strftime('%H:%M')}"
    elif dt_input.date() == (now.date() - timedelta(days=1)):
        formatted = f"Yesterday, {dt_input.strftime('%H:%M')}"
    else:
        if dt_input.year == now.year:
            formatted = dt_input.strftime("%a %d %b, %H:%M")
        else:
            formatted = dt_input.strftime("%a %d %b %Y, %H:%M")
    
    article_data["dt_formatted"] = formatted
    
    img_id = article_data.get("cover", "fallback")

    article_data["cover"] = f"/media/api/get_image/{img_id}"

    if article_data.get("datetime_edited"):
        dt_edited_input = datetime.fromisoformat(str(article_data["datetime_edited"]))

        now = datetime.now(pytz.timezone("Europe/Amsterdam"))

        if dt_edited_input.date() == now.date():
            formatted_edited = f"today, {dt_edited_input.strftime('%H:%M')}"
        elif dt_edited_input.date() == (now.date() - timedelta(days=1)):
            formatted_edited = f"yesterday, {dt_edited_input.strftime('%H:%M')}"
        else:
            if dt_edited_input.year == now.year:
                formatted_edited = dt_edited_input.strftime("%a %d %b, %H:%M")
            else:
                formatted_edited = dt_edited_input.strftime("%a %d %b %Y, %H:%M")
        
        article_data["dt_edited"] = "Last edited on " + formatted_edited

    text = commonmark.commonmark(file_content_clean)

    return render_template("article.html", article_content = text, **article_data)

@app.errorhandler(404)
def not_found(e):
    referrer = request.referrer
    target_path = urlparse(request.url).path

    if not referrer or "api" in target_path or "favicon" in target_path:
        return "404 Not Found", 404

    ref_host = urlparse(referrer).hostname
    current_host = urlparse(request.host_url).hostname

    if ref_host == current_host:
        flash(f"Sorry, <code>{target_path}</code> is not a webpage", "error")

        html = f'''
        <!doctype html>
        <html>
        <head>
            <meta http-equiv="refresh" content="0;url={referrer}">
            <title>Redirecting...</title>
        </head>
        <body>
            <h1>404</h1>
            <p>That page was not found.</p>
            <p>You are being redirected back to to <a href="{referrer}">{referrer}</a>...</p>
        </body>
        </html>
        '''

        response = make_response(html, 404)
        response.headers['Location'] = referrer
        return response

    return "404 Not Found", 404


if __name__ == "__main__":
    app.run(debug=True, port=2000)
