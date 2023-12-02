from asyncore import close_all
from fileinput import close
import model
import controller
import pickle
import getpass
import os
from datetime import datetime
from datetime import date
import compra_automatica
def main():
    eventos = read("Save_Espetaculos")
    utilizadores = read("Save_Utilizadores")
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    while True:
        cabecalho()
        menu_principal()
        user_online = []
        fila=[]
        lugar=[]
        entrada:int = (input("                                                                     Digite a opção que pretende: ")).split(" ")
        if entrada[0] == "1":
            os.system('cls' if os.name in ('nt', 'dos') else 'clear')
            while True:
                cabecalho()
                menu_utilizador()
                entrada:int = (input("                                                                     Digite a opção que pretende: ")).split(" ")
                if entrada[0] == "1":
                    listar_eventos(eventos)
                elif entrada[0] == "2":
                    nif = input("                                                                     Digite o número do seu NIF: ")
                    password = getpass.getpass("                                                                     Digite a senha de acesso: ")
                    if login_user(utilizadores,user_online,nif,password) == True:
                        os.system('cls' if os.name in ('nt', 'dos') else 'clear')
                        while True:
                            cabecalho()
                            menu_online(user_online)
                            entrada:int = (input("                                                                     Digite a opção que pretende: ")).split(" ")
                            if entrada[0] == "1":
                                listar_eventos(eventos)
                            elif entrada[0] == "2":
                                visualizar_reservas(user_online,utilizadores)
                            elif entrada[0] == "3":
                                comprar_bilhetes(eventos, user_online[1],utilizadores)
                            elif entrada[0] == "4":
                                compra_automatica.compra_automatica_bilhetes(eventos,utilizadores,user_online[1])
                            elif entrada[0] == "5":
                                eliminar_reserva(user_online, utilizadores, eventos)
                            elif entrada[0] == "6":
                                help()
                            elif entrada[0] == "0":
                                user_online.clear()
                                os.system('cls' if os.name in ('nt', 'dos') else 'clear')
                                break
                            elif entrada[0]== "7":
                                print("OBRIGADO POR UTILIZAR NOSSOS SERVIÇOES E VOLTE SEMPRE!!!")
                                quit()
                            else:
                                print("Instrução inválida.")

                elif entrada[0] == "3":
                    if registrar_utilizador(utilizadores,user_online) == True:
                        os.system('cls' if os.name in ('nt', 'dos') else 'clear')
                        while True:
                            cabecalho()
                            menu_online(user_online)
                            entrada:int = (input("                                                                     Digite a opção que pretende: ")).split(" ")
                            if entrada[0] == "1":
                                listar_eventos(eventos)
                            elif entrada[0] == "2":
                                visualizar_reservas(user_online,utilizadores)
                            elif entrada[0] == "3":
                                utilizador = user_online[1]
                                comprar_bilhetes(eventos, utilizador, utilizadores)
                            elif entrada[0] == "4":
                                utilizador = user_online[1]
                                compra_automatica.compra_automatica_bilhetes(eventos,utilizadores, utilizador) 
                            elif entrada[0] == "5":
                                eliminar_reserva(eventos, utilizador, utilizadores)
                            elif entrada[0] == "6":
                                help()
                            elif entrada[0] == "0":
                                user_online.clear()
                                os.system('cls' if os.name in ('nt', 'dos') else 'clear')
                                break
                            elif entrada[0] == "7":
                                print("OBRIGADO POR UTILIZAR NOSSOS SERVIÇOES E VOLTE SEMPRE!!!")
                                quit()
                            else:
                                print("Instrução inválida.")
                elif entrada[0] == "4":
                    reset_password(utilizadores)        
                elif entrada[0] == "5":
                    help()
                elif entrada[0] == "0":
                    os.system('cls' if os.name in ('nt', 'dos') else 'clear')
                    break
                elif entrada[0] == "6":
                    print("OBRIGADO POR UTILIZAR NOSSOS SERVIÇOES E VOLTE SEMPRE!!!")
                    quit()
                else:
                    print("Instrução Inválida.")
        elif entrada[0] == "2":
            if login_admin() ==False:
                os.system('cls' if os.name in ('nt', 'dos') else 'clear')
                print("Password inválido, tente novamente.")
            else:
                os.system('cls' if os.name in ('nt', 'dos') else 'clear')
                while True:
                    cabecalho()
                    menu_admin()
                    entrada:int = (input("                                                                     Digite a opção que pretende: ")).split(" ")
                    if entrada[0] == "1":
                        listar_eventos(eventos)
                    elif entrada[0] == "2":
                        os.system('cls' if os.name in ('nt', 'dos') else 'clear')
                        while True:
                            cabecalho()
                            menu_bilheteira()
                            entrada:int = (input("                                                                     Digite a opção que pretende: ")).split(" ")
                            if entrada[0] == "1":
                                bilheteria_dia(eventos,fila,lugar)
                            elif entrada[0] == "2":
                                bilheteria_mes(eventos,fila,lugar)
                            elif entrada[0] == "3":
                                bilheteria_ano(eventos,fila,lugar)
                            elif entrada[0] == "4":
                                print("OBRIGADO POR UTILIZAR NOSSOS SERVIÇOES E VOLTE SEMPRE!!!")
                                quit()
                            elif entrada[0] == "0":
                                os.system('cls' if os.name in ('nt', 'dos') else 'clear')
                                break
                    elif entrada[0] == "3":
                        registrar(eventos)
                    elif entrada[0] == "4":
                        ocupacao_sala(eventos)
                    elif entrada[0] == "5":
                        excluir_evento(eventos,utilizadores)
                    elif entrada[0] == "6":
                        print("OBRIGADO POR UTILIZAR NOSSOS SERVIÇOES E VOLTE SEMPRE!!!")
                        quit()
                    elif entrada[0] == "0":
                        os.system('cls' if os.name in ('nt', 'dos') else 'clear')
                        break
                    else:
                        print("Instrução Inválida.")
        elif entrada[0] == "3":
            print("OBRIGADO POR UTILIZAR NOSSOS SERVIÇOES E VOLTE SEMPRE!!!")
            quit()    
        else:
            os.system('cls' if os.name in ('nt', 'dos') else 'clear')
            print("Instrução Inválida")


