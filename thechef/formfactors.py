from .base import FormFactor
from .tools import Tool

class Powder(FormFactor): pass
class Wholesome(FormFactor): pass
class Fillet(FormFactor): pass
class Peeled(FormFactor): pass
class Chopped(FormFactor): pass
class Sliced(FormFactor): pass
class Diced(FormFactor): pass

class Dispenser(Tool, FormFactor): pass
class Grinder(Tool, FormFactor): pass

