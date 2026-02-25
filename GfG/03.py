def sum(n):
    sum = 0
    i = 0
    while i <= n:
        sum += i
        i = i + 1
    return sum
n = 5
print(sum(n))