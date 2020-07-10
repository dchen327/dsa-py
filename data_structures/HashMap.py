'''
Implementation of HashMap with Singly Linked List to store collisions.

Slightly modified version of this:
https://gist.github.com/pohzipohzi/6ab2e39faf0a887e61a827e3ccaa8b94
'''


class ListNode:
    def __init__(self, key=None, val=None, next_node=None):
        self.key = key
        self.val = val
        self.next_node = next_node

    def __repr__(self):
        return self

    def __str__(self):
        return str(self.key) + ': ' + str(self.val)


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = ListNode(nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next_node = ListNode(elem)
                node = node.next_node

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.val)
            node = node.next_node
        if nodes == []:
            nodes.append(None)
        return '->'.join(map(str, nodes))

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next_node

    def __len__(self):
        return sum(1 for _ in self)

    def get(self, key):
        for node in self:
            if node.key == key:
                return node.val
        raise KeyError(key)

    def put(self, key, val):
        '''
        If key is already in the LinkedList, update val.
        Otherwise, add a new ListNode with key and val.
        Return True if a new node is added, False otherwise.
        '''
        if self.head is None:  # empty linked list
            self.head = ListNode(key, val)
            return True
        for node in self:
            if node.key == key:
                node.val = val
                return False  # no new node
            if node.next_node is None:
                node.next_node = ListNode(key, val) 
                return True  # new node added

    def remove(self, key):
        '''
        Remove element with a given key if it exists, otherwise raise KeyError
        '''
        if not self.head:
            return KeyError(key)

        if self.head.key == key:
            self.head = self.head.next_node
            return

        prev_node = self.head
        for node in self:
            if node.key == key:
                prev_node.next_node = node.next_node
                return
            prev_node = node
        raise KeyError(key)


class HashMap:
    def __init__(self, items=None, size=100):
        self.size = size
        self.arr = [LinkedList() for _ in range(size)]
        self.len = 0
        if items:
            for key, val in items:
                self[key] = val

    def __repr__(self):
        return str(self.__dict__)

    def __str__(self):
        nodes = []
        for llist in self.arr:
            for node in llist:
                if node is not None:
                    nodes.append(node)
        return '{' + ', '.join(map(str, nodes)) + '}'

    def __len__(self):
        return self.len

    def __getitem__(self, key):
        return self.arr[self._hash(key)].get(key)

    def __setitem__(self, key, val):
        node_added = self.arr[self._hash(key)].put(key, val)
        self.len += node_added  # update HashMap length

    def __delitem__(self, key):
        self.arr[self._hash(key)].remove(key)
        self.len -= 1

    def _hash(self, x):
        return hash(x) % self.size


if __name__ == '__main__':
    h = HashMap([('dog', 5), (123, 4.5), ('hello', 'goodbye')], size=5)
    print(h)  # {dog: 5, 123: 4.5, hello: goodbye}
    h[5] = 'hi'
    h[3] = 'hello'
    h[3] = 'bye'
    print(h)  # {dog: 5, 5: hi, 123: 4.5, hello: goodbye, 3: bye}
    h[(1, 2)] = 3
    del h[5]
    print(h)  # {dog: 5, 123: 4.5, hello: goodbye, 3: bye, (1, 2): 3}
    print(h[(1, 2)])  # 3
    print(len(h))  # 5