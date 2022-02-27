from chap2.linked_list import LinkedList, Node


def helper(n: Node, target):
    if n.next is None:
        return (1, n.value) if target == 0 else (1, None)

    currentNode, value = helper(n.next, target)

    if currentNode == target:
        value = n.value
    return (currentNode+1, value)


def kth(ll: LinkedList, k):
    (idx, result) = helper(ll.head, k)
    if result is None:
        print("exception ocurred")
    else:
        print(result)


def main():
    K = 7
    NUM_NODES = 12
    MIN_VALUE = 0
    MAX_VALUE = 99

    ll = LinkedList.generate(NUM_NODES, MIN_VALUE, MAX_VALUE)
    print("list: ", ll)
    kth(ll, K)


if __name__ == "__main__":
    main()
