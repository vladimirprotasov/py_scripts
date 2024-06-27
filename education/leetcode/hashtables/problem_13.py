class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        previous_char = None
        total = 0

        for char in s:
            if char in roman_map:
                num = roman_map[char]
                total += num

                if previous_char == "I" and (char == "V" or char == "X"):
                    total -= 2
                if previous_char == "X" and (char == "L" or char == "C"):
                    total -= 20
                if previous_char == "C" and (char == "D" or char == "M"):
                    total -= 200

                previous_char = char
            else:
                return 0
        return total


if __name__ == "__main__":
    data = "MCMXCIV"

    x = Solution().romanToInt(data)
    print(x)