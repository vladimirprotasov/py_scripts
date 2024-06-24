class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        index = 0
        for _ in range(len(nums)):
            if nums[index] == val:
                nums.remove(nums[index])
            else:
                index += 1
        return len(nums)

if __name__ == "__main__":
    data = [0,1,2,2,3,0,4,2]
    value = 2

    Solution().removeElement(nums=data, val=value)