from datetime import datetime
from flask import Flask, render_template, request, flash
import pandas as pd

app = Flask(__name__)

# Use correct path to your uploaded file
df = pd.read_csv("./data/really_final.csv")

# Filter the data

@app.route("/")
def index():
    return render_template("form.html")

@app.route("/map", methods=["GET", "POST"])
def show_map():
    if request.method == "POST":
        # Data received from form, but not used
        time_of_day = request.form["time_of_day"]
        electric_car = int(request.form["electric_car"])
        handicap = int(request.form["handicap"])
        surveillance = int(request.form["surveillance"])
        price = int(request.form["price"])

        available_df = df[
    (df["time_of_day"] == time_of_day) &
    (df["status"] == 1) &
    (df["is_handicap_accessible"] == handicap) &
    (df["has_camera_surveillance"] == surveillance ) &
    (df["price_per_hour"] <= price)
        ]
        available_df = available_df.dropna(subset=["latitude", "longitude"])
        available_df = available_df[(available_df["latitude"] != 0) & (available_df["longitude"] != 0)]

        

    data_json = available_df.to_dict(orient="records")  # <-- no need to dump to JSON string
    return render_template("index.html", data_json=data_json)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
