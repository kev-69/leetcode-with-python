class Solution:
    def romanToInt(self, s: str) -> int:
        # Corrected the mapping: "X" instead of "x" and "M" should map to 1000
        roman_values = {
            "I": 1,
            "V": 5,
            "X": 10,  # Changed from "x" to "X"
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000  # Corrected value for "M"
        }

        result = 0
        for i in range(len(s)):
            if i + 1 < len(s) and roman_values[s[i]] < roman_values[s[i + 1]]:
                result -= roman_values[s[i]]
            else:
                result += roman_values[s[i]]

        return result

sol = Solution()
print(sol.romanToInt("III"))
print(sol.romanToInt("IV"))
print(sol.romanToInt("IX"))