f = open("B.3.txt")
a=int(f.readline())
data = [[abs(int(x.split()[0]) - int(x.split()[1])), int(x.split()[0]), int(x.split()[1])] for x in f]

def spi(xyz):
    summ = 0
    xyz.sort()
    for i in xyz:
        summ += max(i[1], i[2])
    if summ %3 == 0:
        for x in xyz:
            if x[0] %3 != 0:
                summ-=x[0]
                return summ
    return summ

print(spi(data))


