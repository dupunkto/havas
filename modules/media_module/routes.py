from flask import Blueprint, jsonify, send_file, request, abort
import os
import random

media_module = Blueprint("media_module", __name__)

BASE_DIR = os.path.dirname(__file__)


project_dir = os.path.dirname(__file__)

while not os.path.isdir(os.path.join(project_dir, ".git")):
    project_dir = os.path.dirname(project_dir)

project_dir =  os.path.abspath(project_dir)

@media_module.route("/api/get_image/<string:filename>")
def get_image(filename):
    path = os.path.join(BASE_DIR, "media", "image_pile", filename + ".jpg")

    if os.path.exists(path):
        return send_file(path)

    return send_file(os.path.join(BASE_DIR, "media", "image_pile", "no_image.jpg"))

@media_module.route("/api/list_images")
def list_images():
    files = os.listdir(os.path.join(BASE_DIR, "media", "image_pile"))

    files.sort(key=lambda x: os.path.getmtime(os.path.join(BASE_DIR, "media", "image_pile", x)))

    final_file_list = []

    for file in files:
        final_file_list.append({
            "url": f"/media/api/get_image/{file.removesuffix(".jpg")}",
            "name": file.removesuffix(".jpg")
        })
    
    return jsonify(final_file_list)

@media_module.route("/api/upload", methods=["POST"])
def uploader():
    if "file" not in request.files:
        return jsonify({"success": False, "message": "No file part"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"success": False, "message": "No selected file"}), 400

    if file and "." in file.filename and file.filename.rsplit(".", 1)[1].lower() == "jpg" and file.mimetype == "image/jpeg":
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567" # Base32

        id = "img_" + "".join(random.choices(chars, k=12))

        filepath = os.path.join(BASE_DIR, "media", "image_pile", id + ".jpg")

        if os.path.exists(filepath):
            abort(500)

        file.save(filepath)

        return jsonify({"success": True, "path": filepath})

    return jsonify({"success": False, "message": "Only .jpg images are allowed"}), 400
