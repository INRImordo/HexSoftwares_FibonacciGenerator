
class Generer_fibonacci_number:
    
    def fibonacci_recursive(self, x):
        
        if int(x) <= 1:
            return x
        else:
            param1 = int(x) - 1
            param2 = int(x) - 2
            return self.fibonacci_recursive(param1) + self.fibonacci_recursive(param2)
        
       
