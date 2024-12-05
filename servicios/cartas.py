import random

mazo_usuario = []
usuario_movimientos = [
]

mazo_bot = []
bot_movimientos = [
]

puntos_bot = 0
puntos_user = 0

cartas_truco = [
    {"carta": "1 de espada", "valor": 14, "src": "recursos/cartas/1 de espada.jpg"},
    {"carta": "1 de basto", "valor": 13, "src": "recursos/cartas/1 de basto.jpg"},
    
    {"carta": "7 de espada", "valor": 12, "src": "recursos/cartas/7 de espada.jpg"},
    {"carta": "7 de oro", "valor": 11, "src": "recursos/cartas/7 de oro.jpg"},
    
    {"carta": "3 de espada", "valor": 10, "src": "recursos/cartas/3 de espada.jpg"},
    {"carta": "3 de basto", "valor": 10, "src": "recursos/cartas/3 de basto.jpg"},
    {"carta": "3 de oro", "valor": 10, "src": "recursos/cartas/3 de oro.jpg"},
    {"carta": "3 de copa", "valor": 10, "src": "recursos/cartas/3 de copa.jpg"},
    
    {"carta": "2 de espada", "valor": 9, "src": "recursos/cartas/2 de espada.jpg"},
    {"carta": "2 de basto", "valor": 9, "src": "recursos/cartas/2 de basto.jpg"},
    {"carta": "2 de copa", "valor": 9, "src": "recursos/cartas/2 de copa.jpg"},
    {"carta": "2 de oro", "valor": 9, "src": "recursos/cartas/2 de oro.jpg"},
    
    {"carta": "1 de copa", "valor": 8, "src": "recursos/cartas/1 de copa.jpg"},
    {"carta": "1 de oro", "valor": 8, "src": "recursos/cartas/1 de oro.jpg"},
    
    {"carta": "12 de copa", "valor": 7, "src": "recursos/cartas/12 de copa.jpg"},
    {"carta": "12 de espada", "valor": 7, "src": "recursos/cartas/12 de espada.jpg"},
    {"carta": "12 de basto", "valor": 7, "src": "recursos/cartas/12 de basto.jpg"},
    {"carta": "12 de oro", "valor": 7, "src": "recursos/cartas/12 de oro.jpg"},
    
    {"carta": "11 de copa", "valor": 6, "src": "recursos/cartas/11 de copa.jpg"},
    {"carta": "11 de espada", "valor": 6, "src": "recursos/cartas/11 de espada.jpg"},
    {"carta": "11 de basto", "valor": 6, "src": "recursos/cartas/11 de basto.jpg"},
    {"carta": "11 de oro", "valor": 6, "src": "recursos/cartas/11 de oro.jpg"},
    
    {"carta": "10 de copa", "valor": 5, "src": "recursos/cartas/10 de copa.jpg"},
    {"carta": "10 de espada", "valor": 5, "src": "recursos/cartas/10 de espada.jpg"},
    {"carta": "10 de basto", "valor": 5, "src": "recursos/cartas/10 de basto.jpg"},
    {"carta": "10 de oro", "valor": 5, "src": "recursos/cartas/10 de oro.jpg"},
    
    {"carta": "7 de copa", "valor": 4, "src": "recursos/cartas/7 de copa.jpg"},
    {"carta": "7 de basto", "valor": 4, "src": "recursos/cartas/7 de basto.jpg"},
    
    {"carta": "6 de espada", "valor": 3, "src": "recursos/cartas/6 de espada.jpg"},
    {"carta": "6 de basto", "valor": 3, "src": "recursos/cartas/6 de basto.jpg"},
    {"carta": "6 de copa", "valor": 3, "src": "recursos/cartas/6 de copa.jpg"},
    {"carta": "6 de oro", "valor": 3, "src": "recursos/cartas/6 de oro.jpg"},
    
    {"carta": "5 de espada", "valor": 2, "src": "recursos/cartas/5 de espada.jpg"},
    {"carta": "5 de basto", "valor": 2, "src": "recursos/cartas/5 de basto.jpg"},
    {"carta": "5 de copa", "valor": 2, "src": "recursos/cartas/5 de copa.jpg"},
    {"carta": "5 de oro", "valor": 2, "src": "recursos/cartas/5 de oro.jpg"},
    
    {"carta": "4 de espada", "valor": 1, "src": "recursos/cartas/4 de espada.jpg"},
    {"carta": "4 de basto", "valor": 1, "src": "recursos/cartas/4 de basto.jpg"},
    {"carta": "4 de copa", "valor": 1, "src": "recursos/cartas/4 de copa.jpg"},
    {"carta": "4 de oro", "valor": 1, "src": "recursos/cartas/4 de oro.jpg"},
]

#Tantos

# def envido(el_usuario_envio:bool=True):
#     evento_enviador(el_usuario_envio, {"event":"envido"})

# def real_envido(el_usuario_envio:bool=True):
#     evento_enviador(el_usuario_envio, {"event":"real_envido"})

# def falta_envido(el_usuario_envio:bool=True):
#     evento_enviador(el_usuario_envio, {"event":"falta_envido"})


#Truco

def truco(el_usuario_envio:bool=True):
    evento_enviador(el_usuario_envio, {"event":"truco"})


# def retruco(el_usuario_envio:bool=True):
#     evento_enviador(el_usuario_envio, {"event":"retruco"})


# def vale_cuatro(el_usuario_envio:bool=True):
#     evento_enviador(el_usuario_envio, {"event":"vale_cuatro"})

        
def enviar_carta(carta, el_usuario_envio:bool=True):
    evento_enviador(el_usuario_envio, {"event":"enviar_carta", "carta":carta})

        
#eventos a realizarse

def evento_enviador(el_usuario_envio, event:dict):
    if el_usuario_envio:
        usuario_movimientos.append(event)
    else:
        bot_movimientos.append(event)
    print(usuario_movimientos)
        

def cartas_aleatorias():
    
    cartas_en_juego = []
    cartas_cargadas = cartas_truco
    
    for carta in range(3):  
        try:
            indice_random = random.randrange(0, len(cartas_cargadas))
            carta_seleccionada = cartas_cargadas[indice_random]
            cartas_en_juego.append(carta_seleccionada)
        
            cartas_cargadas.pop(indice_random)

        except:
            print(len(cartas_cargadas))
        
    return cartas_en_juego

