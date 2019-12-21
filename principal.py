import AnaliseLexica
import AnaliseSintatica
import AnaliseSemantica

argumento = AnaliseLexica.argumento
logSintatico = AnaliseSintatica.log
logSemantico = AnaliseSemantica.log
lt = AnaliseLexica.tokens


print(logSemantico)

'''
if argumento[2] == '-ls':
    print('\n-------------- Log Sintatico ----------------')
    for i in logSintatico:
        print(i)
                        
elif argumento[2] == '-lt':
    print('\n-------------- lista de tokens ----------------')
    for l in lt:
        print(l)
elif argumento[2] == '-lse':
    print('\n-------------- Log Semantico ----------------')
    for j in logSemantico:
        print(j)

elif argumento[2] == '-tudo':
    print('\n-------------- Log Sintatico ----------------')
    for u in logSintatico:    
        print(u)
        print('\n-------------- lista de tokens ----------------')
    for o in lt:
        print(o) 
        
    for j in logSemantico:
        print(j)
else:
    print('OK')
    '''