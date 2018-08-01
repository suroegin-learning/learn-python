import pickle
from itertools import permutations

generated = 0
results = []

p = permutations("abcd")

while generated < 10:
    results.append(next(p))
    generated += 1

with open("pickled.data", "wb") as f:
    save_perm = pickle.dump(p, f)

print("All done!")
print("Permutation result:", results)