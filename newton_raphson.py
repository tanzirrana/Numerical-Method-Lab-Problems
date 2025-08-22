EPSILON = 0.001  

def func(x):
    return x**3 - x - 11

def deriv(x):
    return 3*x**2 - 1

def newton_raphson(x0):
    iteration = 0  

    while True:
        iteration += 1
        x1 = x0 - func(x0)/deriv(x0)
        if abs(func(x1)) < EPSILON:
            break
        x0 = x1

    print("\nThe value of root is:", round(x1, 6))
    print("Total iterations:", iteration)
    print("Solved by---Name: Tanzir Rana, ID: 11230321262, Section: 4B")

x0 = 2
newton_raphson(x0)
