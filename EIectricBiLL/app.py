from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    total = None

    if request.method == "POST":
        unit = float(request.form["unit"])
        total = unit * 4.18

    return render_template("index.html", total=total)

if __name__ == "__main__":
    app.run(debug=True)