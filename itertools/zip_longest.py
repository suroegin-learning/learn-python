from itertools import zip_longest as zip

alist = ["Ivan", "Daria", "Dmitry", "Nokolay"]
blist = [1988, 1988, 1991]

print(list(zip(alist, blist)))
