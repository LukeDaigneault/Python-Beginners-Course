class Flyer:
    def fly(self):
        pass


class Swimmer:
    def swim(self):
        pass

# be careful here order is important keep classes abstract


class FlyingFish(Flyer, Swimmer):
    pass
