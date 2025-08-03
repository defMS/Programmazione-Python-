
#Matteo Solini mat: 619738
"""
Definire una classe Data per rappresentare una specifica data all'interno di un anno non bisestile.
#STATO:
- mappa_mesi: dizionario con chiave il numero del mese e valore il numero di giorni. Esempio: {1: 31, 2: 28, ...}. Sfruttare questa mappa per controllare la validità di una data e per calcolare la differenza tra due date.
- giorno: intero con valore compreso tra 1 e il numero di giorni del mese. 
- mese: intero con valore compreso tra 1 e 12.
Ogni volta che si modifica una di queste variabili di istanza, devono essere controllati tipo e valori e sollevate opportune eccezioni ValueError o TypeError se i parametri non sono validi.

#METODI:
- ok Costruttore che prende in input giorno, mese e anno e inizializza le variabili di istanza. Esempio di utilizzo: d = Data(1, 1)
- ok Metodi getter e setter per giorno e mese.
- ok Metodo per la rappresentazione in forma di stringa della data, rispettando il formato di esempio: "1/1"
- ok Metodo per il calcolo della differenza in giorni tra due date. Esempio di utilizzo: d2 - d1 dove d1 = Data(1, 1), d2 = Data(1, 2), risultato -> 31. Nota, d2 - d1 deve essere uguale a d1 - d2.
- ok Metodo per il confronto di uguaglianza tra due date.
- ok Metodo per il confronto di maggiore tra due date. Esempio di utilizzo: d1 < d2
- ok Metodo per il confronto di minore tra due date. Esempio di utilizzo: d1 > d2
- ok Metodo per il confronto di minore o uguale tra due date. Esempio di utilizzo: d1 <= d2
"""
class Data: 
    def __init__(self, giorno, mese):
        
        mappa_mesi = {
            1: 31, 2: 28, 3: 31, 4: 30,
            5: 31, 6: 30, 7: 31, 8: 31,
            9: 30, 10: 31, 11: 30, 12: 31
        }

        #SELF #assegnazione variabili di istanza.
        self.mappa_mesi = mappa_mesi
        self.mese = mese
        self.giorno = giorno

        if not isinstance(giorno, int):
            raise TypeError ('Il giorno deve essere un intero')
        if giorno == 0:
            raise ValueError ('Il giorno deve essere un valore compreso tra 1 e il numero di giorni del mese ')
        if not isinstance(mese, int):
             raise TypeError ('Il mese deve essere un intero')
        if mese not in range(1, 13):
            raise ValueError ('Il mese deve essere un valore compreso tra 1 e 12 ')
       

    #GET
    def get_giorno(self): #mi prende il giorno
        return self.giorno
    
    def get_mese(self):
        return self.mese


    #SETTER
    def set_giorno(self, giorno):
        if not isinstance(giorno, int):
            raise TypeError("Il giorno deve essere un intero")
        if giorno < 1 or giorno > self.mappa_mesi[self.mese]:
            raise ValueError("Il giorno non è valido per il mese corrente")
        self.giorno = giorno

    def set_mese(self, mese):
        if not isinstance(mese, int):
            raise TypeError("Il mese deve essere un intero")
        if mese < 1 or mese > 12:
            raise ValueError("Il mese deve essere compreso tra 1 e 12")
        self.mese = mese
        
    
    def __str__(self):
       return f"{self.giorno}/{self.mese}"
    
    def __sub__(self, other):
        #La differenza tra le due date deve essere sempre positiva d1= data maggiore; d2= data più piccola
        if self > other:
            d1 = self
            d2 = other
        else:
            d1 = other
            d2 = self

        #verifico se si tratti dello stesso mese, nel caso fosse il solito basterà fare la sottrazione dei giorni
        if d1.mese == d2.mese:
            return d1.giorno - d2.giorno


        '''
        15 maggio 
        10 luglio 
        '''

        giorni_totali = d1.giorno # 10
        for mese in range(d2.mese, d1.mese): #maggio e giugno 30 + 30
            giorni_totali += self.mappa_mesi[mese] #60 + 10

        giorni_totali -= d2.giorno #tolgo i giorni della data di arrivo 15
        return giorni_totali


            
    #confronto di uguaglianza tra due date
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return (self.mese, self.giorno) == ( other.mese, other.giorno)
        

    #confronto di maggiore tra due date.
    def __gt__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return (self.mese, self.giorno) > (other.mese, other.giorno)


    #confronto di minore tra due date.
    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return ( self.mese, self.giorno)  < (other.mese, other.giorno)


    #confronto di minore o uguale tra due date.
    def __le__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return ( self.mese, self.giorno)  <= (other.mese, other.giorno)


