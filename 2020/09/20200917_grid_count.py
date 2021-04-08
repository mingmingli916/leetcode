# mxn的格子，从左上角走到右下角，总共有多少种走法？
# 其实是一个排列组合的问题，总共要走m+n步，以n为例子，则为从m+n中选取n个。


def total_count(n, m):
    total = n + m
    num = 1
    den = 1
    for i in range(1, n + 1):
        den = den * i
        num = num * (total - i + 1)
    print(num / den)


for i in range(1, 7):
    total_count(i, i)
