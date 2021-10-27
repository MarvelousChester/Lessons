# All notes on code are on Notion 
class Robot():
    # Constructer
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce(self):
        print("My name is " + self.name + " and owned by: ", end="")


r1 = Robot("Tom", "red", 30)
r2 = Robot("Jerry", "blue", 40)


class Person:
    def __init__(self, n, p, i):
        self.name = n
        self.personality = p
        self.is_setting = i

    def introduce(self):
        print(str(self.name,))

    def sit_down(self):
        self.is_setting = True

    def stand_up(self):
        self.is_setting = False


p1 = Person("Alice", "aggressive", False)
p2 = Person("Becky", "talkative", True)

p1.robot_owned = r2
p2.robot_owned = r1

# Shows who owns what bot 
(str(p1.robot_owned.introduce()) + str(p1.introduce()))
