class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = numbers
        l = 0
        r = len(nums) - 1

        while l < r:
            currSum = nums[l] + nums[r]

            if currSum < target:
                l += 1
            elif currSum > target:
                r -= 1
            else:
                return [l + 1, r + 1]
            
        return []

                
            
        