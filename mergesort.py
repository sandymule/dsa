# O(n log n)
import unittest

def MergeSort(A):
    n = len(A)
    if n <= 1:
        return A
    L = MergeSort(A[:n//2])
    R = MergeSort(A[n//2:])
    return Merge(L, R)

# helper function for merging two sorted subarrays
def Merge(L, R):
    merged_array = []
    i = 0
    j = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            merged_array.append(L[i])
            i += 1
        else:
            merged_array.append(R[j])
            j += 1

    if i < len(L):
        merged_array.extend(L[i:])
    if j < len(R):
        merged_array.extend(R[j:])

    return merged_array

class TestMergeSort(unittest.TestCase):
    data = [([1,3,4,5,2], [1,2,3,4,5]),
            ([1], [1]),
            ([3,9,1,2], [1,2,3,9])]

    def test_merge_sort(self):
        for unsorted, sorted in self.data:
            self.assertEqual(MergeSort(unsorted), sorted)

if __name__ == "__main__":
    unittest.main()
