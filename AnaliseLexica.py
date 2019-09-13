import re
import sys
argumento = sys.argv
numeroLinha = 0
numeroColuna = 0

arquivo = open(argumento[1], 'r')
leitura = arquivo.readlines()
linhasdecomando = []
tokens = []

variavel = ""
modoTexto = False

for line in leitura:
    if not re.search("\"", line):
        line = line.strip().split(' ')
    else:
        line = line.strip().split(' ')
        posicao = 0

        for palavra in line:
            if palavra.startswith("\""):
                modoTexto = True
                posicao = line.index(palavra)
                variavel = variavel + palavra
                line.remove(palavra)

        while modoTexto:
            for palavra in line:
                if line.index(palavra) > posicao:

                    if palavra.endswith("\""):
                        variavel = variavel + " " + palavra
                        modoTexto = False
                        line.remove(palavra)

                    else:
                        line.remove(palavra)
                        variavel = variavel + " " + palavra
                    break

        line.insert(posicao, variavel)


    linhasdecomando.append(line)

for linha in linhasdecomando:
    numeroLinha += 1
    for lexema in linha:
        numeroColuna = linha.index(lexema)
        if lexema:
            if re.match("[\".+?\"]+", lexema):
                tokens.append(['string', lexema, numeroLinha, numeroColuna])
            elif re.match("[a-zA-Z]+", lexema):
                if lexema == 'tchapa':
                    tokens.append(['tk_topo', lexema, numeroLinha, numeroColuna])
                elif lexema == 'cruz':
                    tokens.append(['tk_rodape', lexema, numeroLinha, numeroColuna])
                elif lexema == 'enquanto':
                    tokens.append(['tk_enquanto', lexema, numeroLinha, numeroColuna])
                elif lexema == 'leia':
                    tokens.append(['tk_entra', lexema, numeroLinha, numeroColuna])
                elif lexema == 'ixpia':
                    tokens.append(['tk_sai', lexema, numeroLinha, numeroColuna])
                elif lexema == 'int':
                    tokens.append(['tk_int', lexema, numeroLinha, numeroColuna])
                elif lexema == 'agora':
                    tokens.append(['tk_se', lexema, numeroLinha, numeroColuna])
                elif lexema == 'agoraquando':
                    tokens.append(['tk_senao', lexema, numeroLinha, numeroColuna])
                else:
                    tokens.append(['tk_variavel', lexema, numeroLinha, numeroColuna])

            elif re.match("-[0-9]", lexema): \
                    tokens.append(['tk_numeroNeg', lexema, numeroLinha, numeroColuna])
            elif re.match("[0-9]", lexema):
                tokens.append(['tk_numeroPos', lexema, numeroLinha, numeroColuna])

            elif re.match("[= | > | < | ; | # | <> | ( | ) | [ | \] |\- | + | ++ |* |/ |\--]", lexema):
                if (lexema == '='):
                    tokens.append(['tk_igual', lexema, numeroLinha, numeroColuna])
                elif (lexema == '>'):
                    tokens.append(['tk_maior', lexema, numeroLinha, numeroColuna])
                elif (lexema == '<'):
                    tokens.append(['tk_menor', lexema, numeroLinha, numeroColuna])
                elif (lexema == ';'):
                    tokens.append(['tk_fim', lexema, numeroLinha, numeroColuna])
                elif (lexema == '#'):
                    tokens.append(['tk_comparar', lexema, numeroLinha, numeroColuna])
                elif (lexema == '<>'):
                    tokens.append(['tk_diferente', lexema, numeroLinha, numeroColuna])
                elif (lexema == '('):
                    tokens.append(['tk_abre', lexema, numeroLinha, numeroColuna])
                elif (lexema == ')'):
                    tokens.append(['tk_fecha', lexema, numeroLinha, numeroColuna])
                elif (lexema == '['):
                    tokens.append(['tk_blocoi', lexema, numeroLinha, numeroColuna])
                elif (lexema == ']'):
                    tokens.append(['tk_blocof', lexema, numeroLinha, numeroColuna])
                elif (lexema == '++'):
                    tokens.append(['tk_incremento', lexema, numeroLinha, numeroColuna])
                elif (lexema == '+'):
                    tokens.append(['tk_adicao', lexema, numeroLinha, numeroColuna])
                elif (lexema == '--'):
                    tokens.append(['tk_decremento', lexema, numeroLinha, numeroColuna])
                elif (lexema == '-'):
                    tokens.append(['tk_subtracao', lexema, numeroLinha, numeroColuna])
                elif (lexema == '/'):
                    tokens.append(['tk_divisao', lexema, numeroLinha, numeroColuna])
                elif (lexema == '*'):
                    tokens.append(['tk_multiplicacao', lexema, numeroLinha, numeroColuna])
            else:
                tokens.append(['Erro lexico', lexema, numeroLinha, numeroColuna])

for mostra in tokens:
    if argumento[2] == '-lt':
        print(mostra)

