class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst = s.split(" ")
        word = "".join(lst)
        print(word)
        i=0
        final=''
        for a in word:
            if 'a'<=a<='z' or 'A'<=a<='Z' or '0'<=a<='9':
                final+=a
        final=final.lower()
        if final==final[::-1]:
            return True
        return False