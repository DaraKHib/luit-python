class Robot:
    def __init__(self, name):
        self.name = name
        self.position = [0,0]
        print('My name is', self.name)
    def walk(self, x):
        self.position[0] = self.position[0] + x
        print('New position:', self.position)

class Robot_Dog(Robot):
    def make_noise(self):
        print('Woof Woof!')

# Main program
my_robot_dog = Robot_Dog('Bud')
my_robot_dog.walk(10)
my_robot_dog.make_noise()