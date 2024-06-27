class Solution:
    def isPalindrome(self, x: int) -> bool:
        code = str(x)
        return True if code[::-1] == code else False


if __name__ == "__main__":
    data = 121

    x = Solution().isPalindrome(data)
    print(x)
