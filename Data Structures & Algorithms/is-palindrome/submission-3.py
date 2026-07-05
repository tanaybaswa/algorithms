class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while left < right:
            # Move left pointer forward if it's not alphanumeric
            if not s[left].isalnum():
                left += 1
            # Move right pointer backward if it's not alphanumeric
            elif not s[right].isalnum():
                right -= 1
            # Both are alphanumeric; compare them case-insensitively
            else:
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1
                
        return True