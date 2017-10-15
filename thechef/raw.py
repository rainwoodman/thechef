from .base import Element
from .formfactors import Wholesome
# uncooked
class Raw(Element):
    def __init__(self, recipe, amount, formfactor=Wholesome):
        super(Raw, self).__init__(recipe)
        self.amount = amount
        self.formfactor = formfactor

class Oil(Raw): pass
class Salt(Raw): pass
class SeaSalt(Raw): pass

class PepperCorn(Raw): pass
class BlackPepper(PepperCorn): pass

class Ginger(Raw): pass
class Sesame(Raw): pass
class Carrot(Raw): pass
class Califlower(Raw): pass

class Salmon(Raw): pass
class ChickenStock(Raw): pass


