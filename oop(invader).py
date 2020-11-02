#game Invader, follow the instructions
class County(object):
    total = 0

    def Status():
        print("Total value of counties: ", County.total)
    def __init__(self, name, terr, development = 0, resources = 5):
        print("You have settled a new county!")
        self.__name = name
        self.__terr = terr
        self.development= development
        self.resources = resources
        County.total += 1

    def __pass_time(self):
        self.development += 1
        self.resources -= 1
        if self.resources < 0:
            self.resources = 0

    @property
    def live(self):
        livek = self.development + self.resources
        if livek < 7:
            m = "good for living"
        elif 7 <= livek <= 13:
            m = "urbanized for living"
        elif 13 <= livek <= 16:
            m = "not favorable for living"
        else:
            m = "natural disaster zone"
        return m
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, new_name):
        if new_name=="":
            print("Name of County can not be empty string!")
        else:
            self.__name=new_name
            print("Name has changed! Now you first county is", self.__name)

    def __str__(self):
        rep = "County: "
        rep += "name - " + self.name + "\n"
        return rep


    def exclaim(self):
        print("\nThis is", self.name, "and it's", self.live, "now.\n")
        print("This is the territory of ", self.__terr, "\n")

    def city_extension(self, city = 3):
        print("New block has been built in", self.name)
        self.resources -= city
        self.development += city
        if self.resources < 0:
            self.resources = 0
        self.__pass_time()
    def mining(self, mine=2):
        print("The new mine has been opened!")
        self.resources += mine
        self.development -= mine
        if self.development < 0:
            self.development = 0
        self.__pass_time()

    def __private_method(self):
        print("You want another territory?")
        guess=input()
        if guess=="No":
            print("You have settled a community! But you can play only with three colonies!")
            input("\n\nPress the enter key to exit.")

        else:
            print("Please enter another county and country names: ")


    def public_method(self):
        print("You are",self.__terr,"citizen")
        self.__private_method()

# main
print("Please enter county and country names: ")
county1 = County(name = input(), terr = input())
county1.exclaim()
print("Now you have",County.total,"County","\n")
print(county1.name)
County.Status()
county1.public_method()

county2 = County(name = input(), terr = input())
county2.public_method()

county3 = County(name = input(), terr = input())
county1.exclaim()
county2.exclaim()
county3.exclaim()
print("Now you have",County.total,"Counties","\n")


print("You have settled a community:")
print(county3)

print("Exclaim the name of new county:")
print(county3.name)

County.Status()

print("The name of first country:")
print(county1._County__terr)#it is not good idea
print("The name of second country:")
print(county2._County__terr)#it is not good idea
print("The name of third country:")
print(county3._County__terr)#it is not good idea

print("Change the first county name? Yes?")
guess=input()
if guess=="Yes":
    print("\nAttempting to change my county's name to ...")
    county1.name = input()
else:
    print("Good luck with your colonies then!")
print("You have settled a community:")
print(county1)
print(county2)
print(county3)

choice = None
while choice != "0":
    print \
        ("""
        Invader

        0 - Quit
        1 - Information about your territory
        2 - Build a new city/block
        3 - Extract for some natural resources
        """)

    choice = input("Choice: ")
    print()

    # exit
    if choice == "0":
        print("Good-bye.")

    # Info
    elif choice == "1":
        county1.exclaim()
        county2.exclaim()
        county3.exclaim()
    # building
    elif choice == "2":
        guess=input("Choose county name:")
        if guess==county1.name:
            county1.city_extension()
        elif guess==county2.name:
            county2.city_extension()
        elif guess==county3.name:
            county3.city_extension()
    # mining
    elif choice == "3":
        guess = input("Choose county for mining name:")
        if guess==county1.name:
            county1.mining()
        elif guess==county2.name:
            county2.mining()
        elif guess==county3.name:
            county3.mining()

input("\n\nPress the enter key to exit.")
