# import credentials
from random import randint
import time



class Ayu:
    def __init__(self):
        self.age = 10
        self.hair_color = "Brown"
        self.name = "Ayu Tskukimia"
        self.height = 5
        self.boobs = "None"


    def tanjoubi(self, number_of_years):
        self.age -= number_of_years
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
how_old_responses = ["how old are you", "how old are you?" "ikutsu",
    "Nansai desu ka"]
decrease = ("decrease age")

Greeting = ["How are you", "You're Late!"]
#attempting to add line break after each ayu response
response = input(Greeting[rand])
if response.lower() in good_responses:
    print("Uguu")
    time.sleep(3)
else:
    print("Uguu")
    time.sleep(3)


response = input("I missed you, please take care of me")
if response.lower() in how_old_responses:
    print(ayu.age + 4)
else:
    if response.lower() in decrease:
        while ayu.age <= 10:
            ayu.tanjoubi(1)
            if ayu.age == 5:
                print("AAAH TOO YOUNG")
                break
    else:
        print("Uguu")







#
#
#
# fuck_the_loli(enjoying_it=False)
# fuck_the_loli("Ayu", True)
#
# fuck_the_loli(name="Kobato", enjoying_it=True)
# fuck_the_loli(name="Kobato", enjoying_it=False)
