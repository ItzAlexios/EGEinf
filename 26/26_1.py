f = open('26_813.txt')

s, n = map(int, f.readline().split())

d = []

files = [int(i) for i in f]
files.sort()

for i in range(n):
    while sum(d) <= s:
        d.append(files[-1])
        del(files[-1])
        d.append(files[0])
        del(files[0])
        if sum(d) >= s:
            d.pop()
            break

print(len(d), d[-1])