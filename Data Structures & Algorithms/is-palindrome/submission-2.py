class Solution:
    def isPalindrome(self, s: str) -> bool:

        if not s:
            return True

        def is_alpha(c):
            return c.isalnum()

        def case_insensitive(c):
            return c.lower()

        n = len(s)

        left = 0
        right = n - 1

        while left < n and not is_alpha(s[left]):
            left += 1

        while right >= 0 and not is_alpha(s[right]):
            right -= 1
        
        while left < right:

            if case_insensitive(s[left]) != case_insensitive(s[right]):
                return False

            left += 1
            right -= 1
            
            while left < n and not is_alpha(s[left]):
                left += 1

            while right >= 0 and not is_alpha(s[right]):
                right -= 1

        return True
        