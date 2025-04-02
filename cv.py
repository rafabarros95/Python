"""Generating the CV again"""

def cv_generator():
    # define structure
    cv_structure = {
    "personal_info" : {
        "name": "",
        "email": "",
        "phone": "",
        "address": "",
        "home_town": "",
    },
        "education": [],
        "skills": [],
        "languages": [],
    }

    def add_personal_info():
        cv_structure["personal_info"]["name"] = input("Name: ").capitalize()
        cv_structure["personal_info"]["email"] = input("Email: ").capitalize()
        cv_structure["personal_info"]["phone"] = input("Number: ")
        cv_structure["personal_info"]["address"] = input("Address: ").capitalize()
        cv_structure["personal_info"]["home_town"] = input("Home Town: ").capitalize()
        print("\n Personal Infos added successfully :)")
    
    def add_education(cv_structure):
        print("\n Let's collect your Education(s): Enter 'done' when finished")
        while True:
            education = input("Your Education: ").capitalize()
            if education.lower() == 'done':
                break
            cv_structure["education"].append(education)
        print("\n Education collected Sucessfully")
    
    def add_skills(cv_structure):
        print("\n Let's collect your skills: Enter 'done' when finished ")
        while True:
            skills = input("Your Skills: ").capitalize()
            if skills.lower() == 'done':
                break
            cv_structure["skills"].append(skills)
        print("\n Education collected Sucessfully")
    
    def add_languages(cv_structure):
        print("\n Let's collect your Languages: Enter 'done' when finished ")
        while True:
            languages = input("Your spoken Languages: ").capitalize()
            if languages.lower() == 'done':
                break
            cv_structure["languages"].append(languages)
        print("\n Languages collected Sucessfully")
    
    add_personal_info()
    add_education(cv_structure)
    add_skills(cv_structure)
    add_languages(cv_structure)

    cv_string = f"""
    Personal Information:
        Name: {cv_structure['personal_info']["name"]}
        Email: {cv_structure['personal_info']["email"]}
        Phone: {cv_structure['personal_info']["phone"]}
        Address: {cv_structure['personal_info']["address"]}
        Home Town: {cv_structure['personal_info']["home_town"]}

    Education:
    {'\n      '.join(cv_structure['education'])}

    Skills:
    {'\n      '.join(cv_structure['skills'])}

    Languages:
    {'\n      '.join(cv_structure['languages'])}
"""
    
    # creating and saving data on file

    cv_generator = f"{cv_structure['personal_info']["name"]}_lebenslauf.txt"

    with open (cv_generator, 'w') as file:
        file.write(cv_string)
    print(f"\n CV from {cv_structure["personal_info"]["name"]} saved successfully. Check it out :) ")
    return cv_structure

generated_cv = cv_generator()

print(generated_cv)






