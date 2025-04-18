from flask import Blueprint, redirect, send_file
import os

media_module = Blueprint("media_module", __name__)

BASE_DIR = os.path.dirname(__file__)


project_dir = os.path.dirname(__file__)

while not os.path.isdir(os.path.join(project_dir, '.git')):
    project_dir = os.path.dirname(project_dir)

project_dir =  os.path.abspath(project_dir)


@media_module.route("/cover/<string:id>")
def cover_image(id):
    print(id)
    path = os.path.join(BASE_DIR, "media", "news", "covers", id)
    if os.path.exists(path):
        return send_file(path)
    return redirect("https://picsum.photos/1500/1000")
