from flask import (
    Blueprint,
    send_from_directory,
    current_app,
    url_for,
    jsonify,
    request,
    abort,
)

import os

from .models import random_base36_id

media_bp = Blueprint(
    "media", __name__, url_prefix="/media", static_folder="media_dump/"
)


def get_images_path():
    return os.path.join(current_app.root_path, media_bp.static_folder, "images")


@media_bp.route("/")
def index():
    return "Hello media!"


@media_bp.route("/get_file/", defaults={"id": "default"})
@media_bp.route("/get_file/<string:id>")
def get_file(id):
    filename = f"{id}.jpg"
    return send_from_directory(get_images_path(), filename)


@media_bp.route("/list_images")
def list_images():
    images_path = get_images_path()
    files = sorted(
        os.listdir(images_path),
        key=lambda f: os.path.getmtime(os.path.join(images_path, f)),
    )[::-1]

    result = [
        {
            "url": url_for("media.get_file", id=os.path.splitext(f)[0]),
            "id": os.path.splitext(f)[0],
        }
        for f in files
        if f.lower().endswith(".jpg")
    ]

    return jsonify(result)


@media_bp.route("/api/upload", methods=["POST"])
def uploader():
    file = request.files.get("file")

    if not file or file.filename == "":
        return jsonify({"success": False, "message": "No selected file"}), 400

    if (
        "." in file.filename
        and file.filename.lower().endswith(".jpg")
        and file.mimetype == "image/jpeg"
    ):
        image_id = random_base36_id(10)
        filename = f"{image_id}.jpg"
        filepath = os.path.join(get_images_path(), filename)

        if os.path.exists(filepath):
            abort(500, description="File already exists")

        file.save(filepath)
        return jsonify({"success": True, "path": filepath})

    return jsonify({"success": False, "message": "Only .jpg images are allowed"}), 400
