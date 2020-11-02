class County(object):
    total = 0

    def Status():
        print("Total value of counties: ", County.total)
    def __init__(self, name, terr):
        print("You have settled a new county!")
        self.name = name
        self.__terr = terr
        County.total += 1
    def __str__(self):
        rep = "County: "
        rep += "name - " + self.name + "\n"
        return rep

    def exclaim(self):
        print("\nThis is", self.name)
        print("This is the territory of ", self.__terr, "\n")

    def __private_method(self):
        print("You want another territory?")

    def public_method(self):
        print("You are",self.__terr,"citizen")
        self.__private_method()

# main
print("Please enter county and country names: ")
county1 = County(name = input(), terr = input())
county1.exclaim()
print("Now you have",County.total,"County","\n")
County.Status()
county1.public_method()
print("Please enter second county and country names: ")
county2 = County(name = input(), terr = input())

county2.exclaim()
print("Now you have",County.total,"Counties","\n")


print("You have settled a community:")
print(county2)

print("Exclaim the name of county:")
print(county2.name)

County.Status()

print("The name of first country:")
print(county1._County__terr)#it is not good idea
print("The name of second country:")
print(county2._County__terr)#it is not good idea
input("\n\nPress the enter key to exit.")
