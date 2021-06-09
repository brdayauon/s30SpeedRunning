#!/bin/python

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


# Complete the addOne function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def addOne(A):
    def reverse(head):
        if not head:
            return head
        prev = None
        curr = temp = head
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev
    
    #reverse linked list.. then add 1
    A = reverse(A)
    A2 = SinglyLinkedListNode(1)
    dummy = SinglyLinkedListNode(0)
    x = y = 0
    carry = 0
    curr = dummy
    while A or A2:
        if A:
            x = A.data
        else:
            x = 0
        if A2:
            y = A2.data
        else:
            y = 0
        
        total = x + y + carry
        carry = total // 10
        curr.next = SinglyLinkedListNode(total % 10)
        curr = curr.next 
        if A:
            A = A.next
        if A2:
            A2 = A2.next 
    if carry > 0:
        curr.next = SinglyLinkedListNode(1)
    return reverse(dummy.next)
if __name__ == '__main__':