import re

numeroLinha = 0
numeroColuna = 0

arquivo = open('fatorial.txt', 'r')
leitura = arquivo.readlines()
linhasdecomando = []
tokens = []


variavel = " "
modoTexto = False


for line in leitura:
    line = line.strip().split(' ')
    linhasdecomando.append(line)

for linha in linhasdecomando:
    numeroLinha += 1
    for lexema in linha:
        numeroColuna = linha.index(lexema)

        #if lexema.startswith("\"") == True:
        #    numeroColuna = linha.index(lexema)
        #    modoTexto = True
        #    variavel = variavel + " " + lexema

        #    while modoTexto:
        #       if lexema.endswith("\""):
        #           variavel = variavel + " " + lexema

        #           modoTexto = False
        #       else:
        #           variavel = variavel + " " + lexema
        #           numeroColuna += 1
        #           tokens.append(["tk_string", variavel, numeroLinha, numeroColuna])
        #else:
        if re.match("[A\"\.\"\b]+", lexema):
            tokens.append(['tk_string', lexema, numeroLinha, numeroColuna])
        elif re.match("[a-zA-Z]+", lexema):
                if (lexema == 'tchpa'):
                    tokens.append(['tk_topo', lexema, numeroLinha, numeroColuna])
                elif (lexema == 'cruz'):
                    tokens.append(['tk_rodape', lexema, numeroLinha, numeroColuna])
                elif (lexema == 'enquanto'):
                    tokens.append(['tk_enquanto', lexema, numeroLinha, numeroColuna])
                elif (lexema == 'leia'):
                    tokens.append(['tk_entra', lexema, numeroLinha, numeroColuna])
                elif (lexema == 'ixpia'):
                    tokens.append(['tk_sai', lexema, numeroLinha, numeroColuna])
                elif (lexema == 'int'):
                    tokens.append(['tk_int', lexema, numeroLinha, numeroColuna])
                elif (lexema == 'agora'):
                    tokens.append(['tk_se', lexema, numeroLinha, numeroColuna])
                elif (lexema == 'agoraquando'):
                    tokens.append(['tk_senao', lexema, numeroLinha, numeroColuna])
                else:
                    tokens.append(['tk_variavel', lexema, numeroLinha, numeroColuna])




        elif re.match("-[0-9]", lexema):
                tokens.append(['tk_numeroNeg', lexema, numeroLinha, numeroColuna])
        elif re.match("[0-9]", lexema):
            tokens.append(['tk_numeroPos', lexema, numeroLinha, numeroColuna])
        elif re.match("[= | > | < | ; | # | <> | ( | ) | [ | \] |\- | + | ++ |* |/ | . |\--]", lexema):
            if(lexema == '='):
                tokens.append(['tk_igual', lexema, numeroLinha, numeroColuna])
            elif(lexema == '>'):
                tokens.append(['tk_maior', lexema, numeroLinha, numeroColuna])
            elif(lexema == '<'):
                tokens.append(['tk_menor', lexema, numeroLinha, numeroColuna])
            elif(lexema == ';'):
                tokens.append(['tk_fim', lexema, numeroLinha, numeroColuna])
            elif(lexema == '#'):
                tokens.append(['tk_comparar', lexema, numeroLinha, numeroColuna])
            elif(lexema == '<>'):
                tokens.append(['tk_diferente', lexema, numeroLinha, numeroColuna])
            elif(lexema == '('):
                tokens.append(['tk_abre', lexema, numeroLinha, numeroColuna])
            elif(lexema == ')'):
                tokens.append(['tk_fecha', lexema, numeroLinha, numeroColuna])
            elif(lexema == '['):
                tokens.append(['tk_blocoi', lexema, numeroLinha, numeroColuna])
            elif(lexema == ']'):
                tokens.append(['tk_blocof', lexema, numeroLinha, numeroColuna])
            elif(lexema == '++'):
                tokens.append(['tk_incremento', lexema, numeroLinha, numeroColuna])
            elif(lexema == '+'):
                tokens.append(['tk_adicao', lexema, numeroLinha, numeroColuna])
            elif(lexema == '--'):
                tokens.append(['tk_decremento', lexema, numeroLinha, numeroColuna])
            elif(lexema == '-'):
                tokens.append(['tk_subtracao', lexema, numeroLinha, numeroColuna])
            elif(lexema == '/'):
                tokens.append(['tk_divisao', lexema, numeroLinha, numeroColuna])
            elif(lexema == '*'):
                tokens.append(['tk_multiplicacao', lexema, numeroLinha, numeroColuna])
        else:
            tokens.append(['Erro lexico', lexema, numeroLinha, numeroColuna])


for printa in tokens:
    print(printa)

