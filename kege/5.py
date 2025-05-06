for n in range(1, 500):
    bin_n = bin(n)[2:]
    bin_n += bin(bin_n.count('1')%2)[2:]
    bin_n += bin(bin_n.count('1')%2)[2:]
    r = int(bin_n, 2)
    if r < 253:
        print(n, r)