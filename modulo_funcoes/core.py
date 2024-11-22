def somaLista(valores=[]):
    """
    A função somaLista, recebe uma lista de números e
    faz a soma de todos os números da lista e retorna
    o resultado da soma.

    Parameters
    ------------
    valores: int[]
        Lista de números para soma

    Returns
    ------------
        Retorna a soma de uma lista
    """

    resultado = 0
    for i in valores:
        resultado+=i

    return resultado

def maiorValor(lista=()):
    """
    A função maiorValor encontra o maoir valor
    em uma lista numérica.
      
    Paremeters
    ----------
    lista: int[]

    return
    ----------
      Retorna o maior valor lista      
    """
    m = lista[0]
    for i in lista:
        if i > m:
            m = i

    return m

def inverter(palavra=""):
    # Vamos utilizar o comando len(length-comprimento) pata obter
    # a quantidade de caracteres da palavra
    qtd = len(palavra)
    invertida = ""
    for i in range(qtd-1,-1,-1):
        invertida+=palavra[i]
    return invertida

def palindromo(palavra=""):
    org = inverter(palavra).lower()
    if palavra.lower()==org:
        return "É um palindromo"
    else:
        return "Não é um palindromo"