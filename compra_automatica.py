import view
import controller


def compra_automatica_bilhetes(eventos,utilizadores, utilizador):#A variavel utilizador é o nif do user_online.
    view.listar_eventos(eventos)
    while True:
        try:
            id = int(input("Indique o numero de ID do Espetáculo: "))
        except ValueError:
            print("Você digitou uma entrada inválida, tente novamente.")
            continue
        if controller.valida_id(id, eventos) == True:
            view.ver_sala(id,eventos)
            while True:
                try:
                    quantidade_lugares = int(input("Indique a quantidade de lugares que pretende aquirir: "))
                    print("\n")
                except ValueError:
                    print("Você inseriu um formato não válido!!!")
                    continue
                if quantidade_lugares > 142:
                    print("Você digitou um número excessivo de lugares, tente novamente.")
                    continue
                elif quantidade_lugares > 10:
                    lugares_comprados = compra_sequencial(id,utilizador,utilizadores,eventos,quantidade_lugares)
                    if lugares_comprados == False:
                        break
                    else:
                        escolha_compra(id,lugares_comprados,utilizador,utilizadores,eventos)
                        return
                elif quantidade_lugares > 2:
                    lugares_comprados = []
                    n = 0
                    for i in eventos:
                        if id in i:
                            sala=i[3]
                            tmp = [2,3,4,5,6,7,8,9,10,11]
                            while n < quantidade_lugares:
                                for j in range(12):
                                    lugares_comprados.clear() #DEIXAR TODOS SEMPRE NA MESMA FILA DO ESPETACULO
                                    n = 0
                                    if n == quantidade_lugares or j == 11 :
                                        break
                                    elif j == 0 or j == 5:
                                        continue
                                    else:
                                        for g in tmp:
                                            if n == quantidade_lugares:
                                                break
                                            else:
                                                if sala[j][g] == 0:
                                                        lugar = [id,3,j,g]
                                                        lugares_comprados.append(lugar)
                                                        n+=1
                                                else:
                                                    n=0
                                                    lugares_comprados.clear()   #ALTERAR PARA SEMPRE ESTAREM JUNTOS
                                            while n >= quantidade_lugares:
                                                print("Os seguintes lugares foram escolhidos: ")
                                                for h in lugares_comprados:
                                                    print(f"Poltrona: {view.num_alpha(h[2])}-{h[3]+1}")
                                                escolha = input("Confirme se deseja essa escolha ou fazemos uma nova consulta.\n 1- Confirmar \n 2-Nova consulta\n")
                                                if escolha == "1":
                                                    escolha_compra(id,lugares_comprados,utilizador,utilizadores,eventos)
                                                    return
                                                elif escolha == "2":
                                                    n = 0
                                                    lugares_comprados.clear()
                                                    break
                                                else:
                                                    print("Entrada inválida, tente novamente")
                                                    continue
                                lugares_comprados = compra_sequencial(id,utilizador,utilizadores,eventos,quantidade_lugares)
                                if lugares_comprados == False:
                                    break
                                else:
                                    escolha_compra(id,lugares_comprados,utilizador,utilizadores,eventos)
                                    return
            