def registrar(eventos):
    while True:
        hoje = datetime.today()
        data_final_str = "31-12-2023"
        data_final = datetime.strptime(data_final_str, "%d-%m-%Y")
        evento = input("                                                                     Digite o nome do evento: ")
        data = input("                                                                     Digite a data e hora do evento no formato dia-mês-ano HH:MM: ")
        try:
            data_str = datetime.strptime(data, '%d-%m-%Y %H:%M')
        except ValueError:
            print("Inserir a data no formato dia-mês-ano e a hora HH:MM. Tente novamente")
            continue
        if controller.valida_data(eventos, data_str) == False:
            if data_str >= hoje and data_str < data_final:
                show = controller.criar_eventos(evento,data_str)
                os.system('cls' if os.name in ('nt', 'dos') else 'clear')
                print("Evento registado: ")
                print(f"ID : {show[0]} | Evento: {show[1]} | Data: {data}\n")
                eventos.append(show)
                record("Save_Espetaculos",eventos)
                return
            else:
                print("Deve introduzir uma data entre o dia de hoje e o dia 31/12/2023")
                print("")
        else:
            os.system('cls' if os.name in ('nt', 'dos') else 'clear')
            print("A data já existe para outro espetaculo.")
            return     
            


def registrar_utilizador(utilizadores,user_online):
    nome = input("                                                         Digite o seu nome: ")
    nif = input("                                                         Digite o número do seu NIF: ")
    password = input("                                                         Digite uma senha de acesso: ")
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    for i in utilizadores:
        if nif == i[1]:
            return print("Usuário já existente.")
    utilizador = controller.registrar_user(nome,nif,password)
    utilizadores.append(utilizador)
    record("Save_Utilizadores",utilizadores)
    print("Usuário registrado com sucesso.\n")
    login_user(utilizadores,user_online,nif,password)   
    return True
    


