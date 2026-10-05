class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []

        # Encode each string as: length#string
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)

        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []

        # Start of the encoded length
        i = 0 

        while i < len(s):
            
            # Find the delimiter separating length and string
            j = i 
            while s[j] != "#":
                j += 1

            # Parse the string length
            length = int(s[i:j])

            # Move to the start of the actual string
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        
        return res
            
