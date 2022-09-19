from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    celsius = request.args.get("celsius", "")
    if celsius :
        fahrenheit = fahrenheit_from(celsius)
    else:
        fahrenheit = ""
    return  ("""
            <form action="" method="get">
                Celsius <input type="text" name="celsius">
                <input type="submit" value="Convertir">
            </form>
            """ + "Fahrenheit = " + fahrenheit)

def fahrenheit_from(celsius):
    """Convertir les Fahrenheits en degrees"""
    try:
        fahrenheit = float(celsius) * 9 / 5 + 32
        fahrenheit = round(fahrenheit, 3)
        return str(fahrenheit)
    except ValueError:
        return "Input invalid"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)