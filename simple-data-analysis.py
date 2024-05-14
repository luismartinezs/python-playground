import pandas as pd

data = {
  'name': ['Frodo', 'Sam', 'Aragorn', 'Legolas', 'Gandalf'],
  'age': [50, 36, 87, 2931, 2019],
  'city': ['Shire', 'Shire', 'Gondor', 'Mirkwood', 'Valinor']
}

df = pd.DataFrame(data)

print(df)

mean_age = df['age'].mean()
median_age = df['age'].median()
print(f'Mean age: {mean_age}')
print(f'Median age: {median_age}')