def login_user(utilizadores, user_input,nif,password):
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    if controller.login_user(nif,password,utilizadores) == True:
        for i in utilizadores:
            if nif == i[1]:
                user_input.append(i[0])
                user_input.append(i[1])
                break
        print("Login efetuado com sucesso.")
        return True
    else:
        print("Usuário ou senha incorretos, tente novamente.")

def reset_password(utilizadores):
    nif = input("Introduza o seu NIF: ")
    if controller.valida_nif(nif, utilizadores) == True:
        password = input("Intruduza uma nova password: ")
        os.system('cls' if os.name in ('nt', 'dos') else 'clear')
        for i in utilizadores:
            if nif in i:
                i[2] = password
                print("Password alterada com sucesso")
                return
    else:
        print("O NIF indicado não existe")
    


def login_admin():
    senha = "123456"
    password = getpass.getpass("                                                                     Digite a senha de acesso: ")
    if senha == password:
        return True
    else: return False

def help():
    ajuda = open("help.txt","r")
    mensagem = ajuda.read()
    print(mensagem)
    ajuda.close()
    pass

def listar_eventos(eventos):
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    print("Espétáculos Disponiveis:")
    for i in eventos:
        print(f"ID : {i[0]} | Evento: {i[1]} | Data: {i[2]}\n")


def listar_usuarios(utilizadores):
    for i in utilizadores:
        print(i[0], i[1], i[2])

def ver_sala(id,eventos):
    if controller.valida_id(id,eventos) == True:
        for i in eventos:
            if id in i:
                plateia(i)
    else:
        print(f"A sala do evento com o ID:{id} não exixte.")


def ocupacao_sala(eventos):
    listar_eventos(eventos)
    id = int(input("Indique o numero de ID do Espetáculo: "))
    if controller.valida_id(id, eventos) == True:
        ver_sala(id,eventos)
    else:
        os.system('cls' if os.name in ('nt', 'dos') else 'clear')
        print("ID Inválido")

    
def record(save, eventos): #Salvar o jogo em um ficheiro
    with open(save, "wb") as arquivo:
        pickle.dump(eventos, arquivo)

def read(arquivo):
    try:
        arq = open(arquivo, "rb")
    except FileNotFoundError:
        eventos=[]
    else:
        eventos = pickle.load(arq)
        arq.close()   
    return eventos 

def comprar_bilhetes(eventos, utilizador, utilizadores):#A variavel utilizador é o nif do user_online.
    while True:
        listar_eventos(eventos)
        try:
            id = int(input("Indique o numero de ID do Espetáculo: "))
        except ValueError:
            print("Você digitou uma entrada inválida, tente novamente.")
            continue
        if controller.valida_id(id, eventos) == True:
            ver_sala(id,eventos)
            try:
                quantidade_lugares = int(input("Indique a quantidade de lugares que pretende aquirir: "))
                print("\n")
            except ValueError:
                print("Você inseriu um formato não válido!!!")
                return
            if quantidade_lugares != 0:
                lugares_comprados = []
                n = 0
                while n < quantidade_lugares:
                    resposta = (input("Indique a letra da Fila de A a K: ")).upper()
                    fila = alpha_num(resposta)
                    try:
                        lugar = int(input("Indique o numero do lugar de 1 a 14: "))
                    except ValueError:
                        print("Você digitou uma entrada inválida, tente novamente.")
                        continue
                    print("-"*40)
                    if lugar < 1 or lugar >14:
                        print("Você inseriu um lugar inválido, tente novamente.")
                        continue
                    else:
                        if fila == 0 or fila == 5:
                            lugares  = [3,4,5,10,11,12]
                            if lugar in lugares:
                                print("Você escolheu um lugar inválido tente novamente.")
                                continue
                            else:
                                lugar=lugar-1
                                if controller.compra_bilhete(id, utilizador, fila, lugar, utilizadores,eventos) == True:
                                    valor = controller.valor_bilhete(fila,lugar)
                                    for i in eventos:
                                        if id in i:
                                            i[3][fila][lugar] = "\033[1;31mX\033[m"
                                            poltrona = [id,fila,lugar,valor]
                                            lugares_comprados.append(poltrona)
                                            n+=1
                                            break
                                else:
                                    print("Lugar Ocupado, tente outro sitio.")
                        else:
                            lugar-=1
                            if controller.compra_bilhete(id, utilizador, fila, lugar, utilizadores,eventos) == True:
                                valor = controller.valor_bilhete(fila,lugar)
                                for i in eventos:
                                    if id in i:
                                        i[3][fila][lugar] = "\033[1;31mX\033[m"
                                        poltrona = [id,fila,lugar,valor]
                                        lugares_comprados.append(poltrona)
                                        n+=1
                                        break
                            else:
                                print("Lugar Ocupado, tente outro sitio.")
            record("Save_Espetaculos",eventos)
            record("Save_Utilizadores",utilizadores)
            total = 0 
            c = 0 
            v = 0
            os.system('cls' if os.name in ('nt', 'dos') else 'clear')
            for i in lugares_comprados:
                if i[3] == 4:
                    c+=1
                elif i[3] == 12:
                    v+=1
                total+=i[3]
                print("-"*40)
                print(f"Comprou | Poltrona-. {num_alpha(i[1])}-{i[2]+1}")
            print("-"*40)
            print(f"O total de bilhetes:\nTotal de Comuns: {c}\nTotal de VIPs: {v}\nO valor total dos bilhetes foi de : €{total:2}.")
            print("-"*40)
            break
        else:
            print("Id não exixtente, tente novamente.")    

