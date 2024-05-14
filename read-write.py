import pandas as pd

df = pd.read_csv("input.csv")

filtered_df = df[df["age"] < 30].copy()

filtered_df['age_category'] = ['Adult' if age > 18 else 'Minor' for age in filtered_df['age']]

filtered_df.to_csv("output.csv", index=False)

print(filtered_df)