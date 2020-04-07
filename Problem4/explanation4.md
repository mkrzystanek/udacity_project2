###### Time complexity:
**find_in_group() function:**

Function "find_in_group" searches the tree of groups and users recursively. Returns True if user is in group, if not, calls itself
with every sub group. Using "in" operator has O(n) complexity. Because in this algorithm groups are visited one by one, the overall complexity depends on the
total number of groups in the tree, which is O(n^2).

###### Sace complexity:

