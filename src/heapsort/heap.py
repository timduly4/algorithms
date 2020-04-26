from typing import List


class Heap:
    def __init__(self, listing: List[int]):
        self.A = listing
        self.length = len(listing)
        self.heap_size = len(listing)
        self._build_max_heap()

    def __getitem__(self, i: int) -> int:
        return self.A[i-1]

    def __setitem__(self, i: int, value: int) -> None:
        self.A[i-1] = value

    @staticmethod
    def parent(i: int) -> int:
        return i // 2

    @staticmethod
    def left(i: int) -> int:
        return 2*i

    @staticmethod
    def right(i: int) -> int:
        return 2*i + 1

    def _build_max_heap(self) -> None:
        self.heap_size = self.length
        for i in range(self.length // 2, 0, -1):
            self.max_heapify(i)

    def max_heapify(self, i: int) -> None:
        left = Heap.left(i)
        right = Heap.right(i)

        if left <= self.heap_size and self[left] > self[i]:
            largest = left
        else:
            largest = i
        if right <= self.heap_size and self[right] > self[largest]:
            largest = right

        if largest != i:
            self[i], self[largest] = self[largest], self[i]
            self.max_heapify(largest)

    def sort(self) -> None:
        for i in range(self.length, 1, -1):
            self[1], self[i] = self[i], self[1]
            self.heap_size -= 1
            self.max_heapify(1)

