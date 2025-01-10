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
            while self.head.next:
                self.head = self.head.next
            self.head.next = Node(data)

    def insert(self, n0, P):
        n1 = n0.next
        P.next = n1
        n0.next = P

    def remove(self, n0):
        if not n0.next:
            return
        P = n0.next
        n1 = P.next
        n0.next = n1

    def access(self, head, index):
        for _ in range(index):
            if not head:
                return None
            head = head.next
        return head

    def find(self, head, target):
        index = 0
        while head:
            if head.val == target:
                return index
            head = head.next
            index += 1
        return None