#ESCOLHA DE 2 LUGAR  
                elif quantidade_lugares == 2:
                    lugares_comprados = []
                    n = 0
                    for i in eventos:
                        if id  == i[0]:
                            espetaculo = i[3]
                            lista_out = [2,3,4,5,6,7,8,9,10,11]
                            #while n < quantidade_lugares:
                            for y in range(len(espetaculo)):
                                lugares_comprados.clear() #Garantia de os lugares estarem na mesma fila
                                for j in range(len(espetaculo[y])):
                                    if j in lista_out:
                                        continue
                                    else:
                                        n+=1
                                        if espetaculo[y][j] == 0:
                                            #print(espetaculo[y])
                                            lugares_comprados.append([id,3,y,j])
                                            #lugares_comprados.append([id,3,y,j])
                                            while len(lugares_comprados) == 2:
                                                if lugares_comprados[0][3] == 0 and lugares_comprados[1][3] == 1 or  lugares_comprados[0][3] == 12 and lugares_comprados[1][3] == 13:
                                                    print("Os seguintes lugares foram escolhidos: ")
                                                    for h in lugares_comprados:
                                                        print(f"Poltrona: {view.num_alpha(h[2])}-{h[3]+1}")
                                                    escolha = input("Confirme se deseja essa escolha ou fazemos uma nova consulta.\n 1- Confirmar \n 2-Nova consulta\n")
                                                    if escolha == "1":
                                                        escolha_compra(id,lugares_comprados,utilizador,utilizadores,eventos)
                                                        return
                                                    elif escolha == "2":
                                                        lugares_comprados.clear()
                                                        break
                                                    else:
                                                        print("Entrada inválida, tente novamente.")
                                                        continue
                                                else:
                                                    lugares_comprados.clear()
                                                    break 
                                            else:
                                                if n == 2:
                                                    n=0
                                                    lugares_comprados.clear()
                                                    continue
                                        else:
                                            if n == 2:
                                                lugares_comprados.clear()
                                                n=0
                                                continue
                                            else:
                                                continue
                    for i in eventos:
                        if id  == i[0]:
                            espetaculo = i[3]
                            lista_out = [2,3,4,5,6,7,8,9,10,11]
                            for y in range(len(espetaculo)):
                                if y == 0 or y == 5:
                                    continue
                                else:
                                    for j in range(len(espetaculo[y])):
                                        if j in lista_out:
                                            n+=1
                                            if espetaculo[y][j] == 0:
                                                #print(espetaculo[y])
                                                lugares_comprados.append([id,3,y,j])
                                                #lugares_comprados.append([id,3,y,j])
                                                while len(lugares_comprados) == 2:
                                                    print("Os seguintes lugares foram escolhidos: ")
                                                    for h in lugares_comprados:
                                                        print(f"Poltrona: {num_alpha(h[2])}-{h[3]+1}")
                                                    escolha = input("Confirme se deseja essa escolha ou fazemos uma nova consulta.\n 1- Confirmar \n 2-Nova consulta\n")
                                                    if escolha == "1":
                                                        escolha_compra(id,lugares_comprados,utilizador,utilizadores,eventos)
                                                        return
                                                    elif escolha == "2":
                                                        lugares_comprados.clear()
                                                        break
                                                    else:
                                                        print("Entrada inválida, tente novamente.")
                                                        continue
                                                else:
                                                    if n == 2:
                                                        n=0
                                                        lugares_comprados.clear()
                                                        continue
                                            else:
                                                if n == 2:
                                                    lugares_comprados.clear()
                                                    n=0
                                                    continue
                                                else:
                                                    continue
                                        else:
                                            continue
#ESCOLHA DE 1 LUGAR                                                                         
                else:
                    lugares_comprados = []
                    for i in eventos:
                        if id  == i[0]:
                            espetaculo = i[3]
                            lista_out = [2,3,4,5,6,7,8,9,10,11]
                            #while n < quantidade_lugares:
                            for y in range(len(espetaculo)):
                                for j in range(len(espetaculo[y])):
                                    if j in lista_out:
                                        continue
                                    else:
                                        if espetaculo[y][j] == 0:
                                            #print(espetaculo[y])
                                            lugares_comprados.append([id,3,y,j])
                                            #lugares_comprados.append([id,3,y,j])
                                            while len(lugares_comprados) == 1:
                                                print("Os seguintes lugares foram escolhidos: ")
                                                for h in lugares_comprados:
                                                    print(f"Poltrona: {view.num_alpha(h[2])}-{h[3]+1}")
                                                escolha = input("Confirme se deseja essa escolha ou fazemos uma nova consulta.\n 1- Confirmar \n 2-Nova consulta\n")
                                                if escolha == "1":
                                                    escolha_compra(id,lugares_comprados,utilizador,utilizadores,eventos)
                                                    return
                                                elif escolha == "2":
                                                    lugares_comprados.clear()
                                                    break
                                                else:
                                                    print("Entrada inválida, tente novamente.")
                                                    continue
                                            else:
                                                continue
                                        else:
                                            continue
                    for i in eventos:
                        if id  == i[0]:
                            espetaculo = i[3]
                            lista_out = [2,3,4,5,6,7,8,9,10,11]
                            #while n < quantidade_lugares:
                            for y in range(len(espetaculo)):
                                if y == 0 or y == 5:
                                    continue
                                else:
                                    for j in range(len(espetaculo[y])):
                                        if j in lista_out:
                                            if espetaculo[y][j] == 0:
                                                #print(espetaculo[y])
                                                lugares_comprados.append([id,3,y,j])
                                                #lugares_comprados.append([id,3,y,j])
                                                while len(lugares_comprados) == 1:
                                                    print("Os seguintes lugares foram escolhidos: ")
                                                    for h in lugares_comprados:
                                                        print(f"Poltrona: {view.num_alpha(h[2])}-{h[3]+1}")
                                                    escolha = input("Confirme se deseja essa escolha ou fazemos uma nova consulta.\n 1- Confirmar \n 2-Nova consulta\n")
                                                    if escolha == "1":
                                                        escolha_compra(id,lugares_comprados,utilizador,utilizadores,eventos)
                                                        return
                                                    elif escolha == "2":
                                                        lugares_comprados.clear()
                                                        break
                                                    else:
                                                        print("Entrada inválida, tente novamente.")
                                                        continue
                                                else:
                                                    continue
                                            else:
                                                continue
                                        else:
                                            continue
                return
            return
        else:
            print("Não há evento com o ID inserido, tente novamnete")
            continue
    
