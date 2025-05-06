for i in range(500_001, 10**40):
    divs = []
    for j in range(1, i+1):
        if i % j == 0:
            divs.append(j)
    
    R = sum(divs)

    if str(R)[-1] == '6':
        print(i, R)