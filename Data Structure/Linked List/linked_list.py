class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    # Add an item to the head of the linked list
    def add(self, item):
        self.head = Node(item, self.head)

    # Delete the first item of the linked list
    def remove(self):
        if self.is_empty():
            return None
        else:
            item = self.head.item
            self.head = self.head.next
            return item

    # Find and delete an given item
    def delete(self, item):
        if not self.is_empty() and self.head.item == item:
            self.remove()
            return True
        else:
            current = self.head
            prev = None
            while current != None:
                if current.item == item:
                    prev.next = current.next
                    return True
                prev = current
                current = current.next
        return False

    # Check if the linked list is empty
    def is_empty(self):
        return self.head == None

    # Search for an item in the list
    def find(self, item):
        node = self.head
        while node != None:
            if node.item == item:
                return True
            node = node.next

        return False

    # Print all the items in the list
    def show_all_items(self):
        print("Items in the list:")
        node = self.head
        while node != None:
            print(node.item)
            node = node.next
