
# funzione  con lista invitati e stampa gli invitati

lista1 = ['mario', 'luigi', 'giovanni']

def invitati (lista1):

    nomi = ''

    for i in lista1:
        nomi+= i + '\n'
    return nomi


print(invitati(lista1))



#solo numeri che hanno indice pari

list= ['mario', 'luigi', 'giovanni']

def pari (list):

    risultato = []

    for i in range(len(list)):
        if i % 2 == 0:
            risultato.append(list[i])
    return risultato

print(pari(list))



lista1 = ['mario', 'luigi', 'giovanni']
#stampare la funzione su un foglio



def invitati (lista1, nomefile):

    with open(nomefile, 'w') as f:

        for elemento in lista1:
            f.write(elemento + '\n')
        return True

print(invitati(lista1,'prova.txt'))























