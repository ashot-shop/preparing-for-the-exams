with open ("B.1.txt") as f:
    k = int(f.readline())
    n = int(f.readline())
    data = [int(x) for x in f]
    max1 = max2 = -10**10
    for i in range (k, n):
        max1 = max(max1, data[i-k])
        max2 = max(max2,data[i] + max1)
print(max2)
# #otvet  1993 9999996 a u menia 1993 9999994

f = open('B.1.txt')
k = int(f.readline())
n = int(f.readline())
a = [int(x) for x in f]
summa = 0
maxi = 0
for i in range(n):
    maxi = max(maxi, a[i])
    if i + k < len(a):
        summa = max(summa, maxi+a[i+k])
print(summa)