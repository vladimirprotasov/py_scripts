class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        index_one = 0
        while index_one != len(nums):
            for index_two in range(len(nums)):
                if index_one != index_two:
                    if (nums[index_one] + nums[index_two]) == target:
                        print([index_one, index_two])
                        return [index_one, index_two]
            index_one += 1

    def two_sum_2(self, nums: list[int], target: int):
        pass


if __name__ == "__main__":
    data = [2, 7, 11, 15]
    target_sum = 9

    Solution().two_sum(data, target_sum)