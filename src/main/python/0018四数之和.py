"""
# 第18题. 四数之和

[力扣题目链接](https://leetcode.cn/problems/4sum/)

题意：给定一个包含n 个整数的数组nums和一个目标值target，判断nums中是否存在四个元素 a，b，c和 d，使得a + b + c + d的值与target相等？找出所有满足条件且不重复的四元组。

**注意：**

答案中不可以包含重复的四元组。

示例：
给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

"""



#思路：指针

from typing import List


class Solution:
    def fourSum(self, nums:List[int], target:int) -> List[int]:
        n = len(nums)
        nums.sort()
        ans = []
        for i in range( n ):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i+1, n):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                left = j + 1
                right = n - 1
                while left < right:
                    curr = nums[i] + nums[j] + nums[left] + nums[right]
                    if curr > target:
                        right -= 1
                    elif curr < target:
                        left += 1
                    else:
                        ans.append( [nums[i], nums[j], nums[left], nums[right] ])
                        # 去重
                        while left < right and nums[left+1] == nums[left]:    left += 1
                        while left < right and nums[right-1] == nums[right]:    right -= 1
                        left += 1
                        right -= 1
        return ans

if __name__ == '__main__':
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    ans = Solution().fourSum( nums, target)
    print('ans: ', ans)


