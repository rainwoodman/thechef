from thechef.base import Recipe, Until

from thechef.tools import Spatula, Tongs, Knife, Scissor
from thechef.containers import IronPan
from thechef.platforms import CuttingBoard, StoveTop
from thechef.formfactors import Dispenser, Grinder, Powder, Wholesome, Fillet

from thechef.raw import Ginger, BlackPepper, SeaSalt, Sesame, Oil
from thechef.raw import Salmon, ChickenStock, Califlower, Carrot

from thechef.tools import Heat
from thechef.base import Done, Progress

def test_recipe():
    recipe = Recipe("Grilled Salmon")

    califlower = recipe.use(Califlower, amount=1)
    carrot = recipe.use(Carrot, amount=0.3)
    salmon = recipe.use(Salmon, amount=1, formfactor=Fillet)
    pan    = recipe.use(IronPan, specs='10 inches')
    ginger = recipe.use(Ginger, amount=0.1)
    sesame = recipe.use(Sesame, amount=0.1)

    stock = recipe.use(ChickenStock, amount=100)

    califlower.apply(Knife, 
                   on=CuttingBoard, 
                   amount=Until('small pieces'))

    ginger.apply(Knife, 
                   on=CuttingBoard, 
                   amount=Until('thin slices'))

    carrot.apply(Knife,
                     on=CuttingBoard,
                     technique='rotationary',
                     amount=Until('small pieces'))

    salmon.apply([
                    Grinder(SeaSalt),
                    Grinder(BlackPepper)
                ], amount=0.1,
                technique='both sides')

    pan.apply(Dispenser(Oil), amount=Until('slightly oiled'))
    pan.apply(Grinder(SeaSalt), amount=Until('slightly covered'))
 
    pan.add(ginger, sesame, overlap=True)

    pan.apply(Heat(0.9), on=StoveTop, amount=Until('hot', limit=5))

    pan.add(salmon, overlap=True)

    with pan.apply(Heat(0.7), on=StoveTop, amount=10) as tr:
        def flip():
            salmon.apply(Spatula, amount=Until('flipped'))

        def addvegi():
            pan.add(califlower, carrot, overlap=False)
            pan.add([
                    recipe.use(SeaSalt, amount=0.1),
                    recipe.use(BlackPepper, amount=0.1)
                    ]
                    )

        tr.notify(Progress(amount=5), addvegi)
        tr.notify(Done, flip)

    with pan.apply(Heat(0.7), on=StoveTop, amount=8) as tr:
        def addstock():
            pan.add(stock, overlap=True)
            pan.cover()

        tr.notify(Progress(amount=6), addstock)
        
    pan.apply(Heat(0.4), on=StoveTop, amount=3)
    pan.uncover()
    pan.remove(salmon, califlower, carrot)

    print(recipe)

