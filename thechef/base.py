class Recipe:
    def __init__(self, name):
        self.name = name

    def use(self, element_type, *args, **kwargs):
        return element_type(self, *args, **kwargs)

class Transaction:
    def __enter__(self):
        return self

    def __exit__(self, type, value, tb):
        return

    def notify(self, event, function):
        pass

class Event:
    pass

class Progress(Event):
    def __init__(self, amount):
        self.amount = amount

class Done(Event):
    pass

class Element:
    def __init__(self, recipe):
        self.recipe = recipe

    def apply(self, tool, amount, on=None, technique=None):
        if on is None: on = self

        return Transaction()
        

class Until:
    def __init__(self, condition, limit=None):
        self.condition = condition
        self.limit = limit

class FormFactor:
    def __init__(self, raw):
        self.raw = raw
    def __call__(self, *args, **kwargs):
        return self.raw(*args, **kwargs)