def compra_sequencial(id,utilizador,utilizadores,eventos,quantidade_lugares):
    lugares_comprados = []
    n = 0
    for i in eventos:
        if id in i:
            sala=i[3]
            while n < quantidade_lugares:
                for j in range(12): 
                    if n == quantidade_lugares or j == 11 :
                        print("Foram disponibilizados todas os lugares disponiveis, tente a compra manual.")
                        return False
                    elif j == 0 or j == 5:
                        continue
                    else:
                        for g in range(14):
                            if n == quantidade_lugares or g == 14:
                                break
                            else:
                                if sala[j][g] == 0:
                                        lugar = [id,3,j,g]
                                        lugares_comprados.append(lugar)
                                        n+=1
                                else:
                                    pass   #ALTERAR PARA SEMPRE ESTAREM JUNTOS
                            while n == quantidade_lugares:
                                print("Os seguintes lugares foram escolhidos: ")
                                for h in lugares_comprados:
                                    print(f"Poltrona: {view.num_alpha(h[2])}-{h[3]+1}")
                                escolha = input("Confirme se deseja essa escolha ou fazemos uma nova consulta.\n 1- Confirmar \n 2-Nova consulta\n")
                                if escolha == "1":
                                    escolha_compra(id,lugares_comprados,utilizador,utilizadores,eventos)
                                    return lugares_comprados
                                elif escolha == "2":
                                    n = 0
                                    lugares_comprados.clear()
                                    break
                                else:
                                    print("Entrada inválida, tente novamente")
                                    continue
            print("Foram disponibilizados todas os lugares disponiveis, tente a compra manual.")
            return False

def escolha_compra(id,lugares_comprados,utilizador,utilizadores,eventos):
    for x in lugares_comprados:
        if controller.compra_bilhete(id, utilizador, x[2], x[3], utilizadores,eventos) == True:
            #print(lugar)
            #valor = controller.valor_bilhete(fila,lugar)
            for i in eventos:
                if id in i:
                    i[3][x[2]][x[3]] = "\033[1;31mX\033[m"
                    #n += 1
                    #poltrona = [id,fila,lugar,valor]
                    #lugares_comprados.append(poltrona)
    
    view.record("Save_Espetaculos",eventos)
    view.record("Save_Utilizadores",utilizadores)
    total = 0 
    c = 0 
    v = 0
    
    for i in lugares_comprados:
        if controller.valor_bilhete(i[2],i[3]) == 4:
            c+=1
            total+=4
        elif i[3] == 12:
            v+=1
            total+=12
    print("_"*40)
    print("Comuns\t Valor\t Total")
    print(f"{c}\t €{4.00}\t €{c*4.00}\t")
    print("VIPs\t Valor\t Total")
    print(f"{v}\t €{12}\t €{v*12.00}\t")
    print(f"\nValor Total:\t €{total*100*0.01}")
    print("_"*40)
    print("-"*40)
    for i in lugares_comprados:
        print(f"Poltrona: {view.num_alpha(i[2])}-{i[3]+1}")
    print("-"*40)
    print(f"O total de bilhetes:\nTotal de Comuns: {c}\nTotal de VIPs: {v}\nO valor total dos bilhetes foi de : €{total:2}.")
    print("-"*40)
    return True