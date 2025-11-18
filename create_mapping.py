import pandas as pd


data = {
    "Question": [
        "Q1","Q2","Q3","Q4","Q5","Q6","Q7",
        "Q8","Q9","Q10","Q11","Q12","Q13",
        "Q14","Q15","Q16","Q17","Q18","Q19","Q20"
    ],
    "Skill": [
        "Algebra","Algebra","Algebra","Algebra","Algebra","Algebra","Algebra",
        "Geometry","Geometry","Geometry","Geometry","Geometry","Geometry",
        "Trigonometry","Trigonometry","Trigonometry","Trigonometry","Trigonometry","Trigonometry","Trigonometry"
    ]
}


df = pd.DataFrame(data)


df.to_csv("question_skill_mapping.csv", index=False)

print("question_skill_mapping.csv has been created successfully!")
