from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Bravo, c'est un app web!</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)