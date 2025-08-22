def gauss_elimination():
    n = int(input("\nEnter the size of matrix: "))
    A = []
    for i in range(n):
        row = []
        for j in range(n+1):
            val = float(input(f" A[{i+1}][{j+1}]: "))
            row.append(val)
        A.append(row)

    for j in range(n):
        for i in range(n):
            if i != j:
                c = A[i][j]/A[j][j]
                for k in range(n+1):
                    A[i][k] = A[i][k] - c*A[j][k]

    x = [0]*n
    for i in range(n):
        x[i] = A[i][n]/A[i][i]

    print("\nThe solution is:")
    for i in range(n):
        print(f"\n x{i+1}={x[i]}")

    print("Solved by---Name: Tanzir Rana, ID: 11230321262, Section: 4B")

gauss_elimination()
