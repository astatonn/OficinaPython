# FAÇA UM PROGRAMA QUE UMA QUANTIDADE DINÂMICA DE NOTAS E MOSTRA A MÉDIA DOS VALORES
nota=[]
media=0
while True:
    nota.append(float(input('Digite a nota: ')))
    opcao=input('Deseja continuar? (yes|no)').lower()
    if opcao == 'no':
        break
for i in range (0,len(nota)):
    media=media+nota[i]
print ('A média é: {}'.format(media/len(nota)))
