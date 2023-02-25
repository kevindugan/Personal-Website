from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        print(request.form)
    return render_template("index.html")

if __name__ == "__main__":
    app.run()