


class Carattere: 

    def __init__ (self, nome, valore): 

        if not isinstance( nome, str):
            raise TypeError
        
        if not isinstance( valore, str):
            raise TypeError
        
        if nome == '': 
            raise ValueError
       
        if len(valore) != 1: 

            raise ValueError
        
        self.nome = nome 
        self.valore = valore 




   
   
   
    def __eq__ (self, other): 
        
        if not isinstance(other, Carattere): 
            return False 


        if (self.nome ==  other.nome) and (self.valore == other.valore): 
            return True
        return False
    

class Cifra(Carattere): 

    def __init__(self, nome, valore):

        super().__init__(nome, valore)


 

        if int(valore) not in range (0, 10):

            raise ValueError




        