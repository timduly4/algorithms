from src.heapsort.heap import Heap


class PriorityQueue(Heap):

    @property
    def maximum(self):
        return self[1]

    def extract_max(self) -> int:
        if self.heap_size < 1:
            raise ValueError('Heap Underflow')
        maximum = self[1]
        self[1] = self[self.heap_size]
        self.heap_size -= 1
        self.max_heapify(1)
        return maximum

    def increase_key(self, i: int, key: int) -> None:
        if key < self[i]:
            raise ValueError('New key is smaller than current key')
        self[i] = key
        while i > 1 and self[self.parent(i)] < self[i]:
            self[i], self[self.parent(i)] = self[self.parent(i)], self[i]
            i = self.parent(i)

    def insert(self, key: int) -> None:
        self.heap_size += 1
        self.append(-float('inf'))
        self.increase_key(self.heap_size, key)
