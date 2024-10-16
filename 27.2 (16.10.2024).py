f = open("B.2.txt")

data = [int(x) for x in f]
a = data.pop(0)
d= 0
data.sort(reverse = True)

def count_x(xyz, a):
    for i in range(a):
        for j in range(i+1, a):
            d = xyz[i] * xyz[j]

            if d % 14 == 0:
                return d

print(count_x(data,a))
