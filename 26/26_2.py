f = open('26_838.txt')

n = int(f.readline())

d1 = []
d2 = []

files = [int(i) for i in f]
files.sort()


for i in range(n):
    if len(files) > 1:
        d1.append(files[-1])
        del(files[-1])
    while sum(d1) > sum(d2):
        d2.append(files[0])
        del(files[0])

print(len(d1), len(d2))