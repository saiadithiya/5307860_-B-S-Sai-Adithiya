def reverse(llist):
    current = llist
    temp = None
    while current:
        temp = current.prev
        current.prev = current.next
        current.next = temp
        current = current.prev
    if temp:
        llist = temp.prev
    return llist

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        llist1 = reverse(llist.head)

        print_doubly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()
