def gauss_elimination_backward():
    n = int(input("\nEnter the order of matrix: "))
    A = []
    for i in range(n):
        row = []
        for j in range(n+1):
            val = float(input(f"A[{i+1}][{j+1}] : "))
            row.append(val)
        A.append(row)

    for j in range(n):
        for i in range(n):
            if i > j:
                c = A[i][j]/A[j][j]
                for k in range(n+1):
                    A[i][k] = A[i][k] - c*A[j][k]

    x = [0]*(n+1)
    x[n-1] = A[n-1][n]/A[n-1][n-1]

    for i in range(n-2, -1, -1):
        sum_val = 0
        for j in range(i+1, n):
            sum_val += A[i][j]*x[j]
        x[i] = (A[i][n] - sum_val)/A[i][i]

    print("\nThe solution is: ")
    for i in range(n):
        print(f"\nx{i+1}={x[i]}\t")

    print("Solved by---Name: Tanzir Rana, ID: 11230321262, Section: 4B")

gauss_elimination_backward()
