###### Time complexity:

**find_files() function:**

Calling this function involves calling "check_files()" recursive function, which visits every subdirectory of root
directory tree. Time complexity is O(depth x avg. number of directory in each level).

###### Space complexity:

**find_files() function:**

This function space complexity is O(m), where m is the height of directories tree. It calls recursive "check_files()" function, which
is called for every subdirectory in the root directory. At the worst case the call stack is filled with as many cells as
there is steps to reach the deepest subdirectory, that is, the total number of nodes. Therefore the worst case scenario
space complexity is O(n).


