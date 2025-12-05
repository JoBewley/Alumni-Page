from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/membership", methods=["GET", "POST"])
def membership():
    if request.method == "POST":
        return redirect(url_for("submit_membership"))
    return render_template("membershipform.html")

@app.route("/submitted", methods=["GET", "POST"])
def submit_membership():
    return render_template("submit_membership.html")

@app.route("/volunteer", methods=["GET", "POST"])
def volunteer():
    if request.method == "POST":
        return redirect(url_for("index"))
    return render_template("volunteer.html")


if __name__ == "__main__":
    app.run(debug=True)
