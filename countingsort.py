# O(n) Assume we know the values in advance
from collections import OrderedDict
import unittest

def CountingSort(A):
    A_keys = sorted(list(set(A)))
    A_buckets = OrderedDict()
    for i in A_keys:
        A_buckets[i] = []
    for i in A:
        temp_list = A_buckets[i]
        temp_list.append(i)
        A_buckets[i] = temp_list

    ret_list = []
    for keys, items in A_buckets.items():
        ret_list.extend(items)

    return ret_list

class TestCountingSort(unittest.TestCase):
    data = [([10, 40, 20, 30, 40], [10, 20, 30, 40, 40]),
            ([1, 2], [1, 2])]

    def test_counting_sort(self):
        for unsorted, sorted in self.data:
            self.assertEqual(CountingSort(unsorted), sorted)

if __name__ == "__main__":
    unittest.main()
