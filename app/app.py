from flask import Flask, render_template, request, json
from os.path import join

app = Flask(__name__)

if __name__ == "__main__":
    app.debug = True

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        print(request.form)

    # Filter last 4 jobs
    job_data = get_experience_data()
    filtered_jobs = {job : job_data["Experience"][job] for job in ["woolpert", "xom", "ornl", "cea"]}

    return render_template("index.html", experience=filtered_jobs)

@app.route("/experience_zoom", methods=["GET"])
def experience_zoom():
    job_data = get_experience_data()["Experience"][request.args.get("job")]
    return render_template("experience_zoom.html", data=job_data)

@app.route("/experience", methods=["GET"])
def experience():
    data = get_experience_data()
    return render_template("experience.html", experience=data["Experience"], education=data["Education"])

def get_experience_data():
    return json.load(open(join(app.static_folder, "experience_data.json")))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)