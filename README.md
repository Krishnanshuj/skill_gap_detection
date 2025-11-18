# 🎯 Skill Gap Detection — Student Weakness Analysis (Algebra, Geometry, Trigonometry)

This project is a complete system that identifies which subject areas students are **weak in** by analyzing their responses to a 20-question quiz.  
It includes:

- ✅ A Streamlit-based quiz interface  
- ✅ Automatic saving of student responses  
- ✅ Simple visualizations of overall weak skills  
- ✅ (Optional) Machine Learning model to predict weak subjects  

---

## 🚀 Features

### **1️⃣ Streamlit Quiz App**
- 20 MCQ questions
- Topics: **Algebra, Geometry, Trigonometry**
- Saves responses to `student_responses.csv`
- Shows score after submission
- Balloons animation 🎈 for student-friendly UI

### **2️⃣ Skill Weakness Prediction **
If `multioutput_rf_model.joblib` exists, the app predicts:
- Weak in **Algebra**
- Weak in **Geometry**
- Weak in **Trigonometry**

Prediction is shown in vector form, e.g.:

([0,1,0])    it means students are weak in Geometry section



### **3️⃣ Admin Visualization**
Shows **which subject most students are weak in** using a simple Streamlit bar chart.

Example output:
- Algebra → 30% weak  
- Geometry → 45% weak  
- Trigonometry → 20% weak  

---

## 📁 Project Structure

Skill-Gap-Detection/
│── detector.py # Main Streamlit app
│── skill_gap_quiz_app.py # (Optional) quiz app version
│── student_responses.csv # Auto-generated
│── student_predictions.csv # Auto-generated (if model used)
│── multioutput_rf_model.joblib # ML model (optional)
│── question_skill_mapping.csv # Skill mapping used during training
│── README.md



---

## 🧠 How the ML Model Works 
You can train a model that predicts weak skills from quiz responses.

**Input:**  
20 binary features → Correct/Incorrect for Q1–Q20.

**Output Labels:**  
- `Weak_Algebra`
- `Weak_Geometry`
- `Weak_Trigonometry`

**Model Used:**  
`MultiOutputClassifier(RandomForestClassifier(n_estimators=200))`

This makes the system capable of predicting weak areas even without computing skill averages manually.

---

## 🛠 How to Run the Project

### **Install dependencies**
```bash
pip install streamlit pandas scikit-learn joblib
Run the Streamlit App
bash
Copy code
streamlit run detector.py
The app will open in your browser at:

arduino
Copy code
http://localhost:8501
📊 Visualization Example
Inside the Admin Panel, you will see:

A bar chart showing % of students weak in each subject

Student-wise skill summaries

No external plotting libraries required — everything uses Streamlit’s built-in charts.

📦 Requirements
If you want to create a requirements.txt:

nginx
Copy code
streamlit
pandas
numpy
scikit-learn
joblib
👨‍💻 Author
Krishnanshu Jaiswal
AI/ML Developer — Passionate about creating educational analytics tools.
