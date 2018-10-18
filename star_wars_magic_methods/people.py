class People(object):
    def __init__(self, name, dark_side=False, light_side=True):
        self.name = name
        self.dark_side = dark_side
        self.light_side = light_side
        
        if self.dark_side == True:
            self.light_side = False

    def __str__(self):
        return str(self.name)

    def __call__(self):
        return("Help me {}, you\'re my only hope.".format(self.name))

    def __truediv__(self, other):
        if isinstance(other, People):
            return("{} swings a lightsaber at {}.".format(self, other))
        else:
            raise TypeError()

    def __mul__(self, other):
        if isinstance(other, People):
            return("{} throws a thermal detonator at {}!".format(self, other))
        else:
            raise TypeError()

    def __rshift__(self, other):
        if isinstance(other, People):
            return("{} uses the force to push {} away from them.".format(self, other))
        else:
            raise TypeError()

    def __lshift__(self, other):
        if isinstance(other, People):
            return("{} uses the force to pull {} towards them.".format(self, other))
        else:
            raise TypeError()

    def __neg__(self):
        self.dark_side = True
        self.light_side = False
    
    def __pos__(self):
        if self.dark_side == True:
            self.dark_side = False
            self.light_side = True

    def __invert__(self):
        if self.light_side == True:
            self.light_side = False
        elif self.light_side == False:
            self.light_side = True

        if self.dark_side == True:
            self.dark_side = False
        elif self.dark_side == False:
            self.dark_side = True

    def __xor__(self, other):
        return("{} force chokes {}.".format(self, other))

    def __eq__(self, other):
        if self.name == "Han Solo":
            return("{} shoots {}.".format(self, other))
        else:
            return("Han Solo shoots {}. BECAUSE HAN SHOOTS FIRST.".format(self))






