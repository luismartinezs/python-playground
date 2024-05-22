students_scores = {
    "Alice": 58,
    "Bob": 87,
    "Claire": 91,
    "David": 78,
}

students_scores["Eve"] = 99

students_scores["Alice"] = 78

for name, score in students_scores.items():
    print(f"{name}: {score}")

#

books = [
    {
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "year": 1988,
    },
    {
        "title": "The Little Prince",
        "author": "Antoine de Saint-Exupéry",
        "year": 1943,
    },
    {
        "title": "The Da Vinci Code",
        "author": "Dan Brown",
        "year": 2003,
    },
]

books.append(
    {
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "year": 1937,
    }
)

for book in books:
    if book["year"] > 2000:
        print(f"{book['title']} by {book['author']}")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

for row in transposed:
    print(row)

array = [1, 2, 3, 4, 5]
identity = [array[i] for i in range(len(array))]
inverse = [array[-i] for i in range(1, len(array) + 1)]

print(identity)
print(inverse)

#


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")


car1 = Car("Toyota", "Corolla", 2019)
car2 = Car("Honda", "Civic", 2020)
car3 = Car("Ford", "Fiesta", 2018)

car1.display_info()
car2.display_info()
car3.display_info()

# Working with JSON Data

json_data = """
[
    {"name": "Alice", "age": 30, "department": "HR", "salary": 50000},
    {"name": "Bob", "age": 35, "department": "Engineering", "salary": 75000},
    {"name": "Charlie", "age": 25, "department": "Marketing", "salary": 45000}
]
"""

import json

employees = json.loads(json_data)

new_employee = {"name": "David", "age": 40, "department": "Finance", "salary": 80000}
employees.append(new_employee)

average_salary = sum([employee["salary"] for employee in employees]) / len(employees)
print(f"Average Salary: {average_salary}")

updated_json_data = json.dumps(employees, indent=2)
print(updated_json_data)

# Matrix Operations with NumPy
# tags: numpy, matrix, data-analysis, python

import numpy as np

matrix = np.random.randint(1, 11, size=(3, 3))
print("Original Matrix:\n", matrix)

transpose = np.transpose(matrix)
print("Transposed Matrix:\n", transpose)

sum = np.sum(matrix)
print("Sum of Elements:", sum)

product = np.dot(matrix, transpose)
print("Product of Matrix and Transposed Matrix:\n", product)
