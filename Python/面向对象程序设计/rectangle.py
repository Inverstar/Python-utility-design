class rectangle:
    def __init__(self,w,h):
        self.w, self.h = w, h
    def area(self):
        return self.w * self.h
    def perimeter(self):
        return 2 * (self.h+self.w)
def main():
    w, h = map(int,input().split())
    rect = rectangle(w,h)
    print(rect.area(),rect.perimeter())
    rect.w, rect.h = 10, 20
    print(rect.area(),rect.perimeter())
    rect2 = rectangle(2,3)
    print(rect2.area(),rect2.perimeter())
main()
