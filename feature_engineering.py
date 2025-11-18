import pandas as pd

df_wide = pd.read_csv("student_responses_wide.csv")
mapping = pd.read_csv("question_skill_mapping.csv")

skills = mapping["Skill"].unique()
features = pd.DataFrame()
features["Student"] = df_wide["Student"]

for skill in skills:
    qs = mapping[mapping["Skill"]==skill]["Question"].tolist()
    features[f"{skill}_score"] = df_wide[qs].mean(axis=1)

features["total_correct"] = df_wide.drop(columns=["Student"]).sum(axis=1)
features["avg_score"] = df_wide.drop(columns=["Student"]).mean(axis=1)
features.to_csv("student_features.csv", index=False)

labels = pd.DataFrame()
for skill in skills:
    labels[f"Weak_{skill}"] = (features[f"{skill}_score"] < 0.4).astype(int)
labels.to_csv("student_labels.csv", index=False)
