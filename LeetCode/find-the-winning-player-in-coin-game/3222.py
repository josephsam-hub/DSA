class Solution:
    def winningPlayer(self, n: int, y: int) -> str:
        k=0
        while n>0 and y>=4:
            n=n-1
            y=y-4
            k+=1
        if(k%2==1):
            return "Alice"
        else:
            return "Bob"