
class Student:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    # str function makes the print() function in line 14 to print the object in a readable format
    def __str__(self):
        return f"{self.name} is {self.age} years old and lives in {self.city}"

def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Your Name: ")
    age = int(input("Your Age: "))
    city = input("Your City: ")
    return Student(name, age, city)


if __name__ == "__main__":
    main()