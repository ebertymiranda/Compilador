import re
import sys
argumento = sys.argv
numeroLinha = 0
numeroColuna = 0

arquivo = open('fatorial.txt', 'r')
leitura = arquivo.readlines()
linhasdecomando = []
tokens = []
copy = []
erro = []
lexemas = []

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
            #if re.match("[\".+?\"]+", lexema):
            #    tokens.append(['string', lexema, numeroLinha, numeroColuna])
            #    copy.append('string')
                
            if re.match("[a-zA-Z]+", lexema):
                if lexema == 'tchapa':
                    tokens.append(['tk_topo', lexema, numeroLinha, numeroColuna])
                    copy.append('tk_topo')
                    lexemas.append(lexema)
                elif lexema == 'cruz':
                    tokens.append(['tk_rodape', lexema, numeroLinha, numeroColuna])
                    copy.append('tk_rodape')
                    lexemas.append(lexema)
                elif lexema == 'enquanto':
                    tokens.append(['tk_enquanto', lexema, numeroLinha, numeroColuna])
                    copy.append('tk_enquanto')
                    lexemas.append(lexema)
                elif lexema == 'leia':
                    tokens.append(['tk_entra', lexema, numeroLinha, numeroColuna])
                    copy.append('tk_entra')
                    lexemas.append(lexema)
                elif lexema == 'ixpia':
                    tokens.append(['tk_sai', lexema, numeroLinha, numeroColuna])
                    copy.append('tk_sai')
                    lexemas.append(lexema)
                elif lexema == 'int':
                    tokens.append(['tk_int', lexema, numeroLinha, numeroColuna])
                    copy.append('tk_int')
                    lexemas.append(lexema)
                elif lexema == 'agora':
                    tokens.append(['tk_se', lexema, numeroLinha, numeroColuna])
                    copy.append('tk_se')
                    lexemas.append(lexema)
                elif lexema == 'agoraquando':
                    tokens.append(['tk_senao', lexema, numeroLinha, numeroColuna])
                    copy.append('tk_senao')
                    lexemas.append(lexema)
                else:
                    tokens.append(['tk_variavel', lexema, numeroLinha, numeroColuna])
                    copy.append('tk_variavel')
                    lexemas.append(lexema)
                   
            elif re.match("-[0-9]", lexema): 
                tokens.append(['tk_numneg', lexema, numeroLinha, numeroColuna])
                copy.append('tk_numneg')
                lexemas.append(lexema)
            elif re.match("[0-9]", lexema):
                tokens.append(['tk_numpos', lexema, numeroLinha, numeroColuna])
                copy.append('tk_numpos')
                lexemas.append(lexema)

            elif re.match("[= | > | < | ; | # | <> | ( | ) | [ | \] |\- |\\+ |\\++ |* |/ |\--]", lexema):
                if (lexema == '='):
                    tokens.append(['tk_igual', lexema, numeroLinha, numeroColuna])
                    copy.append('tk_igual')
                    lexemas.append(lexema)
                elif (lexema == '>'):
                    tokens.append(['tk_maior', lexema, numeroLinha, numeroColuna])
                    copy.append('tk_maior')
                    lexemas.append(lexema)
                elif (lexema == '<'):
                    tokens.append(['tk_menor', lexema, numeroLinha, numeroColuna])
                    copy.append('tk_menor')
                    lexemas.append(lexema)
                elif (lexema == ';'):
                    tokens.append(['tk_fim', lexema, numeroLinha, numeroColuna])
                    copy.append('tk_fim')
                    lexemas.append(lexema)
                elif (lexema == '#'):
                    tokens.append(['tk_comparar', lexema, numeroLinha, numeroColuna])
                    copy.append('tk_comparar')
                    lexemas.append(lexema)
                elif (lexema == '<>'):
                    tokens.append(['tk_diferente', lexema, numeroLinha, numeroColuna])
                    copy.append('tk_diferente')
                    lexemas.append(lexema)
                elif (lexema == '('):
                    tokens.append(['tk_abre', lexema, numeroLinha, numeroColuna])
                    copy.append('tk_abre')
                    lexemas.append(lexema)
                elif (lexema == ')'):
                    tokens.append(['tk_fecha', lexema, numeroLinha, numeroColuna])
                    copy.append('tk_fecha')
                    lexemas.append(lexema)
                elif (lexema == '['):
                    tokens.append(['tk_blocoi', lexema, numeroLinha, numeroColuna])
                    copy.append('tk_blocoi')
                    lexemas.append(lexema)
                elif (lexema == ']'):
                    tokens.append(['tk_blocof', lexema, numeroLinha, numeroColuna])
                    copy.append('tk_blocof')
                    lexemas.append(lexema)
                elif (lexema == '++'):
                    tokens.append(['tk_incremento', lexema, numeroLinha, numeroColuna])
                    copy.append('tk_incremento')
                    lexemas.append(lexema)
                elif (lexema == '+'):
                    tokens.append(['tk_adicao', lexema, numeroLinha, numeroColuna])
                    copy.append('tk_adicao')
                    lexemas.append(lexema)
                elif (lexema == '--'):
                    tokens.append(['tk_decremento', lexema, numeroLinha, numeroColuna])
                    copy.append('tk_decremento')
                    lexemas.append(lexema)
                elif (lexema == '-'):
                    tokens.append(['tk_subtracao', lexema, numeroLinha, numeroColuna])
                    copy.append('tk_subtracao')
                    lexemas.append(lexema)
                elif (lexema == '/'):
                    tokens.append(['tk_divisao', lexema, numeroLinha, numeroColuna])
                    copy.append('tk_divisao')
                    lexemas.append(lexema)
                elif (lexema == '*'):
                    tokens.append(['tk_multiplicacao', lexema, numeroLinha, numeroColuna])
                    copy.append('tk_multiplicacao')
                    lexemas.append(lexema)
            else:
                erro.append(['Erro lexico', lexema, numeroLinha, numeroColuna])
                print(erro)
                break
            
            
print('Analise Lexica concluida sem erros')