def visualizar_reservas(user_online,utilizadores):
    nif = user_online[1]
    for i in utilizadores:
        if nif == i[1]:
            if len(i) == 3:
                print("Ainda não efetuou nenhum reserva")
            else:
                for g in range(3,len(i)):
                    print(f"ID Evento: {i[g][0]} | Acento: {num_alpha(i[g][2])}-{i[g][3]+1}")


def eliminar_reserva(user_online, utilizadores,eventos):
    visualizar_reservas(user_online,utilizadores)
    id = int(input("Indique o numero de ID do Espetáculo: "))
    if controller.teste(id,user_online,utilizadores,eventos)==True:
        visualizar_reservas(user_online,utilizadores)
        print(f"As suas reservas com o {id} foram eliminadas com sucesso")
        
    else:
        print(f"Não existe reservas com o {id} ")

    record("Save_Espetaculos",eventos)
    record("Save_Utilizadores",utilizadores)

def excluir_evento(eventos,utilizadores):
    if eventos == []:
        print("Não há eventos registrados.") #A função de clear esta retirando esse print antes do usuario ver.
        return
    else:   
        while True:
            listar_eventos(eventos)
            try:
                id = int(input("Qual o número ID do evento: "))
            except ValueError:
                print("Dado incorreto inserido, tente novamnete.")
                continue
            if controller.verificar_acentos_evento(id,eventos) == True:
                pergunta=input("Há reservas nesse evento, tem a certeza que deseja eliminar o evento? (Y/N)").upper()
                if pergunta =="Y":
                    if controller.excluir_evento(id,eventos) == True:
                        controller.excluir_evento_utilizadores(id,utilizadores)
                        print(f"O evento do id:{id} foi eliminado com sucesso.")
                        record("Save_Espetaculos",eventos)
                        record("Save_Utilizadores",utilizadores)
                        return
                elif pergunta=="N":
                    print("Não foi excluido nenhum evento.")
                    return
                else:
                    print("Instrução inválida,tente novamente")
                    continue
            else:
                if controller.excluir_evento(id,eventos) == True:
                    print(f"O evento do id:{id} foi eliminado com sucesso.")
                    record("Save_Espetaculos",eventos)
                    record("Save_Utilizadores",utilizadores)
                    return
                else:
                    print(f"O evento com o id:{id} não existe.")


def num_alpha(num):
    alpha = ["A","B","C","D","E","F","G","H","I","J","K"]
    resultado = alpha[num]  
    return resultado  

def alpha_num(letra):
    alpha = ["A","B","C","D","E","F","G","H","I","J","K"]
    for i in alpha:
        if i == letra:
            resultado = alpha.index(i) 
            return resultado
        else:
            pass


