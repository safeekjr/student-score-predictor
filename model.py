import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
data = {
    "hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "attendance": [60, 65, 70, 75, 80, 85, 90, 95],
    "score": [45, 50, 55, 61, 68, 75, 82, 88]
}
df = pd.DataFrame(data)
X = df[["hours", "attendance"]]
y = df["score"]
model = LinearRegression()
model.fit(X, y)

new_student = pd.DataFrame([[7, 85]], columns=["hours", "attendance"])
prediction = model.predict(new_student)
print("Predicted Score:", prediction[0])

joblib.dump(model, "model.pkl")

