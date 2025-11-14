import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Skill Gap Detection Quiz", page_icon="🧮", layout="centered")

st.title("🧠 Skill Gap Detection Quiz")
st.markdown("### Topics: Algebra, Geometry, Trigonometry")


student_name = st.text_input("Enter your name:")


questions = [
    
    {"id": "Q1", "question": "Simplify: 3x + 4x", "options": ["5x", "6x", "7x", "8x"], "answer": "7x", "skill": "Algebra"},
    {"id": "Q2", "question": "Solve for x: 2x + 3 = 7", "options": ["1", "2", "3", "4"], "answer": "2", "skill": "Algebra"},
    {"id": "Q3", "question": "If y = 3x + 2, find y when x = 4", "options": ["12", "14", "16", "18"], "answer": "14", "skill": "Algebra"},
    {"id": "Q4", "question": "Factorize: x² − 9", "options": ["x(x−9)", "(x−3)(x+3)", "(x−9)(x+9)", "(x−1)(x+9)"], "answer": "(x−3)(x+3)", "skill": "Algebra"},
    {"id": "Q5", "question": "Roots of x² − 4x + 3 = 0", "options": ["1,3", "2,3", "1,2", "3,4"], "answer": "1,3", "skill": "Algebra"},
    {"id": "Q6", "question": "Simplify: (x² + 2x + 1)", "options": ["x² + 1", "(x+1)²", "x(x+1)", "(x+1)(x+2)"], "answer": "(x+1)²", "skill": "Algebra"},
    {"id": "Q7", "question": "If 5x = 25, find x", "options": ["4", "5", "6", "7"], "answer": "5", "skill": "Algebra"},

    
    {"id": "Q8", "question": "Sum of angles in a triangle?", "options": ["90°", "180°", "270°", "360°"], "answer": "180°", "skill": "Geometry"},
    {"id": "Q9", "question": "Area of a circle (r=7cm)?", "options": ["49", "154", "22", "44"], "answer": "154", "skill": "Geometry"},
    {"id": "Q10", "question": "Perimeter of rectangle (L=10,B=5)?", "options": ["20", "25", "30", "35"], "answer": "30", "skill": "Geometry"},
    {"id": "Q11", "question": "Type of triangle with sides 5, 12, 13?", "options": ["Equilateral", "Isosceles", "Scalene", "Right triangle"], "answer": "Right triangle", "skill": "Geometry"},
    {"id": "Q12", "question": "Area of square (side=6cm)?", "options": ["12", "24", "36", "48"], "answer": "36", "skill": "Geometry"},
    {"id": "Q13", "question": "Circumference of circle (r=3cm)?", "options": ["9.42", "18.84", "12.56", "21.98"], "answer": "18.84", "skill": "Geometry"},


    {"id": "Q14", "question": "sin(90°) = ?", "options": ["0", "1", "0.5", "-1"], "answer": "1", "skill": "Trigonometry"},
    {"id": "Q15", "question": "cos(0°) = ?", "options": ["0", "1", "0.5", "-1"], "answer": "1", "skill": "Trigonometry"},
    {"id": "Q16", "question": "tan(45°) = ?", "options": ["0", "1", "0.5", "-1"], "answer": "1", "skill": "Trigonometry"},
    {"id": "Q17", "question": "sin²θ + cos²θ = ?", "options": ["0", "1", "2", "None"], "answer": "1", "skill": "Trigonometry"},
    {"id": "Q18", "question": "sin(30°) = ?", "options": ["0", "0.5", "1", "√3/2"], "answer": "0.5", "skill": "Trigonometry"},
    {"id": "Q19", "question": "If tan(θ) = 1, θ = ?", "options": ["30°", "45°", "60°", "90°"], "answer": "45°", "skill": "Trigonometry"},
    {"id": "Q20", "question": "cos(60°) = ?", "options": ["0.5", "0", "1", "√3/2"], "answer": "0.5", "skill": "Trigonometry"}
]

responses = {}


st.divider()
st.subheader("📋 Questions")

for q in questions:
    responses[q["id"]] = st.radio(f"{q['id']}. {q['question']}", q["options"], key=q["id"])

if st.button("Submit Quiz"):
    if student_name.strip() == "":
        st.error("⚠️ Please enter your name before submitting.")
    else:
        
        score_data = []
        correct = 0
        for q in questions:
            is_correct = int(responses[q["id"]] == q["answer"])
            score_data.append({
                "Student": student_name,
                "Question": q["id"],
                "Skill": q["skill"],
                "Response": responses[q["id"]],
                "Correct": is_correct
            })
            correct += is_correct

        
        df = pd.DataFrame(score_data)
        csv_file = "student_responses.csv"
        if not os.path.exists(csv_file):
            df.to_csv(csv_file, index=False)
        else:
            df.to_csv(csv_file, mode='a', header=False, index=False)

        st.success(f"✅ Quiz submitted! Your score: {correct}/{len(questions)}")
        st.balloons()
