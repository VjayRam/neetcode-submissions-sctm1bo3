class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = "".join(char.lower() for char in s if char.isalnum())

        left, right = 0, len(clean_str) - 1

        while left < right:
            if clean_str[left] != clean_str[right]:
                return False
            left += 1
            right -= 1
        
        return True
        