sum = 10
n_2 = 2
n_1 = 8
while True:
    n = 4 * n_1 + n_2
    if n >= 4_000_000: break
    n_2, n_1 = n_1, n
    sum += n
print(sum)
