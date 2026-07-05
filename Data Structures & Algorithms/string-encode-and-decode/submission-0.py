class Solution:
    def encode(self, strs: list[str]) -> str:
        # Join lengths, delimiters, and strings together
        res = []
        for s in strs:
            res.append(f"{len(s)}#{s}")
        return "".join(res)

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            # Find the delimiter tracking the end of the length prefix
            while s[j] != '#':
                j += 1
            
            # Extract the length of the upcoming string
            length = int(s[i:j])
            
            # Move our pointer right past the '#' character
            start = j + 1
            end = start + length
            
            # Slice the exact string and append it
            res.append(s[start:end])
            
            # Move the main pointer to the start of the next encoded block
            i = end
            
        return res