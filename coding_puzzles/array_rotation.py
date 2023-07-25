
def rotate(a, k):
    result = [""] * len(a)
    for i in range(len(a)):
        result[(i + k) % len(a)] = a[i]
    return result
