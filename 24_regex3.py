from re import *

s = open('24_19970.txt').readline()

reg = r'(?:[1-9][0-9]*[05]|0)'

pattern = rf'{reg}(?:[+*]{reg})*'

print(max(map(len, findall(pattern, s))))