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
            for j in range(1,n):
                if nums[j]+nums[i] == target and i!=j:
                    return[i,j]
                    break
                else:
                    continue
                    #print(nums[j]+nums[i])
        #print(i,j)

