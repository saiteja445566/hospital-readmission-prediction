from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load the saved model package
model_package = joblib.load("readmission_model.pkl")

model = model_package["model"]
features = model_package["features"]
threshold = model_package["threshold"]


@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    probability = None
    error = None

    if request.method == "POST":

        try:
            # Collect input values from the HTML form
            input_data = {}

            for feature in features:
                input_data[feature] = float(request.form[feature])

            # Convert input into a DataFrame
            input_df = pd.DataFrame(
                [input_data],
                columns=features
            )

            # Generate prediction probability
            probability_value = model.predict_proba(input_df)[0][1]

            # Apply the selected threshold
            if probability_value >= threshold:
                prediction = "High readmission risk"
            else:
                prediction = "Low readmission risk"

            probability = round(probability_value * 100, 2)

        except Exception as e:
            error = str(e)

    return render_template(
        "index.html",
        prediction=prediction,
        probability=probability,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=False, port=5000)