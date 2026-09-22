import random

def minmax_337(A337, lo337, hi337, counter337):
    if hi337 - lo337 == 0:
        return A337[lo337], A337[lo337]

    if hi337 - lo337 == 1:
        counter337[0] += 1
        if A337[lo337] < A337[hi337]:
            return A337[lo337], A337[hi337]
        else:
            return A337[hi337], A337[lo337]

    mid337 = (lo337 + hi337) // 2
    min1_337, max1_337 = minmax_337(A337, lo337, mid337, counter337)
    min2_337, max2_337 = minmax_337(A337, mid337 + 1, hi337, counter337)

    counter337[0] += 1
    minVal337 = min1_337 if min1_337 < min2_337 else min2_337

    counter337[0] += 1
    maxVal337 = max1_337 if max1_337 > max2_337 else max2_337

    return minVal337, maxVal337


def closed_form_337(n337):
    return (3 * n337) // 2 - 2


if __name__ == "__main__":
    sizes337 = [8, 64, 512, 4096]
    for n337 in sizes337:
        arr337 = random.sample(range(-1000000, 1000000), n337)
        counter337 = [0]
        result_min337, result_max337 = minmax_337(arr337, 0, n337 - 1, counter337)
        assert result_min337 == min(arr337)
        assert result_max337 == max(arr337)
        print(n337, counter337[0], closed_form_337(n337), 2*n337 - 2)