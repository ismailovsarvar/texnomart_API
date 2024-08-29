# Nodel class yaratamiz
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# LinkedList class yaratamiz
class LinkedList:
    def __init__(self):
        self.head = None

    # LL boshlanishida tugun qo‘shish usuli
    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    # Istalgan indeksga tugun qo‘shish usuli
    # Indekslash 0 dan boshlanadi.
    def insertAtIndex(self, data, index):
        if (index == 0):
            self.insertAtBegin(data)

        position = 0
        current_node = self.head
        while (current_node != None and position + 1 != index):
            position = position + 1
            current_node = current_node.next

        if current_node != None:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print("Index not present")

    # LL oxiriga tugun qo‘shish usuli
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while (current_node.next):
            current_node = current_node.next

        current_node.next = new_node

    # Berilgan joyda ulangan ro‘yxat tugunini yangilash
    def updateNode(self, val, index):
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = val
        else:
            while (current_node != None and position != index):
                position = position + 1
                current_node = current_node.next

            if current_node != None:
                current_node.data = val
            else:
                print("Index not present")

    # Ulangan ro‘yxatning birinchi tugunini olib tashlash usuli
    def remove_first_node(self):
        if (self.head == None):
            return

        self.head = self.head.next

    # Ulangan ro‘yxatning oxirgi tugunini olib tashlash usuli
    def remove_last_node(self):

        if self.head is None:
            return

        current_node = self.head
        while (current_node != None and current_node.next.next != None):
            current_node = current_node.next

        current_node.next = None

    # Ko‘rsatilgan indeksda olib tashlash usuli
    def remove_at_index(self, index):
        if self.head == None:
            return

        current_node = self.head
        position = 0
        if position == index:
            self.remove_first_node()
        else:
            while (current_node != None and position + 1 != index):
                position = position + 1
                current_node = current_node.next

            if current_node != None:
                current_node.next = current_node.next.next
            else:
                print("Index not present")

    # Biriktirilgan ro‘yxatdan tugunni olib tashlash usuli
    def remove_node(self, data):
        current_node = self.head

        if current_node.data == data:
            self.remove_first_node()
            return

        while (current_node != None and current_node.next.data != data):
            current_node = current_node.next

        if current_node == None:
            return
        else:
            current_node.next = current_node.next.next

    # Ulangan ro‘yxat hajmini chop etish
    def sizeOfLL(self):
        size = 0
        if (self.head):
            current_node = self.head
            while (current_node):
                size = size + 1
                current_node = current_node.next
            return size
        else:
            return 0

    # Ulangan ro‘yxatni chop etish usuli.
    def printLL(self):
        current_node = self.head
        while (current_node):
            print(current_node.data)
            current_node = current_node.next


llist = LinkedList()

# ulangan ro‘yxatga tugunlar qo‘shish
llist.insertAtEnd('a')
llist.insertAtEnd('b')
llist.insertAtBegin('c')
llist.insertAtEnd('d')
llist.insertAtIndex('g', 2)

# print the linked list
print("Node Data")
llist.printLL()

print("\nRemove First Node")
llist.remove_first_node()
print("Remove Last Node")
llist.remove_last_node()
print("Remove Node at Index 1")
llist.remove_at_index(1)

print("\nLinked list after removing a node:")
llist.printLL()

print("\nUpdate node Value")
llist.updateNode('z', 0)
llist.printLL()

print("\nSize of linked list :", end=" ")
print(llist.sizeOfLL())
