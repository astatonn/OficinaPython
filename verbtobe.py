def verb_to_be(noum):

        excecao = ['I']
        plural = ['You', 'They', 'We']
        Singular = ['He', 'She', 'It']

        if noum in excecao:
            print (noum + ' am')
        elif noum in Singular:
            print (noum + ' is')
        elif noum in plural:
            print (noum + ' are')
        else:
            print ('Pronome Desconhecido')

verb_to_be('I')
verb_to_be('You')
verb_to_be('She')