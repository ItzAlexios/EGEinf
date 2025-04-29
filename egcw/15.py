b = [i for i in range(36, 76)]
c = [i for i in range(60, 111)]
a = []

def f(x):
    return (x not in a) <= ( (x in b) == (x in c) )


for x in range(1, 1000):
    if not f(x):
        a.append(x)

print(max(a) - min(a))