class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(f"${len(s)}${s}")
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        j = 1
        count = ""
        while j<len(s):
            sub = ""
            while s[j] != "$":
                count += s[j]
                j += 1
            j += 1
            intcount = int(count)
            while intcount:
                sub += s[j]
                j += 1
                intcount -= 1
            res.append(sub)
            count = ""
            j+=1
        return res
