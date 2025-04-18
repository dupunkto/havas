from flask import Blueprint, render_template, request, jsonify
from datetime import datetime
import re
import os
import yaml


manager_module = Blueprint("manager_module", __name__, template_folder="templates", static_folder="static")

BASE_DIR = os.path.dirname(__file__)


project_dir = os.path.dirname(__file__)

while not os.path.isdir(os.path.join(project_dir, ".git")):
    project_dir = os.path.dirname(project_dir)

project_dir =  os.path.abspath(project_dir)


@manager_module.route("/")
def manager_index():
    article_list = []

    for article in os.listdir(os.path.join(project_dir, "modules", "articles_module", "articles", "news")):
        article_id = article.removesuffix(".md")
        with open(os.path.join(project_dir, "modules", "articles_module", "articles", "news", article), encoding="utf-8") as file:
            article_content = file.read().strip()
        extract = re.match(r"^---\n(.*?)\n---\n", article_content, re.DOTALL)
        article_data = yaml.safe_load(extract.group(1))

        dt_obj = datetime.fromisoformat(str(article_data["datetime"]))
        article_data["datetime_obj"] = dt_obj

        article_data["cover"] = f"/media/cover/{article_id}.jpg"
        article_data["url"] = f"/article/{article_id}"

        article_data["id"] = article_id

        article_list.append(article_data)

    article_list.sort(key=lambda x: x["datetime_obj"], reverse=True)

    return render_template("manager_index.html", article_list = article_list)

@manager_module.route("/editor")
def manager_editor():
    article = request.args.get("id")

    with open(os.path.join(project_dir, "modules", "articles_module", "articles", "news", f"{article}.md"), encoding="utf-8") as file:
        article_content = file.read().strip()
    
    extract = re.match(r"^---\n(.*?)\n---\n", article_content, re.DOTALL)
    article_data = yaml.safe_load(extract.group(1))
    article_content_clean = re.sub(r"^---\s*\n.*?\n---\s*\n", "", article_content, flags=re.DOTALL)


    dt_obj = datetime.fromisoformat(str(article_data["datetime"]))
    article_data["datetime_obj"] = dt_obj

    article_data["cover"] = f"/media/cover/{article}.jpg"
    article_data["url"] = f"/article/{article}"

    article_data["id"] = article

    return render_template("manager_editor.html", article_content = article_content_clean, **article_data)


@manager_module.route("/api/save_markdown", methods=["POST"])
def save_markdown():
    data = request.json
    id = data.get("id")
    content = data.get("content")

    try:
        file_path = os.path.join(project_dir, "modules", "articles_module", "articles", "news", f"{id}.md")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return jsonify({"message": "File saved successfully", "path": file_path}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
