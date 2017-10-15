from .base import Element

class Container(Element): 
    def __init__(self, recipe, specs):
        super(Container, self).__init__(recipe)
        self.specs = specs

    def add(self, *raw, technique=None, overlap=True):
        pass

    def remove(self, *raw):
        pass 

    def cover(self): pass
    def uncover(self): pass

class Pan(Container): pass
class IronPan(Pan): pass
class Pod(Container): pass
class Wok(Container): pass
