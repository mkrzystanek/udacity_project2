class Group(object):
    def __init__(self, _name):
        self.name = _name
        # changed the initial implementation of list to set, because time complexity of lookup in
        # set is O(1) against O(n) in list. This will help make the search more efficient.
        self.groups = set()
        self.users = set()

    def add_group(self, group):
        self.groups.add(group)

    def add_user(self, user):
        self.users.add(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    already_checked = []
    return find_in_group(user, group, already_checked)


def find_in_group(user, group, checked):
    """
    Function "find_in_group" searches the tree of groups and users recursively. Returns True if user is in group, if
    not, calls itself with every sub group. Using "in" operator has O(n) complexity. Because in this algorithm groups
    are visited one by one, the overall complexity depends on the total number of groups in the tree, and is O(n^2).
    For each function call lists returned by "get_users()" and "get_groups()" are read into memory, so the space
    complexity is O(n). However, function is recursive, and its calls are put on the call stack for all nodes in tree
    (in a worst case scenario). Therefore, the space complexity of "find_in_group()" is O(n^2)
    :param user: user to find
    :param group: group to search
    :param checked: a list of groups that were already checked
    :return: True if user is a part of the group
    """
    if group.get_name() in checked:
        return
    if user in group.get_users():
        return True
    for g in group.get_groups():
        return find_in_group(user, g, checked)


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

assert is_user_in_group(sub_child_user, parent)
assert not is_user_in_group("child", parent)
assert not is_user_in_group("subchild", parent)
assert not is_user_in_group("otheruser", parent)
assert is_user_in_group(sub_child_user, child)
assert is_user_in_group(sub_child_user, sub_child)
