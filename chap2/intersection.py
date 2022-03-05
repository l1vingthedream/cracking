from chap2.linked_list import LinkedList


def print_intersection(l1: LinkedList, l2: LinkedList):
    addrSet = []
    m = l1.head
    n = l2.head

    while m is not None:
        addrSet.append(id(m))
        m = m.next

    while n is not None:
        if id(n) in addrSet:
            print("intersection found: ", hex(id(n)))
            return
        n = n.next
    print("no intersection found")


def main():
    MAX_VALUE = 9
    MIN_VALUE = 0
    NUM_NODES = 6

    llA = LinkedList.generate(NUM_NODES, MIN_VALUE, MAX_VALUE)
    llB = LinkedList.generate(NUM_NODES, MIN_VALUE, MAX_VALUE)
    print("list1: ", llA)
    print("list2: ", llB)

    print("intersecting node in list1: ", hex(id(llA.head.next)))
    print("intersecting node in list2: ", hex(id(llB.head.next.next)))

    print("=== creating intersection ===")
    llA.head.next = llB.head.next.next
    print("list1: ", llA)
    print("list2: ", llB)

    print("=== intersecting points ===")
    print("intersecting node in list1: ", hex(id(llA.head.next)))
    print("intersecting node in list2: ", hex(id(llB.head.next.next)))

    print_intersection(llA, llB)


if __name__ == "__main__":
    main()
