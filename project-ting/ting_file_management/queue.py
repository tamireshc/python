from ting_file_management.abstract_queue import AbstractQueue
from collections import deque


class Queue(AbstractQueue):
    def __init__(self):
        self.queue = deque()

    def __len__(self):
        return len(self.queue)

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if len(self.queue) == 0:
            return None
        return self.queue.popleft()

    def search(self, index):
        if index > len(self.queue) - 1 or index < 0:
            raise IndexError

        return self.queue[index]


# fila = Queue()
# fila.search(0)
# fila.enqueue(1)
# fila.enqueue(2)
# fila.enqueue(3)
# print(len(fila.queue))
# print(fila.dequeue())
# print(fila.search(0))
