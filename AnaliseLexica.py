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
        numeroColuna = linha.index(coluna)
        

        if re.search("[a-zA-Z]", coluna):
            
            if (coluna == 'tchpa'):
                tokens.append(['tk_topo', coluna, numeroLinha, numeroColuna])
            if (coluna == 'cruz'):
                tokens.append(['tk_rodape', coluna, numeroLinha, numeroColuna])
            if (coluna == 'enquanto'):
                tokens.append(['tk_enquanto', coluna, numeroLinha, numeroColuna])
            if (coluna == 'leia'):
                tokens.append(['tk_entra',  coluna, numeroLinha, numeroColuna])
            if (coluna == 'ixpia'):
                tokens.append(['tk_sai', coluna, numeroLinha, numeroColuna])
            if (coluna == 'int'):
                tokens.append(['tk_int', coluna, numeroLinha, numeroColuna])
            if (coluna == 'agora'):
                tokens.append(['tk_se', coluna, numeroLinha, numeroColuna])
            if (coluna == 'agoraquando'):
                tokens.append(['tk_senao', coluna, numeroLinha, numeroColuna])


        elif re.search("[0-9]", coluna):
            tokens.append('tk_numeroPos')
        elif re.search("-[0-9]", coluna):
            tokens.append('tk_numeroNeg')
        elif re.search("[= | > | < | ; | # | <> | ( | ) | [ | \] |\- | + | ++ |\--]", coluna):
            if(coluna == '='):
                tokens.append(['tk_igual', coluna, numeroLinha, numeroColuna])
            if(coluna == '>'):
                tokens.append(['tk_maior', coluna, numeroLinha, numeroColuna])
            if(coluna == '<'):
                tokens.append(['tk_menor', coluna, numeroLinha, numeroColuna])
            if(coluna == ';'):
                tokens.append(['tk_fim', coluna, numeroLinha, numeroColuna])
            if(coluna == '#'):
                tokens.append(['tk_comparar', coluna, numeroLinha, numeroColuna])
            if(coluna == '<>'):
                tokens.append(['tk_diferente', coluna, numeroLinha, numeroColuna])
            if(coluna == '('):
                tokens.append(['tk_abre', coluna, numeroLinha, numeroColuna])
            if(coluna == ')'):
                tokens.append(['tk_fecha', coluna, numeroLinha, numeroColuna])
            if(coluna == '['):
                tokens.append(['tk_blocoi', coluna, numeroLinha, numeroColuna])
            if(coluna == ']'):
                tokens.append(['tk_blocof', coluna, numeroLinha, numeroColuna])
            if(coluna == '++'):
                tokens.append(['tk_incremento', coluna, numeroLinha, numeroColuna])
            if(coluna == '+'):
                tokens.append(['tk_adicao', coluna, numeroLinha, numeroColuna])
            if(coluna == '--'):
                tokens.append(['tk_decremento', coluna, numeroLinha, numeroColuna])
            if(coluna == '-'):
                tokens.append(['tk_subtracao', coluna, numeroLinha, numeroColuna])
            if(coluna == '/'):
                 tokens.append(['tk_divisao', coluna, numeroLinha, numeroColuna])
            if(coluna == '*'):
                tokens.append(['tk_multiplicacao', coluna, numeroLinha, numeroColuna])

        #elif coluna.startswith("\"") == True:
        #    numeroColuna = linha.index(coluna)
        #    modoTexto = True
        #    variavel = variavel + " " + coluna
        
        #    while modoTexto:
        #        if coluna.endswith("\""):
        #            variavel = variavel + " " + coluna
        #            modoTexto = False
        #        else:
        #            variavel = variavel + coluna
        #            numeroColuna += 1
        #tokens.append("string")
print(tokens)
        

