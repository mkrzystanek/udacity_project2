###### Time complexity:

**encode() method**

Taking all steps of the "encode" method into account, the time complexity is O(n^2):

   1. Determine a frequency of each letter in given string: O(n^2)
   2. Create a list with nodes that hold letter and its frequency: O(n)
   3. Build Huffman tree from the list of Nodes: O(n^2)
   4. Determine binary codes for leaf nodes: O(n)
   5. Replace character in string with its code. Because iteration over string is needed, time complexity is O(n)
   
**decode() method**

The most complex step of the "decode" method is of O(n log n) time complexity, so it is the same for whole method:
    
   1. Get a list of decoded characters. The "while" loop takes as many iterations as there is encoded characters. The method call inside the loop has O(log n) complexity. This step overall complexity is O(n log n)
   2. Convert list to decoded string, which is O(n)
   
   
###### Space complexity:

**encode() method**

Taking all steps of the "encode" method into account, the space complexity is O(n^2):

   1. Determine a frequency of each letter in given string: O(n)
   2. Create a list with nodes that hold letter and its frequency: O(n)
   3. Build Huffman tree from the list of Nodes: O(n^2)
   4. Determine binary codes for leaf nodes: O(n).
   5. Replace character in string with its code. Because iteration over string is needed: O(n)

**decode() method**

The most complex step of the "decode" method is of O(n^2) space complexity, so it is the same for whole method:
    
   1. Get a list of decoded characters: O(n^2)
   2. Convert list to decoded string, which is O(n)