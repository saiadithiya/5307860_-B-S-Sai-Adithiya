def insertNodeAtPosition(llist, data, position):
    new_node = SinglyLinkedListNode(data)
    if position == 0:
        new_node.next = llist
        return new_node
    current = llist
    for _ in range(position - 1):
        current = current.next
    new_node.next = current.next
    current.next = new_node
    return llist

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    data = int(input())

    position = int(input())

    llist_head = insertNodeAtPosition(llist.head, data, position)

    print_singly_linked_list(llist_head, ' ', fptr)
    fptr.write('\n')

    fptr.close()
