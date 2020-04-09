import operator
import sys
from HuffmanTree import Tree
from HuffmanTree import Node


class HuffmanCoding:
    def encode(self, data):
        """ Taking all steps of the method int account, the time complexity is O(n^2)"""

        # 1. Determine a frequency of each letter in given string: O(n^2)
        frequencies = get_frequency_list(data)

        # 2. Create a list with nodes that hold letter and its frequency: O(n)
        nodes_list = convert_to_nodes_list(frequencies)

        # 3. Build Huffman tree from the list of Nodes: O(n^2)
        huffman_tree = Tree(self.merge_nodes(nodes_list))

        # 4. Determine binary codes for leaf nodes: O(n)
        binary_codes = self.calculate_binary_codes(huffman_tree)

        # 5. Replace character in string with its code. Because iteration over string is needed, time complexity is O(n)
        if len(binary_codes) < 2:
            return "-1", huffman_tree
        encoded_string = ""
        for c in data:
            encoded_string = encoded_string + binary_codes[c]
        return encoded_string, huffman_tree

    def calculate_binary_codes(self, tree):
        return self.get_codes(tree.root, "", {})

    def get_codes(self, node, path, codes):
        """
        If node has left or right node, it adds respective character ("0" for right anf "1" for left) to the path and
        calls itself on the child node. If node does not have any children it means it reached a leaf, and tha path is
        complete. Path is added to the "codes" list. When method reaches the root node again it returns the "codes" list,
        which contain a path to every leaf in the given tree. Because it is needed to visit every node in the tree,
        the time complexity of "get_codes" is directly dependent on number of nodes, so time complexity is O(n).
        Space complexity is O(m), where m is the height of the tree, as the method is recursive and each step to reach
        next child is one cell on call stack. Because in the worst case scenario, in case of the unbalanced tree,
        the height is the same as number of elements, we can say that the space complexity is O(n).
        :param node: node to check
        :param path: the path to current node from root, expressed in string of "1" and "0", which mean "go to left node"
        and "go to right node" respectively
        :param codes: the list of paths to every tree leaf calculated so far.
        :return: the list of paths to every tree leaf calculated so far including the path to current node
        """
        if node is None:
            return ""
        if node.has_left():
            left_path = path + "0"
            self.get_codes(node.left, left_path, codes)
        if node.has_right():
            right_path = path + "1"
            self.get_codes(node.right, right_path, codes)
        if not node.has_left() and not node.has_right():
            codes.update({node.character: path})
        return codes

    def merge_nodes(self, nodes_list):
        """
        Method takes the two first elements of the list (which are of the lowest frequency, because list is sorted)
        and attaches them to a new node, that holds its frequencies sum. The two nodes become new node left and right
        nodes. The original list is then modified by removing merged two elements and replacing them with new node. New
        node is attached to list at the right position, depending on its frequency. Method then calls itself on the
        modified list. When list has only one element, it means we got a tree root.
        Steps of the method include iterating over the nodes list, which means one method call is O(n) in the worst
        case. The number of recursive calls is also dependent on the length of the input list. This means the complexity
        of "merge_nodes" method is O(n^2).
        One call of merge_nodes() has space complexity of O(n-2), because it involves iterating over the input array,
        decreased by two elements. However, this is a recursive method. The maximum cells on call stack it can take is
        directly dependent on the length of input list. Therefore, the overall method space complexity is O(n^2).
        :param nodes_list: sorted list of Nodes holding letters and its frequencies
        :return: root of the Huffman Tree
        """
        if len(nodes_list) == 0:
            return None
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
        return self.merge_nodes(new_list)

    def decode(self, data, tree):
        """
        Each code is a path to get character of string. 0 means get left child, 1 means get right child. Characters are
        only stored in tree leafs.
        The most complex step of the method is of O(n log n) time complexity, so it is the same for all "decode" method.
        :param data: codes to find letters of the string
        :param tree:
        :return: decodes string
        """
        decoded_string = ""
        if data == "-1":
            if tree.root is None:
                return ""
            for n in range(tree.root.frequency):
                decoded_string += tree.root.character
            return decoded_string

        # 1. Get a list of decoded characters. The "while" loop takes as many iterations as there is encoded characters.
        # The method call inside the loop has O(log n) complexity. This step overall complexity is O(n log n)
        answer = []
        while len(data) != 0:
            data, answer = self.get_string(data, tree.root, answer)

        # 2. Convert list to decoded string, O(n)
        for c in answer:
            decoded_string = decoded_string + c

        return decoded_string

    def get_string(self, data, node, answer):
        """
        Method moves across the tree by checking the first character of the encoded data string, moving to the
        respective child node, and calling itself for the next characters of the data. When it reaches the leaf node,
        the character value of leaf is appended to the "answer" list. The time complexity of reaching one of the leaves
        is O(log n). Space complexity is O(n) as the call stack size is dependent on the tree height, and it is the same
        as number of nodes in the worst case scenario.
        :param data: encoded string
        :param node: node to check
        :param answer: list of decoded characters so far
        :return: tuple of data for current node and answer list
        """
        if not node.has_right() and not node.has_left():
            answer.append(node.character)
            return data, answer
        else:
            if data[0] == "0" and node.has_left():
                return self.get_string(data[1:], node.left, answer)
            if data[0] == "1" and node.has_right():
                return self.get_string(data[1:], node.right, answer)


