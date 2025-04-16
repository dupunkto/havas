from flask import Blueprint, render_template, abort
from datetime import datetime, timedelta
import commonmark
import os
import pytz
import yaml
import re

article_module = Blueprint("article_module", __name__)

BASE_DIR = os.path.dirname(__file__)


project_dir = os.path.dirname(__file__)

while not os.path.isdir(os.path.join(project_dir, '.git')):
    project_dir = os.path.dirname(project_dir)

project_dir =  os.path.abspath(project_dir)


@article_module.route("/<string:slug>")
def article(slug):
    file_name = slug + ".md"
    try:
        with open(os.path.join(project_dir, "articles", "news", file_name), encoding="utf-8") as file:
            file_content = file.read().strip()
    except FileNotFoundError:
        abort(404) 

    extract = re.match(r"^---\n(.*?)\n---\n", file_content, re.DOTALL)
    article_data = yaml.safe_load(extract.group(1))

    file_content_clean = re.sub(r"^---\s*\n.*?\n---\s*\n", "", file_content, flags=re.DOTALL)

    dt_input = datetime.fromisoformat(str(article_data["datetime"]))

    now = datetime.now(pytz.timezone("Europe/Amsterdam"))

    if dt_input.date() == now.date():
        formatted = f"Today, {dt_input.strftime('%H:%M:%S')}"
    elif dt_input.date() == (now.date() - timedelta(days=1)):
        formatted = f"Yesterday, {dt_input.strftime('%H:%M:%S')}"
    else:
        if dt_input.year == now.year:
            formatted = dt_input.strftime("%a %d %b, %H:%M:%S")
        else:
            formatted = dt_input.strftime("%a %d %b %Y, %H:%M:%S")
    
    article_data["dt_formatted"] = formatted
    article_data["cover"] = f"/static/assets/news/covers/{slug}.jpg"

    text = commonmark.commonmark(file_content_clean)

    return render_template("article.html", article_content = text, **article_data)
