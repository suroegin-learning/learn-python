import pickle
from itertools import permutations

class Permuter:
    def __init__(self, symbols, length):
        self.symbols = symbols
        self.length = length
        self.results = list()

    def _store_state(self):
        with open("pickled.data", "wb") as f:
            pickle.dump(self, f)

    def start(self):
        p = permutations(self.symbols, self.length)

        no_more = False
        while not no_more:
            while len(self.results) < 10:
                try:
                    self.results.append("".join(next(p)))
                except StopIteration:
                    no_more = True
                    break
            print("Result:", self.results)
            self._store_state()
            self.results = []
            break

a = Permuter("abcd", 4)
a.start()