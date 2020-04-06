from flask import Flask, render_template, url_for


COLORS = {
    "00": "#FF4415",
    "01": "#FF9E7B",
    "10": "#007FEC",
    "11": "#ACC3DC",
}


app = Flask(__name__)


@app.route("/table/<string:sex>/<int:age>")
def distribution(sex, age):
    params = {
        "title": "Цвет каюты",
        "image": "child.png" if age < 21 else "adult.png",
        "color": COLORS[f"{int(sex == 'male')}{int(age < 21)}"],
    }
    return render_template("table.html", **params)


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
