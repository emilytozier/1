class Girl(object):
    def gift(self, tier):
        print("Girl give to animal food")
        tier.joy()
class Animal(object):
    def joy(self):
        print("Thank you, sweet girl! Yammm...")

print("\t\t Животное и девочка\n")
anna=Girl()
kitty=Animal()
anna.gift(kitty)
input("\n\n Нажмите Enter чтобы выйти")