"""
Definire una classe Prenotazione per rappresentare una prenotazione di una stanza di un hotel.
Le prenotazioni saranno solo all'interno dello stesso anno solare. Ad esempio, non è possibile avere come data di arrivo il 27/12 e come data di partenza il 5/1.
#STATO:
- id_prenotazione: intero non negativo.
- numero_stanza: intero positivo.
- data_arrivo: oggetto di tipo Data.
- data_partenza: oggetto di tipo Data, non deve essere precedente alla data di arrivo.
- nome_cliente: stringa non vuota.
- numero_persone: intero positivo.
Ogni volta che si modifica una di queste variabili di istanza, devono essere controllati tipo e valori e sollevate opportune eccezioni ValueError o TypeError se i parametri non sono validi.

#METODI:
- Costruttore che prende in input il numero della stanza, la data di arrivo, la data di partenza, il nome del cliente e il numero di persone. Esempio di utilizzo: p = Prenotazione(101, Data(1, 1), Data(5, 1), "Mario Rossi", 2)
- Metodi getter e setter per il numero della stanza, la data di arrivo, la data di partenza, il nome del cliente e il numero di persone.
- Metodo per la rappresentazione in forma di stringa della prenotazione. Rispettando il formato di esempio: "Prenotazione 1 per stanza 101 da 1/1 a 5/1 a nome Mario Rossi per 1 persone"
- Metodo per il confronto di uguaglianza profonda tra due prenotazioni.
"""
class Prenotazione:
    def __init__(self, id_prenotazione, numero_stanza, data_arrivo, data_partenza, nome_cliente, numero_persone):


        if not isinstance(id_prenotazione, int) :
            raise TypeError ('id prenotazione deve essere un intero')
        if id_prenotazione < 0:
            raise ValueError ('Il valore non deve essere negativo')

        if not isinstance(numero_stanza, int) :
            raise TypeError ('Il numero della stanza deve essere un intero')
        if numero_stanza < 0:
            raise ValueError ('Il valore non deve essere negativo')

        if data_partenza <= data_arrivo:
            raise ValueError ('La data di partenza precede la data di arrivo')

        if not isinstance(nome_cliente, str):
            raise TypeError ('Il nome_cliente deve essere una stringa ')

        if nome_cliente == "":
            raise ValueError ('Il nome_cliente non può essere una stringa vuota')

        if not isinstance(numero_persone, int):
            raise TypeError ('Il numero delle persone deve essere un valore intero ')

        if numero_persone <= 0:
            raise ValueError ('Il numero delle persone deve essere un valore positivo')

        #SELF
        self.id_prenotazione = id_prenotazione
        self.numero_stanza = numero_stanza
        self.data_arrivo = data_arrivo
        self.data_partenza = data_partenza
        self.nome_cliente = nome_cliente
        self.numero_persone = numero_persone
    #GET
    def get_numero_stanza(self): #mi prende il giorno
        return self.numero_stanza
    
    def get_data_arrivo(self):
        return self.data_arrivo
    
    def get_data_partenza(self):
        return self.data_partenza
    
    def get_nome_cliente(self):
        return self.nome_cliente
    
    def get_numero_persone(self):
        return self.numero_persone
    
    #SET
    def set_numero_stanza(self, numero_stanza):
        if not isinstance(numero_stanza, int):
            raise TypeError('Il numero della stanza deve essere un intero')
        if numero_stanza < 0:
            raise ValueError('Il valore non deve essere negativo')
        self.numero_stanza = numero_stanza

    def set_data_arrivo(self, data_arrivo):
        if self.data_partenza and data_arrivo >= self.data_partenza:
            raise ValueError('La data di arrivo deve precedere la data di partenza')
        self.data_arrivo = data_arrivo

    def set_data_partenza(self, data_partenza):
        if self.data_arrivo and data_partenza <= self.data_arrivo:
            raise ValueError('La data di partenza deve essere successiva alla data di arrivo')
        self.data_partenza = data_partenza

    def set_nome_cliente(self, nome_cliente):
        if not isinstance(nome_cliente, str):
            raise TypeError('Il nome_cliente deve essere una stringa')
        if nome_cliente == "":
            raise ValueError('Il nome_cliente non può essere una stringa vuota')
        self.nome_cliente = nome_cliente

    def set_numero_persone(self, numero_persone):
        if not isinstance(numero_persone, int):
            raise TypeError('Il numero delle persone deve essere un valore intero')
        if numero_persone <= 0:
            raise ValueError('Il numero delle persone deve essere un valore positivo')
        self.numero_persone = numero_persone


    def __str__(self):
        return f"Prenotazione {self.id_prenotazione} per stanza {self.numero_stanza} da {self.data_arrivo} a {self.data_partenza} a nome {self.nome_cliente} per {self.numero_persone} persone"

    #confronto di uguaglianza tra due prenotazioni
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return (self.id_prenotazione, self.numero_stanza, self.data_arrivo, self.data_partenza, self.nome_cliente, self.numero_persone) == (other.id_prenotazione, other.numero_stanza, other.data_arrivo, other.data_partenza, other.nome_cliente, other.numero_persone)