def bilheteria_mes(eventos,fila,lugar):
    total=0
    try:
        date = input("                                                                     Digite o mês que pretende consultar no formato MM-YYYY: ")
        str_date = datetime.strptime(date, '%m-%Y').date()
    except ValueError:
            print("-"*50)
            print("Formato da data inválido")
            print("-"*50)
            print("")
            return
    for i in eventos:
        if str_date.month==i[2].month:
            if str_date.year==i[2].year:
                sala=i[3]
                for j in sala:
                    for g in range(len(j)):
                        if j[g]== "\033[1;31mX\033[m":
                            total+=controller.valor_bilhete(sala.index(j),g)
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')  
    print("-"*40)      
    print(f" Os eventos do mês {i[2].month} tem o valor de {total}€")
    print("-"*40)
    print("")



def bilheteria_dia(eventos,fila,lugar):
    total=0
    try:
        date = input("                                                                     Digite o dia que pretende consultar no formato DD-MM-YYYY: ")
        print("")
        str_date = datetime.strptime(date, '%d-%m-%Y').date()
    except ValueError:
            print("-"*50)
            print("Formato da data inválido")
            print("-"*50)
            print("")
            return
    for i in eventos:
        if str_date.day==i[2].day:
            if str_date.month==i[2].month:
                if str_date.year==i[2].year:
                    sala=i[3]
                    for j in sala:
                        for g in range(len(j)):
                            if j[g]== "\033[1;31mX\033[m":
                                total+=controller.valor_bilhete(sala.index(j),g)
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    print("-"*50)
    print(f" Os eventos do dia {date} tem o valor de {total}€")
    print("-"*50)
    print("")
    return

def bilheteria_ano(eventos,fila,lugar):
    total=0
    try:
        date = input("                                                                     Digite o ano que pretende consultar no formato YYYY: ")
        str_date = datetime.strptime(date, '%Y').date()
    except ValueError:
            print("-"*50)
            print("Formato da data inválido")
            print("-"*50)
            print("")
            return
    for i in eventos:
        if str_date.year==i[2].year:
            sala=i[3]
            for j in sala:
                for g in range(len(j)):
                    if j[g]== "\033[1;31mX\033[m":
                        total+=controller.valor_bilhete(sala.index(j),g)
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    print("-"*45)
    print(f" Os eventos do ano {i[2].year} tem o valor de {total}€")
    print("-"*45)
    print("")



    #------------------*******************---------------------**PRINTS DOS MENUS**-----------------------*************************---------------------------

