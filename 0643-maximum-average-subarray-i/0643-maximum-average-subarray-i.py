class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if k > len(nums):
            return 0
        sm = sum(nums[:k])
        maxavg = sm / float(k)
        for i in range(len(nums)-k):
            sm -= nums[i]
            sm +=nums[i+k]
            avg = sm / float(k)
            maxavg = max(maxavg,avg)
        return maxavg
        