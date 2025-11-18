import pandas as pd

df = pd.read_csv("student_responses.csv")
df_wide = df.pivot_table(index='Student', columns='Question', values='Correct', aggfunc='max')
df_wide = df_wide.fillna(0).reset_index()
df_wide.to_csv("student_responses_wide.csv", index=False)
