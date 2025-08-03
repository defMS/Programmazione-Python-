import tkinter as tk
from tkinter import messagebox
from hotel import Hotel
from classi import Data
root= tk.Tk()


#Matteo Solini mat: 619738

"""
 Deve essere realizzata un'interfaccia grafica usando il modulo tkinter che carichi automaticamente il file 
 hotel_base.txt, permetta di mostrare sin da subito le stanze dell'hotel indicando tipo e numero della stanza 
 (con extra in caso di suite) e le seguenti funzionalità:
 - ok mostrare la lista di prenotazioni dell'hotel;
 - ok prenotazione di una stanza;
 - ok disdire la prenotazione di una stanza;
 - ok ottenere il prezzo di una prenotazione dato l'indice:
 - ok mostrare l'hotel ad una certa data inserendo i nomi dei clienti nelle stanze a quella data;
 - ok ottenere le prenotazioni di uno specifico cliente inserendo il nome;
 - ok ottenere il numero di persone nell'albergo ad una certa data;
 - ok salvare o caricare da file lo stato dell'hotel permettendo di inserire il nome del file.
 - ok uscire dall'applicazione 
 Per uscire dall'applicazione deve essere possibile usare sia mouse che tastiera.
 L'aspetto dell'interfaccia viene deciso dallo studente.
"""

class HotelGUI:
    def  __init__(self, root):
        self.Hotel = Hotel()
        self.root = root
        self.root.title("Hotel")

        
        self.contenitoreSup = tk.Frame(self.root) #creo un contenitore per i bottoni
        self.contenitoreSup.pack(side="top")

        self.contenitoreInf = tk.Frame(self.root) #creo un contenitore per le operazioni dei bottoni
        self.contenitoreInf.pack(side="bottom")


        self.labelVar = tk.StringVar()

        #widget per far inserire testo all'utente 
        self.entry= tk.Entry(self.contenitoreSup)
        self.entry.pack()

        # Text per visualizzare contenuto 
        self.text = tk.Text(self.root, height=80, width=100)
        self.text.pack()

        #Label per mostrare informazione sull'esecuzione del comando richiesto 
        self.labelId = tk.Label(self.contenitoreInf,textvariable=self.labelVar, height=30, width=60)
        self.labelId.pack()



        # Carica automaticamente il file
        self.carica_file("hotel_base.txt")

    def carica_file(self, percorso_file):
        try:
            with open(percorso_file, "r", encoding="utf-8") as f:
                contenuto = f.read()
                self.text.insert("1.0", contenuto)
        except FileNotFoundError:
            self.labelVar.set(f"File non trovato: {percorso_file}")

        #BOTTONI 
        self.mostra_prenBtn= tk.Button(self.contenitoreSup, text="Prenotazioni Hotel", background="yellow", foreground="black") #creiamo un widget Button
        self.mostra_prenBtn.pack(side="left") #inseriamo i bottoni nella finestra

        self.pren_stanzaBtn= tk.Button(self.contenitoreSup, text="Prenotare Stanza", background="yellow", foreground="black")
        self.pren_stanzaBtn.pack(side="left")

        self.elimina_prenBtn= tk.Button(self.contenitoreSup, text="Disdire Prenotazione", background="yellow", foreground="black")
        self.elimina_prenBtn.pack(side="left")

        self.prez_prenBtn= tk.Button(self.contenitoreSup, text="Prezzo Prenotazioni", background="yellow", foreground="black")
        self.prez_prenBtn.pack(side="left")

        self.stato_hotelBtn= tk.Button(self.contenitoreSup, text="Hotel a data", background="yellow", foreground="black")
        self.stato_hotelBtn.pack(side="left")

        self.pren_clienteBtn= tk.Button(self.contenitoreSup, text="Prenotazione Cliente", background="yellow", foreground="black")
        self.pren_clienteBtn.pack(side="left")

        self.pers_totBtn= tk.Button(self.contenitoreSup, text="num persone tot", background="yellow", foreground="black")
        self.pers_totBtn.pack(side="left")

        self.salvaBtn= tk.Button(self.contenitoreSup, text="Salva", background="yellow", foreground="black")
        self.salvaBtn.pack(side="left")

        self.carica_Btn= tk.Button(self.contenitoreSup, text="carica", background="yellow", foreground="black")
        self.carica_Btn.pack(side="left")

        self.esci_btn= tk.Button(self.contenitoreSup, text="esci", background="yellow", foreground="black")
        self.esci_btn.pack(side="left")

        self.istruzioniBtn = tk.Button(self.contenitoreSup, text="?", background="yellow", foreground="black")
        self.istruzioniBtn.pack(side="left")


       #BIND

        self.mostra_prenBtn.bind("<Button-1>", self.mostra_prenHandler)
        self.pren_stanzaBtn.bind("<Button-1>", self.pren_stanzaHandler)
        self.elimina_prenBtn.bind("<Button-1>", self.elimina_prenHandler)
        self.prez_prenBtn.bind("<Button-1>", self.prez_prenHandler)
        self.stato_hotelBtn.bind("<Button-1>", self.stato_hotelHandler)
        #self.st_libereBtn.bind("<Button-1>", self.st_libereHandler)
        self.pren_clienteBtn.bind("<Button-1>", self.pren_clienteHandler)
        self.pers_totBtn.bind("<Button-1>", self.totpersHandler)
        self.salvaBtn.bind("<Button-1>", self.salvaHandler)
        self.carica_Btn.bind("<Button-1>", self.caricaHandler)
        self.esci_btn.bind("<Button-1>", self.esciHandler)
        self.istruzioniBtn.bind("<Button-1>", self.istruzioniHandler) 

        


