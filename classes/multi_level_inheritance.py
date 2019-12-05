class Animal:

    def eat(self):
        print("eat")


class Bird(Animal):

    def fly(self):
        print("fly")

# But chickens can't fly inheritance abuse
# limit to 1 to 2 levels


class Chicken(Bird):
    pass
