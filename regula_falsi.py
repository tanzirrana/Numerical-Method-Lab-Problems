EPSILON = 0.001  

def func(x):
    return x**3 - x - 11

def regula_falsi(a, b):
    if func(a) * func(b) >= 0:
        print("You have not assumed right a and b")
        return

    c = a
    iteration = 0  

    while True:
        iteration += 1
        
        c = (a * func(b) - b * func(a)) / (func(b) - func(a))
        if abs(func(c)) < EPSILON:
            break
        if func(c) * func(a) < 0:
            b = c
        else:
            a = c

    print("\nThe value of root is:", round(c, 6))
    print("Total iterations:", iteration)
    print("Solved by---Name: Tanzir Rana, ID: 11230321262, Section: 4B")

a = 2
b = 3
regula_falsi(a, b)
