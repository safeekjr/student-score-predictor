from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd
app = Flask(__name__)
model = joblib.load("model.pkl")
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    hours = data["hours"]
    attendance = data["attendance"]
    new_student = pd.DataFrame(
    [[hours, attendance]],
    columns=["hours", "attendance"]
)
    prediction = model.predict(new_student)
    return jsonify({
        "predicted_score": prediction[0]
    })
if __name__ == "__main__":
    app.run(debug=True)

