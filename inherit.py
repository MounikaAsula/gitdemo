from demo import caluculator


class childImpl(caluculator):
    num2 =400
    def __init__(self):
        caluculator.__init__(self,3,5)
    def getCompleteData(self):

        return self.num2 + self.num + self.summation()+self.getData(8,1)
obj = childImpl()
print(obj.getCompleteData())
