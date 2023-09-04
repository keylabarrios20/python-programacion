def insertarNumero():
    lista=[]
    while True:
        n=int(input("Ingresar un numero (0 terminar):"))
        if n==0:
            return lista
        else:
            lista.append(n)
def ordenPorInsercion(lista):
    pos=0
    i=0
    aux=0
    for _ in lista:
        pos=i
        aux=lista[i]
        while pos>0 and lista[pos-1]>aux: 
            lista[pos]=lista[pos-1]
            pos=pos-1
        lista[pos]=aux
        i=i+1
    return lista
def mostrarlista(lista):
    for numero in lista:
        print(numero)
lista=insertarNumero()
lista=ordenPorInsercion(lista)
print("Aqui esta la lista ordenada por insercion")
mostrarlista(lista)
