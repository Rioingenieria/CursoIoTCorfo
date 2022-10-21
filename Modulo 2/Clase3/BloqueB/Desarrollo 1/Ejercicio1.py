from random import choice
def cadena_al_azar(n): 
	i = 0
	final = ''
	while i < n: 
		final += choice('acgt')
		i += 1
	return final
