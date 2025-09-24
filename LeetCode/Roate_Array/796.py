class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        a=list(s)
        n=len(s)
        while n>0:
            f=a[0]
            del a[0]
            a.append(f)
            if "".join(a)==goal:
                return True
            n-=1
        return False
        