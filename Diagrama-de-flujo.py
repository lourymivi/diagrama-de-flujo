print ("Bienvenido(a) a REPARA TU MOTO\n")
print ("Las decisiones que tomes durante el juego te llevaran a arreglar o dañar tu moto\n")
nombre = input ("Ingresa tu nombre: ")
print ("\nQue comience el juego!\n")
print ("*REGLA: Recuerda contestar las preguntas en MAYUSCULA y con la palabra indicada en cada opciOn que se encuentra escrita tambiEn en MAYUSCULA*\n")
print ("> CapÃ­tulo 1")
print (nombre + ", vas en tu moto camino a tu casa y se te parte la cadena debes hacer algo antes que caiga la noche. Tienes dos opciones para solucionar el problema\n")
print ("- 1ra: Desplazarte hacia la DERECHA en busca de ayuda.")
print ("- 2da: Desplazarte hacia la IZQUIERDA y buscar tu kit de herramientas")

intento = 0
while (intento == 0):
    direccion = input ("\nÂ¿QuÃ© direcciÃ³n escoges?: ")
    if direccion == ("IZQUIERDA"):
        print ("\nÂ¡Que bien " + nombre + "!" + " tienes el kit vamos a reparar\n")
        intento = -1


        print ("> CapÃ­tulo 2")
        print (nombre + ", en el kit encontraras varias herramientas debes elegir una de ellas para reparar la averia\n")
        print ("- 1ra: DESTORNILLADOR")
        print ("- 2da: DESPINADOR")
        print ("- 3ra: PRENSA")


        intento = 0
        while (intento == 0):
            color = input ("\nÂ¿Que herramienta escoges?: ")
            if color == ("DESPINADOR"):
                print ("\nÂ¡Que bien " + nombre + "!" + " comencemos la reparacion de la cadena\n")
                intento = -1


                print ("> CapÃ­tulo 3")
                print ("Vas por el camino correcto ya casis terminas la reparacion. " + nombre + ", notas que la cadena esta muy larga para la moto ¿que haras?")
                print ("- 1ra: AJUSTARLA al largo correcto")
                print ("- 2da: COLOCARLA asi")


                intento = 0
                while (intento == 0):
                    arma = input ("\nÂ¿Que opcion tomaras?: ")
                    if arma == ("AJUSTARLA"):
                        print ("\nÂ¡Que bien " + nombre + "!" + " estas mas cerca de arreglar la moto, te esta quedando bien la cadena\n")
                        intento = -1


                        print ("> CapÃ­tulo Final")
                        print ("Lograste ajustar la cadena.")
                        print ("debes probarla ahora. Asi­ que te planteas dos opciones\n")
                        print ("- 1ra: Deberias VALIDAR los ajustes realizados")
                        print ("- 2da: Deberias ARRANCAR la moto enseguida")


                        intento = 0
                        while (intento == 0):
                            accion = input ("\nÂ¿Que decides hacer?: ")
                            if accion == ("VALIDAR"):
                                print ("\nÂ¡" + nombre + " GANASTE! Excelemnte hiciste un buen trabajo\n")
                                intento = -1
                            elif accion == ("ARRANCAR"):
                                print ("\nPERDISTE: " + nombre + ", No estaba buen ajustada la cadena y se volvio a partir")
                                intento = -2
                            else:
                                   print ("\n*Entrada invalida*")


                    elif arma == ("COLOCARLA"):
                        print ("\nPERDISTE: La cadena no se ajusta por el largo" + nombre)
                        intento = -2
                    else:
                        print ("\n*Entrada invalida*")


            elif color == ("DESTORNILLADOR"):
                print ("\nPERDISTE: " + nombre + " esta herramienta no es la indicada para arreglar la cadena")
                intento = -2
            elif color == ("PRENSA"):
                print ("\nPERDISTE: " + nombre + " Doblaste la cadena y ya no te sirve")
                intento = -3
            else:
                print ("\n*Entrada invalida*")

    elif direccion == ("DERECHA"):
        print ("\nPERDISTE: " + nombre + " Estas en un camino solitario nadie puede ayudarte")
    intento = -2