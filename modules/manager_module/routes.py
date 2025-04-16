from flask import Blueprint, render_template
import os

manager_module = Blueprint("manager_module", __name__, template_folder="templates", static_folder="static")

BASE_DIR = os.path.dirname(__file__)


project_dir = os.path.dirname(__file__)

while not os.path.isdir(os.path.join(project_dir, '.git')):
    project_dir = os.path.dirname(project_dir)

project_dir =  os.path.abspath(project_dir)


@manager_module.route("/")
def manager_index():
    return render_template("manager_index.html")
