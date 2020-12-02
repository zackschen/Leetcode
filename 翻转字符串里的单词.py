class Solution:
    def reverseWords(self, s: str) -> str:
        phrases = s.split()
        if len(phrases) == 0 : return ''
        s = phrases[-1]
        for i in reversed(range(0,len(phrases)-1)):
            s = s + ' ' + phrases[i]
        return s

print(Solution().reverseWords("a good   example"))