from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Des APIs Linguistiques</h1><p>Veuillez patienter, car ce site est en construction</p>"

if __name__ == '__main__':
    app.run()