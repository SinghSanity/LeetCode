class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: # type: ignore
        lst = []
        for idx, number in enumerate(nums):
            if target - number in nums[idx + 1:]:
                lst.append(idx)
                lst.append(nums.index(target-number, idx + 1))
                break
        return lst
