import AnaliseSemantica
import AnaliseLexica
cont = 0
token = AnaliseLexica.copy
lexema = AnaliseLexica.lexemas
variaveis = AnaliseSemantica.variaveis
codigo = []

codigo.append(".global main\n")
codigo.append("main:")

for i in token:
    
    cont += 1
    if i == 'tk_adicao':
        if token[cont - 2] == 'tk_variavel':
            valor1 = variaveis.get(lexema[cont - 2])
        elif token[cont - 2] == 'tk_numpos' or 'tk_numneg':
            valor1 = lexema[cont - 2]
        if token[cont] == 'tk_variavel':
            valor2 = variaveis.get(lexema[cont])
        elif token[cont] == 'tk_numpos' or 'tk_numneg':
            valor2 = lexema[cont]     
                                      
        codigo.append('      MOV r0, #' + valor1)
        codigo.append('      MOV r1, #' + valor2)
        codigo.append('      add r0, r0, r1')

    if i == 'tk_rodape':
        codigo.append('      bx lr')

            

for code in codigo:
    print(code)