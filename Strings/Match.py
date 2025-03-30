# Testing match cases function from python

name = input("What is your name? ")
match name:
    case "John":
        print("Hello John")
    case "Jane":
        print("Hello Jane")
    case "Doe":
        print("Hello Mr. Doe")
    case _:
        print("Hello Stranger")