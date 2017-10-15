from .base import Element

class Platform(Element):
    def __init__(self, recipe, specs):
        super(self, Element).__init__(self, recipe)
        self.specs = specs

class CuttingBoard(Platform): pass
class StoveTop(Platform): pass
