class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:

        x = init
        while iterations > 0:
            gradient = self.calcDerivative(x)
            x -= learning_rate * gradient
            loss_fun_val = self.loss_fun(x)
            iterations -= 1

        return round(x, 5)
    
    def loss_fun(self, x: float) -> float:
        return x**2

    def calcDerivative(self, x):
        return 2*x