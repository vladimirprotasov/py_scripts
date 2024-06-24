from statistics import median


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        return median(sorted(nums1 + nums2))


if __name__ == "__main__":
    data_1 = [1,3]
    data_2 = [2]

    Solution().findMedianSortedArrays(data_1, data_2)