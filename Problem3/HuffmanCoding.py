import operator
import sys
from HuffmanTree import Tree
from HuffmanTree import Node


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


class HuffmanCoding:
    def huffman_encoding(self, data):
        # 1. Determine a frequency of each letter in given string
        frequencies = get_frequency_list(data)

        # 2. Create a list with nodes that hold letter and its frequency
        nodes_list = convert_to_nodes_list(frequencies)

        # 3. As long length of list is > 1 merge nodes:
        #         1. Find two nodes that have the lowest frequency
        #         2. Create new root node
        #         3. Root node will store sum of two nodes frequencies and no letter
        #         4. Two nodes will become root node left and right children
        huffman_tree = Tree(self.merge_nodes(nodes_list))

        # 4. Determine binary codes for leaf nodes:
        #         1. Need to traverse the tree in pre-order fashion
        #         2. If on the way to reaching leaf algorithm passes left node, 0 is appended to code
        #         3. If on a way to reaching leaf algorithm passes right node, 1 is appended to code
        binary_codes = self.calculate_binary_codes(huffman_tree)
        encoded_string = ""
        for c in data:
            encoded_string = encoded_string + binary_codes[c]
        return encoded_string, huffman_tree

    def calculate_binary_codes(self, tree):
        return self.get_codes(tree.root, "", {})

    def get_codes(self, node, path, codes):
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

    def huffman_decoding(self, data, tree):
        """
        Each code is a path to get character of string. 0 means get left child, 1 means get right child. Characters are
        only stored in tree leafs.
        :param data: codes to find letters of the string
        :param tree:
        :return: decodes string
        """
        answer = []
        while len(data) != 0:
            data, answer = self.get_string(data, tree.root, answer)

        decoded_string = ""
        for c in answer:
            decoded_string = decoded_string + c

        return decoded_string

    def get_string(self, data, node, answer):
        if not node.has_right() and not node.has_left():
            answer.append(node.character)
            return data, answer
        else:
            if data[0] == "0" and node.has_left():
                return self.get_string(data[1:], node.left, answer)
            if data[0] == "1" and node.has_right():
                return self.get_string(data[1:], node.right, answer)


if __name__ == "__main__":

    # get_frequency_list tests

    input = "alabama"
    output = get_frequency_list(input)
    # print(output)
    assert output == [('b', 1), ('l', 1), ('m', 1), ('a', 4)]

    # merge nodes tests

    test_frequencies = convert_to_nodes_list(output)
    huffman_coding = HuffmanCoding()
    merged_tree = huffman_coding.merge_nodes(test_frequencies)
    tree1 = Tree(merged_tree)
    # tree1.print_tree()

    # test_string = "entire galaxy"
    # merged_tree2 = merge_nodes(convert_to_nodes_list(get_frequency_list(test_string)))
    # Tree(merged_tree2).print_tree()

    # get binary codes tests

    code = huffman_coding.calculate_binary_codes(tree1)
    # print(code)
    # assert code == ['00', '010', '011', '1']

    # encoding test
    encoded, tree2 = huffman_coding.huffman_encoding(input)
    # print(encoded)

    # decoding test
    decoded_string = huffman_coding.huffman_decoding(encoded, tree2)
    # print(decoded_string)

    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_coding.huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_coding.huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
