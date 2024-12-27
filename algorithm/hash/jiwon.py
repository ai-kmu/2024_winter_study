#Source Repository
#https://github.com/easyandones/Algorithm/blob/main/LeetCode/Python/705.py


class LinkedListNode:
    def __init__(self, key: int):
        self.data: int = key
        self.next: LinkedListNode | None = None


class LinkedList:
    def __init__(self):
        self.next: LinkedListNode | None = None

    def add(self, key: int) -> None:
        target = self
        while True:
            if target.next is None:
                target.next = LinkedListNode(key)
                return
            if target.next.data == key:
                return
            target = target.next

    def remove(self, key: int) -> None:
        target = self
        while True:
            if target.next is None:
                return
            if target.next.data == key:
                target.next = target.next.next
                return
            target = target.next

    def contains(self, key: int) -> bool:
        target = self
        while True:
            if target.next is None:
                return False
            if target.next.data == key:
                return True
            target = target.next


class MyHashSet:
    def __init__(self, bucket_size: int = 10):
        self.bucket_size: int = bucket_size
        self.data: list[LinkedList] = [LinkedList() for _ in range(bucket_size)]

    def getHash(self, key: int) -> int:
        return key % self.bucket_size

    def add(self, key: int) -> None:
        self.data[self.getHash(key)].add(key)

    def remove(self, key: int) -> None:
        self.data[self.getHash(key)].remove(key)

    def contains(self, key: int) -> bool:
        return self.data[self.getHash(key)].contains(key)
