def valida(cadena):
    retorno = True
    for i in cadena.upper():
        if "ACGT ".count(i.upper()) == 0:
            retorno = False
    return retorno