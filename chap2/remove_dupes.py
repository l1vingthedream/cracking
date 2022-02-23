from chap2.linked_list import LinkedList


def remove_dupes(ll: LinkedList):
    knownValues = []
    if ll.head is None:
        return

    n = ll.head
    knownValues.append(n.value)

    while n.next is not None:
        if n.next.value in knownValues:
            n.next = n.next.next
        else:
            knownValues.append(n.next.value)
            n = n.next


def main():
    NUM_NODES = 11
    MIN_VALUE = 0
    MAX_VALUE = 9
    ll = LinkedList.generate(NUM_NODES, MIN_VALUE, MAX_VALUE)
    print("before de-dup: ", ll)

    remove_dupes(ll)
    print("after de-dup: ", ll)


if __name__ == "__main__":
    main()
