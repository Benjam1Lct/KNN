def dist_hamming(m1,m2):
    d = 0
    for a,b in zip(m1,m2):
        if a != b :
            d += 1
    return d

m = input("Entrez un mot")
d = int(input("Distance max"))

for i in lexique:
    if dist_hamming(i, m) >= d:
        print(i)