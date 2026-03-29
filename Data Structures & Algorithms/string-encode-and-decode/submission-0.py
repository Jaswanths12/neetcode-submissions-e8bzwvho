class Solution:
    def encode(self, strs: list[str]) -> str:
        if not strs:
            return ""
        result = []
        for s in strs:
            result.append(f"{len(s)}#{s}")
        return "".join(result)

    def decode(self, s: str) -> list[str]:
        if not s:
            return []
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            word = s[j + 1 : j + 1 + length]
            result.append(word)
            i = j + 1 + length
        return result