#--D'Hodnt Method--
def calcula_quocientes(votos_apurados, numero_de_deputados):
    """
    Devolve um dicionário com quocientes por ordem crescente calculados através do método de Hondt para cada partido.
    
    Argumentos:
        votos_apurados: dicionário (chaves correspondem a partidos, tem pelo
                                    menos um partido)
        numero_de_deputados: inteiro (positivo)
    No fundo, é feita uma divisão sucessiva (1,2,...,número de deputados)
    dos votos iniciais de cada partido, devolvendo-se um dicionário com as
    mesmas chaves do argumento, em que cada valor é a lista com
    essas divisões.

    calcula_quocientes: dicionário x inteiro --> dicionário
    """

    quociente={}
    div_sucessiva=[]
    
    for partido,votos in votos_apurados.items():
        divisor=1
        
        while divisor<=numero_de_deputados: 
            div_sucessiva+=[votos/divisor]
            divisor+=1
        
        quociente[partido]=div_sucessiva
        div_sucessiva=[]
    
    return quociente


def atribui_mandatos(votos_apurados, numero_de_deputados):
    """
    Devolve uma lista ordenada em que cada elemento corresponde a um deputado eleito, contendo o nome partido que o obteve.

    Argumentos:
        votos_apurados: dicionário (chaves correspondem a partidos, tem pelo
                                    menos um partido)
        numero_de_deputados: inteiro (positivo)
    Os quocientes são calculados com recurso à função anterior e
    são comparados, um mandato é atribuído em função da ordem crescente
    destes quocientes, quando se dão divisões iguais os mandatos são
    atribuídos por ordem crescente aos partidos menos votados.
    atribui_mandatos: dicionário x inteiro --> lista
    """
    
    quociente=calcula_quocientes(votos_apurados,numero_de_deputados)
    mandatos=[]
    divisoes=[]
    
    for lista_divisoes in quociente.values():
        for div2 in lista_divisoes:
            divisoes.append(div2)
    divisoes=sorted(divisoes,reverse=True)
    #junta-se numa só lista e ordena-se todas as divisões sucessivas do maior
    #para o menor
    d_anterior=0
    for d in divisoes:
        numero_de_correncias=divisoes.count(d)
        if numero_de_correncias>=2: #quando existe quocientes iguais
            
            if d==d_anterior:
                continue 

            d_anterior=d
            quocientes_iguais=[]
            for partido,lista_por_partido in quociente.items():
                
                if d in lista_por_partido:
                    quocientes_iguais.append(partido)
                #armazena na lista os partidos cujos quocientes são iguais

            quocientes_iguais_par_partido_votos=[]
            for partido,votos in votos_apurados.items():
                
                if partido in quocientes_iguais:
                    quocientes_iguais_par_partido_votos.append((partido,votos))
            quocientes_iguais_par_partido_votos=sorted(quocientes_iguais_par_partido_votos,key=lambda x:x[1]) 
            #lista ordenada por número de votos com pares partido/votos dos partidos
            #com quocientes iguais

            for i in quocientes_iguais_par_partido_votos:
                mandatos.append(i[0])  
                if len(mandatos)==numero_de_deputados:
                    break
        else:
            
            for partido,lista_por_partido in quociente.items():
                  
                if d in lista_por_partido:
                    mandatos.append(partido)
        
        if len(mandatos)==numero_de_deputados:
            break
    
    
    return mandatos


def obtem_partidos(eleicoes_num_territorio):
    """
    Devolve uma lista com os partidos presentes no território.

    Argumentos:
        eleicoes_num_territorio: dicionário
    No fundo, a função procura partidos em todos os círculos eleitorais do
    território e devolve numa lista com os partidos que participaram nas
    eleições por ordem alfabética. 

    obtem_partidos: dicionário --> lista
    """
  
    partidos=[]
    
    for circulo in eleicoes_num_territorio.keys():
        votos_num_circulo=eleicoes_num_territorio[circulo]['votos']
        
        for partido in votos_num_circulo.keys():
            
            if partido not in partidos:
                partidos.append(partido)
    
    return sorted(partidos)


