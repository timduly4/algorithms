import unittest

from src.heapsort.priority_queue import PriorityQueue


class TestPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.listing = [14, 10, 8, 7, 16, 9, 3, 2, 4, 1]
        self.priority_queue = PriorityQueue(self.listing)

    def test_maximum(self):
        # invocation
        max_value = self.priority_queue.maximum

        # assertion
        self.assertEqual(max_value, 16)

    def test_extract_max(self):
        # invocation
        max_value = self.priority_queue.extract_max()

        # assertion
        self.assertEqual(max_value, 16)
        self.assertEqual(
            self.priority_queue.heap_size,
            len(self.listing) - 1,
        )

    def test_increase_key(self):
        # fixture
        i_fixture = 5
        key_fixture = self.priority_queue[i_fixture] + 1

        # invocation
        self.priority_queue.increase_key(i_fixture, key_fixture)

        # assertion
        self.assertEqual(
            self.priority_queue[i_fixture],
            key_fixture,
        )

    def test_insert(self):
        # fixture
        key_fixture = max(self.listing) + 100

        # invocation
        self.priority_queue.insert(key_fixture)

        # assertion
        self.assertEqual(
            self.priority_queue.maximum,
            key_fixture,
        )
