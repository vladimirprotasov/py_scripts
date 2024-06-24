class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        index = 1
        counter = 1
        for _ in range(1, len(nums)):
            if nums[index] != nums[index - 1]:
                counter = 1
                index += 1
                continue
            if nums[index] == nums[index - 1]:
                if counter < 2:
                    counter += 1
                    index += 1
                    continue
                if counter == 2:
                    nums.remove(nums[index])
        return len(nums)


if __name__ == "__main__":
    data = [0,0,1,1,1,1,2,3,3]

    Solution().removeDuplicates(nums=data)