from re import findall

s = open("24_21421.txt").readline()

reg = r'[1-9AB][0-9AB]*[02468A]'

print(max(map(len, findall(reg, s))))