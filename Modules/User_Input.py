import csv

while True:
    Name = input("Enter your name: ")
    Age_Input = input("Enter your age: ")
    try:
        Age = int(Age_Input)
    except ValueError:
        break

    if not Name.isalpha() or Age <= 0:
        break
    else:
        with open('Modules/User_Input.csv', 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["Name", "Age"])
            writer.writerow({"Name": Name, "Age": Age_Input})








        
