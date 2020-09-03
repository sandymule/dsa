# O(n^2)
import unittest

def InsertionSort(A):
    for i in range(len(A)):
        curr_val = A[i]
        j = i - 1
        while j >= 0 and curr_val < A[j]:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = curr_val
    return A

class TestInsertionSort(unittest.TestCase):
    data = [([1,3,4,5,2], [1,2,3,4,5]),
            ([1], [1]),
            ([3,9,1,2], [1,2,3,9])]

    def test_insertion_sort(self):
        for unsorted, sorted in self.data:
            self.assertEqual(InsertionSort(unsorted), sorted)

if __name__ == "__main__":
    unittest.main()

