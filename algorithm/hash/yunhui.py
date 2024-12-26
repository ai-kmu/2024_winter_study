class MyHashSet:

    def __init__(self):
        self.hash = []

    def add(self, key: int) -> None:
        if key not in self.hash:
            self.hash.append(key)
        

    def remove(self, key: int) -> None:
        if key in self.hash:
            self.hash.remove(key)

    def contains(self, key: int) -> bool:
        if key in self.hash:
            return True
        else:
            return False
