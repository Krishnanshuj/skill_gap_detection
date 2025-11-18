import joblib
import numpy as np

model = joblib.load("skill_gap_model.joblib")

new_student = np.array([[1,0,1,1,0,1,1, 0,1,1, 1,0,1, 1,1,1,0, 1,1,1]])  
prediction = model.predict(new_student)

print("Prediction:", prediction)
