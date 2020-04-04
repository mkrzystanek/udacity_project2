As the most important requirement of implementing a cache is its efficiency, the ideal data structure to use while
building it is hash map (all operations like reading or adding a value have constant time complexity). This is how
I chose to store the data. However, the tricky part of LRU requirement is that when the limited capacity of cache is
filled when we attempt to add another value, we must release space by removing the least used value. This could not
be easily done by using the hash map only, as it would mean iterating over the whole map and comparing "times used"
values, most of the times we would try to add new value. To fix this, I used another data structure, a linked list,
to store values alongside map. In map, I do not store raw values, but list nodes. Therefore, every time I "used" a
value, I also had a reference to node in the list, which allowed me to put this node to the head of list. Reading a
reference from the map is O(1) and changing a nodes's position in the list is also O(1). By doing that, I know, that
the least used node is the one at the tail of the list. When the capacity of the cache is be full while another
element is added, the element from the tail is removed (O(1)) and the reference of the node is removed from map
(O(1)).
