class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CicruleSingeLinkedList:

    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def __len__(self):
        """
        func to get CSLL length
        :return:
        """
        return self.length

    def __str__(self):
        """
        fun to return str representation of CSLL
        :return:
        """

        if self.length == 0:
            return ""
        else:
            node = self.head
            result = ""
            while node:
                result += str(node.data)
                node = node.next
                if node is self.head:
                    break
                result += " --> "
            return result

    def treaves(self):
        """
        traves through node in CSLL
        :return:
        """
        if self.head is None:
            return
        node = self.head
        while node:
            print(node.data)
            if node.next is self.head:
                break
            node = node.next

    def append(self, data):
        """
        insert node to end of CSLL
        :param data:
        :return:
        """
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
            self.tail.next = node
        else:
            self.tail.next = node
            self.tail = node
            self.tail.next = self.head
        self.length += 1

    def pre_append(self, data):
        """
        insert node at the begging of CSLL
        :param data:
        :return:
        """
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
            self.tail.next = node
        else:
            node.next = self.head
            self.head = node
            self.tail.next = self.head
        self.length += 1

    def insert(self, index, data):
        """
        insert node into CSLL by index
        :param data:
        :param index:
        :return:
        """
        if index < -1 or index > self.length:
            return
        node = Node(data)
        if self.length == 0:
            self.head = node
            self.tail = node
            self.tail.next = node
        elif index == 0:
            node.next = self.head
            self.head = node
            self.tail.next = node
        elif index == -1:
            self.tail.next = node
            self.tail = node
            self.tail.next = self.head
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            node.next = temp.next
            temp.next = node
        self.length += 1

    def get(self, index):
        """
        get node data from CSLL by index
        :param index:
        :return:
        """
        if self.head is None:
            return None
        if index == 0:
            return self.head.data
        if index == -1:
            return self.tail.data
        if index > self.length or index < -1:
            return None
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            return temp.next.data

    def _get(self, index):
        """
        get node from CSLL by index
        :param index:
        :return:
        """

        if index == -1:
            return self.tail
        if index > self.length or index < -1:
            return None
        node = self.head
        for _ in range(index - 1):
            node = node.next
        return node

    def find(self, data):
        """
        find node index by data
        :param data:
        :return:
        """
        if self.head is None:
            return
        index = 0
        node = self.head
        while self.tail.next == self.head:
            if node.data == data:
                return index
            node = node.next
            index += 1
        return None

    def set(self, index, data):
        if self.head is None:
            return None
        node = self._get(index)
        if node:
            node.data = data
        return node.data

    def pop(self):
        """
        remove last node from CSLL
        :return:
        """
        if self.head is None:
            return None
        node = self.tail
        if self.length == 1:
            self.head = self.tail = None
            return node.data
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            temp.next = self.head
            self.tail = temp
            self.length -= 1
            return node.data

    def pop_first(self):
        """
        remove first node from CSLL
        :return:
        """
        if self.head is None:
            return None
        node = self.head
        if self.length == 1:
            self.head = self.tail = None
            return node.data
        self.head = node.next
        node.next = None
        self.tail.next = self.head
        self.length -= 1
        return node.data

    def remove(self, index):
        """
        remove node from CSLL by index
        :param index:
        :return:
        """
        if self.head is None:
            return None
        if index == 0:
            self.pop_first()
        elif index == -1 or self.length - 1 == index:
            self.pop()
        else:
            prev = self._get(index - 1)
            node = prev.next
            prev.next = node.next
            node.next = None
        self.length -= 1

    def celer(self):
        """
        celer entire CSLL
        :return:
        """
        self.head = self.length
        self.length = 0
