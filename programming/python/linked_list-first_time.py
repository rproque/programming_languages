#!/usr/local/bin/python3
# MACOSX

# TODO Need to figure out recursion, not merging then sorting

import random

class Node:
    # Function to initialize the node object
    def __init__(self, v):
        self.val = v  # Assign value
        self.next = None  # Initialize next as null


# Linked List class
class ListNode:
    # Function to initialize the Linked List
    def __init__(self):
        self.head = None

    def get_nodes(self):
        node = self.head
        list_of_nodes = []
        while node.next is not None:
            list_of_nodes.append(node.val)
            node = node.next
        # get last node
        list_of_nodes.append(node.val)
        return list_of_nodes

    def count_nodes(self):
        number_of_nodes = 1  # count head as a node
        node = self.head
        while node.next is not None:
            number_of_nodes += 1
            node = node.next
        return number_of_nodes

    def sort_ll(self):
        current = self.head
        index = current.next
        temp = 0

        while (True):
            if current.val <= index.val:
                pass
            elif current.val > index.val:
                temp = index.val
                index.val = current.val
                current.val = temp

            # Move index one if more data
            if (index.next is not None) and (current.next is not None):
                index = index.next
            # Index and current at the end of the list
            elif (index.next is None) and (current.next.next is None):
                break
            # Index at end of list, but more nodes need to be processed
            elif (index.next is None) and (current.next is not None):
                current = current.next
                index = current.next


if __name__ == '__main__':
    llist1, llist2 = ListNode(), ListNode()
    llist1.head, llist2.head = Node(1000), Node(2000)
    current_node_1, current_node_2 = llist1.head, llist2.head

    for x in range(1, 10):
        y = random.randint(1, 500)
        current_node_1.next = Node(y)
        current_node_1 = current_node_1.next

    for x in range(1, 5):
        y = random.randint(1, 500)
        current_node_2.next = Node(y)
        current_node_2 = current_node_2.next

    #print("*" * 100)
    #nodes_before_sort = llist1.get_nodes()
    #print("llist1 Nodes {}".format(nodes_before_sort))
    # print("llist1 Number of nodes: {}".format(llist1.count_nodes()))
    # llist1.sort_ll()
    # nodes_after_sort = llist1.get_nodes()
    # print("llist1 Done: Nodes {}".format(nodes_after_sort))
    #
    # print("*" * 100)
    #nodes_before_sort = llist2.get_nodes()
    #print("llist2 Nodes {}".format(nodes_before_sort))
    # print("llist2 Number of nodes: {}".format(llist2.count_nodes()))
    # llist2.sort_ll()
    # nodes_after_sort = llist2.get_nodes()
    # print("llist2 Done: Nodes {}".format(nodes_after_sort))

    index = llist1.head
    while True:
        index = index.next
        if index.next == None:
            index.next = llist2.head
            break

    nodes_before_sort = llist1.get_nodes()
    #print("llist1 Nodes {}".format(llist1.get_nodes()))
    llist1.sort_ll()
    nodes_after_sort = llist1.get_nodes()
    print("llist1 Done: Nodes {}".format(nodes_after_sort))