import random, time

def merge_sort_337(arr, steps):
    if len(arr) <= 1: return arr, steps
    mid = len(arr)//2
    left, steps = merge_sort_337(arr[:mid], steps)
    right, steps = merge_sort_337(arr[mid:], steps)
    result, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        steps += 1
        if left[i] <= right[j]: result.append(left[i]); i += 1
        else: result.append(right[j]); j += 1
    return result + left[i:] + right[j:], steps

array_337, n_337, steps_337 = [], 0, 0

while True:
    print("\n1.Generate 2.Display 3.Ascend(Merge) 4.Descend 5.Random Time 6.Sorted Time 7.Descending Time 0.Exit")
    choice = input("Choice: ")
    
    if choice == '1':
        n_337 = int(input("n: "))
        array_337 = [random.randint(1,1000) for _ in range(n_337)]
        print(f"Generated {n_337} numbers")
    
    elif choice == '2': print(f"Array: {array_337}")
    
    elif choice == '3':
        if array_337:
            array_337, steps_337 = merge_sort_337(array_337, 0)
            print(f"Sorted: {array_337}, Steps: {steps_337}")
        else: print("Empty!")
    
    elif choice == '4':
        if array_337: array_337.sort(reverse=True); print(f"Descending: {array_337}")
        else: print("Empty!")
    
    elif choice in ['5','6','7']:
        labels = {'5':'Random','6':'Sorted','7':'Descending'}
        print(f"\n{labels[choice]} Data Analysis_337")
        print(f"{'Size':<10}{'Steps':<15}{'Time(ms)':<15}")
        for size in [100,500,1000,2000,3000]:
            if choice == '5': arr = [random.randint(1,1000) for _ in range(size)]
            elif choice == '6': arr = list(range(size))
            else: arr = list(range(size,0,-1))
            start = time.perf_counter()
            _, steps = merge_sort_337(arr, 0)
            elapsed = (time.perf_counter() - start) * 1000
            print(f"{size:<10}{steps:<15}{elapsed:<15.3f}")
    
    elif choice == '0': break
    else: print("Invalid choice!")


 # Q2: Merge Sort Analysis - Analysis & Conclusion
# Merge Sort consistently shows O(n log n) time complexity regardless of input order.
# Step counts remain relatively stable for random, sorted, and reverse-sorted data.
# This demonstrates Merge Sort's stability and predictable performance.
# The algorithm efficiently handles all input types with the same time complexity.
# Best/Average/Worst case: O(n log n) - making it suitable for large datasets.