class Calculadora:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def somar(self):
        return self.num1 + self.num2
    
    def subtrair(self):
        return self.num1 - self.num2
    
    def multiplicar(self):
        return self.num1 * self.num2
    
    def dividir(self):
        if self.num2 == 0:
            return "Não é possível dividir por zero."
        return self.num1 / self.num2
    
if __name__ == "__main__":
    calc = Calculadora(10, 2)

    print(f"Soma: {calc.somar()}")          
    print(f"Subtração: {calc.subtrair()}")   
    print(f"Multiplicação: {calc.multiplicar()}") 
    print(f"Divisão: {calc.dividir()}")     