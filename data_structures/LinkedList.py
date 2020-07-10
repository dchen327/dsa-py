"""
Implementation of Singly Linked List.

Slightly modified version of this:
https://realpython.com/linked-lists-python/#how-to-create-a-linked-list
"""


class ListNode:
    def __init__(self, val=None, next_node=None):
        self.val = val
        self.next_node = next_node

    def __repr__(self):
        return self

    def __str__(self):
        return str(self.val)


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
        nodes.append('None')
        return '->'.join(map(str, nodes))

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next_node

    def __getitem__(self, key):
        for i, node in enumerate(self):
            if i == key:
                return node
        raise Exception('Key out of range')

    def __setitem__(self, key, value):
        for i, node in enumerate(self):
            if i == key:
                node.val = value
                return
        raise Exception('Key out of range')

    def add_first(self, node):
        node.next_node = self.head
        self.head = node

    def add_last(self, node):
        if not self.head:
            self.head = node
            return
        
        for curr_node in self:
            pass
        curr_node.next_node = node

    def add_before(self, target_node_val, new_node):
        if not self.head:
            raise Exception('List is empty')

        prev_node = self.head
        for node in self:
            if node.val == target_node_val:
                prev_node.next_node = new_node
                new_node.next_node = node
                return
            prev_node = node
    
        raise Exception(f'Node with val {target_node_val} not found')

    def add_after(self, target_node_val, new_node):
        if not self.head:
            raise Exception('List is empty')

        if self.head.val == target_node_val:
            return self.add_first(new_node)

        for node in self:
            if node.val == target_node_val:
                new_node.next_node = node.next_node
                node.next_node = new_node
                return

        raise Exception(f'Node with val {target_node_val} not found')

    def remove_node(self, target_node_val):
        if not self.head:
            raise Exception('List is empty')

        if self.head.val == target_node_val:
            self.head = self.head.next
            return

        prev_node = self.head
        for node in self:
            if node.val == target_node_val:
                prev_node.next_node = node.next_node
                return
            prev_node = node


if __name__ == '__main__':
    llist = LinkedList([1, 2, 3])
    llist.add_first(ListNode('hi'))
    llist.add_last(ListNode(5.5))
    print(llist)  # hi->1->2->3->5.5->None
    llist.add_after(1, ListNode('after 1'))
    llist.add_before(5.5, ListNode('before 5.5'))
    print(llist)  # hi->1->after 1->2->3->5.5->None
    llist.remove_node(3)
    llist[0] = 'hello'
    print(llist[2])  # after 1
    print(llist)  # hello->1->after 1->2->before 5.5->5.5->None
