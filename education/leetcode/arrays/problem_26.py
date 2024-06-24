class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        unique = 1
        index = 1
        for _ in range(1, len(nums)):
            if nums[index] > nums[index - 1]:
                unique += 1
            else:
                nums.remove(nums[index])
                continue
            index += 1

        return unique







if __name__ == "__main__":
    data = [0,1,1,2,3]

    Solution().removeDuplicates(nums=data)