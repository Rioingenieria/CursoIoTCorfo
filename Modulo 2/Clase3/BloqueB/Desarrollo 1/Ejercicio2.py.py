def complementaria(c):
  print("cadena =", c)
  complement = c.replace('a','T').replace('t','A').replace('c','G').replace('g','C').lower()
  print("complementaria =", complement)