import credentials
from random import randint


class Ayu:
    def __init__(self):
        self.age = 0
        self.hair_color = "brown"
        self.name = "Ayu Tskukimia"

    def tanjoubi(self, number_of_years):
        self.age += number_of_years
        print("Happy Birthday! You are " + str(self.age) + " years old!")



def fuck_the_loli(name="Ayu", enjoying_it=True):
    print(name + ": ONII CHAN!!!")
    if enjoying_it:
        print("DON'T STOP!")
    else:
        if name == "Kobato":
            print("i hate you")
        else:
            print("YAMETE!!!!")



ayu = Ayu()
rand = randint(0,1)

print("Hi I'm Ayu")

good_responses = ["good", "all right"]

Greeting = ["How are you", "You're Late!"]
response = input(Greeting[rand] + "¥n")
if response.lower() in good_responses:
    print("Uguu")




# while ayu.age >= 0:
#     ayu.tanjoubi(1)
#     if ayu.age == 10:
#         print("AAAH")
#         break

#
#
#
# fuck_the_loli(enjoying_it=False)
# fuck_the_loli("Ayu", True)
#
# fuck_the_loli(name="Kobato", enjoying_it=True)
# fuck_the_loli(name="Kobato", enjoying_it=False)
