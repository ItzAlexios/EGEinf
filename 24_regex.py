from re import *

s = open('24_19969.txt').readline()

reg = r'([a-z]+\@[a-z]+\.[a-z]+)'

print(max(map(len, findall(reg, s))))