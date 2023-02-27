class Burger:
    def __init__(self, ingredients) :
        self.ingredients = ingredients

    def print(self):
        print(self.ingredients)


class BurgerFactory:
    def createCheeseBurger(self):
        ingredients=["bun", "cheese", "beef-patty"]
        return Burger(ingredients)

    def createDeluxeCheeseBurger(self):
        ingredients=["bun", "tomate", "lettuce","cheese", "beef-patty"]
        return Burger(ingredients)

    def createVeganBurger(self):
        ingredients=["bun", "special-sauce", "veggie-patty"]
        return Burger(ingredients)


burger_factory = BurgerFactory()
burger_factory.createCheeseBurger().print()
burger_factory.createDeluxeCheeseBurger().print()
burger_factory.createVeganBurger().print()