def plateia(sala:list):
    print("")
    print("                                              1   2         3    4    5    6    7    8    9    10   11  12        13   14")
    print("                                            ___  ___       ___  ___  ___  ___  ___  ___  ___  ___  ___  ___       ___  ___")
    print(f"                                        K  |_{sala[3][10][0]}_||_{sala[3][10][1]}_|     |_{sala[3][10][2]}_||_{sala[3][10][3]}_||_{sala[3][10][4]}_||_{sala[3][10][5]}_||_{sala[3][10][6]}_||_{sala[3][10][7]}_||_{sala[3][10][8]}_||_{sala[3][10][9]}_||_{sala[3][10][10]}_||_{sala[3][10][11]}_|     |_{sala[3][10][12]}_||_{sala[3][10][13]}_|")
    print("                                            ___  ___       ___  ___  ___  ___  ___  ___  ___  ___  ___  ___       ___  ___")
    print(f"                                        J  |_{sala[3][9][0]}_||_{sala[3][9][1]}_|     |_{sala[3][9][2]}_||_{sala[3][9][3]}_||_{sala[3][9][4]}_||_{sala[3][9][5]}_||_{sala[3][9][6]}_||_{sala[3][9][7]}_||_{sala[3][9][8]}_||_{sala[3][9][9]}_||_{sala[3][9][10]}_||_{sala[3][9][11]}_|     |_{sala[3][9][12]}_||_{sala[3][9][13]}_|")
    print("                                            ___  ___       ___  ___  ___  ___  ___  ___  ___  ___  ___  ___       ___  ___")
    print(f"                                        I  |_{sala[3][8][0]}_||_{sala[3][8][1]}_|     |_{sala[3][8][2]}_||_{sala[3][8][3]}_||_{sala[3][8][4]}_||_{sala[3][8][5]}_||_{sala[3][8][6]}_||_{sala[3][8][7]}_||_{sala[3][8][8]}_||_{sala[3][8][9]}_||_{sala[3][8][10]}_||_{sala[3][8][11]}_|     |_{sala[3][8][12]}_||_{sala[3][8][13]}_|")
    print("                                            ___  ___       ___  ___  ___  ___  ___  ___  ___  ___  ___  ___       ___  ___")
    print(f"                                        H  |_{sala[3][7][0]}_||_{sala[3][7][1]}_|     |_{sala[3][7][2]}_||_{sala[3][7][3]}_||_{sala[3][7][4]}_||_{sala[3][7][5]}_||_{sala[3][7][6]}_||_{sala[3][7][7]}_||_{sala[3][7][8]}_||_{sala[3][7][9]}_||_{sala[3][7][10]}_||_{sala[3][7][11]}_|     |_{sala[3][7][12]}_||_{sala[3][7][13]}_|")
    print("                                            ___  ___       ___  ___  ___  ___  ___  ___  ___  ___  ___  ___       ___  ___")
    print(f"                                        G  |_{sala[3][6][0]}_||_{sala[3][6][1]}_|     |_{sala[3][6][2]}_||_{sala[3][6][3]}_||_{sala[3][6][4]}_||_{sala[3][6][5]}_||_{sala[3][6][6]}_||_{sala[3][6][7]}_||_{sala[3][6][8]}_||_{sala[3][6][9]}_||_{sala[3][6][10]}_||_{sala[3][6][11]}_|     |_{sala[3][6][12]}_||_{sala[3][6][13]}_|")
    print("                                            ___  ___                      ___  ___  ___  ___                      ___  ___")
    print(f"                                        F  |_{sala[3][5][0]}_||_{sala[3][5][1]}_|              VIP ->|_{sala[3][5][5]}_||_{sala[3][5][6]}_||_{sala[3][5][7]}_||_{sala[3][5][8]}_|<- VIP              |_{sala[3][5][12]}_||_{sala[3][5][13]}_|")
    print("                                            ___  ___       ___  ___  ___  ___  ___  ___  ___  ___  ___  ___       ___  ___")
    print(f"                                        E  |_{sala[3][4][0]}_||_{sala[3][4][1]}_|     |_{sala[3][4][2]}_||_{sala[3][4][3]}_||_{sala[3][4][4]}_||_{sala[3][4][5]}_||_{sala[3][4][6]}_||_{sala[3][4][7]}_||_{sala[3][4][8]}_||_{sala[3][4][9]}_||_{sala[3][4][10]}_||_{sala[3][4][11]}_|     |_{sala[3][4][12]}_||_{sala[3][4][13]}_|")
    print("                                            ___  ___       ___  ___  ___  ___  ___  ___  ___  ___  ___  ___       ___  ___")
    print(f"                                        D  |_{sala[3][3][0]}_||_{sala[3][3][1]}_|     |_{sala[3][3][2]}_||_{sala[3][3][3]}_||_{sala[3][3][4]}_||_{sala[3][3][5]}_||_{sala[3][3][6]}_||_{sala[3][3][7]}_||_{sala[3][3][8]}_||_{sala[3][3][9]}_||_{sala[3][3][10]}_||_{sala[3][3][11]}_|     |_{sala[3][3][12]}_||_{sala[3][3][13]}_|")
    print("                                            ___  ___       ___  ___  ___  ___  ___  ___  ___  ___  ___  ___       ___  ___")
    print(f"                                        C  |_{sala[3][2][0]}_||_{sala[3][2][1]}_|     |_{sala[3][2][2]}_||_{sala[3][2][3]}_||_{sala[3][2][4]}_||_{sala[3][2][5]}_||_{sala[3][2][6]}_||_{sala[3][2][7]}_||_{sala[3][2][8]}_||_{sala[3][2][9]}_||_{sala[3][2][10]}_||_{sala[3][2][11]}_|     |_{sala[3][2][12]}_||_{sala[3][2][13]}_|")
    print("                                            ___  ___       ___  ___  ___  ___  ___  ___  ___  ___  ___  ___       ___  ___")
    print(f"                                        B  |_{sala[3][1][0]}_||_{sala[3][1][1]}_|     |_{sala[3][1][2]}_||_{sala[3][1][3]}_||_{sala[3][1][4]}_||_{sala[3][1][5]}_||_{sala[3][1][6]}_||_{sala[3][1][7]}_||_{sala[3][1][8]}_||_{sala[3][1][9]}_||_{sala[3][1][10]}_||_{sala[3][1][11]}_|     |_{sala[3][1][12]}_||_{sala[3][1][13]}_|")
    print("                                            ___  ___                      ___  ___  ___  ___                      ___  ___")
    print(f"                                        A  |_{sala[3][0][0]}_||_{sala[3][0][1]}_|              VIP ->|_{sala[3][0][5]}_||_{sala[3][0][6]}_||_{sala[3][0][7]}_||_{sala[3][0][8]}_|<- VIP              |_{sala[3][0][12]}_||_{sala[3][0][13]}_|")

    print("                                                    ______________________________________________________________")
    print("                                                   |                                                              |")
    print("                                                   |                            PALCO                             |")
    print("                                                   |                                                              |")
    print("                                                   |______________________________________________________________|")
    print("")


