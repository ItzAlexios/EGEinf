from re import*

s = open('24_19968.txt').readline()

reg = r'(?:[1-5][0-5]*|0)'
pattern = rf'{reg}(?:[+*]{reg})*'

print(max(map(len, findall(pattern, s) ) ) )