# Name : Muhammad Hassan Rasheed
# RollNo : EB20102079
# II SEMESTER BSCS SECTION A EVENING
import math
# #                                                  LL
# class Node:
#     def __init__(self, data=None,next=None):
#         self.data = data
#         self.next = next
# class LinkedList:
#     def __init__(self):
#         self.head = None
#     def insertAtBegining(self, data):
#         node = Node(data, self.head)
#         self.head = node
#     def insertAtEnd(self, data):
#         if self.head is None:
#             self.head = Node(data, None)
#             return
#
#         itr = self.head
#         while itr.next:
#             itr = itr.next
#         itr.next = Node(data, None)
#
#     def getLength(self):
#         count = 1
#
#         itr = self.head
#         while itr:
#             count += 1
#             itr = itr.next
#         return count
#     def insertAt(self, data, index):
#         if index<0 or index > self.getLength() - 1:
#             raise Exception('Invalid Index')
#         if index==0:
#             self.insertAtBegining(data)
#             return
#         count = 0
#         itr = self.head
#         while itr:
#             if count == index - 1:
#                 itr.next = Node(data, itr.next)
#                 return
#             count += 1
#             itr = itr.next
#     def removeFirst(self):
#         self.head = self.head.next
#     def removeEnd(self):
#         itr = self.head
#         while itr.next.next:
#             itr = itr.next
#         itr.next = None
#     def removeAt(self,index):
#         if index < 0 or index > self.getLength() - 1:
#             raise Exception('Invalid Index')
#         if index==0:
#             self.removeFirst()
#             return
#
#         count = 0
#         itr = self.head
#         while itr:
#             if count == index - 1:
#                 itr.next = itr.next.next
#                 return
#             count += 1
#             itr = itr.next
#     def find(self, data):
#         count = 0
#         itr = self.head
#         while itr:
#             if data == itr.data:
#                 print(count)
#                 return
#             count += 1
#             itr = itr.next
#     def print(self):
#         if self.head is None:
#             print('LL is Empty')
#             return
#
#         itr = self.head
#         strL = ''
#         while itr:
#             strL += str(itr.data) + '==>'
#             if itr.next:
#                 pass
#             else:
#                 str(itr.data)
#             itr = itr.next
#         print(strL)
#
# LL = LinkedList()
# LL.insertAtBegining(1)
# LL.insertAtBegining(2)
# LL.print()
# LL.insertAtEnd(3)
# LL.insertAtEnd(4)
# LL.print()
# LL.find(3)
# LL.removeEnd()
# LL.removeEnd()
# LL.print()
# LL.insertAt(0, 0)
# LL.insertAt(1, 1)
# LL.print()


# #                                               STACK
# class stack:
#     def __init__(self):
#         self.items = []
#     def isEmpty(self):
#         return self.items == []
#     def isFull(self):
#         return len(self.items) == 3
#     def push(self, val):
#         if not self.isFull():
#             self.items.append(val)
#         else:
#             print('Stack OverFlow')
#     def pop(self):
#         if not self.isEmpty():
#             print(self.items.pop())
#         else:
#             print('Stack UnderFlow')
#     def peek(self):
#         return self.items[-1]
# s = stack()
# print(s.isEmpty())
# s.push(1)
# s.push(2)
# s.push(3)
# print(s.isFull())
# s.push(1)
# print(s.peek())
# s.pop()
# s.pop()
# s.pop()
# s.pop()

# #                                        QUEUE
# class queue:
#     def __init__(self):
#         self.items = []
#     def isEmpty(self):
#         return self.items == []
#     def queueSize(self):
#         return len(self.items)
#     def peekFront(self):
#         return self.items[0]
#     def rear(self):
#         return self.items[-1]
#     def enqueue(self, val):
#         self.items.append(val)
#     def dequeue(self):
#         print(self.items.pop(0))
# q = queue()
# q.enqueue(1)
# q.enqueue(12)
# q.enqueue(13)
# print(q.isEmpty())
# print(q.queueSize())
# print(q.peekFront())
# print(q.rear())

# #                                       SEARCHING AND SORTING ALGOS
# array = [23, 8, 1, 223, 4, 2.45, 9]
#
# sarray = [1,2,3,4,5,6,7,8,9]
#
# def linearSearch(array, vts):
#     for i in range(0, len(array)):
#         if array[i] == vts:
#             print(i)
#
# linearSearch(sarray, 8)
#
# def binarySearch(array, vts):
#     first = 0
#     last = len(array) - 1
#     while True:
#         mid = (first + last) // 2
#         mid = math.floor(mid)
#         if vts == array[mid]:
#             print(mid)
#             break
#         else:
#             if vts > array[mid]:
#                 first = mid + 1
#             else:
#                 last = mid - 1
# binarySearch(sarray, 8)
#
# def bubbleSort(array):
#     for i in range(0, len(array)):
#         for j in range(0, len(array) - 1 -i):
#             if array[j] > array[j + 1]:
#                 array[j], array[j + 1] = array[j + 1], array[j]
#     print(array)
#
# bubbleSort(array)
#
# def selectionSort(array):
#     for i in range(0, len(array)):
#         minVal = array[i]
#         for j in range(i, len(array)):
#             if minVal > array[j]:
#                 minVal = array[j]
#         minVal, array[i] = array[i], minVal
#     print(array)
# selectionSort(array)
#
# def insertionSort(array):
#     for i in range(1, len(array)):
#         pointer = array[i]
#         j = i - 1
#         while j >= 0:
#             if pointer < array[j]:
#                 temp = array[j]
#                 array[j] = array[i]
#                 array[i] = temp
#                 j-=1
#             else:
#                 break
#     print(array)
# insertionSort(array)



