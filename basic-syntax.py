name = "Luis"
age = 39
city = "Krabi"

print(f"Hello, my name is {name}. I am {age} years old anf I am in {city}.")


def print_numbers(n):
    for i in range(1, n + 1):
        print(i)


print_numbers(10)

numbers = list(range(1, 21))

even_numbers = [number for number in numbers if number % 2 == 0]
# value + loop + filtering condition

print(even_numbers)

person1 = {"name": "Luis", "age": 39, "city": "Krabi"}

person1["occupation"] = "Software Engineer"

person1["city"] = "Bangkok"

for key, value in person1.items():
    print(f"{key}: {value}")


#  create new text file
with open("sample.txt", "w") as file:
    file.write("Hello, world.")


# read file content and print in console
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)


class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def introduce(self):
        print(
            f"Hello, my name is {self.name}. I am {self.age} years old and I am in {self.city}."
        )


person1 = Person("Luis", 39, "Krabi")

person1.introduce()


class Employee(Person):
    def __init__(self, name, age, city, occupation):
        super().__init__(name, age, city)
        self.occupation = occupation

    def introduce(self):
        super().introduce()
        print(
            f"Hello, my name is {self.name}. I am a {self.occupation}. I am {self.age} years old and I am in {self.city}."
        )


employee1 = Employee("Luis", 39, "Krabi", "Software Engineer")
employee1.introduce()


try:
    num1 = float(input("Enter first number:"))
    num2 = float(input("Enter second number:"))

    result = num1 / num2
    print(f"The result of {num1} divided by {num2} is {result}")
except ZeroDivisionError:
    print("Error: Division by zero")
except ValueError:
    print("Error: Invalid input. Please enter a number.")
except Exception as e:
    print(f"Error: {e}")


num = list(range(1, 21))
squares = [num**2 for num in num if num % 2 == 0]

print(squares)
