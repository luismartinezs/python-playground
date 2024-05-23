import pandas as pd
import numpy as np

d = {
    "A": np.random.randint(5, size=(3)),
    "B": np.random.randint(5, size=(3)),
    "C": np.random.randint(5, size=(3)),
}

df = pd.DataFrame(data=d)

df["D"] = df["A"] + df["B"]

df["C"][0] = np.nan

mean_values = df.mean()  # mean of each column

print(df)
print(mean_values)

# Replace any NaN values in the DataFrame with the mean of the respective column
df = df.apply(lambda x: x.fillna(x.mean()), axis=0)


print(df)
