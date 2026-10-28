"""
Experiment 7: Hashing and Strings
Program 1: Hash Table (Chaining and Linear Probing)
Aim: Implement collision handling using chaining and linear probing.
"""

class HashChaining:
    def __init__(self, size=10):
        self.table = [[] for _ in range(size)]
        self.size = size
    def insert(self, key):
        self.table[key % self.size].append(key)
    def search(self, key):
        return key in self.table[key % self.size]

class HashLinearProbing:
    def __init__(self, size=10):
        self.table = [None] * size
        self.size = size
    def insert(self, key):
        idx = key % self.size
        for _ in range(self.size):
            if self.table[idx] is None or self.table[idx] == key:
                self.table[idx] = key
                return
            idx = (idx + 1) % self.size
        raise OverflowError("Hash table is full")
    def search(self, key):
        idx = key % self.size
        for _ in range(self.size):
            if self.table[idx] is None:
                return False
            if self.table[idx] == key:
                return True
            idx = (idx + 1) % self.size
        return False

h = HashChaining()
h.insert(15); h.insert(25); h.insert(35)
print(h.search(25))
p = HashLinearProbing()
p.insert(15); p.insert(25); p.insert(35)
print(p.search(25))
