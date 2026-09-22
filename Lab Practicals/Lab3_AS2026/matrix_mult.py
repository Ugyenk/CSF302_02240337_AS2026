# Q1: Traditional vs Strassen's Matrix Multiplication
import random, time
import matplotlib.pyplot as plt

def traditional(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]

def add(A, B): return [[x + y for x, y in zip(r, s)] for r, s in zip(A, B)]
def sub(A, B): return [[x - y for x, y in zip(r, s)] for r, s in zip(A, B)]

def strassen(A, B):
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    h = n // 2
    q = lambda M, r, c: [row[c:c + h] for row in M[r:r + h]]  # quadrant
    a, b, c, d = q(A, 0, 0), q(A, 0, h), q(A, h, 0), q(A, h, h)
    e, f, g, k = q(B, 0, 0), q(B, 0, h), q(B, h, 0), q(B, h, h)
    p1 = strassen(a, sub(f, k))
    p2 = strassen(add(a, b), k)
    p3 = strassen(add(c, d), e)
    p4 = strassen(d, sub(g, e))
    p5 = strassen(add(a, d), add(e, k))
    p6 = strassen(sub(b, d), add(g, k))
    p7 = strassen(sub(a, c), add(e, f))
    C11 = add(sub(add(p5, p4), p2), p6)
    C12 = add(p1, p2)
    C21 = add(p3, p4)
    C22 = sub(sub(add(p1, p5), p3), p7)
    return ([l + r for l, r in zip(C11, C12)] +
            [l + r for l, r in zip(C21, C22)])

def rand_matrix(n): return [[random.randint(0, 9) for _ in range(n)] for _ in range(n)]

# Show a small example
A_337, B_337 = rand_matrix(4), rand_matrix(4)
print("A =", A_337, "\nB =", B_337)
print("Traditional:", traditional(A_337, B_337))
print("Strassen   :", strassen(A_337, B_337))

# Timing table
sizes_337, t1_337, t2_337 = [2, 4, 8, 16, 32, 64, 128], [], []
print(f"\n{'n':>5}{'Traditional(s)':>16}{'Strassen(s)':>14}{'Match':>7}")
for n in sizes_337:
    A_337, B_337 = rand_matrix(n), rand_matrix(n)
    start_337 = time.time(); R1_337 = traditional(A_337, B_337); t1_337.append(time.time() - start_337)
    start_337 = time.time(); R2_337 = strassen(A_337, B_337);    t2_337.append(time.time() - start_337)
    print(f"{n:>5}{t1_337[-1]:>16.5f}{t2_337[-1]:>14.5f}{str(R1_337 == R2_337):>7}")

plt.plot(sizes_337, t1_337, 'o-', label="Traditional O(n^3)")
plt.plot(sizes_337, t2_337, 's--', label="Strassen O(n^2.81)")
plt.xlabel("Matrix size n"); plt.ylabel("Time (s)"); plt.title("Matrix Multiplication")
plt.legend(); plt.savefig("matrix_graph.png"); plt.show()

# Conclusion:
# Both methods give the same result for every n.
# Traditional does n^3 multiplications -> T(n) = O(n^3).
# Strassen does 7 multiplications per split: T(n) = 7T(n/2) + O(n^2) = O(n^log2(7)) ~ O(n^2.81).
# In practice (in Python, recursing down to 1x1) Strassen is SLOWER for these sizes because
# of the heavy overhead of recursion, splitting and many matrix additions. Its advantage
# only shows for very large n, or when recursion stops at a larger base size.
