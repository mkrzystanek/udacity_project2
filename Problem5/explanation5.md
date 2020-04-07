###### Time complexity:
**add() method:**

O(1), because it involves adding new element to a linked list.

**print_chain() method**

O(n), because it involves traversing every element of the list.

**\_\_str()\_\_ method**
O(n), because it involves traversing every element if the list.

###### Sace complexity:

Because I chose to implement BlockChain as LinkedList, operations like "add" will take O(1), while operations that
need traversing over chain (like "print_chain") will take O(n).