from math import floor
from chap2.linked_list import LinkedList


def list_sum(a: LinkedList, b: LinkedList, sum: LinkedList):
    m = a.head
    n = b.head
    carry = 0

    while m is not None or n is not None:
        if m is not None:
            valA = m.value
            m = m.next
        else:
            valA = 0
        if n is not None:
            valB = n.value
            n = n.next
        else:
            valB = 0
        sum.add((valA + valB + carry) % 10)
        carry = floor((valA + valB) / 10)


def main():
    MAX_VALUE = 9
    MIN_VALUE = 0
    NUM_NODES = 4

    llA = LinkedList.generate(NUM_NODES, MIN_VALUE, MAX_VALUE)
    llB = LinkedList.generate(NUM_NODES, MIN_VALUE, MAX_VALUE)
    llSum = LinkedList()
    print("list1: ", llA)
    print("list1: ", llB)
    list_sum(llA, llB, llSum)
    print("sum list: ", llSum)


if __name__ == "__main__":
    main()
