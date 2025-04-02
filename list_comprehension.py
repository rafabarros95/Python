# Even numbers
print("\n Evens only")
even_odd = [number for number in range(30) if number%2 == 0]

print(even_odd)

# Even or odd numbers in list comprehension
print("\n Even or Odd numbers")
categories = [
    "even" if x % 2 == 0 else "odd" for x in range(10)
]
print(categories)

print("\n Specific Characters in list of strings")
options = ["array", "abbey", "arrange", "error", "abbray", "tour", "any", "python"]
valid_chars = [
    string
    for string in options
        if len(string) >= 2
        if string[0] == "a"
        if string[-1] == "y"
]

print(valid_chars)