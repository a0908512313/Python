class Node():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkList():
    def __init__(self, head=None):
        self.head = head

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            pass
