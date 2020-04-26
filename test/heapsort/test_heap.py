import unittest

from src.heapsort.heap import Heap


class TestHeap(unittest.TestCase):
    def setUp(self):
        self.listing = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
        self.heap = Heap(self.listing)

    def test_build_max_heap(self):
        # fixture
        listing_fixture = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]

        # invocation
        heap = Heap(listing_fixture)

        # assertion
        self.assertEqual(
            heap.A,
            [16, 14, 10, 8, 7, 9, 3, 2, 4, 1],
        )

    def test_max_heapify(self):
        # fixture
        listing_fixture = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
        heap = Heap(listing_fixture)

        # invocation
        heap.max_heapify(2)

        # assertion
        self.assertEqual(heap.A, self.listing)



