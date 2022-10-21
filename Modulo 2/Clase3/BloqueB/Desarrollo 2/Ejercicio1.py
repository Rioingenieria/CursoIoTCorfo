def cadena_adn(n):
    from random import choice

    adn = ""
    for i in range(n):
        adn += choice('atcg')
    return adn

dato=int(input("Ingrese largo: "))
print(cadena_adn(dato))
