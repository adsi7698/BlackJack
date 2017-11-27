import random
class house():
    def __init__(self):
        self.count = 0

    def draw_card(self,card):
        self.card = card
        self.total = 0
        self.count += 1

    def check(self):
        self.total += self.card

        if self.card == 11:
            print("Ace")
        elif self.card == 10:
            print("Face Card")
        else:
            print("Normal Card")

        print("admin total is " , self.total )
        print()

class player():
    def __init__(self):
        self.count = 0

    def draw_card(self, card):
        self.card = card
        self.total = 0
        self.count += 1

    def check(self):
        self.total += self.card

        if self.card == 11:
            print("Ace")
        elif self.card == 10:
            print("Face Card")
        else:
            print("Normal Card")

        print("player total is " , self.total )
        print()

x = random.randint(2,11)
admin = house()
admin.draw_card(x)
admin.check()

y = random.randint(2,11)
Adi = player()
Adi.draw_card(y)
Adi.check()

if admin.total > Adi.total :
    print("admin wins")
elif admin.total < Adi.total :
    print("Player wins")
else:
    print("Draw")