from ast import Break
from copy import copy, deepcopy
#from asyncio.windows_events import NULL
import random
from copy import deepcopy


def gerador_id():
    n = random.randrange(10,10000)
    return n


def criar_eventos(evento, str_data):
    id = gerador_id()
    evento = [id,evento,str_data,[[0,0,None,None,None,0,0,0,0,None,None,None,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,None,None,None,0,0,0,0,None,None,None,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0]]]
    return evento

def valida_id(id,eventos):
    for i in eventos:
        if id in i:
            return True
    return False

def valida_data(eventos, data_str):
    for i in eventos:
        if i[2] == data_str:
            return True
    return False
 
def compra_bilhete(id, utilizador, fila, lugar, utilizadores,eventos):
    lugares = [id,3,fila,lugar]
    if verifca_lugar(id,fila,lugar,eventos) == True:
        for i in utilizadores:
            if utilizador == i[1]:
                i.append(lugares)
                break
        return True    
    else:
        return False

def verifca_lugar(id,fila, lugar, eventos):
    for i in eventos:
        if id in i:
            if i[3][fila][lugar] == 0:
                return True
    else:
        return False



def login_user(nif,password,utilizadores):
    for i in utilizadores:
        if nif in i:
            if password == i[2]:
                return True
    return False


def excluir_evento(id, eventos):
    for i in eventos:
        if id == i[0]:
            eventos.remove(i)
            return True
    return False

def excluir_evento_utilizadores(id, utilizadores):
    tmp = deepcopy(utilizadores)
    for i in tmp:
        for g in range(3,len(i)):
            if id == i[g][0]:
                utilizadores[tmp.index(i)].remove(i[g])
            else:
                pass
    return

def verificar_acentos_evento(id,eventos):
    teste = "\033[1;31mX\033[m"
    for i in eventos:
        if id == i[0]:
            for g in i[3]:
                if teste in g:
                    return True
    return False


def registrar_user(nome,nif,password):
    utilizador = [nome,nif,password]
    return utilizador


def valor_bilhete(fila,lugar):
    if fila == 0 or fila == 5:
        vip=[5,6,7,8]
        if lugar in vip:
            valor = 12
            return valor
        else:
            valor = 4
            return valor
    else:
        valor = 4
        return valor


def teste(id,user_online,utilizadores,eventos):
    for i in utilizadores:
        if user_online[1] in i:
            tmp=i.copy()
            for j in range(3,len(tmp)):
                fila=tmp[j][2]
                lugar=tmp[j][3]
                if id in tmp[j]:
                    i.remove(tmp[j])
                    tudo_normal(eventos,fila,lugar,id)

    return True

def tudo_normal(eventos,fila,lugar,id):
    for i in eventos:
        if id in i:
            i[3][fila][lugar] = 0
            return True


def valida_id(id,eventos):
    for i in eventos:
        if id in i:
            return True
    return False

def compra_bilhete(id, utilizador, fila, lugar, utilizadores,eventos):
    lugares = [id,3,fila,lugar]
    if verifca_lugar(id,fila,lugar,eventos) == True:
        for i in utilizadores:
            if utilizador == i[1]:
                i.append(lugares)
                break
        return True    
    else:
        return False

def verifca_lugar(id,fila, lugar, eventos):
    for i in eventos:
        if id in i:
            if i[3][fila][lugar] == 0:
                return True
    else:
        return False

def valida_nif(nif, utilizadores):
    for i in utilizadores:
        if nif in i:
            return True
        else:
            return False


def login_user(nif,password,utilizadores):
    for i in utilizadores:
        if nif in i[1]:
            if password == i[2]:
                return True
    return False

def registrar_user(nome,nif,password):
    utilizador = [nome,nif,password]
    return utilizador



def teste(id,user_online,utilizadores,eventos):
    for i in utilizadores:
        if user_online[1] in i:
            tmp=i.copy()
            for j in range(3,len(tmp)):
                fila=tmp[j][2]
                lugar=tmp[j][3]
                if id in tmp[j]:
                    i.remove(tmp[j])
                    tudo_normal(eventos,fila,lugar,id)

    return True

def tudo_normal(eventos,fila,lugar,id):
    for i in eventos:
        if id in i:
            i[3][fila][lugar] = 0
            return True

