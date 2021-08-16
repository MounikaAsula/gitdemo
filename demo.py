class caluculator:
    num= 250
    def __init__(self,c,d):
        self.c = c
        self.d = d

        print("succesufuly initiated the constructor")
    def getData(self,a,b):
        self.a = a
        self.b = b
        return self.a + self.b

        print("iam one of the method")
    def summation(self):

        return self.c+self.d


obj = caluculator(2,2)
obj.getData(5,6)

print(obj.summation())
print(obj.num)

print(obj.getData(5,6))