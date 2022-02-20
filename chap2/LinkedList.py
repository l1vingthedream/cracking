class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return str(self.data)


class LinkedList:
    def __init__(self, nodes=None) -> None:
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for el in nodes:
                node.next = Node(data=el)
                node = node.next

    def __repr__(self) -> str:
        node = self.head
        result: str

        if node is not None:
            result = str(node.data)
            node = node.next
        while node is not None:
            result = result + " -> " + str(node.data)
            node = node.next
        return result

    def add_value(self, value) -> bool:
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = Node(data=value)

    def delete_value(self, value) -> bool:

        if self.head.data == value:
            self.head = self.head.next

        node = self.head
        while node.next is not None:
            if node.next.data == value:
                node.next = node.next.next
            node = node.next


ll: LinkedList = LinkedList([2, 5, 1, 2, 8, 4, 3, 6, 3, 7])
print(ll)
ll.add_value(33)
print(ll)
ll.delete_value(3)
print(ll)
ll.delete_value(2)
print(ll)
