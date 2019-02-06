
# 1. two sum

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mapping = dict()
        for i in range(len(nums)):
            x = nums[i]
            if target-x in mapping:
                return [mapping[target-x], i]
            mapping[x]=i
        return False

# Another solution for 1. two sum
class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        index1, index2, total = 0, len(num)-1, 0
        sortedNum = sorted(enumerate(num), key=lambda x:x[1])
        while index1 != index2:
            total = sortedNum[index1][1] + sortedNum[index2][1]
            if total == target:
                if sortedNum[index1][0] > sortedNum[index2][0] :
                    return (sortedNum[index2][0]+1, sortedNum[index1][0]+1)
                else:
                    return (sortedNum[index1][0]+1, sortedNum[index2][0]+1)
            elif total > target:
                index2 -= 1
            else:
                index1 += 1
        return (-1, -1)