from flask import Blueprint
import os

manager_module = Blueprint("manager_module", __name__)

BASE_DIR = os.path.dirname(__file__)


project_dir = os.path.dirname(__file__)

while not os.path.isdir(os.path.join(project_dir, '.git')):
    project_dir = os.path.dirname(project_dir)

project_dir =  os.path.abspath(project_dir)


@manager_module.route("/")
def manager_index():
    return "Test"
