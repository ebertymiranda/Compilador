import AnaliseSemantica
import AnaliseLexica
index = 0
controle = 0
token = AnaliseLexica.copy
lexema = AnaliseLexica.lexemas
variaveis = AnaliseSemantica.variaveis
codigo = []



codigo.append(".global main\n")
codigo.append("main:")

for i in token:
    
    index += 1
    
    if i == 'tk_adicao':     
        if token[index - 2] == 'tk_variavel':
            valor1 = variaveis.get(lexema[index - 2])
        elif token[index - 2] == 'tk_numpos' or 'tk_numneg':
            valor1 = lexema[index - 2]
        if token[index] == 'tk_variavel':
            valor2 = variaveis.get(lexema[index])
        elif token[index] == 'tk_numpos' or 'tk_numneg':
            valor2 = lexema[index]     

        if controle == 0:                                     
            codigo.append('      MOV r0, #' + valor1)
            codigo.append('      MOV r1, #' + valor2)
            codigo.append('      add r0, r0, r1')
            controle = 1
        else:
            codigo.append('      MOV r1, #' + valor2)
            codigo.append('      add r0, r0, r1')

    if i == 'tk_subtracao':     
        if token[index - 2] == 'tk_variavel':
            valor1 = variaveis.get(lexema[index - 2])
        elif token[index - 2] == 'tk_numpos' or 'tk_numneg':
            valor1 = lexema[index - 2]
        if token[index] == 'tk_variavel':
            valor2 = variaveis.get(lexema[index])
        elif token[index] == 'tk_numpos' or 'tk_numneg':
            valor2 = lexema[index]     

        if controle == 0:                                     
            codigo.append('      MOV r0, #' + valor1)
            codigo.append('      MOV r1, #' + valor2)
            codigo.append('      sub r0, r0, r1')
            controle = 1
        else:
            codigo.append('      MOV r1, #' + valor2)
            codigo.append('      sub r0, r0, r1')
    if i == 'tk_se':
        if token[index + 2] == 'tk_menor':
            if token[index + 1] == 'tk_variavel':
                valor1 = variaveis.get(lexema[index + 1])
            elif token[index + 1] == 'tk_numpos' or 'tk_numneg':
                valor1 = lexema[index + 1]
            if token[index + 3] == 'tk_variavel':
                valor2 = variaveis.get(lexema[index + 3])
            elif token[index + 3] == 'tk_numpos' or 'tk_numneg':
                valor2 = lexema[index + 3]
    
            if controle == 0:
                codigo.append('      MOV r1, #'+ valor1)
                codigo.append('      MOV r2, #'+ valor2)
                codigo.append('      CMP r1, r2')
                codigo.append('      blt r1_lower')
                codigo.append('      MOV r0, r1')
                codigo.append('      b end')
                

                if token[index + 10] == 'tk_senao':
                    codigo.append('r1_lower:')
                    codigo.append('      MOV r0, r2')
                    codigo.append('      b end')
                    codigo.append('end:')
                
                
                







    if i == 'tk_fim':
        controle = 0

    if i == 'tk_rodape':
        codigo.append('      bx lr')
        
for code in codigo:
    print(code)