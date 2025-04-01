from re import *

s = open('24_19967.txt').readline()

reg = r'(?:[1-9][0-9]*|0)'
r = rf'AFD{reg}(?:[+*]{reg})*'
print(max(map(len,  findall(r, s))))