import random
import sys
import time
import os

#funcion para limpiar la consola
def limpiar_consola():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

limpiar_consola()
time.sleep(1)

print("!ESTO ES PIEDRA PAPEL O TIJERA¡ \n")
time.sleep(2)

nombre_jugador = str(input(" Cual es tu primer nombre? : "))

#Variables marcadores
marcador_sis= 0
marcador_jug= 0
while marcador_sis <= 3 or marcador_jug <= 3:
    limpiar_consola()

    #Variables selectores
    selector_sis= random.choice(["piedra", "papel", "tijera"])
    selector_jug= int(input("""
    Haz tu selección con numeros, estas son tus opciones...
    1.piedra
    2.papel
    3.tijera
    =  """))
    limpiar_consola()

    #Validador de palabras invalidas 
    if selector_jug < 1 or selector_jug > 3:
        print("!Esta opcion no esta en el rango solicitado")
        time.sleep(2)
        continue
    #Selector de ganador 
    elif selector_sis == "piedra" and selector_jug == 1:
        print(f"""
        sistema= {selector_sis} 
        {nombre_jugador}= piedra 
        
        !EMPATE¡ \n""")
        time.sleep(2)
        limpiar_consola()
        
    elif selector_sis == "papel" and selector_jug == 2:
        print(f"""
        sistema= {selector_sis}
        {nombre_jugador}= papel 
        
        !EMPATE¡ \n""")
        time.sleep(2)
        limpiar_consola()
        
    elif selector_sis == "tijera" and selector_jug == 3:
        print(f"""
        sistema= {selector_sis} 
        {nombre_jugador}= tijera 
        
        !EMPATE¡ \n""")
        time.sleep(2)
        limpiar_consola()

    elif selector_sis == "piedra" and selector_jug == 2:
        print(f"""
        sistema= {selector_sis} 
        {nombre_jugador}= papel 
        
        !RONDA DE {nombre_jugador.upper()}¡ \n""")
        marcador_jug+=1
        time.sleep(2)
        limpiar_consola()

    elif selector_sis == "piedra" and selector_jug == 3:
        print(f"""
        sistema= {selector_sis} 
        {nombre_jugador}= tijera 
        
        !RONDA DE SISTEMA¡ \n""")
        marcador_sis+=1
        time.sleep(2)
        limpiar_consola()

    elif selector_sis == "papel" and selector_jug == 1:
        print(f"""
        sistema= {selector_sis} 
        {nombre_jugador}= piedra
        
        !RONDA DE SISTEMA¡ \n""")
        marcador_sis+=1
        time.sleep(2)
        limpiar_consola()
 
    elif selector_sis == "papel" and selector_jug == 3:
        print(f"""
        sistema= {selector_sis} 
        {nombre_jugador}= tijera 
        
        !RONDA DE {nombre_jugador.upper()}¡ \n""")
        marcador_jug+=1
        time.sleep(2)
        limpiar_consola()

    elif selector_sis == "tijera" and selector_jug == 1:
        print(f"""
        sistema= {selector_sis} 
        {nombre_jugador}= piedra
        
        !RONDA DE {nombre_jugador.upper()}¡ \n""")
        marcador_jug+=1
        time.sleep(2)
        limpiar_consola()

    elif selector_sis == "tijera" and selector_jug == 2:
        print(f"""
        sistema= {selector_sis} 
        {nombre_jugador}= papel 
        
        !RONDA DE SISTEMA¡ \n""")
        marcador_sis+=1
        time.sleep(2)
        limpiar_consola()

    print(f"""
         !MARCADOR¡
    Sistema: {marcador_sis} puntos 
    {nombre_jugador}: {marcador_jug} puntos \n""")
    time.sleep(2)

    if marcador_jug == 3:
        print(f"!!Ganador {nombre_jugador}¡¡ felicitaciones")
        time.sleep(2)
        limpiar_consola()
        break
        
    elif marcador_sis == 3:
        print("!!El sistema te ha ganado¡¡")
        time.sleep(2)
        limpiar_consola()
        break
time.sleep(1)
print("MUCHAS GRACIAS POR JUGAR ESTE JUEGO")
time.sleep(3)