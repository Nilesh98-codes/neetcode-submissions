class Solution:
    def findMin(self, nums: List[int]) -> int:
        # sorted approach but it doesnt meet the criteria, BS is the way
        nums = sorted(nums)
        return nums[0]
        