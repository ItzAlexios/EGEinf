f = open('26 вар1.txt')

all_act = []

for x in f:
    start, end = map(int, x.split())
    all_act.append((start, end + start))
max_first_element= max(all_act)

all_act.sort(key = lambda x:x[1])
otvet=[]
end = 0
for i in range(len(all_act)):
    if end <= all_act[i][0]:
        end = all_act[i][1]
        otvet.append(all_act[i])
print(len(otvet), max_first_element[0] - otvet[-2][1])