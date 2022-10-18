def invertir_digitos(n):
	final = ''
	while n > 0:
		d = n % 10
		n = n // 10
		final += str(d)
	return int(final)