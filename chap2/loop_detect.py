from chap2.linked_list import LinkedList


def find_loop(ll: LinkedList):
    addrSet = []
    m = ll.head

    while m is not None:
        if id(m) in addrSet:
            print("loop detected at: ", m.value, " address: ", hex(id(m)))
            return
        addrSet.append(id(m))
        m = m.next
    print("no intersection found")


def main():
    MAX_VALUE = 9
    MIN_VALUE = 0
    NUM_NODES = 9
    LOOP_AT = 4

    ll = LinkedList.generate(NUM_NODES, MIN_VALUE, MAX_VALUE)
    print("list before loop: ", ll)

    print("=== creating loop at node #: ", LOOP_AT, "===")
    n = ll.head
    i = LOOP_AT
    while i < LOOP_AT:
        n = n.next
        i += 1
    n.next = ll.head

    find_loop(ll)


if __name__ == "__main__":
    main()
