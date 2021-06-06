#NAME
name = input("Name: ")
print("Hello, " + name + "!")
print(f"Hello, {name}, nice to meet you!")


#CONDITIONS
n = int(input("Numer: "))
if n > 0:
    print(f"{n} is positive")
elif n == 0:
    print(f"{n} is 0")
else: 
    print(f"{n} is negative")