#                                                   PRACTISE

array = [85,2,8,6,7,4,15,14,177,63,5]

sarray = [1,2,3,4,5,6,7,8]

def linearSearch(array, vts):
    for i in range(0, len(array)):
        if vts == array[i]:
            print('Index ==> ',i)

linearSearch(sarray,8)

def binarySearch(array, vts):
    first = 0
    last = len(array) -1

    while True:
        mid = (first + last) // 2
        mid = math.floor(mid)

        if vts == array[mid]:
            print('Index ==>',mid)
            return
        else:
            if vts < array[mid]:
                last = mid - 1
            else:
                first = mid + 1

binarySearch(sarray, 8)

def bubbleSort(array):
    for i in range(0, len(array)):
        for j in range(0, len(array) - i -1):
            if array[j] > array[j + 1]:
                temp = array[j + 1]
                array[j + 1] = array[j]
                array[j] = temp
    print(array)
bubbleSort(array)

def selectionSort(array):
    for i in range(0, len(array)):
        minVal = array[i]
        for j in range(i, len(array)):
            if minVal > array[j]:
                minVal = array[j]
        array[i], minVal = minVal, array[i]
    print(array)
selectionSort(array)

def insertionSort(array):
    for i in range(1, len(array)):
        pointer = array[i]
        j = i - 1
        while j >= 0:
            if pointer < array[j]:
                array[j], array[i] = array[i], array[j]
            j -= 1
    print(array)
insertionSort(array)


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        if self.head is None:
            return True
    def insertFirst(self, data):
        node = Node(data, self.head)
        self.head = node
    def insertLast(self, data):
        if self.head is None:
            self.insertFirst(data)
            return
        itr = self.head
        while itr:
            if itr.next is None:
                itr.next = Node(data, None)
                return
            itr = itr.next
    def removeFirst(self):
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next
    def removeLast(self):
        if self.head.next is None:
            self.head = None
            return
        itr = self.head
        while itr.next.next:
            itr =itr.next
        itr.next = None

    def removeLastStack(self):
        if self.head.next is None:
            lastVal = self.head.data
            self.head = None
            return lastVal
        itr = self.head
        while itr.next.next:
            itr = itr.next
        lastVal = itr.next.data
        itr.next = None
        return lastVal
    def getLength(self):
        count = 1
        itr = self.head
        while itr.next:
            count +=1
            itr = itr.next
        return count
    def insertAt(self, data, index):
        if index < 0 or index > self.getLength() - 1:
          raise Exception('Invalid Index')
        if index ==0:
            self.insertFirst(data)

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = Node(data, itr.next)
                return
            count += 1
            itr = itr.next
    def removeAt(self, index):
        if index < 0 or index > self.getLength() - 1:
          raise Exception('Invalid Index')
        if index ==0:
            self.removeFirst()
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                return
            count += 1
            itr = itr.next
    def find(self, data):
        count = 0
        itr = self.head
        while itr:
            if data == itr.data:
                print(count)
                return
            count += 1
            itr = itr.next
    def peek(self):
        itr = self.head
        while itr:
            if itr.next is None:
                return itr.data
            itr = itr.next
    def print(self):
        if self.head is None:
            print('LL is Empty')
            return

        itr = self.head
        lStr = ''
        while itr:
            lStr += str(itr.data) + '==>'
            if itr.next:
                pass
            else:
                print(lStr)
                return
            itr = itr.next

# LL = LinkedList()
# LL.insertFirst(1)
# LL.insertFirst(2)
# LL.print()
# LL.insertLast(3)
# LL.insertLast(4)
# LL.print()
# LL.find(3)
# LL.removeLast()
# LL.removeLast()
# LL.print()
# LL.insertAt(0, 0)
# LL.insertAt(1, 1)
# LL.print()

class Stack:
    def __init__(self):
        LL = LinkedList()
        self.items = LL
    def push(self, data):
        self.items.insertLast(data)
    def pop(self):
        if self.items.isEmpty():
            print('Stack Underflow')
            return
        print(self.items.removeLastStack())
    def peek(self):
        print(self.items.peek())

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.peek()
stack.pop()
stack.pop()
stack.pop()