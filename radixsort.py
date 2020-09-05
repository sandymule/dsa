# O(n + r) Assume we are sorting integers
from collections import OrderedDict
from collections import deque
import unittest

def RadixSort(A):
    A_buckets = OrderedDict()
    for i in range(10):
        A_buckets[i] = deque([])

    num_iters = len(str(max(A)))
    A_list = A

    for iter in range(num_iters):
        for item in A_list:
            if iter < len(str(item)):
                mod_val = str(item % 10 ** (iter + 1))
                digit = int(mod_val[0])
            else:
                digit = 0

            temp_deque = A_buckets[digit]
            temp_deque.append(item)
            # A_buckets[digit] = temp_deque

        A_list = []
        for queue in A_buckets.values():
            while True:
                try:
                    item = queue.popleft()
                    A_list.append(item)
                except:
                    break

    return A_list




class TestRadixSort(unittest.TestCase):
    data = [([10, 234, 168, 90, 0], [0, 10, 90, 168, 234]),
            ([2, 2, 1], [1, 2, 2])]

    def test_radix_sort(self):
        for unsorted, sorted in self.data:
            self.assertEqual(RadixSort(unsorted), sorted)

if __name__ == "__main__":
    unittest.main()



