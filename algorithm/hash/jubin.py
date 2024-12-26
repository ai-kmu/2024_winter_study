class MyHashSet:

    def __init__(self):
        self.hash_list = set()

    def add(self, key: int):
        self.hash_list.add(key)

    def remove(self, key: int):
        self.hash_list.discard(key)

    def contains(self, key: int):
        if key in self.hash_list:
            return True
        else:
            return False