def convert_to_nodes_list(letter_frequencies):
    """
    A function to convert the tuples of letters and their frequencies to list of Nodes, that will be used to build
    Huffman Tree. Time complexity is O(n). Spsce complexity in O(n).
    :param letter_frequencies: set of tuples of letter and its frequency
    :return: list of Nodes containing letter and its frequency
    """
    nodes_list = []
    for element in letter_frequencies:
        nodes_list.append(Node(element[0], element[1]))
    return nodes_list


def get_frequency_list(string):
    """
    The frequency of each letter it the given string is determined. Because it involves iterating over the string
    inside for loop of elements of string characters set, the worst case time complexity is O(n^2). The space complexity
    is O(n), because the space taken by "frequencies" list is dependent on the length of input string in linear way.
    :param string: Any string
    :return: sorted list of tuples of letter and its frequency
    """
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


if __name__ == "__main__":

    # get_frequency_list tests

    input = "alabama"
    output = get_frequency_list(input)
    # print(output)
    # assert output == [4, 1, 1, 1]

    # merge nodes tests

    test_frequencies = convert_to_nodes_list(output)
    huffman_coding = HuffmanCoding()
    merged_tree = huffman_coding.merge_nodes(test_frequencies)
    tree1 = Tree(merged_tree)
    # tree1.print_tree()

    # get binary codes tests

    code = huffman_coding.calculate_binary_codes(tree1)
    # print(code)
    assert code == {'m': '00', 'b': '010', 'l': '011', 'a': '1'}

    # encoding test
    encoded, tree2 = huffman_coding.encode(input)
    # print(encoded)
    assert encoded == "101110101001"

    # decoding test
    decoded_string = huffman_coding.decode(encoded, tree2)
    # print(decoded_string)
    assert decoded_string == "alabama"


    def test(string):
        huffman_coding = HuffmanCoding()
        print ("The size of the data is: {}\n".format(sys.getsizeof(string)))
        print ("The content of the data is: {}\n".format(string))

        encoded_data, tree = huffman_coding.encode(string)

        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print ("The content of the encoded data is: {}\n".format(encoded_data))

        decoded_data = huffman_coding.decode(encoded_data, tree)

        print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print ("The content of the encoded data is: {}\n".format(decoded_data))
        assert decoded_data == string


    a_great_sentence = "The bird is the word"
    duplicates = "aaaaa"
    empty = ""
    long_sentence = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    test(a_great_sentence)
    test(empty)
    test(long_sentence)
    test(duplicates)


