def pow(x, n, i=0):
    if i == n:
        return 1
    return pow(x, n, i+1)*x


print(pow(42, 0)) # 1
print(pow(1, 10)) # 1
print(pow(2, 5)) # 32
print(pow(7, 2)) # 49
