EPSILON = 0.001  

def func(x):
    return x**3 - x - 11

def secant(a, b):
    iteration = 0  

    while True:
        iteration += 1

        c = b - (func(b) * (b - a)) / (func(b) - func(a))

        if abs(func(c)) < EPSILON:
            break

        a, b = b, c

    print("\nThe value of root is:", round(c, 6))
    print("Total iterations:", iteration)
    print("Solved by---Name: Tanzir Rana, ID: 11230321262, Section: 4B")

a = 2
b = 3
secant(a, b)
