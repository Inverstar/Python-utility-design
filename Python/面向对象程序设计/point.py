class point:
    def __init__(self,x,y=0) -> None:
        self.x,self.y = x,y
    def __eq__(self, other: object) -> bool:
        return self.x==other.x and self.y==other.y
    def __lt__(self, other: object) -> bool:
        if self.x == other.x:
            return self.y<other.y
        else:
            return self.x<other.x
    def __str__(self) -> str:
        return ("(%d,%d)"%(self.x,self.y))

a, b = point(1,2), point(1,2)
print(a==b)
print(a!=b)
print(a>point(0,1))
print(a>point(1,3))
print(str(a))
