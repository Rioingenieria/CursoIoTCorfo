def codigo_palabra(n):
  i = 1
  nueva = ''
  while i <= len(n):
    nueva += n[-i]
    i += 2
  return nueva