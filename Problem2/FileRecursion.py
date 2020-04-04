import os

# As the problem title suggests, the easy way to achieve this result is to use a recursive function. The "check_files"
# function checks if given directory is a file, then checks if the file has desired suffix. If directory is not a file,
# it calls itself for every subdirectory. Because this function must be called on every subdirectory of the root
# directory to find all the files with given suffix, the time complexity depends on the total number of subdirectories.
# If the number is n, the overall complexity is O(n).


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    files_with_suffix_paths = []
    check_files(suffix, path, files_with_suffix_paths, "")
    return files_with_suffix_paths


def check_files(suffix, path, result_list, parent_dir):
    full_directory = os.path.join(parent_dir, path)

    if os.path.isfile(full_directory):
        if path.endswith(suffix):
            result_list.append(full_directory)
        else:
            return
    else:
        subdirectories_list = os.listdir(full_directory)
        for dir in subdirectories_list:
            check_files(suffix, dir, result_list, full_directory)


directories = find_files(".c", ".")
print(directories)
assert directories == ['./testdir/subdir3/subsubdir1/b.c', './testdir/t1.c', './testdir/subdir1/a.c', './testdir/subdir5/a.c']
