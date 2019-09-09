import re

numeroLinha = 0
numeroColuna = 0

arquivo = open('fatorial.txt', 'r')
leitura = arquivo.readlines()
linhasdecomando = []
tokens = []
variavel = " "
modoTexto = False


palavrasreservadas = ['int', 'agora', 'agoraquando', 'enquanto', 'tchapa', 'cruz', 'leia', 'ixpia']

for line in leitura:
    line = line.strip().split(' ')
    linhasdecomando.append(line)

for linha in linhasdecomando:
    numeroLinha += 1
    for coluna in linha:
        numeroColuna += 1

        if re.search("[a-zA-Z]", coluna):
            if coluna not in palavrasreservadas:
               tokens.append('tk_variavel')
            if 'tchapa' == coluna:
                tokens.append('tk_topo')
            if 'cruz' == coluna:
                tokens.append('tk_rodape')
            if 'enquanto' == coluna:
                tokens.append('tk_enquanto')
            if 'leia' == coluna:
                tokens.append('tk_entra')
            if 'ixpia' == coluna:
                tokens.append('tk_sai')
            if 'int' == coluna:
                tokens.append('tk_int')
            if 'agora' == coluna:
                tokens.append('tk_se')
            if 'agoraquando' == coluna:
                tokens.append('tk_senao')


        elif re.search("[0-9]", coluna):
            tokens.append('tk_numeroPos')
        elif re.search("-[0-9]", coluna):
            tokens.append('tk_numeroNeg')
        elif re.search("[= | > | < | ; | # | <> | ( | ) | [ | \] |\- | + | ++ |\--]", coluna):
            if(coluna == '='):
                tokens.append('tk_igual')
            if(coluna == '>'):
                tokens.append('tk_maior')
            if(coluna == '<'):
                tokens.append('tk_menor')
            if(coluna == ';'):
                tokens.append('tk_fim')
            if(coluna == '#'):
                tokens.append('tk_comparar')
            if(coluna == '<>'):
                tokens.append('tk_diferente')
            if(coluna == '('):
                tokens.append('tk_abre')
            if(coluna == ')'):
                tokens.append('tk_fecha')
            if(coluna == '['):
                tokens.append('tk_blocoi')
            if(coluna == ']'):
                tokens.append('tk_blocof')
            if(coluna == '++'):
                tokens.append('tk_incremento')
            if(coluna == '+'):
                tokens.append('tk_adicao')
            if(coluna == '--'):
                tokens.append('tk_decremento')
            if(coluna == '-'):
                tokens.append('tk_subtração')

        elif coluna.startswith("\"") == True:
            numeroColuna = linha.index(coluna)
            modoTexto = True
            variavel += " " + coluna
            while modoTexto:
                if coluna.endswith("\""):
                    variavel += coluna
                    modoTexto = False
                else:
                    variavel += coluna
                    numeroColuna += 1
print(tokens)







