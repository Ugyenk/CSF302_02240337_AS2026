import random

def multiply_337(A, B, n):
    C = [[0]*n for _ in range(n)]
    steps = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
                steps += 1
    return C, steps

def print_mat_337(M, name):
    print(f"\n{name}:")
    for row in M: print(row)

A, B, n = [], [], 0

while True:
    print("\n1.Generate 2.Enter 3.Display 4.Multiply 5.Analysis 0.Exit")
    choice = input("Choice: ")
    
    if choice == '1':
        p = int(input("Power of 2 (e.g., 2 for 4x4): "))
        n = 2 ** p
        A = [[random.randint(1,10) for _ in range(n)] for _ in range(n)]
        B = [[random.randint(1,10) for _ in range(n)] for _ in range(n)]
        print(f"Generated {n}x{n} matrices")
    
    elif choice == '2':
        n = int(input("Size (power of 2): "))
        print("Matrix A (space separated rows):")
        A = [list(map(int, input().split())) for _ in range(n)]
        print("Matrix B:")
        B = [list(map(int, input().split())) for _ in range(n)]
    
    elif choice == '3':
        if A and B: print_mat_337(A, "A"); print_mat_337(B, "B")
        else: print("Empty!")
    
    elif choice == '4':
        if A and B:
            C, steps = multiply_337(A, B, n)
            print_mat_337(C, "Result")
            print(f"Operations: {steps}")
        else: print("Empty!")
    
    elif choice == '5':
        print(f"\n{'Size':<10}{'Operations':<20}")
        for p in range(1,6):
            size = 2 ** p
            At = [[random.randint(1,10) for _ in range(size)] for _ in range(size)]
            Bt = [[random.randint(1,10) for _ in range(size)] for _ in range(size)]
            _, ops = multiply_337(At, Bt, size)
            print(f"{size}x{size:<7}{ops:<20}")
        print("Theoretical: O(n³)")
    
    elif choice == '0': break
    else: print("Invalid!")

    # Q3: Square Matrix Multiplication - Analysis & Conclusion
# The standard matrix multiplication algorithm has O(n³) time complexity.
# Step count grows cubically with matrix size (n³ operations).
# For power of 2 matrices (2x2, 4x4, 8x8, 16x16, 32x32), operations = n³ exactly.
# Performance degrades quickly for larger matrices due to cubic complexity.
# Optimization techniques like Strassen's algorithm (O(n²·⁸¹)) could improve performance.