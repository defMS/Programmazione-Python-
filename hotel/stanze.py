from classi import Data

#Matteo Solini mat: 619738
"""
Definire una classe Stanza che rappresenta una stanza di un hotel.
#STATO:
- numero_stanza: intero positivo.
- posti: intero positivo.
- prezzo_base: numero con virgola maggiore di 1.
Ogni volta che si modifica una di queste variabili di istanza, devono essere controllati tipo e valori e sollevate opportune eccezioni ValueError o TypeError se i parametri non sono validi.
#METODI:
- ok Costruttore che prende in input il numero della stanza, il numero di posti e il prezzo base. Esempio di utilizzo: s = Stanza(101, 2, 50.0)
- ok Metodi getter e setter per il numero della stanza, il numero di posti e il prezzo base.
- ok Metodo calcola_prezzo che prende in input l'intero numero_notti e restituisce il prezzo della stanza per il periodo indicato. Il prezzo della stanza è dato dal prezzo base moltiplicato per il numero di notti di permanenza.
- ok Metodo per la rappresentazione in forma di stringa della stanza, rispettando il formato di esempio: "101, 2 posti" dove 101 è il numero della stanza e 2 il numero di posti.
- ok Metodo per il confronto di uguaglianza profonda tra due stanze.
- ok Metodo get_tipo_stanza che restituisce il nome della classe. Esempio di utilizzo: s.get_tipo_stanza() restituisce "Stanza"
"""

class Stanza:

    def __init__(self, numero_stanza, posti, prezzo_base):

        if not isinstance(numero_stanza, int):
             raise TypeError ('Il numero della stanza deve essere un intero ')
        if not numero_stanza > 0:
            raise ValueError('Il numero della stanza deve essere maggiore di 0')

        if not isinstance(posti, int):
            raise TypeError ('I posti deve essere un intero ')
        if not posti > 0:
            raise ValueError('I posti deve essere positivo ')

        if not isinstance(prezzo_base, float):
            raise TypeError ('Il prezzo base deve essere un numero con virgola')

        #ASSEGNAZIONI
        self.numero_stanza = numero_stanza
        self.posti = posti
        self.prezzo_base = prezzo_base


    #GET
    def get_numero_stanza(self):
        return self.numero_stanza

    def get_posti(self):
        return self.posti

    def get_prezzo_base(self):
        return self.prezzo_base

    # restituisce il nome della classe
    def get_tipo_stanza(self):
        return self.__class__.__name__ # solo il nome

    #SET
    def set_numero_stanza(self, numero_stanza):
        if not isinstance(numero_stanza, int):
             raise TypeError ('Il numero della stanza deve essere un intero ')
        if not numero_stanza > 0:
            raise ValueError('Il numero della stanza deve essere maggiore di 0')
        self.numero_stanza = numero_stanza

    def set_posti(self, posti):
        if not isinstance(posti, int):
            raise TypeError ('I posti deve essere un intero ')
        if not posti > 0:
            raise ValueError('I posti deve essere positivo ')
        self.posti = posti


    def set_prezzo_base(self, prezzo_base):
        if not isinstance(prezzo_base, float):
            raise TypeError ('Il prezzo base deve essere un numero con virgola')
        self.prezzo_base = prezzo_base


    def calcola_prezzo(self,numero_notti):
        if not isinstance(numero_notti, int):
            raise TypeError("Il numero di notti deve essere un intero")
        if numero_notti <= 0:
            raise ValueError("Il numero di notti deve essere maggiore di 0")
        prezzo = numero_notti * self.prezzo_base
        return prezzo


    def __str__(self):
        return f" {self.numero_stanza},{self.posti} posti"


    #confronto di uguaglianza profonda fra due stanze
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return (self.numero_stanza, self.posti, self.prezzo_base) == (other.numero_stanza, other.posti, other.prezzo_base)


