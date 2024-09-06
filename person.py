class Person:
  def __init__(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender
  def introduce(self):
    print(f"Hello, my name is {self.name}. I am {self.age} years old, and I am {self.gender}.")

name = input("Enter Your Name: ")
age = input("Enter Your Age: ")
gender = input("Enter Your Gender: ")

person = Person(name, age, gender)
person.introduce()