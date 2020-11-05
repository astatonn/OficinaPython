def verb_to_be(noum):

  excecao = ['I']
  plural = ['You', 'They', 'We']
  Singular = ['He', 'She', 'It']

  if noum in excecao:
    return noum + ' am'
  elif noum in Singular:
    return noum + ' is'
  elif noum in plural:
    return noum + ' are'
  else:
    return 'Pronome Desconhecido' 

