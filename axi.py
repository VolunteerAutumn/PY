# ----1
n1 = int(input("> "))
n2 = int(input("> "))
for i in range(n1, n2 + 1):
    print(i)

# ----2
n1 = int(input("> "))
n2 = int(input("> "))
for i in range(n1, n2 + 1):
    if i%2 != 0:
            print(i)

# ----3
n1 = int(input("> "))
n2 = int(input("> "))
for i in range(n2, n1-1, -1):
    if i%2==0:
        print(i)

# ----4
n1 = int(input("> "))
n2 = int(input("> "))
w = int(input("mode? (1/2)> "))
if w==1:
    for i in range(n1, n2+1):
        print(i)
elif w==2:
    for i in range(n2, n1-1, -1):
        print(i)
else:
    print("err")

# ----5
n1 = int(input("> "))
n2 = int(input("> "))
if n1>n2:
    for i in range(n2, n1):
        if i%2!=0:
            print(i)
elif n2>n1:
    for i in range(n1, n1):
        if i%2!=0:
            print(i)

# ----6
n1 = int(input("> "))
n2 = int(input("> "))
if n1>n2:
    for i in range(n2, n1+1):
        if i%2==0:
            print(i)
    print("-------")
    for i in range(n1, n2-1, -1):
        if i%2!=0:
            print(i)
elif n2>n1:
    for i in range(n1, n2+1):
        if i%2==0:
            print(i)
    print("-------")
    for i in range(n2, n1-1, -1):
        if i%2!=0:
            print(i)

# PART 2
# ----1
n1 = int(input("> "))
n2 = int(input("> "))
sup = 0
for i in range(n1, n2+1):
    sup += i
print("sum: ", sup)
print("avg: ", round(sup/((n2+1)/n1)))

# ----2
n = int(input("> "))
f = 1
for i in range(1, n+1):
    f *= i
print(f"factorial: {f}")

# ----3
n = int(input("> "))
for i in range(n):
    print("*", end="")

# ----4
a, s = input("> ").split()
for i in range(int(a)):
    print(s, end="")

# ----5
while True:
    option = int(input("Enter option (1 for a minimum, 2 for a maximum, 3 to quit > "))
    if option == 1:
        n1 = int(input("> "))
        n2 = int(input("> "))
        print(f"Largest of them is {max(n1, n2)}")
    elif option == 2:
        n1 = int(input("> "))
        n2 = int(input("> "))
        print(f"Smallest of them is {min(n1, n2)}")
    elif option == 3:
        print("Exiting the program...\n\n")
        break
    else:
        print("Please enter 1, 2 or 3.")

# ----6
while True:
    option = int(input("Enter option (1 for a add, 2 for a substract, 3 to divide, 4 to quit) > "))
    if option == 1:
        n1 = int(input("> "))
        n2 = int(input("> "))
        print(f"Sum: {n1+n2}")
    elif option == 2:
        n1 = int(input("> "))
        n2 = int(input("> "))
        print(f"Sub: {n1-n2}")
    elif option == 3:
        n1 = int(input("> "))
        n2 = int(input("> "))
        print(f"Div: {n1/n2}")
    elif option == 4:
        print("Exiting the program...\n\n")
        break
    else:
        print("Please enter 1, 2, 3 or 4.")
