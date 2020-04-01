class Group(object):
    def __init__(self, _name):
        self.name = _name
        # changed the initial implementation on list to set, because time complexity of lookup in
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
