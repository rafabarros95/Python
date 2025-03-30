import re
# -------------------------------------------------------------------------
# Users Input
# -------------------------------------------------------------------------

# name = input("Enter your name: ").strip()

# if "," in name:
#     first, second = name.split()
#     full_name = (f"Hello {second} {first}, Nice to meet you!")

# print(full_name)
    

# -------------------------------------------------------------------------
# Using Regular Expressions "re" module and functions like .search() and .groups()
# -------------------------------------------------------------------------

name = input("Enter your name: ").strip()

matches = re.search(r"^(.+), (.+)$", name)

if matches:
    last, first = matches.groups()
    full_name = f"Hello {first} {last}, Nice to meet you!"

print(full_name)


#------------------------------------------------------------------------
# Another way using new python assignment - walrus operator ":=" (Assign and compare same time)
# -----------------------------------------------------------------------

name = input("Enter your name: ").strip()

if matches := re.search("^(.+), (.+)$", name):
    full_name = matches.group(2) + " " + matches.group(1)

print(full_name)