def busca_linear(lista,alvo):
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
        return -1
lista = [3,6,7,10,4,12,9,5,8]

alvo = 12

busca_linear (lista, alvo)
