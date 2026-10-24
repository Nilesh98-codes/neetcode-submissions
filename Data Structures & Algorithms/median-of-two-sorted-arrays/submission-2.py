import statistics

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = nums1 + nums2
        med = statistics.median(res)
        return med