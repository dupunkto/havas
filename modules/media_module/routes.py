from flask import Blueprint, jsonify, send_file
import os
import json

media_module = Blueprint("media_module", __name__)

BASE_DIR = os.path.dirname(__file__)


project_dir = os.path.dirname(__file__)

while not os.path.isdir(os.path.join(project_dir, '.git')):
    project_dir = os.path.dirname(project_dir)

project_dir =  os.path.abspath(project_dir)


@media_module.route("/api/cover/<string:id>")
def cover_image(id):
    with open(os.path.join(BASE_DIR, "data", "coverlist.json")) as jf:
        coverlist = json.load(jf)

    image_id = coverlist.get(id.removesuffix(".jpg"), "fallback")
    
    path = os.path.join(BASE_DIR, "media", "image_pile", image_id + ".jpg")
    return send_file(path)

@media_module.route("/api/get_image/<string:filename>")
def get_image(filename):
    path = os.path.join(BASE_DIR, "media", "image_pile", filename + ".jpg")
    return send_file(path)

@media_module.route("/api/list_images")
def list_images():
    files = os.listdir(os.path.join(BASE_DIR, "media", "image_pile"))

    final_file_list = []

    for file in files:
        final_file_list.append({
            "url": f"/media/api/get_image/{file.removesuffix(".jpg")}",
            "name": file.removesuffix(".jpg")
        })
    
    return jsonify(final_file_list)
