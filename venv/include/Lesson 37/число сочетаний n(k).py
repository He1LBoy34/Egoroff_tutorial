def factorilal(x):
    pr = 1
    for i in range(2, x + 1):
        pr = pr * i
    return pr

def sochetanie(n, k):
    return factorilal(n) / (factorilal(k) * factorilal(n - k))

print(sochetanie(5, 3))

