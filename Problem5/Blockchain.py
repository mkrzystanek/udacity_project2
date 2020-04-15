import hashlib
import datetime


class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = str(self.data).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def get_hash(self):
        return self.hash

    def __repr__(self):
        return "(Data: {}, hash: {}, previous hash: {})".format(self.data, self.hash, self.previous_hash)


def get_timestamp():
    return datetime.datetime.now(datetime.timezone.utc)


class BlockChain:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, value):
        if self.head is None:
            self.head = Block(get_timestamp(), value, 0)
            self.tail = self.head
        else:
            new_block = Block(get_timestamp(), value, self.tail.get_hash())
            self.tail.next = new_block
            self.tail = new_block
        self.size += 1

    def print_chain(self):
        current = self.head
        while current:
            print(current)
            current = current.next

    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return str(result)


chain = BlockChain()
chain.add("cat")
chain.add("dog")
assert chain.head.data == "cat"
assert chain.tail.data == "dog"

chain.add("")
chain.add("aaa")
chain.add(23)
chain.print_chain()
assert str(chain) == "['cat', 'dog', '', 'aaa', 23]"
assert chain.size == 5

chain.add("zebra")
assert str(chain) == "['cat', 'dog', '', 'aaa', 23, 'zebra']"
assert chain.size == 6

chain2 = BlockChain()
chain2.add("pink")
chain2.add("gray")
assert str(chain2) == "['pink', 'gray']"
assert chain2.size == 2

chain3 = BlockChain()
assert str(chain3) == "[]"
assert chain3.size == 0

block = chain.head
previous_hash = 0
while block:
    assert block.previous_hash == previous_hash
    previous_hash = block.hash
    block = block.next


