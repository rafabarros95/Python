# Let's play with try catch blocks for error handling


def main():
        names = []
        another_function(names) #Call the function
        # Print the list of names
        print(names)

def another_function(names):
        while True:
            name =input('Name:')
            if name == '' or  name == 'Exit' or name.isdigit():
                break
            names.append(name)
        return names
        
main()
