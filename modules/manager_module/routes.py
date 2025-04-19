from flask import Blueprint, render_template, request, jsonify, abort, redirect
from datetime import datetime
import re
import random
import os
import yaml
import pytz
import json


manager_module = Blueprint("manager_module", __name__, template_folder="templates", static_folder="static")

BASE_DIR = os.path.dirname(__file__)


project_dir = os.path.dirname(__file__)

while not os.path.isdir(os.path.join(project_dir, ".git")):
    project_dir = os.path.dirname(project_dir)

project_dir =  os.path.abspath(project_dir)


@manager_module.route("/")
def manager_home():
    article_list = []

    for article in os.listdir(os.path.join(project_dir, "modules", "articles_module", "articles", "news")):
        article_id = article.removesuffix(".md")
        with open(os.path.join(project_dir, "modules", "articles_module", "articles", "news", article), encoding="utf-8") as file:
            article_content = file.read().strip()
        extract = re.match(r"^---\n(.*?)\n---\n", article_content, re.DOTALL)
        article_data = yaml.safe_load(extract.group(1))

        dt_obj = datetime.fromisoformat(str(article_data["datetime"]))
        article_data["datetime_obj"] = dt_obj
        article_data["datetime_formatted"] = dt_obj.strftime("%d-%m-%Y %H:%M:%S")

        img_id = article_data.get("cover", "fallback")
        article_data["cover"] = f"/media/api/get_image/{img_id}"

        article_data["url"] = f"/article/{article_id}"

        article_data["id"] = article_id

        article_list.append(article_data)

    article_list.sort(key=lambda x: x["datetime_obj"], reverse=True)

    return render_template("manager_home.html", article_list = article_list)


@manager_module.route("/editor/<string:article>")
def manager_editor(article):
    with open(os.path.join(project_dir, "modules", "articles_module", "articles", "news", f"{article}.md"), encoding="utf-8") as file:
        article_content = file.read().strip()
    
    extract = re.match(r"^---\n(.*?)\n---\n", article_content, re.DOTALL)
    article_data = yaml.safe_load(extract.group(1))
    article_content_clean = re.sub(r"^---\s*\n.*?\n---\s*\n", "", article_content, flags=re.DOTALL)


    dt_obj = datetime.fromisoformat(str(article_data["datetime"]))
    article_data["datetime_obj"] = dt_obj

    img_id = article_data.get("cover", "fallback")
    article_data["cover"] = f"/media/api/get_image/{img_id}"

    article_data["img_id"] = img_id
    
    article_data["url"] = f"/article/{article}"

    article_data["id"] = article

    return render_template("manager_editor.html", article_content = article_content_clean, **article_data)


@manager_module.route("/editor/new")
def manager_editor_new():
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567" # Base32

    id = "".join(random.choices(chars, k=12))

    path = os.path.join(project_dir, "modules", "articles_module", "articles", "news", f"{id}.md")

    if os.path.exists(path):
        abort(500)

    current_time = datetime.now(pytz.utc).isoformat()

    with open(os.path.join(project_dir, "modules", "articles_module", "articles", "news", f"{id}.md"), "w", encoding="utf-8") as file:
        file.write(f'---\ntitle: "Lorem ipsum dolor sit amet"\ndescription: "Consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"\ndatetime: "{current_time}"\ntags: []\nauthors: []\n---\n\nLorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.\n')
   


    return redirect(f"/manager/editor/{id}")


@manager_module.route("/api/save_article", methods=["POST"])
def save_article():
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


@manager_module.route("/api/delete_article", methods=["POST"])
def delete_article():
    id = request.args.get("id")

    try:
        os.remove(os.path.join(project_dir, "modules", "articles_module", "articles", "news", f"{id}.md"))
        return jsonify({"message": "File removed successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

