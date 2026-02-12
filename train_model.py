import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import joblib

# Load dataset
data = pd.read_csv("student_data.csv")

# Select features
X = data[['studytime','failures','famrel','freetime','goout',
          'Dalc','Walc','health','absences','G1','G2']]
y = data['G3']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "student_model.pkl")

# Test
y_pred = model.predict(X_test)
accuracy = r2_score(y_test, y_pred)
print("Model Accuracy:", accuracy)
print("Model saved as student_model.pkl")
