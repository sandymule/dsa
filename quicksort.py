# Expected: O(n log n); Worst Case: O(n^2)
# Can be done inplace

import unittest

def QuickSort(A):
    n = len(A)

    if n <= 1:
        return A

    # Paritioning Element Position
    current_position = 0

    for i in range(1, n):
        if A[i] <= A[0]:
            current_position += 1
            temp = A[i]
            A[i] = A[current_position]
            A[current_position] = temp

    temp = A[0]
    A[0] = A[current_position]
    A[current_position] = temp

    L = QuickSort(A[:current_position])
    R = QuickSort(A[current_position + 1:])

    A = L + [A[current_position]] + R

    return A

class TestQuickSort(unittest.TestCase):
    data = [([1, 3, 4, 5, 2], [1, 2, 3, 4, 5]),
            ([1], [1]),
            ([3, 9, 1, 2], [1, 2, 3, 9])]

    def test_quick_sort(self):
        for unsorted, sorted in self.data:
            self.assertEqual(QuickSort(unsorted), sorted)

if __name__ == "__main__":
    unittest.main()
