from thechef.recipe import Recipe
from thechef.utensils import Spatula, Tongs
from thechef.containers import IronPan
from thechef.cultaries import Knife, Scissor
from thechef.platforms import CuttingBoard, StoveTop
from thechef.formfactor import GrinderBottle, Powder, Wholesome, Fillet
from thechef.spices import Ginger, BlackPepper, SeaSalt

from thechef.raw import Salmon, ChickenStock, Califlower, Carrot

def test_recipe():
    recipe = Recipe("Grilled Salmon")

    califlower = recipe.use(Califlower, amount=1)
    carrot = recipe.use(Carrot, amount=0.3)
    salmon = recipe.use(Salmon, amount=1, formfactor=Fillet)
    pan = recipe.use(IronPan, amount=1, spec='10 inches'))
    ginger = recipe.use(Ginger, amount=0.1)

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
                    GrinderBottle(Salt),
                    GrinderBottle(BlackPepper),
                ],
                amount='*', technique='both sides')

    pan.apply(Oil, amount=Until('slightly oiled'))
 
    pan.add(ginger)

    pan.apply(Heat(0.9), on=StoveTop, amount=Until('hot', limit=5))

    pan.add(salmon, location=Top(ginger))

    with pan.apply(Heat(0.7) on=StoveTop, amount=10) as tr:
        def flip():
            salmon.apply(Spatula, amount=Until('flipped'))

        def addvegi():
            pan.add(califlower, carrot, location=Side(salmon))

        tr.notify(Progress(amount=5), addvegi)
        tr.notify(Done, flip)

    with pan.apply(Heat(0.7), on=Stovetop, amount=8) as tr:
        def addstock():
            pan.add(stock)

        tr.notify(Progress(amount=6), addstock)
        
    pan.apply([Cover, Heat(0.4)], on=Stovetop, amount=3)

    pan.remove(salmon, califlower, carrot)

    print(recipe)

