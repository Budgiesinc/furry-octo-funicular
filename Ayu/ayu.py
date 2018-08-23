# import credentials
from random import randint
import time
import numpy



class Ayu:
    def __init__(self):
        self.age = 10
        self.hair_color = "Brown"
        self.name = "Ayu Tskukimia"
        self.nickname = "Ayu"
        self.height = 5
        self.boobs = "None"
        self.favorite_food = "tayaki"
        self.friends = ["Yuuichi", "Nayuki", "Makoto"]
        self.phrase = "Uguu"
        self.letters = ["A", "B", "C", "D"]

    def tanjoubi(self, number_of_years):
        self.age -= number_of_years
        print("Happy Birthday! You are " + str(self.age) + " years old!")
    def love(self):
        self.friends
        print(random(self.friends) + "but ... I wish I could make more")
    def alphabet(self, alphabetical):
        for x in self.letters:
            print(x)
        time.sleep(1)
        print("E")
        time.sleep(1)
        print("F")
        time.sleep(1)
        print("G...")
        print("...Yuuichi?")


ayu = Ayu()
rand = randint(0,3)
rand1 = randint(0,2)



good_responses = ["good", "all right"]
how_old_responses = ["how old are you", "how old are you?" "ikutsu",
    "Nansai desu ka"]
decrease = ["decrease age"]
Greeting = ["How are you", "You're Late!","Where have you been!", "Uguu You're Always Late"]
negative_responses = ["no", "fuck you", "I can't"]
looking_for = ["僕の探し物がある", "I'm missing something", "I lost something", "I'm looking for something"]
first_encounters = ["Have we met before" , "I feel like we used to be friends" , "You look very familiar"]
looking_for_what = ["What are you looking for", "What is it", "what did you lose" "Are you looking for me"]

# list[good_responses, how_old_responses, decrease, Greeting, negative_responses, looking_for, first_encounters, looking_for_what]
#attempting to add line break after each ayu response

print("Hi I'm Ayu")
time.sleep(1.5)
print(ayu.nickname + ": what's your name?")
init_response = input()


response = input(ayu.nickname + ": " + Greeting[rand])
if response.lower() in good_responses:
    print(ayu.nickname + ": I'm Glad")
    time.sleep(1)
else:
    print(ayu.nickname + ": Uguu")
    time.sleep(1)


response1 = input(ayu.nickname + ": " + "I missed you, please take care of me, " + init_response)

# FIX LATER
if response1.lower() in how_old_responses:
    print(ayu.nickname + ":" + str(ayu.age) + str(4))
else:
    if response1.lower() in decrease:
        while ayu.age <= 10:
            ayu.tanjoubi(1)
            if ayu.age == 5:
                print("AAAH TOO YOUNG")
                break
    if response1.lower() in negative_responses:
        print(ayu.nickname + ": You're Mean!")
    else:
        print(ayu.nickname + ": Uguu")
time.sleep(2)
print(ayu.nickname + ": " + first_encounters[rand])
print(ayu.nickname + ": " + looking_for[rand1])



def r2(name="Ayu", response2=True):
    response2 = input()
    if response2.lower() in how_old_responses:
        print(name + ayu.age + 4)
    else:
        if response2.lower() in decrease:
            while ayu.age <= 10:
                ayu.tanjoubi(1)
                if ayu.age == 5:
                    print("GOD: AAAH TOO YOUNG")
                    break
        if response2.lower() in negative_responses:
            print(name + ": You're Mean!")
        if response2.lower() in looking_for_what:
            print(name + ": Something very special to me")
        else:
            print(name + ": Uguu")
    time.sleep(2)
    print(first_encounters[rand])
    return(response2)


# r2 = r2()

r2(name="Ayu", response2=True)
#
#
# # while rt()
# # recursive testing: see testing_ops.py
#
# response3 = input()
# if len(str(r2)) <= 5:
#     return


# r2(response2=True)
# r2(response2=True)
#
# if len(r2) >= 4
#     then n
#     print("I'm sorry I'm not very social today")


# response2 = input()
# r1()





# def fuck_the_loli(name="Ayu", enjoying_it=True):
#     print(name + ": ONII CHAN!!!")
#     if enjoying_it:
#         print("DON'T STOP!")
#     else:
#         if name == "Kobato":
#             print("i hate you")
#         else:
#             print("YAMETE!!!!")
#
# #
# fuck_the_loli(enjoying_it=False)
# fuck_the_loli("Ayu", True)
#
# fuck_the_loli(name="Kobato", enjoying_it=True)
# fuck_the_loli(name="Kobato", enjoying_it=False)
