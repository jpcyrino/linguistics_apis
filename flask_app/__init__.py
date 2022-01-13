import os
from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/")
    def home():
        return "<h1>Merci !</h1><p>Merci pour avoir accedé notre site. En ce moment nous sommes en construction. Veuillez patienter.</p>"

    return app
