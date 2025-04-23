class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        index = 0
        pl = [i for i in range(1,n+1)]
        while len(pl) > 1:
            index = (index + k - 1) % len(pl)
            pl.pop(index)
        return pl[0]
