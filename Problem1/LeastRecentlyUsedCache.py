
# As the most important requirement of implementing a cache is its efficiency, the ideal data structure to use while
# building it is hash map (all operations like reading or adding a value have constant time complexity). This is how
# I chose to store the data. However, the tricky part of LRU requirement is that when the limited capacity of cache is
# filled when we attempt to add another value, we must release space by removing the least used value. This could not
# be easily done by using the hash map only, as it would mean iterating over the whole map and comparing "times used"
# values, most of the times we would try to add new value. To fix this, I used another data structure, a linked list,
# to store values alongside map. In map, I do not store raw values, but list nodes. Therefore, every time I "used" a
# value, I also had a reference to node in the list, which allowed me to put this node to the head of list. Reading a
# reference from the map is O(1) and changing a nodes's position in the list is also O(1). By doing that, I know, that
# the least used node is the one at the tail of the list. When the capacity of the cache is be full while another
# element is added, the element from the tail is removed (O(1)) and the reference of the node is removed from map
# (O(1)).


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, node):
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            self.head.previous = node
            node.next = self.head
            self.head = node
            self.head.previous = None

    def move_to_head(self, node):
        if self.head == node:
            return

        if self.tail == node:
            self.tail = node.previous
            self.tail.next = None
        else:
            node.next.previous = node.previous
            node.previous.next = node.next

        self.head.previous = node
        node.next = self.head
        self.head = node
        self.head.previous = None

    def pop(self):
        removed = self.tail
        self.tail = removed.previous
        return removed

    def __repr__(self):
        values = []
        current = self.head
        while current:
            values.append([current.key, current.value])
            current = current.next
        return values

    def __str__(self):
        return str(self.__repr__())


class LRU_Cache:

    def __init__(self, capacity):
        self.MAX_CACHE_CAPACITY = capacity
        self.cache = dict()
        self.list = LinkedList()

    def get(self, key):
        try:
            value = self.cache[key].value
            self.list.move_to_head(self.cache[key])
            return value
        except KeyError:
            return -1

    def set(self, key, value):
        if len(self.cache) == self.MAX_CACHE_CAPACITY:
            self.cache.pop(self.list.pop().key)
        new_node = Node(key, value)
        self.cache.update({key: new_node})
        self.list.append(new_node)


# Linked list tests
test_list = LinkedList()
node0 = Node(1, 2)
test_list.append(node0)
test_list.append(Node(3, 4))
test_list.append(Node(5, 6))
print(test_list)  # prints [[1, 2], [3, 4], [5, 6]]
assert test_list.__repr__() == [[5, 6], [3, 4], [1, 2]]

test_list.move_to_head(node0)
print(test_list)  # prints [[1, 2], [5, 6], [3, 4]]
assert test_list.__repr__() == [[1, 2], [5, 6], [3, 4]]

node1 = Node(7, 8)
test_list.append(node1)
test_list.move_to_head(node1)
print(test_list)  # prints [[7, 8], [1, 2], [5, 6], [3, 4]]
assert test_list.__repr__() == [[7, 8], [1, 2], [5, 6], [3, 4]]

node2 = Node(9, 10)
test_list.append(node2)
test_list.append(Node(11, 12))
print(test_list)
test_list.move_to_head(node2)
print(test_list)  # prints [[9, 10], [11, 12], [7, 8], [1, 2], [5, 6], [3, 4]]
assert test_list.__repr__() == [[9, 10], [11, 12], [7, 8], [1, 2], [5, 6], [3, 4]]

our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))     # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
