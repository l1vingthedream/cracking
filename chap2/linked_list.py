class Node:
    def __init__(self, value, next_node=None) -> None:
        self.value = value
        self.next = next_node

    def __str__(self) -> str:
        return str(self.value)


class LinkedList:
    def __init__(self, values=None) -> None:
        self.head = None
        if values is not None:
            self.add_many(values)

    def __iter__(self):
        n = self.head
        while n is not None:
            yield n
            n = n.next

    def __len__(self) -> int:
        n = self.head
        result = 0
        while n is not None:
            result += 1
            n = n.next
        return result

    def __str__(self) -> str:
        values = [str(x) for x in self]
        return " -> ".join(values)

    def add(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = Node(value)
        return self.head

    def add_many(self, values):
        for v in values:
            self.add(v)

    def delete_value(self, value):
        if self.head.value == value:
            self.head = self.head.next

        n = self.head
        while n.next is not None:
            if n.next.value == value:
                n.next = n.next.next
            n = n.next
