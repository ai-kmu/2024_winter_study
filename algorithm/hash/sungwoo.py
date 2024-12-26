class MyHashSet(object):
    def __init__(self):
        self.size = 1000001
        self.arr = [False] * self.size

    def add(self, key):
        self.arr[key] = True

    def remove(self, key):
        self.arr[key] = False

    def contains(self, key):
        return self.arr[key]
