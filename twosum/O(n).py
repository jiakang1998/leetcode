class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        n = len(nums)
        for i in range(n):
            diff = target - nums[i]
            if diff in nums:
                index = nums.index(diff)
                if index != i :
                    return (i,index)
                    break
                else:
                    continue