def menu_principal():

    print("                                                                            MENU PRINCIPAL")
    print("")
    print('''                                                                            [1] Utilizador
                                                                            [2] Administrador
                                                                            [3] Sair
                                                                     ''')
    print("")
    

def cabecalho():
    print("                                              \033[1;3;45m                                                                             \033[m")
    print("                                              \033[1;3;45m                               SALA DE ESPETÁCULOS                           \033[m")
    print("                                              \033[1;3;45m                                                                             \033[m")
    print("                                              \033[1;3;45m                                 JOAQUIM VIANA                               \033[m")
    print("                                              \033[1;3;45m                                                                             \033[m")
    print("")


def menu_utilizador():
    print("                                                                                   MENU UTILIZADOR")
    
    print("")
    
    print("")
    print('''                                                                    [1] Visualizar Espetáculos Disponiveis
                                                                    [2] Login
                                                                    [3] Registrar-se
                                                                    [4] Recuperar Password
                                                                    [5] Ajuda
                                                                    [6] Sair
                                                                    [0] Voltar ao Menu Anterior''')
    print("")
    

def menu_admin():
    print("                                                                                   MENU ADIMINSTRADOR")
    print("")
    print('''                                                                    [1] Visualizar Espetáculos Disponiveis
                                                                    [2] Visualizar Bilheteria
                                                                    [3] Inserir Evento
                                                                    [4] Ver a ocupação de um Evento
                                                                    [5] Excluir Evento
                                                                    [6] Sair
                                                                    [0] Voltar ao Menu Anterior''')
    print("")

def menu_bilheteira():
    print("                                                                                   MENU ADIMINSTRADOR")
    print("")
    print('''                                                                    [1] Visualizar valores de bilheteira num dia especifico
                                                                    [2] Visualizar valores de bilheteira num mês especifico
                                                                    [3] Visualizar valores de bilheteira num ano especifico
                                                                    [4] Sair
                                                                    [0] Voltar ao Menu Anterior''')
    print("")


def menu_online(user_online):
    print("                                                                                   MENU UTILIZADOR")
    if user_online != []: 
        print("")
        print("                                                                    SEJA BEM VINDO(A): ",''.join(user_online[0]).replace("'", ""))
    else:
        print("")
    
    print("")
    print('''                                                                    [1] Visualizar Espetáculos Disponiveis
                                                                    [2] Ver meus bilhetes
                                                                    [3] Comprar bilhetes
                                                                    [4] Compra Automática de Bilhetes
                                                                    [5] Eliminar reservas
                                                                    [6] Ajuda
                                                                    [7] Sair
                                                                    [0] Voltar ao Menu Anterior''')
