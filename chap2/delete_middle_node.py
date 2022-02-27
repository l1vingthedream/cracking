from chap2.linked_list import LinkedList, Node


def remove_node(n: Node):
    n.value = n.next.value
    n.next = n.next.next


# assume idx starts at 1
def get_node(ll: LinkedList, k: int):
    n = ll.head
    i = 1
    while i < k:
        if n is not None:
            n = n.next
        i += 1
    return n


def main():
    NODE_GIVEN = 5
    NUM_NODES = 11
    MIN_VALUE = 0
    MAX_VALUE = 9
    ll = LinkedList.generate(NUM_NODES, MIN_VALUE, MAX_VALUE)
    print("before: ", ll)

    n = get_node(ll, NODE_GIVEN)
    print(n)
    remove_node(n)
    print("after: ", ll)


if __name__ == "__main__":
    main()
