import AnaliseLexica

Fim = False
manipulador = []
log = []
argumento = AnaliseLexica.argumento
lt = AnaliseLexica.tokens
manipulador.append('PROGRAMA')
listatk = AnaliseLexica.copy
listatk.append('$')
if manipulador[0] == 'PROGRAMA':
    if listatk[0] == 'tk_topo':
        log.append('Removeu: ' + manipulador[0] + ' do manipulador')
        del manipulador[0]
        manipulador.append('tk_topo')
        manipulador.append('LISTA_COMANDO')
        manipulador.append('tk_rodape')
        log.append(manipulador[0] + ' Foi adicionado ao manipulador')
        log.append(manipulador[1] + ' Foi adicionado ao manipulador')
        log.append(manipulador[2] + ' Foi adicionado ao manipulador')
        if manipulador[0] == listatk[0]:
            log.append('Removeu: ' + manipulador[0] + ' do manipulador')
            log.append('Removeu:  ' + listatk[0] + ' lista de token')
            del manipulador[0]
            del listatk[0]
        
        while Fim == False:
            if manipulador[0] == 'LISTA_COMANDO':
                if listatk[0] == 'tk_rodape':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
            
                elif listatk[0] == 'tk_senao':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]

                elif listatk[0] == 'tk_blocof':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]        

                elif listatk[0] == 'tk_entra':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0 ,'COMANDO')
                    manipulador.insert(1,'LISTA_COMANDO')
                    log.append(manipulador[0] + ' Foi adicionado ao manipulador')
                    log.append(manipulador[1] + ' Foi adicionado ao manipulador')
     
                elif listatk[0] == 'tk_sai':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0 ,'COMANDO')
                    manipulador.insert(1,'LISTA_COMANDO')
                    log.append(manipulador[0] + ' Foi adicionado ao manipulador')
                    log.append(manipulador[1] + ' Foi adicionado ao manipulador')

                elif listatk[0] == 'tk_enquanto':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0 ,'COMANDO')
                    manipulador.insert(1,'LISTA_COMANDO')
                    log.append(manipulador[0] + ' Foi adicionado ao manipulador')
                    log.append(manipulador[1] + ' Foi adicionado ao manipulador')
           
                elif listatk[0] == 'tk_se':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0 ,'COMANDO')
                    manipulador.insert(1,'LISTA_COMANDO')
                    log.append(manipulador[0] + ' Foi adicionado ao manipulador')
                    log.append(manipulador[1] + ' Foi adicionado ao manipulador')

                elif listatk[0] == 'tk_int':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0 ,'COMANDO')
                    manipulador.insert(1,'LISTA_COMANDO')
                    log.append(manipulador[0] + ' Foi adicionado ao manipulador')
                    log.append(manipulador[1] + ' Foi adicionado ao manipulador')

                elif listatk[0] == 'tk_var':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0 ,'COMANDO')
                    manipulador.insert(1,'LISTA_COMANDO')
                    log.append(manipulador[0] + ' Foi adicionado ao manipulador')
                    log.append(manipulador[1] + ' Foi adicionado ao manipulador')
                
                
                

            if manipulador[0] == 'COMANDO':

                if listatk[0] == 'tk_int':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0,'INT')
                    manipulador.insert(1,'VAR')
                    manipulador.insert(2,'ARGGENERICO')
                    manipulador.insert(3,'tk_fim')
                    log.append(manipulador[0] + ' Foi adicionado ao manipulador')
                    log.append(manipulador[1] + ' Foi adicionado ao manipulador')
                    log.append(manipulador[2] + ' Foi adicionado ao manipulador')
                    log.append(manipulador[3] + ' Foi adicionado ao manipulador')

                elif listatk[0] == 'tk_entra':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0,'tk_entra')
                    manipulador.insert(1,'tk_abre')
                    manipulador.insert(2,'ATRIBUTO')
                    manipulador.insert(3,'tk_fecha')
                    manipulador.insert(4,'tk_fim')
                    log.append(manipulador[0] + ' Foi adicionado ao manipulador')
                    log.append(manipulador[1] + ' Foi adicionado ao manipulador')
                    log.append(manipulador[2] + ' Foi adicionado ao manipulador')
                    log.append(manipulador[3] + ' Foi adicionado ao manipulador')
                    log.append(manipulador[4] + ' Foi adicionado ao manipulador')
                    if manipulador[0] == listatk[0]:
                        log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                        log.append('Removeu:  ' + listatk[0] + ' lista de token')
                        del manipulador[0]
                        del listatk[0]

                elif listatk[0] == 'tk_sai':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0,'tk_sai')
                    manipulador.insert(1,'tk_abre')
                    manipulador.insert(2,'ATRIBUTO')
                    manipulador.insert(3,'tk_fecha')
                    manipulador.insert(4,'tk_fim')
                    log.append(manipulador[0] + ' Foi adicionado ao manipulador')
                    log.append(manipulador[1] + ' Foi adicionado ao manipulador')
                    log.append(manipulador[2] + ' Foi adicionado ao manipulador')
                    log.append(manipulador[3] + ' Foi adicionado ao manipulador')
                    log.append(manipulador[4] + ' Foi adicionado ao manipulador')
                    if manipulador[0] == listatk[0]:
                        log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                        log.append('Removeu:  ' + listatk[0] + ' lista de token')
                        del manipulador[0]
                        del listatk[0]

                elif listatk[0] == 'tk_enquanto':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0,'ENQUANTO')
                    manipulador.insert(1,'tk_abre')
                    manipulador.insert(2,'LOGICA')
                    manipulador.insert(3,'tk_fecha')
                    manipulador.insert(4,'BLOCOCODIGO')
                    log.append(manipulador[0] + ' Foi adicionado ao manipulador')
                    log.append(manipulador[1] + ' Foi adicionado ao manipulador')
                    log.append(manipulador[2] + ' Foi adicionado ao manipulador')
                    log.append(manipulador[3] + ' Foi adicionado ao manipulador')
                    log.append(manipulador[4] + ' Foi adicionado ao manipulador')

            
                elif listatk[0] == 'tk_se':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0,'CASO')
                    manipulador.insert(1,'tk_abre')
                    manipulador.insert(2,'LOGICA')
                    manipulador.insert(3,'tk_fecha')
                    manipulador.insert(4,'BLOCOI')
                    manipulador.insert(5,'LISTA_COMANDO')
                    manipulador.insert(6,'CASOCONTRARIO')
                    manipulador.insert(7,'BLOCOF')
                    log.append(manipulador[0] + ' Foi adicionado ao manipulador')
                    log.append(manipulador[1] + ' Foi adicionado ao manipulador')
                    log.append(manipulador[2] + ' Foi adicionado ao manipulador')
                    log.append(manipulador[3] + ' Foi adicionado ao manipulador')
                    log.append(manipulador[4] + ' Foi adicionado ao manipulador')
                    log.append(manipulador[5] + ' Foi adicionado ao manipulador')
                    log.append(manipulador[6] + ' Foi adicionado ao manipulador')
                    log.append(manipulador[7] + ' Foi adicionado ao manipulador')

            
                            
                elif listatk[0] == 'tk_var':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0,'VAR')
                    manipulador.insert(1,'ARGUMENTO')
                    manipulador.insert(2,'tk_fim')
                    log.append(manipulador[0] + ' Foi adicionado ao manipulador')
                    log.append(manipulador[2] + ' Foi adicionado ao manipulador')
                    log.append(manipulador[3] + ' Foi adicionado ao manipulador')

            if manipulador[0] == 'STRING':
                if listatk[0] == 'string':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0,'string')
                    if manipulador[0] == listatk[0]:
                        log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                        log.append('Removeu:  ' + listatk[0] + ' lista de token')
                        del manipulador[0]
                        del listatk[0]

            if manipulador[0] == 'ATRIBUTO':
                if listatk[0] == 'tk_numpos' or 'tk_numneg':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0,'NUM')
                    log.append(manipulador[0] + ' Foi adicionado ao manipulador')

            if manipulador[0] == 'ATRIBUTO':
                if listatk[0] == 'string':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0,'STRING')
                    log.append(manipulador[0] + ' Foi adicionado ao manipulador')

            if manipulador[0] == 'ATRIBUTO':
                if listatk[0] == 'tk_var':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0,'VAR')
                    log.append(manipulador[0] + ' Foi adicionado ao manipulador')

            if manipulador[0] == 'NUM':
                    if listatk[0] == 'tk_numpos':
                        log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                        del manipulador[0]
                        manipulador.insert(0,'tk_numpos')
                        if manipulador[0] == listatk[0]:
                            log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                            log.append('Removeu:  ' + listatk[0] + ' lista de token')
                            del manipulador[0]
                            del listatk[0]

            if manipulador[0] == 'NUM':
                if listatk[0] == 'tk_numneg':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0,'tk_numneg')
                    if manipulador[0] == listatk[0]:
                        log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                        log.append('Removeu:  ' + listatk[0] + ' lista de token')
                        del manipulador[0]
                        del listatk[0]

            if manipulador[0] == 'CONTMAT':
                if listatk[0] == 'tk_soma':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0,'tk_soma')
                    if manipulador[0] == listatk[0]:
                        log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                        log.append('Removeu:  ' + listatk[0] + ' lista de token')
                        del manipulador[0]
                        del listatk[0]

            
                if listatk[0] == 'tk_subtracao':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0,'tk_subtracao')
                    if manipulador[0] == listatk[0]:
                        log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                        log.append('Removeu:  ' + listatk[0] + ' lista de token')
                        del manipulador[0]
                        del listatk[0]

            
                if listatk[0] == 'tk_multiplicacao':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0,'tk_multiplicacao')
                    if manipulador[0] == listatk[0]:
                        log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                        log.append('Removeu:  ' + listatk[0] + ' lista de token')
                        del manipulador[0]
                        del listatk[0]

            
                if listatk[0] == 'tk_divisao':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0,'tk_divisao')
                    if manipulador[0] == listatk[0]:
                        log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                        log.append('Removeu:  ' + listatk[0] + ' lista de token')
                        del manipulador[0]
                        del listatk[0]

            if manipulador[0] == 'INT':
                if listatk[0] == 'tk_int':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0,'tk_int')
                    if manipulador[0] == listatk[0]:
                        log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                        log.append('Removeu:  ' + listatk[0] + ' lista de token')
                        del manipulador[0]
                        del listatk[0]

            if manipulador[0] == 'EXPRESSAOLOG':
                if listatk[0] == 'tk_igual':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0,'tk_igual')
                    if manipulador[0] == listatk[0]:
                        log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                        log.append('Removeu:  ' + listatk[0] + ' lista de token')
                        del manipulador[0]
                        del listatk[0]

            if manipulador[0] == 'EXPRESSAOLOG':
                if listatk[0] == 'tk_diferente':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0,'tk_diferente')
                    if manipulador[0] == listatk[0]:
                        log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                        log.append('Removeu:  ' + listatk[0] + ' lista de token')
                        del manipulador[0]
                        del listatk[0]

            if manipulador[0] == 'EXPRESSAOLOG':
                if listatk[0] == 'tk_maior':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0,'tk_maior')
                    if manipulador[0] == listatk[0]:
                        log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                        log.append('Removeu:  ' + listatk[0] + ' lista de token')
                        del manipulador[0]
                        del listatk[0]

            if manipulador[0] == 'EXPRESSAOLOG':
                if listatk[0] == 'tk_menor':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0,'tk_menor')
                    if manipulador[0] == listatk[0]:
                        log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                        log.append('Removeu:  ' + listatk[0] + ' lista de token')
                        del manipulador[0]
                        del listatk[0]

            if manipulador[0] == 'EXPRESSAOLOG':
                if listatk[0] == 'tk_comparar':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0,'tk_comparar')
                    if manipulador[0] == listatk[0]:
                        log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                        log.append('Removeu:  ' + listatk[0] + ' lista de token')
                        del manipulador[0]
                        del listatk[0]

            if manipulador[0] == 'VAR':
                if listatk[0] == 'tk_variavel':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0, 'tk_variavel')
                    if manipulador[0] == listatk[0]:
                        log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                        log.append('Removeu:  ' + listatk[0] + ' lista de token')
                        del manipulador[0]
                        del listatk[0]

            if manipulador[0] == 'ARGGENERICO':
                if listatk[0] == 'tk_igual':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0, 'tk_igual')
                    manipulador.insert(1, 'OPERADORAUX')
                    if manipulador[0] == listatk[0]:
                        log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                        log.append('Removeu:  ' + listatk[0] + ' lista de token')
                        del manipulador[0]
                        del listatk[0]

            elif manipulador[0] == 'OPERADOR':
                
                if listatk[0] == 'tk_numpos':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0, 'VARNUM')
                    manipulador.insert(1, 'EXPRESSAOMAT')
                    log.append(manipulador[0] + ' Foi adicionado ao manipulador')
                    log.append(manipulador[1] + ' Foi adicionado ao manipulador')

            
                if listatk[0] == 'tk_numneg':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0, 'VARNUM')
                    manipulador.insert(1, 'EXPRESSAOMAT')
                    log.append(manipulador[0] + ' Foi adicionado ao manipulador')
                    log.append(manipulador[1] + ' Foi adicionado ao manipulador')

            
                if listatk[0] == 'tk_variavel':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0, 'VARNUM')
                    manipulador.insert(1, 'EXPRESSAOMAT')
                    log.append(manipulador[0] + ' Foi adicionado ao manipulador')
                    log.append(manipulador[1] + ' Foi adicionado ao manipulador')

            if manipulador[0] == 'VARNUM':
                if listatk[0] == 'tk_numpos':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0, 'NUM')
                    log.append(manipulador[0] + ' Foi adicionado ao manipulador')

            if manipulador[0] == 'VARNUM':
                if listatk[0] == 'tk_numneg':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0, 'NUM')
                    log.append(manipulador[0] + ' Foi adicionado ao manipulador')

            if manipulador[0] == 'VARNUM':
                if listatk[0] == 'tk_variavel':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0, 'VAR')
                    log.append(manipulador[0] + ' Foi adicionado ao manipulador')

            if manipulador[0] == 'EXPRESSAOMAT':
                if listatk[0] == 'tk_soma':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0, 'CONTMAT')
                    manipulador.insert(1, 'OPERADOR')
                    log.append(manipulador[0] + ' Foi adicionado ao manipulador')
                    log.append(manipulador[1] + ' Foi adicionado ao manipulador')

                if listatk[0] == 'tk_subtracao':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0, 'CONTMAT')
                    manipulador.insert(1, 'OPERADOR')
                    log.append(manipulador[0] + ' Foi adicionado ao manipulador')
                    log.append(manipulador[1] + ' Foi adicionado ao manipulador')

                if listatk[0] == 'tk_multplicacao':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0, 'CONTMAT')
                    manipulador.insert(1, 'OPERADOR')
                    log.append(manipulador[0] + ' Foi adicionado ao manipulador')
                    log.append(manipulador[1] + ' Foi adicionado ao manipulador')

                if listatk[0] == 'tk_divisao':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0, 'CONTMAT')
                    manipulador.insert(1, 'OPERADOR')
                    log.append(manipulador[0] + ' Foi adicionado ao manipulador')
                    log.append(manipulador[1] + ' Foi adicionado ao manipulador')

                if listatk[0] == 'tk_fim':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]

            if manipulador[0] == 'OPERADORAUX':
                if listatk[0] == 'tk_numpos':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0, 'OPERADOR')
                    log.append(manipulador[0] + ' Foi adicionado ao manipulador')

            if manipulador[0] == 'OPERADORAUX':
                if listatk[0] == 'tk_numneg':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0, 'OPERADOR')
                    log.append(manipulador[0] + ' Foi adicionado ao manipulador')

            if manipulador[0] == 'OPERADORAUX':
                if listatk[0] == 'tk_variavel':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0, 'OPERADOR')
                    log.append(manipulador[0] + ' Foi adicionado ao manipulador')

            if manipulador[0] == 'OPERADORAUX':
                if listatk[0] == 'tk_abre':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0, 'STRINGO')
                    log.append(manipulador[0] + ' Foi adicionado ao manipulador')

            if manipulador[0] == 'STRINGO':
                if listatk[0] == 'tk_abre':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0, 'tk_abre')
                    manipulador.insert(1, 'STRING')
                    manipulador.insert(2, 'tk_fecha')
                    if manipulador[0] == listatk[0]:
                        log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                        log.append('Removeu:  ' + listatk[0] + ' lista de token')
                        del manipulador[0]
                        del listatk[0]

            if manipulador[0] == 'ARGUMENTO':
                if listatk[0] == 'tk_igual':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0, 'tk_igual')
                    manipulador.insert(1, 'OPERADORAUX')
                    if manipulador[0] == listatk[0]:
                        log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                        log.append('Removeu:  ' + listatk[0] + ' lista de token')
                        del manipulador[0]
                        del listatk[0]

            if manipulador[0] == 'ARGUMENTO':
                if listatk[0] == 'tk_incremento':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0, 'INTERACAO')

            if manipulador[0] == 'ARGUMENTO':
                if listatk[0] == 'tk_decremento':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0, 'INTERACAO')

            if manipulador[0] == 'ARGUMENTO':
                if listatk[0] == 'tk_fim':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]

            if manipulador[0] == 'INTERACAO':
                if listatk[0] == 'tk_incremento':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0, 'INTERACAO')

            if manipulador[0] == 'INTERACAO':
                if listatk[0] == 'tk_decremento':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0, 'INTERACAO')

            if manipulador[0] == 'INTERACAO':
                if listatk[0] == 'tk_incremento':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0, 'tk_incremento')
                    if manipulador[0] == listatk[0]:
                        log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                        log.append('Removeu:  ' + listatk[0] + ' lista de token')
                        del manipulador[0]
                        del listatk[0]

            elif manipulador[0] == 'INTERACAO':
                if listatk[0] == 'tk_decremento':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0, 'tk_decremento')
                    if manipulador[0] == listatk[0]:
                        log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                        log.append('Removeu:  ' + listatk[0] + ' lista de token')
                        del manipulador[0]
                        del listatk[0]

            if manipulador[0] == 'ENQUANTO':
                if listatk[0] == 'tk_enquanto':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0, 'tk_enquanto')
                    if manipulador[0] == listatk[0]:
                        log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                        log.append('Removeu:  ' + listatk[0] + ' lista de token')
                        del manipulador[0]
                        del listatk[0]

            if manipulador[0] == 'BLOCOI':
                if listatk[0] == 'tk_blocoi':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0, 'tk_blocoi')
                    if manipulador[0] == listatk[0]:
                        log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                        log.append('Removeu:  ' + listatk[0] + ' lista de token')
                        del manipulador[0]
                        del listatk[0]

            if manipulador[0] == 'CASO':
                if listatk[0] == 'tk_se':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0, 'tk_se')
                    if manipulador[0] == listatk[0]:
                        log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                        log.append('Removeu:  ' + listatk[0] + ' lista de token')
                        del manipulador[0]
                        del listatk[0]

            if manipulador[0] == 'CASONAO':
                if listatk[0] == 'tk_senao':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0, 'tk_senao')
                    if manipulador[0] == listatk[0]:
                        log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                        log.append('Removeu:  ' + listatk[0] + ' lista de token')
                        del manipulador[0]
                        del listatk[0]

            if manipulador[0] == 'BLOCOF':
                if listatk[0] == 'tk_blocof':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0, 'tk_blocof')
                    if manipulador[0] == listatk[0]:
                        log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                        log.append('Removeu:  ' + listatk[0] + ' lista de token')
                        del manipulador[0]
                        del listatk[0]

            if manipulador[0] == 'ARGEXPRESSAO':
                if listatk[0] == 'tk_igual':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0, 'EXPRESSAOLOG')
                    manipulador.insert(1, 'VARNUM')
                    log.append(manipulador[0] + ' Foi adicionado ao manipulador')
                    log.append(manipulador[1] + ' Foi adicionado ao manipulador')

            if manipulador[0] == 'ARGEXPRESSAO':
                if listatk[0] == 'tk_diferente':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0, 'EXPRESSAOLOG')
                    manipulador.insert(1, 'VARNUM')
                    log.append(manipulador[0] + ' Foi adicionado ao manipulador')
                    log.append(manipulador[1] + ' Foi adicionado ao manipulador')

            if manipulador[0] == 'ARGEXPRESSAO':
                if listatk[0] == 'tk_maior':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0, 'EXPRESSAOLOG')
                    manipulador.insert(1, 'VARNUM')
                    log.append(manipulador[0] + ' Foi adicionado ao manipulador')
                    log.append(manipulador[1] + ' Foi adicionado ao manipulador')

            if manipulador[0] == 'ARGEXPRESSAO':
                if listatk[0] == 'tk_comparar':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0, 'EXPRESSAOLOG')
                    manipulador.insert(1, 'VARNUM')
                    log.append(manipulador[0] + ' Foi adicionado ao manipulador')
                    log.append(manipulador[1] + ' Foi adicionado ao manipulador')

            if manipulador[0] == 'ARGEXPRESSAO':
                if listatk[0] == 'tk_fim':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]

            if manipulador[0] == 'LOGICA':
                if listatk[0] == 'tk_variavel':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0, 'VAR')
                    manipulador.insert(1, 'ARGEXPRESSAO')
                    log.append(manipulador[0] + ' Foi adicionado ao manipulador')
                    log.append(manipulador[1] + ' Foi adicionado ao manipulador')

            if manipulador[0] == 'BLOCOCODIGO':
                if listatk[0] == 'tk_blocoi':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0, 'BLOCOI')
                    manipulador.insert(1, 'LISTA_COMANDO')
                    manipulador.insert(2, 'BLOCOF')
                    log.append(manipulador[0] + ' Foi adicionado ao manipulador')
                    log.append(manipulador[1] + ' Foi adicionado ao manipulador')
                    log.append(manipulador[2] + ' Foi adicionado ao manipulador')

            if manipulador[0] == 'CASOCONTRARIO':
                if listatk[0] == 'tk_senao':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    manipulador.insert(0, 'CASONAO')
                    manipulador.insert(1, 'BLOCOCODIGO')
                    log.append(manipulador[0] + ' Foi adicionado ao manipulador')
                    log.append(manipulador[1] + ' Foi adicionado ao manipulador')

            if manipulador[0] == 'CASOCONTRARIO':
                if listatk[0] == 'tk_blocof':
                    log.append('Removeu: ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
            
            else:
                
                if manipulador[0] == listatk[0]:
                              
                    log.append('Removeu ' + listatk[0] + ' lista de token')
                    log.append('Removeu ' + manipulador[0] + ' do manipulador')
                    del manipulador[0]
                    del listatk[0]
                    Fim = True

                    '''
                    
                    if argumento[2] == '-ls':
                        print('\n-------------- log ----------------')
                        for i in log:
                            print(i)
                        
                    if argumento[2] == '-lt':
                        print('\n-------------- lista de tokens ----------------')
                        for l in lt:
                            print(l)
                    if argumento[2] == '-tudo':
                        print('\n-------------- log ----------------')
                        for u in log:    
                            print(u)
                        print('\n-------------- lista de tokens ----------------')
                        for o in lt:
                            print(o)  
                         '''           
    else:
        print('Erro nao foi encontrado o inicio do programa')
print('Analise Sintatica concluida sem erros')