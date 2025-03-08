class employee:
    totalSalay = 0
    def __init__(self,name,income) -> None:
        self.name, self.income = name, income
    def pay(self,salary):
        self.income += salary
        employee.totalSalay += salary
    @staticmethod
    def printTotalSalary():
        print(employee.totalSalay)
e1 = employee("Jack",0)
e2 = employee("Tom",0)
e1.pay(100)
e2.pay(200)
e1.printTotalSalary()
print(employee.totalSalay)