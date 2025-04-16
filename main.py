from flask import Flask

from modules import load_modules

app = Flask(__name__)

for module, prefix in load_modules():
    try:
        app.register_blueprint(module, url_prefix=prefix)
    except Exception as e:
        print(f"An error occured while trying to load {module} as a blueprint: {e}")


@app.route("/")
def homepage():
    return "Havas"


if __name__ == "__main__":
    app.run(debug=True, port=2000)