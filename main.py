cheerios = 10

class Ayu():
    def __init__(self):
        self.age = 10
        self.hair_color = "Brown"
        self.last_name = "Zukimiya"

    def reverse_tanjoubi(self):
        self.age -= 1
        print("Happy Birthday! You are " + str(self.age) + " years old!")


ayu = Ayu()

while ayu.age > 0:
    ayu.reverse_tanjoubi()
