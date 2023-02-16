class Emobilisstudent:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def hello_me(self):
        print(f"My name is {self.name} and im {self.age} years old")
class magari:
    def __init__(self,name, cost, year):
        self.name=name
        self.cost=cost
        self.year=year
    def magari(self):
        print(f"i love {self.name} and it is {self.cost} it was manufactured in {self.year}")
class darasa:
        def __init__(self, name, head):
            self.name=name
            self.head=head
        def darasa(self):
            print(f"Our class is called {self.name} and it is headed by {self.head}")
class shule:
    def __init__(self,name,year):
        self.name=name
        self.year=year
    def shule(self):
        print(f"I am a student in {self.name} i was there {self.year}")
class classmates:
    def __init__(hey,name,age):
        hey.name=name
        hey.age=age
    def classmates(hey):
        print(f"one of my classmates is called {hey.name} he is {hey.age} years old")
class walimu:
    def __init__(boby,name,relationship):
        boby.name=name
        boby.relationship=relationship
    def walimu(boby):
        print(f"My highschool tr was called {boby.name} He was {boby.relationship}")
#creating an object
myobj=Emobilisstudent("Sylvia",19)

myobj.hello_me()
obj=magari("jeep",2000000,1897)

obj.magari()

objs=darasa("safari lab","Eric")
objs.darasa()

myobjs=shule("Ngaru girls",2020)
myobjs.shule
slys=classmates("Solomon",19)
slys.classmates()
myobj=walimu("Benah","the best tr there could be")
myobj.walimu()