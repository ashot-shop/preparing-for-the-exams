#27991
f = open("B.4.txt") 
a = int(f.readline())
data = [int(x) for x in f]
m = 0
l=[]
for i in range(a):
    for j in range(i+1, a):
        if (abs(data[i]-data[j])) %2 == 0:
            if (data[i]%17 == 0) or (data[j]%17==0 ):
                if m < (data[i]+ data[j]):
                    m = data[i]+ data[j]
                    l=[data[i], data[j]]

print(l)
