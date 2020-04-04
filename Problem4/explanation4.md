Function "find_in_group" searches the tree of groups and users recursively. Returns True if user is in group, if not, calls itself
with every sub group. Because "users" and "groups" of Group object are sets, using "in" operator has only O(1)
complexity. However, because in this algorithm groups are visited one by one, the overall complexity depends on the
total number of groups in the tree, which is O(n).