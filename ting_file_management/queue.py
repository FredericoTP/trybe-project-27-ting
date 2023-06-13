from ting_file_management.abstract_queue import AbstractQueue


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.previous = None

    def __str__(self):
        return f"Node(value={self.value}, next={self.next})"

    def previous_view(self):
        return f"Node(value={self.value}, previous={self.previous})"

    def reset(self):
        self.next = None
        self.previous = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node("HEAD")
        self.tail = Node("TAIL")
        self.head.next = self.tail
        self.tail.previous = self.head
        self.__length = 0

    def __str__(self):
        return f"DoublyLinkedList(len={self.__length} value={self.head})"

    def __len__(self):
        return self.__length

    def insert_first(self, value):
        node_value = Node(value)
        node_value.next = self.head.next
        node_value.previous = self.head
        node_value.next.previous = node_value
        self.head.next = node_value
        self.__length += 1

    def insert_last(self, value):
        node_value = Node(value)
        node_value.previous = self.tail.previous
        node_value.next = self.tail
        node_value.previous.next = node_value
        self.tail.previous = node_value
        self.__length += 1

    def insert_at(self, value, position):
        if position < 1:
            return self.insert_first(value)
        if position >= len(self):
            return self.insert_last(value)
        new_node = Node(value)
        position_node = self.__get_node_at(position)
        new_node.next = position_node
        new_node.previous = position_node.previous
        new_node.previous.next = new_node
        position_node.previous = new_node
        self.__length += 1

    def remove_first(self):
        value_to_be_removed = None
        if not self.is_empty():
            value_to_be_removed = self.head.next
            element_later_than_removed = value_to_be_removed.next
            self.head.next = element_later_than_removed
            element_later_than_removed.previous = self.head
            value_to_be_removed.reset()
            self.__length -= 1
        return value_to_be_removed.value

    def remove_last(self):
        value_to_be_removed = None
        if not self.is_empty():
            value_to_be_removed = self.tail.previous
            element_later_than_removed = value_to_be_removed.previous
            self.tail.previous = element_later_than_removed
            element_later_than_removed.next = self.tail
            value_to_be_removed.reset()
            self.__length -= 1
        return value_to_be_removed

    def remove_at(self, position):
        if position < 1:
            return self.remove_first()
        if position >= len(self):
            return self.remove_last()
        value_to_be_removed = None
        if not self.is_empty():
            value_to_be_removed = self.__get_node_at(position)

            previous_to_be_removed = value_to_be_removed.previous
            next_to_be_removed = value_to_be_removed.next

            previous_to_be_removed.next = next_to_be_removed
            next_to_be_removed.previous = previous_to_be_removed

            value_to_be_removed.reset()
            self.__length -= 1

        return value_to_be_removed

    def get_element_at(self, position):
        value_returned = None
        value_to_be_returned = self.__get_node_at(position)
        if value_to_be_returned:
            value_returned = Node(value_to_be_returned.value)
        return value_returned

    def __get_node_at(self, position):
        value_to_be_returned = None
        if self.head.next != self.tail:
            value_to_be_returned = self.head.next
            while position > 0:
                value_to_be_returned = value_to_be_returned.next
                position -= 1
        return value_to_be_returned

    def is_empty(self):
        return not self.__length


class Queue(AbstractQueue):
    def __init__(self):
        self.data = DoublyLinkedList()

    def __len__(self):
        return len(self.data)

    def enqueue(self, value):
        self.data.insert_last(value)

    def dequeue(self):
        return self.data.remove_first()

    def search(self, index):
        if index < 0 or index > (self.data.__len__() - 1):
            raise IndexError("Índice Inválido ou Inexistente")

        return self.data.get_element_at(index).value
