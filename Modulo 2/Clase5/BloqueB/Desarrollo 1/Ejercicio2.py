pais = {
    'juan': {'chile', 'argentina'},
    'pedro': {'francia', 'suiza', 'chile'},
    'diego': {'chile', 'italia', 'francia', 'peru'}
}

def cuantos_en_comun(a, b):
    return len(pais[a] & pais[b])
print(cuantos_en_comun('diego', 'pedro'))
