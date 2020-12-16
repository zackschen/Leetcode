class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dict = {}
        reversDict = {}
        chars = s.split()
        if len(chars) != len(pattern):
            return False
        for i in range(len(chars)):
            char = pattern[i]
            phase = chars[i]
            if char in dict.keys():
                if not (dict[char] == phase):
                    return False
            elif chars[i] in reversDict.keys():
                if not (reversDict[phase] == char):
                    return False
            else:
                dict[char] = phase
                reversDict[phase] = char
        return True

print(Solution().wordPattern("abcd","dog dog dog dog"))