import os
import pandas as pd 
import sys


# CAMINHO PARA SALVAR O ARQUIVO
SPatch = r"C:\Users\Admin\Desktop\data csv"

# V2.0


# PARTIÇÃO PARA LEITURA DE CAMINHO E FORMATAÇÃO
# LEITURA DO CAMINHO TXT
user_input = input ("Enter the path of your txt file: ")
check_enter = os.path.exists(user_input)

# MENSAGEM DE ERRO CASO O ARQUIVO NÃO EXISTA
if  check_enter is True:

    # LEIURA DO CAMINHO DESTINO
    user_output = input ("Enter the destination folder: ")
    Aux_user_output = len(str(user_output))

    # VERIFICAÇÃO SE O ÚLTIMO CARACTER É BARRA INVERTIDA PARA ADCIONAR OU NÃO A BARRA
    if str (user_output)[Aux_user_output-1] == "\\": 
        file_name = input ("Enter the file name: ")
        Aux = str(user_output) + str (file_name) + ".csv"
        # METODOS PARA DEFINIR OS ARQUIVOS DE ENTRADA E SAIDA


        in_filename = os.path.join(SPatch,user_input)
        out_filename = os.path.join(SPatch,Aux)


        print ('============WORKING============')
    # LEITURA DO ARQUIVO TXT SEPARANDO POR VÍRGURA
        df = pd.read_csv(in_filename, sep=",")
    # MÉTODO PARA CONVERSÃO PARA CSV
        df.to_csv(out_filename, index=False)
        print ('============SUCESSFULL============')
    else:
        print ("PLEASE, ENTER THE DESTINATION FOLDER WITH \\")

    # FIM DA PARTIÇÃO PARA LEITURA DE CAMINHO E FORMATAÇÃO   
else:
    print("I did not find the file at, "+str(user_input))


# END OF V2.0
