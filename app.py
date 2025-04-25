from datetime import datetime
from flask import Flask, render_template, request, flash
import pandas as pd

app = Flask(__name__)

# Use correct path to your uploaded file
df = pd.read_csv("./data/really_final.csv")

# Filter the data
available_df = df[
    (df["time_of_day"] == "afternoon") &
    (df["status"] == 1) &
    (df["is_handicap_accessible"] == 1) &
    (df["has_camera_surveillance"] == 1)
]
available_df = available_df.dropna(subset=["latitude", "longitude"])
available_df = available_df[(available_df["latitude"] != 0) & (available_df["longitude"] != 0)]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Data received from form, but not used
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        date_str = request.form["date"]
        occupation = request.form["occupation"]

        # Convert date
        date_object = datetime.strptime(date_str, "%Y-%m-%d")

    data_json = available_df.to_dict(orient="records")  # <-- no need to dump to JSON string
    return render_template("index.html", data_json=data_json)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
