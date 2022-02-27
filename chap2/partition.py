from chap2.linked_list import LinkedList


def partition(ll: LinkedList, p: int):
    l2 = LinkedList()
    n = ll.head

    while n.next is not None:
        if n.next.value > p:
            l2.add(n.next.value)
            n.next = n.next.next
        else:
            n = n.next

    if ll.head.value > p:
        ll.add(ll.head.value)
        n = n.next
        n.next = l2.head
        ll.head = ll.head.next
    else:
        n.next = l2.head


def main():
    MAX_VALUE = 10
    MIN_VALUE = 0
    NUM_NODES = 12
    PARTITION = 6

    ll = LinkedList.generate(NUM_NODES, MIN_VALUE, MAX_VALUE)
    print("before: ", ll)
    print("partitioning at: ", PARTITION)
    partition(ll, PARTITION)
    print("after", ll)


if __name__ == "__main__":
    main()
