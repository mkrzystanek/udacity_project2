import operator


class Node:
    def __init__(self, char = None, freq = None):
        self.character = char
        self.frequency = freq
        self.left = None
        self.right = None

    def has_left(self):
        return self.left is not None

    def has_right(self):
        return self.right is not None

    def __repr__(self):
        values = self.character, self.frequency
        return str(values)

    def __str__(self):
        return "[{}, {}]".format(self.character, self.frequency)


class Tree:
    def __init__(self, root):
        self.root = root

    def print_tree(self):
        self._print_tree(self.root)

    def _print_tree(self, node):
        if node:
            print()
            print(node)
            print("left:")
            print(node.left)
            print("right:")
            print(node.right)
            self._print_tree(node.left)
            self._print_tree(node.right)

def huffman_encoding(data):
    """
    1. Determine a frequency of each letter in given string
    2. Create a list with nodes that hold letter and its frequency
    3. As long length of list is > 1 merge nodes:
        1. Find two nodes that have the lowest frequency
        2. Create new root node
        3. Root node will store sum of two nodes frequencies and no letter
        4. Two nodes will become root node left and right children
    4. Determine binary codes for leaf nodes:
        1. Need to traverse the tree in pre-order fashion
        2. If on the way to reaching leaf algorithm passes left node, 0 is appended to code
        3. If on a way to reaching leaf algorithim passes right node, 1 is appended to code
    :param data:
    :return: code, huffman tree
    """
    # 1. Determine a frequency of each letter in given string
    frequencies = get_frequency_list(data)

    # 2. Create a list with nodes that hold letter and its frequency
    nodes_list = convert_to_nodes_list(frequencies)

    # 3. As long length of list is > 1 merge nodes:
    #         1. Find two nodes that have the lowest frequency
    #         2. Create new root node
    #         3. Root node will store sum of two nodes frequencies and no letter
    #         4. Two nodes will become root node left and right children
    huffman_tree = Tree(merge_nodes(nodes_list))


def calculate_binary_codes(tree):
    root = tree.root
    codes = traverse(root, [], [])
    return codes


def traverse(node, path, codes):
    print()
    print(node)
    if node.has_left():
        print("left")
        print(node.left)
        path.append("0")
        traverse(node.left, path, codes)
    if node.has_right():
        print("right")
        print(node.right)
        path.append("1")
        traverse(node.right, path, codes)
    if not node.has_left() and not node.has_right():
        print("no leafs")
        codes.append(list(path))
    return codes


def merge_nodes(nodes_list):
    if len(nodes_list) == 1:
        return nodes_list[0]
    new_node = Node()
    new_node.left = nodes_list[0]
    new_node.right = nodes_list[1]
    new_node.frequency = new_node.right.frequency + new_node.left.frequency
    new_list = nodes_list[2:]

    index = 0
    for element in new_list:
        if new_node.frequency <= element.frequency:
            break
        index += 1

    new_list.insert(index, new_node)
    return merge_nodes(new_list)


def convert_to_nodes_list(letter_frequencies):
    nodes_list = []
    for element in letter_frequencies:
        nodes_list.append(Node(element[0], element[1]))
    return nodes_list


def get_frequency_list(string):
    chars_set = set([char for char in string])
    frequencies = set()
    for char in chars_set:
        count = 0
        for letter in string:
            if char == letter:
                count += 1
        frequencies.add((char, count))
    frequencies = list(frequencies)
    frequencies.sort(key=operator.itemgetter(1, 0))
    return frequencies


def huffman_decoding(data,tree):
    """
    Each code is a path to get character of string. 0 means get left child, 1 means get right child. Characters are
    only stored in tree leafs.
    :param data: codes to find letters of the string
    :param tree:
    :return: decodes string
    """
    pass


if __name__ == "__main__":

    # get_frequency_list tests

    input = "alabama"
    output = get_frequency_list(input)
    # print(output)
    assert output == [('b', 1), ('l', 1), ('m', 1), ('a', 4)]

    # merge nodes tests

    test_frequencies = convert_to_nodes_list(output)
    merged_tree = merge_nodes(test_frequencies)
    tree1 = Tree(merged_tree)
    # tree1.print_tree()

    # test_string = "entire galaxy"
    # merged_tree2 = merge_nodes(convert_to_nodes_list(get_frequency_list(test_string)))
    # Tree(merged_tree2).print_tree()

    # get binary codes tests

    code = calculate_binary_codes(tree1)
    print(code)

    # codes = {}
    #
    # a_great_sentence = "The bird is the word"
    #
    # print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # print ("The content of the data is: {}\n".format(a_great_sentence))
    #
    # encoded_data, tree = huffman_encoding(a_great_sentence)
    #
    # print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # print ("The content of the encoded data is: {}\n".format(encoded_data))
    #
    # decoded_data = huffman_decoding(encoded_data, tree)
    #
    # print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # print ("The content of the encoded data is: {}\n".format(decoded_data))