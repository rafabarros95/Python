# Lists 


numbers = [2,4,7,1,8,3,45,89,5,17,77,8]
Even = []
Odd = []

for num in numbers:
    if num%2 == 0:
       Even.append(num)
    else:
        Odd.append(num) 

print("Even numbers: ", Even)
print("Odd numbers: ", Odd)