from random import randint
import time






# collection = ['hey', 5, 'd']
# for x in collection:
#     print(x)

# response3 = input()
# while len(str(response3)) <= 5:
#     print("hello")

# THIS RUNS A FUNCTION WILL

rand = randint(0,2)

response = ["Hello", "Moshi Moshi", "Ohayouuuuuuuuuuuuu"]

class Call_Ayu:
    def __init__(self):
        self.name = "Ayu Tskukimia"
        self.nickname = "Ayu"
        self.response = response[rand]


    def call_her(self, name="Ayu"):
        print("Hey is this " + self.nickname)
        if name == "Ayu":
            print(self.response)
        else:
            print("I'm Not Ayu")
        time.sleep(1)
        # return len(str(self.response))
        if len(str(self.response)) <= 15:
            print("I'm sorry I'm not very talketive today")
        elif len(str(self.response)) >= 16:
            print("...")
        # print(len(str(self.response)))

random = Call_Ayu()

random.call_her(name="Ayu")










# call_her("Bako")
