from flask import Blueprint, send_from_directory, current_app
import os

media_bp = Blueprint(
    "media", __name__, url_prefix="/media", static_folder="media_dump/"
)


@media_bp.route("/")
def index():
    return "Hello media!"


@media_bp.route("/get_file/", defaults={"id": "default"})
@media_bp.route("/get_file/<string:id>")
def get_file(id):
    folder = os.path.join(current_app.root_path, media_bp.static_folder, "images")
    return send_from_directory(folder, id + ".jpg")
