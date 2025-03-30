students = [
    {"Name": "Alice"},
    {"Name": "Bob"} ,
    {"Name": "Charlie"},
    {"Name": "Ana"}

    ]
# students[0]["Name"] = "Pedro"
# for student in students:
#     print(student["Name"])

# Interactive user input to add names to the list
names = []

while True:
    name = input("Name: ")

    if name == "exit":
        break
    names.append({"Name": name})

print(names)



