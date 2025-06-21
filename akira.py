#1
n = int(input("> "))

for i in range(1, 11):
    print(f"{n} * {i} = {n*i}")

#2
while True:
    option = input("choose the currency you want to comvert (euros, pounds or yens (e/p/y/x for exit)) > ")
    summ = int(input("How much money should I convert (in USD)? > "))
    if option.lower().startswith("e"):
        print(f"{summ}$ is {round(summ*0.87, 2)} euros")
    elif option.lower.startswith("p"):
        print(f"{summ}$ is {round(summ*0.74, 2)} pound sterlings")
    elif option.lower.startswith("y"):
        print(f"{summ}$ is {round(summ*145.92, 2)} yen")
    elif option == "x":
        break
    else:
        print("Enter a valid option.")

#3
n1 = int(input("> "))
n2 = int(input("> "))
n = int(input("> "))

for i in range(n1, n2):
    if i == n:
        print(f"!{i}! ", end="")
    else:
        print(f"{i} ", end="")

#4
l = []

while True:
    n = input("Enter da number (e to stop) > ")
    if n == "e":
        break
    else:
        l.append(int(n))

print(f"Biggest of them all is {max(l)}")

#5
import random


print("Guess ma numbah between 1 and 500!")
n = random.randint(1, 501)
while True:
    g = int(input("Your guess? "))
    if g > n:
        print("Lower bruh")
    elif g < n:
        print("Higher bruh")
    elif g == n:
        print(f"Ok u got me da numbah was {n}")
        break
    else:
        print("wtf did you just type")
    
#6
print("WELCUM")
shape = input("Enter the shape - (S)quare or (R)ectangle > ")
a = 0
b = 0
if shape.lower().startswith("s"):
    a = int(input(f"How long is it's side? > "))
    symbol = input("Choose a symbol > ")
    for i in range(a):
        for j in range (a):
            print(symbol, end='')
        print("")
elif shape.lower().startswith("r"):
    a = int(input(f"How long is it's width? > "))
    b = int(input(f"How long is it's height? > "))
    symbol = input("Choose a symbol > ")
    for i in range(b):
        for j in range (a):
            print(symbol, end='')
        print("")
