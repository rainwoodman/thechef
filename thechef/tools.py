class Tool: pass

class Spatula(Tool): pass
class Tongs(Tool): pass
class Knife(Tool): pass
class Scissor(Tool): pass

class Heat(Tool):
    def __init__(self, intensity):
        self.intensity = intensity

