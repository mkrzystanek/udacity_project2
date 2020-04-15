###### Time complexity:
**find_in_group() function:**

Function "find_in_group" searches the tree of groups and users recursively. Returns True if user is in group, if not, calls itself
with every sub group. Using "in" operator has O(n) complexity. Because in this algorithm groups are visited one by one, the overall complexity depends on the
total number of groups in the tree, and is O(depth x no. of users).

###### Space complexity:
**find_in_group() function:**

For each function call lists returned by "get_users()" and "get_groups()" are read into memory, so the space 
complexity is O(n). However, function is recursive, and its calls are put on the call stack for all nodes in tree 
(in a worst case scenario). Therefore, the space complexity of "find_in_group()" is O(depth x no. of users)
    