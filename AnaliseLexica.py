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
        if re.search(r'\"(.+?)\"', lexema):
            tokens.append(['string', lexema, numeroLinha, numeroColuna])
        else:

            if re.search("[a-zA-Z]", lexema):

                if (lexema == 'tchpa'):
                    tokens.append(['tk_topo', lexema, numeroLinha, numeroColuna])
                else:
                    if (lexema == 'cruz'):
                        tokens.append(['tk_rodape', lexema, numeroLinha, numeroColuna])
                    else:
                        if (lexema == 'enquanto'):
                            tokens.append(['tk_enquanto', lexema, numeroLinha, numeroColuna])
                        else:
                            if (lexema == 'leia'):
                                tokens.append(['tk_entra', lexema, numeroLinha, numeroColuna])
                            else:
                                if (lexema == 'ixpia'):
                                    tokens.append(['tk_sai', lexema, numeroLinha, numeroColuna])
                                else:
                                    if (lexema == 'int'):
                                        tokens.append(['tk_int', lexema, numeroLinha, numeroColuna])
                                    else:
                                        if (lexema == 'agora'):
                                            tokens.append(['tk_se', lexema, numeroLinha, numeroColuna])
                                        else:
                                            if (lexema == 'agoraquando'):
                                                tokens.append(['tk_senao', lexema, numeroLinha, numeroColuna])
                                            else:

                                                if lexema not in palavrasreservadas:
                                                    tokens.append(['tk_variavel', lexema, numeroLinha, numeroColuna])



            elif re.search("-[0-9]", lexema):
                tokens.append(['tk_numeroNeg', lexema, numeroLinha, numeroColuna])
            elif re.search("[0-9]", lexema):
                tokens.append(['tk_numeroPos', lexema, numeroLinha, numeroColuna])
            elif re.search("[= | > | < | ; | # | <> | ( | ) | [ | \] |\- | + | ++ |* |/ |\--]", lexema):
                if(lexema == '='):
                    tokens.append(['tk_igual', lexema, numeroLinha, numeroColuna])
                else:
                    if(lexema == '>'):
                        tokens.append(['tk_maior', lexema, numeroLinha, numeroColuna])
                    else:
                        if(lexema == '<'):
                            tokens.append(['tk_menor', lexema, numeroLinha, numeroColuna])
                        else:
                            if(lexema == ';'):
                                tokens.append(['tk_fim', lexema, numeroLinha, numeroColuna])
                            else:
                                if(lexema == '#'):
                                    tokens.append(['tk_comparar', lexema, numeroLinha, numeroColuna])
                                else:
                                    if(lexema == '<>'):
                                        tokens.append(['tk_diferente', lexema, numeroLinha, numeroColuna])
                                    else:
                                        if(lexema == '('):
                                            tokens.append(['tk_abre', lexema, numeroLinha, numeroColuna])
                                        else:
                                            if(lexema == ')'):
                                                tokens.append(['tk_fecha', lexema, numeroLinha, numeroColuna])
                                            else:
                                                if(lexema == '['):
                                                    tokens.append(['tk_blocoi', lexema, numeroLinha, numeroColuna])
                                                else:
                                                    if(lexema == ']'):
                                                        tokens.append(['tk_blocof', lexema, numeroLinha, numeroColuna])
                                                    else:
                                                        if(lexema == '++'):
                                                            tokens.append(['tk_incremento', lexema, numeroLinha, numeroColuna])
                                                        else:
                                                            if(lexema == '+'):
                                                                tokens.append(['tk_adicao', lexema, numeroLinha, numeroColuna])
                                                            else:
                                                                if(lexema == '--'):
                                                                    tokens.append(['tk_decremento', lexema, numeroLinha, numeroColuna])
                                                                else:
                                                                    if(lexema == '-'):
                                                                        tokens.append(['tk_subtracao', lexema, numeroLinha, numeroColuna])
                                                                    else:
                                                                        if(lexema == '/'):
                                                                             tokens.append(['tk_divisao', lexema, numeroLinha, numeroColuna])
                                                                        else:
                                                                            if(lexema == '*'):
                                                                                tokens.append(['tk_multiplicacao', lexema, numeroLinha, numeroColuna])
            else:
                tokens.append(['erro lexico' ,lexema, numeroLinha, numeroColuna])


for printa in tokens:
    print(printa)

