class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.cache = {} # map key to node

        # Left=LRU, Right=MRU
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.next, self.right.prev = self.right, self.left

    # remove node from List
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # insert node at right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev    

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove from the list and delete the LRU from the hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


# Test Case
cache = LRUCache(2)
cache.put(1, 1)  # LRU: [1:1]
cache.put(2, 2)  # LRU: [1:1] -> [2:2]
print(cache.get(1))  # Expected output: 1
cache.put(3, 3)  # LRU: [2:2] -> [3:3]
print(cache.get(2))  # Expected output: -1 (Key 2 was evicted)
cache.put(4, 4)  # LRU: [3:3] -> [4:4]
print(cache.get(1))  # Expected output: -1 (Key 1 was evicted)
print(cache.get(3))  # Expected output: 3
print(cache.get(4))  # Expected output: 4
