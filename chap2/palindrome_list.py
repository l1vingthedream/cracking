from chap2.linked_list import LinkedList, Node


def helper(n: Node, rev: LinkedList):
    if n.next is None:
        rev.add(n.value)
    else:
        helper(n.next, rev)
        rev.add(n.value)


def is_palindrome(ll: LinkedList) -> bool:
    # reverse the linked list
    rll = LinkedList()
    helper(ll.head, rll)

    # if nodes don't match, not palindrome
    m = ll.head
    n = rll.head
    while m is not None:
        if m.value is not n.value:
            return False
        m = m.next
        n = n.next
    return True


def main():
    WORD = "cabdbac"

    ll = LinkedList()
    for c in WORD:
        ll.add(c)
    print("list: ", ll)
    result = is_palindrome(ll)
    print(str(result))


if __name__ == "__main__":
    main()
