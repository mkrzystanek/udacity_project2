###### Time complexity:
**union() function:**

O(n+m), where n is the length of the first parameter list, 
and m the length of the second parameter list. This is because 
method involves iterating over both lists while "add_to_set()" function
is invoked and over the "set when convert_to_linked_list()" is
invoked.

**intersection() method**

O(n*m), because it involves iterating over both input lists, when 
converting them to sets, then looping over one of the sets and 
using the "in" operator on other set inside.


###### Sace complexity:

**union() function:**

O(n+m), because at one time method puts two sets (which would have 
size of n and m in worst case scenario) and linked list that represents 
a union of those sets into memory.

**intersection() method**

O(n+m), because it involves creating two sets of the input list and a new
set that represents intersection of them. 