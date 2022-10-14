
class Node:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:

    def __init__(self, head=None):
        self.head = head
        self.tail = self.__tail(head)

    def insert(self, node):
        # TODO
        pass

    def add(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node

    def remove(self, index=None, value=None):
        # TODO
        pass

    def __tail(self, head):
        if head is None:
            return None

        while head:
            tail = head
            head = head.next
        
        return tail

    def __len__(self):
        if self.head is None:
            return 0

        node = self.head
        count = 0
        while node:
            count += 1
            node = node.next
        return count

    def __str__(self):
        string = "[ "
        node = self.head
        while node:
            string += f"{node.val} "
            node = node.next
        return string + "]"

if __name__ == "__main__":
    head = Node(5)
    llist = LinkedList()
    llist.add(Node(25))
    print(llist)