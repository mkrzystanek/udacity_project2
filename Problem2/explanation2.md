As the problem title suggests, the easy way to achieve this result is to use a recursive function. The "check_files"
function checks if given directory is a file, then checks if the file has desired suffix. If directory is not a file,
it calls itself for every subdirectory. Because this function must be called on every subdirectory of the root
directory to find all the files with given suffix, the time complexity depends on the total number of subdirectories.
If the number is n, the overall complexity is O(n).