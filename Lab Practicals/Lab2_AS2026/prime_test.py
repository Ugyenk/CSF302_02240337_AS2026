import math, time, matplotlib.pyplot as plt

def naive_prime_337(n):
    if n < 2: return False, 0
    steps = 0
    for i in range(2, n):
        steps += 1
        if n % i == 0: return False, steps
    return True, steps
10
def optimized_prime_337(n):
    if n < 2: return False, 0
    steps = 0
    for i in range(2, int(math.sqrt(n)) + 1):
        steps += 1
        if n % i == 0: return False, steps
    return True, steps

numbers_337 = []
print("Enter at least 10 numbers:")
while len(numbers_337) < 10:
    try:
        numbers_337.append(int(input(f"Number {len(numbers_337)+1}: ")))
    except: print("Invalid input")

naive_times_337, opt_times_337 = [], []
naive_steps_337, opt_steps_337 = [], []

for n in numbers_337:
    start = time.perf_counter()
    is_naive, s1 = naive_prime_337(n)
    naive_times_337.append((time.perf_counter() - start) * 1000)
    naive_steps_337.append(s1)
    
    start = time.perf_counter()
    is_opt, s2 = optimized_prime_337(n)
    opt_times_337.append((time.perf_counter() - start) * 1000)
    opt_steps_337.append(s2)
    
    print(f"{n}: Naive={is_naive}({s1} steps), Optimized={is_opt}({s2} steps)")

print(f"\nAvg Time: Naive={sum(naive_times_337)/len(naive_times_337):.3f}ms, Opt={sum(opt_times_337)/len(opt_times_337):.3f}ms")
print(f"Speedup: {sum(naive_times_337)/sum(opt_times_337):.2f}x faster")

plt.figure(figsize=(12,4))
plt.subplot(1,2,1)
plt.plot(numbers_337, naive_times_337, 'ro-', label='Naive')
plt.plot(numbers_337, opt_times_337, 'bs-', label='Optimized')
plt.xlabel('Numbers'); plt.ylabel('Time (ms)'); plt.title('Time Comparison_337'); plt.legend(); plt.grid(True)

plt.subplot(1,2,2)
plt.plot(numbers_337, naive_steps_337, 'ro-', label='Naive')
plt.plot(numbers_337, opt_steps_337, 'bs-', label='Optimized')
plt.xlabel('Numbers'); plt.ylabel('Steps'); plt.title('Step Comparison_337'); plt.legend(); plt.grid(True)
plt.tight_layout(); plt.show()

# Q1: Prime Number Testing - Analysis & Conclusion
# The optimized method (checking up to √n) is significantly faster than the naive method (checking up to n-1).
# Time complexity: Naive = O(n), Optimized = O(√n)
# The step count reduction is approximately √n times, making it much more efficient for larger numbers.
# For prime numbers, the difference is most noticeable as the naive method checks all numbers up to n-1.