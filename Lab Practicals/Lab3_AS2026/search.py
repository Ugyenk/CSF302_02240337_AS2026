# Q3: Binary Search vs Ternary Search (menu driven) with comparison counts
import random
import matplotlib.pyplot as plt

def binary(a, key):
    lo, hi, c = 0, len(a) - 1, 0
    while lo <= hi:
        mid = (lo + hi) // 2
        c += 1
        if a[mid] == key: return mid, c
        c += 1
        if key > a[mid]: lo = mid + 1
        else: hi = mid - 1
    return -1, c

def ternary(a, key):
    lo, hi, c = 0, len(a) - 1, 0
    while lo <= hi:
        t = (hi - lo) // 3
        m1, m2 = lo + t, hi - t
        c += 1
        if a[m1] == key: return m1, c
        c += 1
        if a[m2] == key: return m2, c
        c += 1
        if key < a[m1]: hi = m1 - 1; continue
        c += 1
        if key > a[m2]: lo = m2 + 1
        else: lo, hi = m1 + 1, m2 - 1
    return -1, c

def gen(n): return sorted(random.sample(range(1, n * 10), n))
def best_keys(a): return a[(len(a) - 1) // 2], a[(len(a) - 1) // 3]  # first middle probed
def worst_key(a): return a[-1] + 1                                                # absent, larger than all

arr_337 = []
while True:
    print("\n1.Generate  2.Display  3.Binary  4.Ternary  5.Best case  6.Worst case  7.Table  0.Exit")
    choice_337 = input("Choice: ")
    if choice_337 == "1": arr_337 = gen(int(input("n: "))); print("Array generated.")
    elif choice_337 == "2": print(arr_337)
    elif choice_337 in ("3", "4"):
        key_337 = int(input("Key: "))
        idx_337, cnt_337 = (binary if choice_337 == "3" else ternary)(arr_337, key_337)
        print(f"Index: {idx_337}  Comparisons: {cnt_337}")
    elif choice_337 == "5":
        if not arr_337: print("Generate an array first (option 1)."); continue
        kb_337, kt_337 = best_keys(arr_337)
        print("Best case -> Binary:", binary(arr_337, kb_337)[1], " Ternary:", ternary(arr_337, kt_337)[1])
    elif choice_337 == "6":
        if not arr_337: print("Generate an array first (option 1)."); continue
        k_337 = worst_key(arr_337)
        print("Worst case -> Binary:", binary(arr_337, k_337)[1], " Ternary:", ternary(arr_337, k_337)[1])
    elif choice_337 == "7":
        ns_337, bw_337, tw_337 = [10, 100, 1000, 10000, 100000, 1000000], [], []
        print(f"{'n':>8}{'Bin best':>9}{'Ter best':>9}{'Bin worst':>10}{'Ter worst':>10}")
        for n_337 in ns_337:
            a_337 = gen(n_337); kb_337, kt_337 = best_keys(a_337); k_337 = worst_key(a_337)
            bw_337.append(binary(a_337, k_337)[1]); tw_337.append(ternary(a_337, k_337)[1])
            print(f"{n_337:>8}{binary(a_337, kb_337)[1]:>9}{ternary(a_337, kt_337)[1]:>9}{bw_337[-1]:>10}{tw_337[-1]:>10}")
        plt.plot(ns_337, bw_337, 'o-', label="Binary (worst)")
        plt.plot(ns_337, tw_337, 's--', label="Ternary (worst)")
        plt.xscale("log"); plt.xlabel("n"); plt.ylabel("Comparisons")
        plt.title("Binary vs Ternary Search"); plt.legend()
        plt.savefig("search_graph.png"); plt.show()
    elif choice_337 == "0": break

# Conclusion:
# Best case: both need only 1 comparison (key found at the first middle point) -> O(1).
# Worst case:
#   Binary : T(n) = T(n/2) + O(1) -> about 2*log2(n) comparisons -> O(log n)
#   Ternary: T(n) = T(n/3) + O(1) -> about 4*log3(n) comparisons -> O(log n)
# Ternary makes fewer iterations (log3 n < log2 n) but does up to 4 comparisons per
# iteration instead of 2. Since 4*log3(n) = 2.52*log2(n) > 2*log2(n),
# Binary Search makes FEWER total comparisons and is better in practice.
