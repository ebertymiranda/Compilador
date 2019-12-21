import AnaliseLexica
cont = 0
lexema = AnaliseLexica.lexemas
token = AnaliseLexica.copy
variaveis = {}
log = []
argumento = AnaliseLexica.argumento

for i in token:
    cont += 1
    if i == 'tk_int':
        if token[cont] == 'tk_variavel' and token[cont + 1] == 'tk_igual':
            if lexema[cont] in variaveis.keys():
                log.append('Variavel ' + lexema[cont] + ' já foi declarada')
                
                break
            else:
                variaveis.update({lexema[cont]: lexema[cont + 2]})
                log.append('Variavel ' + lexema[cont] + ' declarada com o valor ' + variaveis.get(lexema[cont]))

    if i == 'tk_divisao':
        if variaveis.get(lexema[cont]) or lexema[cont] == '0':
            log.append('Ocorreu uma divisao por zero')
            
            break
                
    if i == 'tk_variavel': 
        if lexema[cont - 1] in variaveis.keys() and not token[cont - 2] == 'tk_int' and token[cont + 1] == 'tk_igual':    
            variaveis.update({lexema[cont - 1]: lexema[cont + 1]})
        if lexema[cont - 1] not in variaveis.keys():
            log.append('Variavel ' + lexema[cont - 1] + ' não foi declarada')
            
            break





    