def obtem_resultado_eleicoes(eleicoes_num_territorio):
    """
    Devolve uma lista com o resultado das eleições num território.
    
    Argumentos:
        eleicoes_num_territorio: dicionário
    No fundo, aplica-se o Método de Hondt recorrendo às funções
    atribui_mandatos e obtem_partidos de modo obter os mandatos de cada
    círculo eleitoral e chegar ao resultado das eleições. Para validar os
    argumentos recebidos recorre-se à função auxiliar "validar_arg" gerando
    ValueError com a mensagem: "obtem_resultados_eleicoes: argumentos
    inválidos" em caso de argumentos errados.

    obtem_resultado_eleicoes: dicionário --> lista
    """
    
    def validar_arg(eleicoes_num_territorio):
        if eleicoes_num_territorio=={} or not isinstance(eleicoes_num_territorio,dict):
            raise ValueError ('obtem_resultado_eleicoes: argumento invalido')
            #Verifica se o argumento é nao vazio e é um dicionário

        for circulo in eleicoes_num_territorio:
            
            if (not isinstance (circulo,str) or eleicoes_num_territorio[circulo]=='' or
                    not isinstance(eleicoes_num_territorio[circulo],dict) or
                    len(eleicoes_num_territorio[circulo])!=2 or
                    'votos' not in eleicoes_num_territorio[circulo] or
                    'deputados' not in eleicoes_num_territorio[circulo] or
                    not isinstance(eleicoes_num_territorio[circulo]['deputados'],int) or
                    not isinstance(eleicoes_num_territorio[circulo]['votos'],dict) or
                    eleicoes_num_territorio[circulo]['deputados']<1 or
                    len(eleicoes_num_territorio[circulo]['votos'])<1):

                raise ValueError ('obtem_resultado_eleicoes: argumento invalido')
                #Verifica se cada nome de um círculo eleitoral é uma cadeia de carateres
                #não vazia, se em cada círculo existe um dicionário com um comprimento
                #igual a 2, com as chaves "votos" e "deputados" e que estas são
                #respetivamente um dicionário com pelo menos um partido e um inteiro
                #maior ou igual a 1.

            for partido in eleicoes_num_territorio[circulo]['votos']:
                    
                    if (not isinstance(partido,str) or partido=='' or
                        not isinstance(eleicoes_num_territorio[circulo]['votos'][partido],int)):
                    
                        raise ValueError ('obtem_resultado_eleicoes: argumento invalido')
                        #Verifica se o nome dos partidos em cada círculo eleitoral são cadeias de
                        #carateres não vazias, e se os votos obtidos por cada partido são inteiros.

                    if eleicoes_num_territorio[circulo]['votos'][partido]<=0:
                        raise ValueError ('obtem_resultado_eleicoes: argumento invalido')
                        #Verifica se todos os partidos em cada círculo eleitoral receberam votos

    validar_arg(eleicoes_num_territorio)
    
    partidos=obtem_partidos(eleicoes_num_territorio)
    
    eleicoes_resultado=[]
    for partido in partidos:
        eleicoes_por_circulo=[]    
        for circulo in eleicoes_num_territorio:
            mandatos_por_circulo=atribui_mandatos(eleicoes_num_territorio[circulo]['votos'],
                                                  eleicoes_num_territorio[circulo]['deputados'])
            #São atribuídos os mandatos em cada círculo
            
            if partido in eleicoes_num_territorio[circulo]['votos'].keys():
                eleicoes_por_circulo.append([partido,
                                             mandatos_por_circulo.count(partido),
                                             eleicoes_num_territorio[circulo]['votos'][partido]])
        #É armazenada na lista os votos obtidos, nome do partido e número de
        #deputados obtidos, em que cada elemento da lista corresponde ao resultado
        #desse partido em cada círculo eleitoral.

        soma_mandatos=0
        soma_votos=0
        for i in range(len(eleicoes_por_circulo)):
            soma_mandatos+=eleicoes_por_circulo[i][1]
            soma_votos+=eleicoes_por_circulo[i][2]
        eleicoes_resultado.append((partido,soma_mandatos,soma_votos))
        #Para cada partido são somados os votos e mandatos que obteve nos
        #diversos círculos.
    
    eleicoes_resultado=sorted(eleicoes_resultado,key=lambda x: (x[1],x[2]),reverse=True)
    #O resultado final das eleições é ordenado de acordo com o número
    #de mandatos, e em caso de empate, conforme o número de votos obtidos.
    return eleicoes_resultado
