class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(f"{len(s)}${s}")
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        print(s)
        res = []
        i,j = 0,0
        while j<len(s):
            while s[j] != "$":
                j+=1
            count = int(s[i:j])
            word = s[j+1: j+1+count]
            res.append(word)
            i = j+1+count
            j = i
        return res

