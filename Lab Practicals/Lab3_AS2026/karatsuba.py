# Q2: Traditional (grade-school) vs Karatsuba Multiplication of large integers
import random, time
import matplotlib.pyplot as plt

def traditional(x, y):                       # x, y are digit strings
    res = [0] * (len(x) + len(y))
    for i, a in enumerate(reversed(x)):
        for j, b in enumerate(reversed(y)):
            res[i + j] += int(a) * int(b)
    for i in range(len(res) - 1):            # handle carries
        res[i + 1] += res[i] // 10
        res[i] %= 10
    return int("".join(map(str, reversed(res))))

def karatsuba(x, y):
    n = max(len(x), len(y))
    if n <= 32:                                  # small numbers: use traditional (less overhead)
        return traditional(x, y)
    m = 1
    while m < n: m *= 2                  # next power of 2
    x, y = x.zfill(m), y.zfill(m)   # pad both to same length
    h = m // 2
    a, b, c, d = x[:h], x[h:], y[:h], y[h:]
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    mid = karatsuba(str(int(a) + int(b)), str(int(c) + int(d))) - ac - bd
    return ac * 10**m + mid * 10**h + bd   # only 3 multiplications

def rand_num(d): return str(random.randint(1, 9)) + "".join(random.choice("0123456789") for _ in range(d - 1))

x_337, y_337 = rand_num(8), rand_num(8)
print(f"{x_337} x {y_337}\nTraditional: {traditional(x_337, y_337)}\nKaratsuba  : {karatsuba(x_337, y_337)}")

sizes_337, t1_337, t2_337 = [8, 16, 32, 64, 128, 256, 512, 1024, 2048], [], []
print(f"\n{'digits':>7}{'Traditional(s)':>16}{'Karatsuba(s)':>14}{'Match':>7}")
for digits_337 in sizes_337:
    x_337, y_337 = rand_num(digits_337), rand_num(digits_337)
    start_337 = time.time(); r1_337 = traditional(x_337, y_337); t1_337.append(time.time() - start_337)
    start_337 = time.time(); r2_337 = karatsuba(x_337, y_337);   t2_337.append(time.time() - start_337)
    print(f"{digits_337:>7}{t1_337[-1]:>16.5f}{t2_337[-1]:>14.5f}{str(r1_337 == r2_337):>7}")

plt.plot(sizes_337, t1_337, 'o-', label="Traditional O(n^2)")
plt.plot(sizes_337, t2_337, 's--', label="Karatsuba O(n^1.585)")
plt.xlabel("Number of digits"); plt.ylabel("Time (s)"); plt.title("Large Integer Multiplication")
plt.legend(); plt.savefig("karatsuba_graph.png"); plt.show()

# Conclusion:
# Karatsuba's result matched the traditional method in every test case.
# Traditional: every digit times every digit -> O(n^2).
# Karatsuba: 3 multiplications of half size -> T(n) = 3T(n/2) + O(n) = O(n^log2(3)) ~ O(n^1.585).
# Recursion stops at 32 digits (switches to traditional) because recursion overhead makes
# Karatsuba slow on tiny numbers. Up to ~512 digits both take similar time, but from
# ~1024 digits Karatsuba starts to pull ahead, and the gap widens as n grows.
# (Exact timings vary from run to run.)
