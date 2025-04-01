"""Project to generate a Lebenslauf (CV) using Python."""

def lebenslauf_generator():
    """Generates a Lebenslauf (CV) based on user input."""
    lebenslauf_structure = {
        "personal_information": {
            "name": "",
            "address": "",
            "phone": "",
            "email": "",
            "date_of_birth": "",
            "city_of_birth": "",
        },
        
        "education": [],
        "experience": [],
        "skills": [],
        "languages": [],
    }

    def add_personal_information(lebenslauf_structure):
        """Collecting user input for personal information"""
        lebenslauf_structure["personal_information"]["name"] = input("Name: ").capitalize()
        lebenslauf_structure["personal_information"]["address"] = input("Address: ").capitalize()
        lebenslauf_structure["personal_information"]["phone"] = input("Phone: ")
        lebenslauf_structure["personal_information"]["email"] = input("Email: ").lower()
        lebenslauf_structure["personal_information"]["date_of_birth"] = input("Date of Birth (DD/MM/YYYY): ")
        lebenslauf_structure["personal_information"]["city_of_birth"] = input("City of Birth: ").capitalize()
        print("\nPersonal Information added successfully!")
    
    def add_education(lebenslauf_structure):
        """Collecting user input for education """
        print("\nPlease enter your education details: \nEnter 'done' when finished")
        while True:
            education = input("Education: ").capitalize()
            if education.lower() == "done":
                break
            lebenslauf_structure["education"].append(education)
        print("\nEducation details added successfully!")  

    def add_experience(lebenslauf_structure):
        """ Collecting experience"""
        print("\n Please enter your experience details: \nEnter 'done' when finished")
        while True:
            experience = input("Experience: ").capitalize()
            if experience.lower() == "done":
                break
            lebenslauf_structure["experience"].append(experience)
        print("Experience collected successfully. ")
    
    def add_skills(lebenslauf_structure):
        """ Collecting Skills"""
        print("\n Please enter your skills details: \nEnter 'done' when finished")
        while True:
            skills = input("Skills: ").capitalize()
            if skills.lower() == "done":
                break
            lebenslauf_structure["skills"].append(skills)
        print("Skills collected successfully. ")
    
    def add_languages(lebenslauf_structure):
        """ Collecting Languages"""
        print("\n Please enter your language(s) details: \nEnter 'done' when finished")
        while True:
            language = input("language: ").capitalize()
            if language.lower() == "done":
                break
            lebenslauf_structure["languages"].append(language)
        print("Languages collected successfully. ")
    
    # Calling all functions to collect information
    add_personal_information(lebenslauf_structure)
    add_education(lebenslauf_structure)
    add_experience(lebenslauf_structure)
    add_skills(lebenslauf_structure)
    add_languages(lebenslauf_structure)

    # Format the lebenslauf_structure into a string representation
    lebenslauf_string = f"""
    Personal Information:
        Name: {lebenslauf_structure['personal_information']['name']}
        Address: {lebenslauf_structure['personal_information']['address']}
        Phone: {lebenslauf_structure['personal_information']['phone']}
        Email: {lebenslauf_structure['personal_information']['email']}
        Date of Birth: {lebenslauf_structure['personal_information']['date_of_birth']}
        City of Birth: {lebenslauf_structure['personal_information']['city_of_birth']}

    Education:
        {'\n        '.join(lebenslauf_structure['education'])}

    Experience:
        {'\n        '.join(lebenslauf_structure['experience'])}

    Skills:
        {'\n        '.join(lebenslauf_structure['skills'])}

    Languages:
        {'\n        '.join(lebenslauf_structure['languages'])}
    """

    # Write the string to a text file
    lebenslauf = "lebenslauf.txt"
    with open(lebenslauf, 'w') as file:
        file.write(lebenslauf_string)

    print(f"\nCV data saved to '{lebenslauf}' successfully!")

    # Return the lebenslauf_structure if needed

    return lebenslauf_structure
    
# variable to grab the generated CV
generated_lebenslauf = lebenslauf_generator()

print(generated_lebenslauf)
    





    
    
    