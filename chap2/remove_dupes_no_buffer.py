from chap2.linked_list import LinkedList


def remove_dupes(ll: LinkedList):
    if ll.head is None:
        return

    left = ll.head
    # TODO - this has a bug where left.next to NoneType in while cond
    while left.next is not None:
        right = left.next
        preDelete = left
        while right is not None:
            if left.value == right.value:
                if right.next is not None:
                    preDelete.next = right.next
            else:
                preDelete = right
            right = right.next
        left = left.next


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
