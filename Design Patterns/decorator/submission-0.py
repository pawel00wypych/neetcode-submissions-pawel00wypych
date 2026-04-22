class Coffee(ABC):
    @abstractmethod
    def getCost(self):
        pass

class SimpleCoffee(Coffee):
    def getCost(self):
        return 1.1

class CoffeeDecorator(Coffee):
    def __init__(self, decoratedCoffee):
        self.decoratedCoffee = decoratedCoffee

    def getCost(self):
        return self.decoratedCoffee.getCost()

class MilkDecorator(CoffeeDecorator):
    def __init__(self, coffee_decorator: Coffee):
        self.coffee_decorator = coffee_decorator

    def getCost(self):
        return self.coffee_decorator.getCost() + 0.5

class SugarDecorator(CoffeeDecorator):
    def __init__(self, coffee_decorator: Coffee):
        self.coffee_decorator = coffee_decorator

    def getCost(self):
        return self.coffee_decorator.getCost() + 0.2

class CreamDecorator(CoffeeDecorator):
    def __init__(self, coffee_decorator: Coffee):
        self.coffee_decorator = coffee_decorator

    def getCost(self):
        return self.coffee_decorator.getCost() + 0.7

