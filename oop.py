class County(object):
    total=0
    def Status():
        print("Total value of counties: ",County.total)
    def __init__(self, name):
        print("You have settled a new county!")
        self.name=name
        County.total+=1

    def __str__(self):
        rep = "County: "
        rep += "name - " + self.name + "\n"
        return rep

    def exclaim(self):
        print("This is", self.name, "\n")

#main
county1=County("Maine")
county1.exclaim()
print("Now you have",County.total,"County","\n")

County.Status()

county2=County("Devonshire")
county2.exclaim()
print("Now you have",County.total,"Counties","\n")


print("You have settled a community:")
print(county2)

print("Exclaim the name of county:")
print(county2.name)

County.Status()