# Handler che mostra le prenotazioni dell'hotel
   
    def mostra_prenHandler(self,event):
        
        prenotazioni = self.Hotel.get_prenotazioni()

        if len(prenotazioni) == 0:
            mostra = "Nessuna prenotazione presente."
          
        else:
            mostra = "Prenotazioni attuali:\n"
            for pren in prenotazioni:
                mostra += f"{pren}\n"

        self.text.delete("1.0", tk.END)
        self.text.insert("1.0", mostra)
        self.entry.delete(0, tk.END)


#aggiungere una prenotazione
    def pren_stanzaHandler(self, event):
        try:
            input_str = self.entry.get().strip()  
            parts = input_str.split(",")
            for i in range(len(parts)):
                parts[i] = parts[i].strip()

            if len(parts) != 5:
                raise ValueError("Formato errato. Usa: numero_stanza, data_arrivo, data_partenza, nome_cliente, numero_persone")

            numero_stanza = int(parts[0])

            arrivo_split = parts[1].split("/")
            giorno_arrivo = int(arrivo_split[0])
            mese_arrivo = int(arrivo_split[1])
            data_arrivo = Data(giorno_arrivo, mese_arrivo)

            partenza_split = parts[2].split("/")
            giorno_partenza = int(partenza_split[0])
            mese_partenza = int(partenza_split[1])
            data_partenza = Data(giorno_partenza, mese_partenza)

            nome_cliente = parts[3]
            numero_persone = int(parts[4])
            self.Hotel.prenota(numero_stanza, data_arrivo, data_partenza, nome_cliente, numero_persone)

            self.labelVar.set("Prenotazione effettuata con successo.")
            self.entry.delete(0, tk.END)

        except Exception as e:
            messagebox.showerror("Errore", str(e))


    #ottenere il prezzo di una prenotazione dato l'indice
    def prez_prenHandler(self, event):
        
        try:
            indice = int(self.entry.get().strip())

            prezzo = self.Hotel.prezzo_prenotazione(indice)
            
            self.text.delete("1.0", tk.END)
            self.text.insert("1.0", f"Prezzo prenotazione n{indice}: {prezzo} €")
            self.entry.delete(0, tk.END)
            
            
        except ValueError:
            self.root.after(250, lambda: messagebox.showerror("Errore", "Inserisci un ID numerico valido."))

        except KeyError as e:
            self.root.after(250, lambda error=e: messagebox.showerror("Errore", str(error)))


    #eliminare una prenotazione        
    def elimina_prenHandler(self, event):

        try:
            indice = int(self.entry.get().strip())
            self.Hotel.disdici(indice)

        except ValueError:
            self.root.after(250, lambda: messagebox.showerror("Errore", "Inserisci un ID numerico valido."))
            return

        except KeyError as e:
            self.root.after(250, lambda error=e: messagebox.showerror("Errore, l'ID della prenotazione non esiste", str(error)))
            return

        self.labelVar.set("Prenotazione eliminata con successo.")
        


    #mostrare l'hotel ad una certa data inserendo i nomi dei clienti nelle stanze a quella data;
    def stato_hotelHandler(self, event):
        try:
            # Ottieni la data inserita (formato: GG/MM)
            data_str = self.entry.get().strip()
            giorno_str, mese_str = data_str.split('/')
            giorno = int(giorno_str)
            mese = int(mese_str)

            # Crea oggetto Data
            data_richiesta = Data(giorno, mese)

            # Ottieni le prenotazioni attive a quella data
            prenotazioni_attive = self.Hotel.get_prenotazioni_data(data_richiesta)

            if not prenotazioni_attive:
                testo = f"Nessuna prenotazione attiva il {data_richiesta}."
            else:
                testo = f"Occupazione hotel il {data_richiesta}:\n"
                for pren in prenotazioni_attive:
                    testo += f"Stanza {pren.numero_stanza}: {pren.nome_cliente}\n"
                    

            self.text.delete("1.0", tk.END)
            self.text.insert("1.0", testo)
            self.entry.delete(0, tk.END)
            self.labelVar.set("Nomi mostrati con successo.")


        except ValueError:
            messagebox.showerror("Errore", "Inserisci la data nel formato GG/MM")
        except Exception as e:
            messagebox.showerror("Errore", str(e))



    
   # def st_libereHandler(self, event):
        

    #ottenere le prenotazioni di uno specifico cliente inserendo il nome;
    def pren_clienteHandler(self, event):
        try:
            cliente = self.entry.get().strip()  # prendo il nome cliente dall'input
            if not cliente:
                messagebox.showwarning("Attenzione", "Inserisci il nome del cliente.")
                return

            prenotazioni = self.Hotel.get_prenotazioni_cliente(cliente)

            if not prenotazioni:
                testo = f"Nessuna prenotazione trovata per il cliente '{cliente}'."
            else:
                testo = f"Prenotazioni di {cliente}:\n"
                for p in prenotazioni:
                    testo += (f"Stanza: {p.numero_stanza}, "
                            f"Arrivo: {p.data_arrivo}, "
                            f"Partenza: {p.data_partenza}\n")
                           
            self.text.delete("1.0", tk.END)
            self.text.insert("1.0", testo)
            self.entry.delete(0, tk.END)
            self.labelVar.set("prenotazioni ottenute con successo.")

        except Exception as e:
            messagebox.showwarning("Errore", f"Errore durante la ricerca: {e}")

    
    #numero di persone nell'albergo ad una certa data;
    def totpersHandler(self, event):

        try:
            # Ottieni la data dal campo di input
            data_str = self.entry.get().strip()
            giorno_str, mese_str = data_str.split('/')
            giorno = int(giorno_str)
            mese = int(mese_str)

            # Crea oggetto Data
            data_richiesta = Data(giorno, mese)

            # Chiama il metodo dell'Hotel per ottenere il numero di persone
            num_persone = self.Hotel.get_numero_persone_data(data_richiesta)

            # Mostra il risultato
            self.text.delete("1.0", tk.END)
            self.text.insert("1.0",f"Numero di persone presenti in hotel il  {data_richiesta}: {num_persone}")
            self.entry.delete(0, tk.END)
            self.labelVar.set("numero di persone presenti nell'albergo mostrate con successo")

   

        except ValueError:
            messagebox.showerror("Errore", "Inserisci la data nel formato GG/MM")
        except Exception as e:
            messagebox.showerror("Errore", str(e))



    #salvare il file 
    def salvaHandler(self, event):
        nomefile = self.entry.get().strip()
        if not nomefile:
            messagebox.showwarning("Attenzione", "Inserisci il nome del file per salvare.")
            return
        
        if not nomefile.endswith(".txt"):
            nomefile += ".txt"
        try:
            self.Hotel.salva(nomefile)
            self.entry.delete(0, tk.END)
            self.labelVar.set("File salvato con successo.")
        except IOError as e:
            self.root.after(250, lambda error=e: messagebox.showerror("Errore salva file", str(error)))



    def caricaHandler(self, event):
        nomefile = self.entry.get().strip()
        if not nomefile:
            messagebox.showwarning("Attenzione", "Inserisci il nome del file da caricare.")
            return
        try:
            # Carica i dati dell'hotel (stanze, prenotazioni, ecc.)
            self.Hotel.carica(nomefile)

            self.entry.delete(0, tk.END)

            self.text.delete("1.0", tk.END)

            # Apri e leggi il file per mostrarlo nel Text widget
            with open(nomefile, "r", encoding="utf-8") as f:
                contenuto = f.read()
                self.text.insert("1.0", contenuto)

            self.labelVar.set("File caricato con successo.")

                
        except FileNotFoundError:
            messagebox.showerror("Errore", f"File '{nomefile}' non trovato.")
        except ValueError:
            messagebox.showerror("Errore", "Errore nel contenuto del file.")
        except TypeError:
            messagebox.showerror("Errore", "Errore di tipo nei dati del file.")


    #Handler per le istruzioni con message box
    def istruzioniHandler(self, event):
        root.after(250, lambda :messagebox.showinfo("Istruzioni", "Prenotare Stanza: numero stanza, data arrivo, data partenza, nome cliente, numero persone es: 101, 1/2, 1/5, Mario, 5 \n\n Disdire Prenotazione: inserire numero prenotazione \n\n Prezzo Prenotazioni: inserire il numero della prenotazione \n\n Hotel a data: inserire la data nel formato GG/MM  \n\n Prenotazione Cliente: inserire il nome del cliente per sapere quando ha prenotato \n\n Num persone tot: inserire data GG/MM per sapere il numero delle persone presenti in Hotel in una certa data \n\n Salva: inserire nome file per salvare \n\n Carica: inserire il nome del file per caricare \n\n esci: cliccare il pulsante per uscire dall'applicazione "))

    #uscire
    def esciHandler(self, event):
        risposta = messagebox.askyesno("Conferma uscita", "Vuoi davvero uscire dall'applicazione?")
        if risposta:
            self.root.destroy()

HotelGUI(root)

#meccanismo di ascolto degli eventi esterni
root.mainloop()

