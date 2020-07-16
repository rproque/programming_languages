#!/usr/local/bin/python3
# MACOSX


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


# Create a linked list of: 6, 3, 4, 2, 1

if __name__ == '__main__':
    a_linkedlist = ListNode()
    a_linkedlist.head = Node(6)
    Head = a_linkedlist.head
    Node3 = Node(3)
    Node4 = Node(4)
    Node2 = Node(2)
    Node1 = Node(1)
    list_of_nodes = [Head, Node3, Node4, Node2, Node1]
#
#         #initialize
#         for node in list_of_nodes:
#             print("Node{} has a value of {} and next of Node{}".format(node.val, node.val, node.next))
#
#         #connect the dots
#         for index in range(0, len(list_of_nodes)):
#             # If last in list, ignore Node.next
#             if index == len(list_of_nodes) - 1:
#                 break
#             else:
#                 list_of_nodes[index].next = list_of_nodes[index + 1]
#             print("Node{} has a value of {} and next of Node{}".format(list_of_nodes[index].val, list_of_nodes[index].val, list_of_nodes[index].next.val))
#
#         print("Number of nodes is {}".format(Head.count_nodes(Head)))