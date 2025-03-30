import csv

# ------------------------1-With Strings------------------------------
# students = []

# with open('students.csv') as file:
#     for line in file:
#         name, house = line.rstrip().split(',')

#         # option1
#         # student = {}
#         # student["name"] = name
#         # student["house"] = house

#         # option2 - Defining keys
#         student = {
#             "name": name,
#             "house": house
#         }

#         students.append(student)

# # def get_name(student):
# #     return student["name"]

# # functions can be passed as arguments to other functions
# #  lambda is called one time, no need of extra function for get_name
# for student in sorted(students, key=lambda student: student["name"]): 
#     print(f"{student['name']} is from {student['house']}") 

# --------------------2-With CSV Module---------------------------

students = []

with open('Modules/Students.csv') as file:
    # reader = csv.reader(file)
    reader = csv.DictReader(file)
    # for name, city in reader:
    for row in reader:
        students.append({ "Name": row["Name"], "City": row["City"]})
        
for student in sorted(students, key=lambda student: student["Name"]):
    print(f"{student['Name']} is from {student['City']}")

