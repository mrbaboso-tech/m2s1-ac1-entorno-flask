import os
from flask import Flask, render_template
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env (o LALALA.env si lo tienes así)
load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")


@app.route("/")
def index():
    return "Hello, Flask!"


@app.route("/about")
def about():
    return render_template("about.html", proyecto="Mi primer app Flask")


if __name__ == "__main__":
    app.run(debug=True)
