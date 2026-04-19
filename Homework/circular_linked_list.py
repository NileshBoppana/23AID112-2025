class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.last = None

    def insert_end(self, data):
        new_node = Node(data)

        if self.last is None:
            self.last = new_node
            new_node.next = new_node
            return

        new_node.next = self.last.next
        self.last.next = new_node
        self.last = new_node

    def delete_node(self, key):
        if self.last is None:
            print("List is empty")
            return

        current = self.last.next
        previous = self.last

        while True:
            if current.data == key:
                if current == self.last and current.next == self.last:
                    self.last = None
                else:
                    previous.next = current.next
                    if current == self.last:
                        self.last = previous
                print(key, "deleted")
                return

            previous = current
            current = current.next

            if current == self.last.next:
                break

        print("Node not found")

    def traverse(self):
        if self.last is None:
            print("List is empty")
            return

        current = self.last.next
        while True:
            print(current.data, end=" ")
            current = current.next
            if current == self.last.next:
                break
        print()


cll = CircularLinkedList()

cll.insert_end(10)
cll.insert_end(20)
cll.insert_end(30)
cll.insert_end(40)

print("Circular Linked List:")
cll.traverse()

cll.delete_node(30)

print("After deletion:")
cll.traverse()