"""
Definire una classe Suite che estende Stanza e rappresenta una suite di un hotel. Una suite è una stanza con almeno 4 posti e con una lista di extra.
#STATO:
- extra: lista di stringhe.
Ogni volta che si modifica questa variabile devono essere controllati tipo e valori e sollevate opportune eccezioni ValueError o TypeError in casi errati.
#METODI:
- ok Costruttore che prende in input il numero della stanza, il numero di posti, la lista di extra e il prezzo base, e inizializza le variabili ereditate. Esempio di utilizzo: s = Suite(102, 4, ["TV", "WiFi", "Jacuzzi"], 200.0)
- ok Metodi getter e setter per la lista di extra.
- ok Metodo calcola_prezzo che prende in input l'intero numero_notti e calcola il prezzo della stanza per il periodo indicato. Il prezzo di una notte per una suite è dato dal prezzo base maggiorato del 50% più 10 euro per ogni extra.
- ok Metodo per la rappresentazione in forma di stringa della suite. Rispettando il formato di esempio: "Suite 102, 4 posti, con TV, WiFi e Jacuzzi"
- ok Metodo per il confronto di uguaglianza profonda tra due suite.
- ok Metodo get_tipo_stanza che restituisce il nome della classe. Esempio di utilizzo: s.get_tipo_stanza() restituisce "Suite"
"""
class Suite(Stanza):
    def __init__(self, numero_stanza, posti, extra, prezzo_base):

        super().__init__(numero_stanza, posti, prezzo_base)
        self.extra = extra # definisco il nuovo attributo

       #almeno 4 posti
        if posti < 4:
            raise ValueError('La suite deve avere almeno 4 posti')

        # controllo lista di stringhe
        if not isinstance(extra, list):
            raise TypeError('deve essere una lista')

        # tutti gli elementi all'interno di extra devono essere delle stringhe
        for i in extra:
            if not isinstance(i, str):
                raise TypeError('deve essere una lista di stringhe')



    #GETTER
    def get_extra(self):
        return self.extra

    #SETTER
    def set_extra(self, extra):
               #almeno 4 posti
        if self.posti < 4:
            raise ValueError('La suite deve avere almeno 4 posti')

        # controllo lista di stringhe
        if not isinstance(extra, list):
            raise TypeError('deve essere una lista')

        #tutti gli elementi all'interno di extra devono essere delle stringhe
        for i in extra:
            if not isinstance(i, str):
                raise TypeError('deve essere una lista di stringhe')

        if len(extra)<2:
            raise ValueError('Una suite deve contenere almeno due extra')

    def calcola_prezzo(self, numero_notti):
        if not isinstance(numero_notti, int):
            raise TypeError("Il numero di notti deve essere un intero")
        if numero_notti <= 0:
            raise ValueError("Il numero di notti deve essere maggiore di 0")
        prezzo = numero_notti * (self.prezzo_base * 1.5 + len(self.extra) * 10)
        return prezzo

    def __str__(self):
        stanze_suite = []
        for l in self.extra:
            stanze_suite.append(l)
        lista_extra = ", ".join(stanze_suite)
        return f"Suite {self.numero_stanza}, {self.posti} posti, con {lista_extra}"

    # confronto di uguaglianza profonda fra due suite
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return (self.numero_stanza, self.posti, self.prezzo_base, self.extra) == (other.numero_stanza, other.posti, other.prezzo_base, other.extra)

    def get_tipo_stanza(self):
        return self.__class__.__name__


"""
Definire una classe Singola che estende Stanza e rappresenta una stanza singola di un hotel. Una stanza singola è una stanza con un solo posto.
#METODI:
- ok Costruttore che prende in input il numero della stanza e il prezzo base, e inizializza opportunamente le variabili ereditate. Esempio di utilizzo: s = Singola(103, 40.0)
- ok Metodo per la rappresentazione in forma di stringa della stanza. Rispettando il formato di esempio: "Singola 103, 1 posto"
- ok Metodo per il confronto di uguaglianza profonda tra due stanze singole.
- ok Metodo get_tipo_stanza che restituisce il nome della classe. 
"""
class Singola(Stanza):
    def __init__ (self, numero_stanza, prezzo_base):
        super().__init__(numero_stanza, 1,  prezzo_base)

    # confronto di uguaglianza profonda fra due stanze singole
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return (self.numero_stanza, self.prezzo_base,) == (other.numero_stanza, other.prezzo_base)

    def __str__(self):
        return f"Singola {self.numero_stanza}, {self.posti} posto"

    def get_tipo_stanza(self):
        return self.__class__.__name__


"""
Definire una classe Doppia che estende Stanza e rappresenta una stanza doppia di un hotel. Una stanza doppia è una stanza con due posti.
#METODI:
- ok Costruttore che prende in input il numero della stanza e il prezzo base, e inizializza opportunamente le variabili ereditate. Esempio di utilizzo: s = Doppia(104, 60.0)
- ok Metodo per la rappresentazione in forma di stringa della stanza. Rispettando il formato di esempio: "Doppia 104, 2 posti"
- ok Metodo calcola_prezzo che prende in input l'intero  numero_notti e calcola il prezzo della stanza per il periodo indicato. Il prezzo di una notte per una doppia è dato dal prezzo base maggiorato del 20%.
- ok Metodo per il confronto di uguaglianza profonda tra due stanze doppie.
- ok Metodo get_tipo_stanza che restituisce il nome della classe. 
"""

class Doppia(Stanza):
    def __init__ (self, numero_stanza, prezzo_base):
        super().__init__(numero_stanza, 2,  prezzo_base)

    # confronto di uguaglianza profonda fra due stanze singole
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return (self.numero_stanza, self.prezzo_base) == (other.numero_stanza, other.prezzo_base)

    def __str__(self):
        return f"Doppia {self.numero_stanza}, {self.posti} posti"

    def get_tipo_stanza(self):
        return self.__class__.__name__


    def calcola_prezzo(self, numero_notti):
        if not isinstance(numero_notti, int):
            raise TypeError("Il numero di notti deve essere un intero")
        if numero_notti <= 0:
            raise ValueError("Il numero di notti deve essere maggiore di 0")
        prezzo = numero_notti * (self.prezzo_base * 1.2)
        return prezzo

