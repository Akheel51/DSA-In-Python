class SmallestInfiniteSet:

    def __init__(self):
        self.s=set()
        for i in range(1,1001):
            self.s.add(i)
        

    def popSmallest(self) -> int:
        
        return self.s.pop()

    def addBack(self, num: int) -> None:
        self.s.add(num)

        self.s=set(sorted(list(self.s)))
