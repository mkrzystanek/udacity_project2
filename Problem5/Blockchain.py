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
        hash_str = self.data.encode('utf-8')
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

    def add(self, value):
        if self.head is None:
            self.head = Block(get_timestamp(), value, 0)
            self.tail = self.head
        else:
            new_block = Block(get_timestamp(), value, self.tail.get_hash())
            self.tail.next = new_block
            self.tail = new_block

    def print_chain(self):
        current = self.head
        while current:
            print(current)
            current = current.next


chain = BlockChain()
chain.add("cat")
chain.add("dog")
chain.add("giraffe")
chain.add("pangolin")
chain.print_chain()

block = chain.head
previous_hash = 0
while block:
    assert block.previous_hash == previous_hash
    previous_hash = block.hash
    block = block.next
