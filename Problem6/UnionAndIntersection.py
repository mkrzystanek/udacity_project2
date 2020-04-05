class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

    def __eq__(self, other):
        """ custom __eq__ method was needed to allow correct result of set methods being invoked on sets of Nodes, as well
        as streamlined testing by allowing comparing them to sets of string values"""
        return self.value == other or self.value == other.value

    def __hash__(self):
        """ custom __hash__ method was needed to allow correct result of set methods being invoked on sets of Nodes """
        return hash(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    union_set = set()
    union_set = add_to_set(llist_1, union_set)
    union_set = add_to_set(llist_2, union_set)

    return convert_to_linked_list(union_set)


def intersection(llist_1, llist_2):
    set_1 = add_to_set(llist_1, set())
    set_2 = add_to_set(llist_2, set())
    intersection_set = set()

    for element in set_1:
        if element in set_2:
            intersection_set.add(element)

    return convert_to_linked_list(intersection_set)


def add_to_set(llist, set):
    current = llist.head
    while current:
        set.add(current.value)
        current = current.next

    return set


def convert_to_linked_list(a_set):
    a_list = LinkedList()
    for element in a_set:
        a_list.append(element)
    return a_list

# Test case 1
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2))
assert str(union(linked_list_1, linked_list_2)) == "32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 -> "
print(intersection(linked_list_1, linked_list_2))
assert str(intersection(linked_list_1, linked_list_2)) == "4 -> 21 -> 6 -> "

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))
assert str(union(linked_list_3, linked_list_4)) == "65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 -> "
print(intersection(linked_list_3, linked_list_4))
assert str(intersection(linked_list_3, linked_list_4)) == ""

# Test case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = []
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print(union(linked_list_5, linked_list_6))
assert str(union(linked_list_5, linked_list_6)) == "1 -> 7 -> 8 -> 9 -> 11 -> 21 -> "
print(intersection(linked_list_5, linked_list_6))
assert str(intersection(linked_list_5, linked_list_6)) == ""

# Test case 4

linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = [4, 4, 4, 4]
element_2 = [1, 7, 8, 4, 11, 21, 1]

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

print(union(linked_list_7, linked_list_8))
assert str(union(linked_list_7, linked_list_8)) == "1 -> 4 -> 7 -> 8 -> 11 -> 21 -> "
print(intersection(linked_list_7, linked_list_8))
assert str(intersection(linked_list_7, linked_list_8)) == "4 -> "
