"""
1.两数之和
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
你可以按任意顺序返回答案。
示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 外层循环遍历每个元素
        for i in range(len(nums)):
            # 内层循环从当前元素的下一个元素开始
            for j in range(i+1, len(nums)):
                # 检查两个元素之和是否等于目标值
                if nums[i] + nums[j] == target:
                    # 找到答案，返回索引
                    return [i, j]


if __name__ == "__main__":
    # 创建Solution实例
    sol = Solution()

    # 测试用例1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = sol.twoSum(nums1, target1)
    print(f"输入: nums = {nums1}, target = {target1}")
    print(f"输出: {result1}")
