
from stanze import *
from classi import Data, Prenotazione
#Matteo Solini mat: 619738
"""
Definire una classe Hotel che rappresenta un hotel.
#STATO:
- stanze: dizionario con chiave il numero della stanza e valore l'oggetto stanza.
- prenotazioni: dizionario con chiave un intero e valore l'oggetto prenotazione.
- id_prenotazioni: intero progressivo inizializzato a 1 e incrementato ogni volta che una prenotazione viene aggiunta, da usare come chiave per le prenotazioni.
#METODI:
- Costruttore che inizializza le variabili di istanza. Esempio di utilizzo: h = Hotel()
- Metodo per il confronto di uguaglianza profonda tra due hotel.
- Metodo per la rappresentazione in forma di stringa dell'hotel. Rispettando il formato di esempio: "Hotel: 3 stanze (101,102,103), 2 prenotazioni." (Nota: non è necessario stampare i dettagli delle stanze e delle prenotazioni).
- Metodi specificati in seguito.
"""
class Hotel:
    def __init__(self):
        self.stanze = {}
        self.prenotazioni = {}
        self.id_prenotazioni = 1

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.stanze == other.stanze and self.prenotazioni == other.prenotazioni



    def __str__(self):
        stanze_hotel=[]
        for n in self.stanze:
            stanze_hotel.append(str(n))
        lista_numeri = ", ".join(stanze_hotel)
        return f"Hotel: {len(self.stanze)} stanze ({lista_numeri}), {len(self.prenotazioni)} prenotazioni."


    """
    Inserisce una nuova stanza nell'hotel.
    :param stanza oggetto di tipo Stanza da aggiungere all'hotel
    :raise TypeError: se i parametri non hanno il tipo corretto
    :raise ValueError: se i parametri non sono nel range di valori ammessi
    """
    def aggiungi_stanza(self, stanza):

        #controllo sul tipo
        if not isinstance(stanza, Stanza):
            raise TypeError ("il parametro stanza deve essere un oggetto di tipo Stanza")

        # numero_stanza deve essere un numero maggiore di zero
        if not isinstance(stanza.numero_stanza, int) or stanza.numero_stanza <= 0:
            raise ValueError("il numero della stanza deve essere un numero maggiore di 0 ")

        #controllo se la stanza è già presente
        if stanza.numero_stanza in self.stanze:
            raise ValueError("la stanza è già presente")

        #aggiungo la stanza
        self.stanze[stanza.numero_stanza] = stanza


    """
    Prenota una stanza nell'hotel e incrementa id_prenotazioni se la prenotazione va a buon fine.
    Crea un oggetto Prenotazione con id_prenotazioni e i parametri in ingresso, e lo aggiunge al dizionario delle prenotazioni.
    :param numero_stanza: numero della stanza da prenotare
    :param data_arrivo: oggetto di tipo Data rappresentante la data di arrivo
    :param data_partenza: oggetto di tipo Data rappresentante la data di partenza
    :param nome_cliente: stringa rappresentante il nome del cliente
    :param numero_persone: intero rappresentante il numero di persone
    :return indice della prenotazione
    :raise TypeError: se i parametri non hanno il tipo corretto
    :raise ValueError: se la stanza è già occupata nelle date indicate
    :raise KeyError: se la stanza non è presente nell'hotel
    """
    def prenota(self, numero_stanza, data_arrivo, data_partenza, nome_cliente, numero_persone):

        if not isinstance (numero_stanza, int):
            raise TypeError ("il numero della stanza deve essere un numero")

        if numero_stanza <= 0:
            raise ValueError("il numero della stanza deve essere maggiore di 0 ")

        if not isinstance (nome_cliente, str):
            raise TypeError ("il nome_cliente deve essere una stringa")

        if nome_cliente == " ":
            raise ValueError("il nome del cliente non può essere una stringa vuota ")

        if not isinstance(numero_persone, int):
            raise TypeError("il numero delle persone deve essere un numero")

        if numero_persone <= 0:
            raise ValueError("il numero delle persone deve essere maggiore di 0 ")

        if numero_stanza not in self.stanze:
            raise KeyError("la stanza non è presente nell'hotel")


       #verifico se c'è già una prenotazione per quella stanza
        for prenotazione in self.prenotazioni.values():
            if prenotazione.numero_stanza == numero_stanza: #se la stanza ha già una prenotazione
                arrivo_esistente = prenotazione.data_arrivo #var che mi salva la data arrivo esistente
                partenza_esistente = prenotazione.data_partenza #var che mi salva la data partenza esistente

                # Controllo sovrapposizione: intervalli di date tra date esistenti e nuove date
                if (data_arrivo <= partenza_esistente) and (data_partenza >= arrivo_esistente):
                    raise ValueError("La stanza è già occupata nelle date indicate")

        #assegno l'id della nuova prenotazione
        id_corrente = self.id_prenotazioni
        nuova_prenotazione = Prenotazione(id_corrente, numero_stanza, data_arrivo, data_partenza, nome_cliente, numero_persone)
        self.prenotazioni[id_corrente] = nuova_prenotazione #inserisco la nuova prenotazione nel dizionario delle prenotazioni
        self.id_prenotazioni += 1 #aggiorno il numero delle prenotazioni
        return id_corrente


    """
    Disdice una prenotazione dell'hotel.
    :param indice della prenotazione da disdire
    :raise KeyError: se la prenotazione non è presente nell'hotel
    """
    def disdici(self, indice):
        if indice in self.prenotazioni:
            del self.prenotazioni[indice]
        else:
            raise KeyError("la prenotazione non è presente nell'hotel")


    """
    Rimuove una stanza dall'hotel e tutte le prenotazioni relative a quella stanza.
    :param numero_stanza: numero della stanza da rimuovere
    :raise KeyError: se la stanza non è presente nell'hotel
    """
    def rimuovi_stanza(self, numero_stanza):
        if numero_stanza not in self.stanze:
            raise KeyError("la stanza non è presente nell'hotel")
        else:
            del self.stanze[numero_stanza]  # rimuovo la stanza di hotel

        # X RIMUOVERE LE PRENOTAZIONI DELLA STANZA
        id_da_rimuovere = [] #lista vuota che mi conterrà gli id delle prenotazioni che hanno la stanza da eliminare
        for id_stanza, p in self.prenotazioni.items(): #con il for entro dentro le prenotazioni
            if p.numero_stanza == numero_stanza: #se le prenotazioni hanno la stanza da eliminare
                id_da_rimuovere.append(id_stanza)  #inserisco la prenotazione in id_da_rimuovere
        for d in id_da_rimuovere:
            del self.prenotazioni[d] #elimino le prenotazioni


    """
    Restituisce una stanza specifica dell'hotel.
    :param numero_stanza: numero della stanza da restituire
    :return: la stanza con numero_stanza
    :raise KeyError: se la stanza non è presente nell'hotel
    """
    def get_stanza(self, numero_stanza):
        if not numero_stanza in self.stanze:
            raise KeyError("la stanza non è presente nell'hotel")
        return self.stanze[numero_stanza]


    """
    Restituisce la lista delle stanze presenti nell'hotel.
    :return: la lista delle stanze presenti nell'hotel
    """
    def get_stanze(self):
        stanze= []
        for stanza in self.stanze.values():
            stanze.append(stanza)
        return stanze

    """
    Restituisce la lista delle stanze per tipo passato presenti nell'hotel.
    :param tipo: stringa rappresentante il tipo di stanza da cercare
    :return: la lista delle stanze per tipo passato presenti nell'hotel
    """
    def get_stanze_tipo(self, tipo):
        lista = []
        for stanza in self.stanze.values():
            if stanza.get_tipo_stanza() == tipo:
                lista.append(stanza)
        return lista


    """
    Restituisce la lista delle prenotazioni presenti nell'hotel.
    :return: la lista delle prenotazioni presenti nell'hotel
    """
    def get_prenotazioni(self):
        prenotazioni = []
        for p in self.prenotazioni.values():
            prenotazioni.append(p)
        return prenotazioni

    """
    Restituisce una prenotazione specifica dell'hotel.
    :param indice: indice della prenotazione da restituire
    :return: la prenotazione con indice
    :raise KeyError: se la prenotazione non è presente nell'hotel
    """
    def get_prenotazione(self, indice):
        if indice not in self.prenotazioni:
            raise KeyError ("la prenotazione non è presente nell'hotel")
        return self.prenotazioni[indice]

    """
    Restituisce la lista delle prenotazioni presenti nell'hotel in una data specifica.
    :param data: data da cercare
    :return: la lista delle prenotazioni presenti nell'hotel in una data specifica
    :raise TypeError: se data non è un oggetto di tipo Data
    """
    def get_prenotazioni_data(self, data):
        if not isinstance(data, Data):
            raise TypeError("data non è un oggetto di tipo Data")
        pren = []
        # controllo che la data sia maggiore o uguale rispetto alla data di arrivo e che sia minore rispetto alla data di partenza.
        for prenotazione in self.prenotazioni.values():
            if prenotazione.data_arrivo <= data < prenotazione.data_partenza:
                pren.append(prenotazione)
        return pren


    """
    Restituisce il prezzo di una prenotazione specifica ottenuto dal prezzo della stanza per il numero di persone e per il numero di notti.
    :param indice: indice della prenotazione da cercare
    :return: il prezzo della prenotazione con indice
    :raise KeyError: se la prenotazione non è presente nell'hotel

    """

    def prezzo_prenotazione(self, indice):

        # attraverso l'indice accedo alla prenotazione
        prenotazione = self.prenotazioni[indice]

        # ricavo l'oggetto stanza grazie al numero della stanza che ho preso dalla prenotazione
        stanza = self.stanze[prenotazione.numero_stanza]

        # calcolo il numero delle notti da inserire poi in calcola_prezzo
        numero_notti = prenotazione.data_partenza - prenotazione.data_arrivo

        prezzo_totale = stanza.calcola_prezzo(numero_notti)

        # moltiplico per il numero di persone
        prezzo_totale *= prenotazione.numero_persone
        return prezzo_totale


    """
    Restituisce la lista delle prenotazioni presenti nell'hotel per un cliente specifico.
    :param cliente: nome del cliente da cercare
    :return: la lista delle prenotazioni presenti nell'hotel per un cliente specifico    
    """
    def get_prenotazioni_cliente(self, cliente):
        prenotazione = []
        for p in self.prenotazioni.values():
            if p.nome_cliente == cliente:
                prenotazione.append(p)
        return prenotazione


    """
    Restituisce la lista delle stanze libere nell'hotel in una data specifica.
    :param data: data da cercare
    :return: la lista delle stanze libere nell'hotel in una data specifica
    :raise TypeError: se data non è un oggetto di tipo Data
    """
    def get_stanze_libere(self, data):
        if not isinstance(data, Data):
            raise TypeError("data non è un oggetto di tipo Data")
        stanze_occupate = []
        for prenotazione in self.prenotazioni.values():
            if prenotazione.data_arrivo <= data < prenotazione.data_partenza:
                stanze_occupate.append(prenotazione.numero_stanza)
        stanze_libere = []
        for numero, stanza in self.stanze.items():
            if numero not in stanze_occupate:
                stanze_libere.append(stanza)
        return stanze_libere

    """
    Restituisce la lista delle prenotazioni presenti nell'hotel per un tipo di stanza specifico.
    :param tipo_stanza: stringa rappresentante il tipo di stanza da cercare
    :return: la lista delle prenotazioni presenti nell'hotel per un tipo di stanza specifico
    """
    def get_prenotazioni_tipo_stanza(self, tipo_stanza):
            prenotazioni = []

            for prenotazione in self.prenotazioni.values():
                stanza = self.stanze[prenotazione.numero_stanza]
                if stanza.get_tipo_stanza() == tipo_stanza:
                    prenotazioni.append(prenotazione)
            return prenotazioni

    """
    Restituisce la lista delle stanze dell'hotel sopra un prezzo specifico fra due date.
    :param numero_notti: numero di notti da considerare
    :param prezzo: prezzo da confrontare
    :return: la lista delle stanze dell'hotel sopra un prezzo specifico
    """
    def get_stanze_sopra_prezzo(self, numero_notti, prezzo):
        stanze_p = []

        for stanza in self.stanze.values():
            #attraverso calcola.prezzo verifico il prezzo di ogni stanza
            prezzo_stanza = stanza.calcola_prezzo(numero_notti)
            # se il prezzo della stanza è maggiore di prezzo allora lo metto dentro la lista
            if prezzo_stanza > prezzo:
                stanze_p.append(stanza)
        return stanze_p

    """
    Restituisce il numero totale di persone presenti nell'hotel in una data specifica.
    :param data: data da cercare
    :return: il numero totale di persone presenti nell'hotel in una data specifica
    :raise TypeError: se data non è un oggetto di tipo Data
    """
    def get_numero_persone_data(self, data):
        if not isinstance(data, Data):
            raise TypeError("data non non è un oggetto di tipo Data")

        persone = 0
        for i in self.prenotazioni.values():
            if i.data_arrivo <= data < i.data_partenza:
                persone += i.numero_persone
        return persone


    """
    Salva lo stato dell'hotel su un file. Le eccezioni non devono essere gestite in questo metodo.
    :param nomefile: nome del file su cui salvare lo stato dell'hotel
    """
    def salva(self, nomefile):
        with open(nomefile, "w") as f:
           # f.write(f"numero prenotazioni:{self.id_prenotazioni}\n")

            for stanza in self.stanze.values():
                tipo = stanza.get_tipo_stanza()
                if tipo == "Singola" or tipo == "Doppia":
                    f.write(f"{tipo}:{stanza.numero_stanza}:{stanza.prezzo_base}\n")
                elif tipo == "Suite":
                    extra = ";".join(stanza.extra)
                    f.write(f"{tipo}:{stanza.numero_stanza}:{stanza.posti}:{stanza.prezzo_base}:{extra}\n")

            for p in self.prenotazioni.values():
                f.write(f"prenotazione:{p.id_prenotazione}:{p.numero_stanza}:{p.data_arrivo}:{p.data_partenza}:{p.nome_cliente}:{p.numero_persone}\n")

    """ 
    Singola:100:50.0
    Suite:103:200.0:TV;
    Prenotazione:5:103:1/3:1/4:Sempronio:1

    a = ["Suite","103","200.0","Tv;Frigo"]
    num = int(a[1])
    b = a[3].split(";")
    b -> ["Tv", "Frigo"]
    """
    """
    Carica lo stato dell'hotel da un file e sostituisce lo stato corrente se il caricamento va a buon fine. Le eccezioni non devono essere gestite in questo metodo.
    :param nomefile: nome del file da cui caricare lo stato dell'hotel
    :raise ValueError: se il file non è nel formato corretto (es. se non è presente il nome dell'hotel)
    """

    def carica(self, nomefile):
        stanze_temp = {}
        prenotazioni_temp = {}
        max_id = 0

        with open(nomefile, "r") as f:
            righe = f.readlines()
            if not righe:
                raise ValueError("il file non è nel formato corretto")
            for riga in righe:
                riga = riga.strip()
                if riga.startswith("Singola") or riga.startswith("Doppia"):
                    a = riga.split(":")
                    if len(a) != 3:
                        raise ValueError(f"Formato errato")
                    tipo = a[0]
                    numero = int(a[1])
                    prezzo = float(a[2])
                    if tipo == "Singola":
                        stanza = Singola(numero, prezzo)
                    else:
                        stanza = Doppia(numero, prezzo)
                    stanze_temp[numero] = stanza

                elif riga.startswith("Suite"):
                    a = riga.split(":")
                    if len(a) != 5:
                        raise ValueError(f"Formato errato")
                    numero = int(a[1])
                    posti = int(a[2])
                    prezzo = float(a[3])
                    extra = a[4].split(";")
                    stanza = Suite(numero, posti, extra, prezzo)
                    stanze_temp[numero] = stanza


                elif riga.startswith("prenotazione"):
                    a = riga.split(":")
                    if len(a) != 7:
                        raise ValueError(f"Formato errato")
                    idp = int(a[1])
                    numero_stanza = int(a[2])
                    parti = a[3].split("/")
                    giorno_arrivo = int(parti[0])
                    mese_arrivo = int(parti[1])
                    data_arrivo = Data(giorno_arrivo, mese_arrivo)

                    parti = a[4].split("/")
                    giorno_partenza = int(parti[0])
                    mese_partenza = int(parti[1])
                    data_partenza = Data(giorno_partenza, mese_partenza)
                    cliente = a[5]
                    numero_persone = int(a[6])
                    prenotazione = Prenotazione(idp, numero_stanza, data_arrivo, data_partenza, cliente, numero_persone)
                    prenotazioni_temp[idp] = prenotazione
                    if idp > max_id:
                        max_id = idp

        self.stanze = stanze_temp
        self.prenotazioni = prenotazioni_temp
        self.id_prenotazioni = max_id + 1





