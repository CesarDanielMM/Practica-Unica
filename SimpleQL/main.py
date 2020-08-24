import json
import re




while(True):


    print("Ingrese un comando de SimpleQl")
    comando = input()
    Palabra = comando.split()
    Palabra2 = comando.split(',')
    A1 = Palabra2[0].lower().lstrip("cargar").lstrip("")
    Palabra2[0] = A1
    Condicion = False
    C1 = "Cargar"
    C2 = "Seleccionar"
    C3 = "Donde"
    C3N = "Nombre"
    C3E = "Edad"
    C3A = "Activo"
    C3P = "Promedio"
    C3M = "*"
    C4 = "Maximo"
    C5 = "Minimo"
    DN = False
    DE = False
    DA = False
    DP = False
    DM = False







    if (Palabra[0].lower() == C1.lower()):
        ruta = Palabra2[0].lstrip()

        with open(ruta) as contenido:
            dict = json.load(contenido)
        for i in range(len(Palabra2)):
            if(i!=0):
                ruta = Palabra2[i].lstrip()
                with open(ruta) as contenido:
                    dict2 = json.load(contenido)
                    dict = dict+dict2



    if (Palabra[0].lower() == C2.lower()):

        for j in range(len(Palabra)):
            if(Palabra[j].lower() == C3.lower()):

                Condicion = True
                PosicionC = j

        if (Condicion == True):
            x = 0
            while (Palabra[x].lower() != C3.lower()):
                if (Palabra[x].lower().replace(',', '') == C3N.lower()):
                    DN = True
                elif (Palabra[x].lower().replace(',', '') == C3E.lower()):
                    DE = True
                elif (Palabra[x].lower().replace(',', '') == C3A.lower()):
                    DA = True
                elif (Palabra[x].lower().replace(',', '') == C3P.lower()):
                    DP = True
                elif (Palabra[x].lower().replace(',', '') == C3M.lower()):
                    DM = True
                x = x + 1

            if (Palabra[PosicionC + 1].lower() == C3N.lower()):

                NombreIngresado = re.findall(r"(?:\".*?\")", comando)
                for dict3 in dict:
                    NombreABuscar = dict3.get('nombre')

                    if (NombreABuscar == NombreIngresado[0][1: -1]):

                        if (DN == True):
                            print("nombre: ", dict3.get('nombre'))
                        if (DE == True):
                            print("edad: ", dict3.get('edad'))
                        if (DA == True):
                            print("activo: ", dict3.get('activo'))
                        if (DP == True):
                            print("promedio: ", dict3.get('promedio'))
                        if (DM == True):
                            print("nombre: ", dict3.get('nombre'))
                            print("edad: ", dict3.get('edad'))
                            print("activo: ", dict3.get('activo'))
                            print("promedio: ", dict3.get('promedio'))

            elif (Palabra[PosicionC + 1].lower() == C3E.lower()):

                EdadIngresada = Palabra[PosicionC + 3]
                for dict3 in dict:
                    EdadABuscar = dict3.get('edad')



                    if (str(EdadABuscar) == str(EdadIngresada)):


                        if (DN == True):
                            print("nombre: ", dict3.get('nombre'))
                        if (DE == True):
                            print("edad: ", dict3.get('edad'))
                        if (DA == True):
                            print("activo: ", dict3.get('activo'))
                        if (DP == True):
                            print("promedio: ", dict3.get('promedio'))
                        if (DM == True):
                            print("nombre: ", dict3.get('nombre'))
                            print("edad: ", dict3.get('edad'))
                            print("activo: ", dict3.get('activo'))
                            print("promedio: ", dict3.get('promedio'))

            elif (Palabra[PosicionC + 1].lower() == C3A.lower()):

                ActivoIngresado = Palabra[PosicionC + 3]
                for dict3 in dict:
                    ActivoABuscar = dict3.get('activo')



                    if (str(ActivoABuscar) == str(ActivoIngresado)):


                        if (DN == True):
                            print("nombre: ", dict3.get('nombre'))
                        if (DE == True):
                            print("edad: ", dict3.get('edad'))
                        if (DA == True):
                            print("activo: ", dict3.get('activo'))
                        if (DP == True):
                            print("promedio: ", dict3.get('promedio'))
                        if (DM == True):
                            print("nombre: ", dict3.get('nombre'))
                            print("edad: ", dict3.get('edad'))
                            print("activo: ", dict3.get('activo'))
                            print("promedio: ", dict3.get('promedio'))

            elif (Palabra[PosicionC + 1].lower() == C3P.lower()):

                PromedioIngresado = Palabra[PosicionC + 3]
                for dict3 in dict:
                    PromediooABuscar = dict3.get('promedio')



                    if (str(PromediooABuscar) == str(PromedioIngresado)):


                        if (DN == True):
                            print("nombre: ", dict3.get('nombre'))
                        if (DE == True):
                            print("edad: ", dict3.get('edad'))
                        if (DA == True):
                            print("activo: ", dict3.get('activo'))
                        if (DP == True):
                            print("promedio: ", dict3.get('promedio'))
                        if (DM == True):
                            print("nombre: ", dict3.get('nombre'))
                            print("edad: ", dict3.get('edad'))
                            print("activo: ", dict3.get('activo'))
                            print("promedio: ", dict3.get('promedio'))

        else:
            for y in range(len(Palabra)):
                if (Palabra[y].lower().replace(',', '') == C3N.lower()):
                    DN = True
                elif (Palabra[y].lower().replace(',', '') == C3E.lower()):
                    DE = True
                elif (Palabra[y].lower().replace(',', '') == C3A.lower()):
                    DA = True
                elif (Palabra[y].lower().replace(',', '') == C3P.lower()):
                    DP = True
                elif (Palabra[y].lower().replace(',', '') == C3M.lower()):
                    DM = True
            for dict3 in dict:
                    if (DN == True):
                        print("nombre: ", dict3.get('nombre'))
                    if (DE == True):
                        print("edad: ", dict3.get('edad'))
                    if (DA == True):
                        print("activo: ", dict3.get('activo'))
                    if (DP == True):
                        print("promedio: ", dict3.get('promedio'))
                    if (DM == True):
                        print("nombre: ", dict3.get('nombre'))
                        print("edad: ", dict3.get('edad'))
                        print("activo: ", dict3.get('activo'))
                        print("promedio: ", dict3.get('promedio'))

    if (Palabra[0].lower() == C4.lower()):
        if(Palabra[1].lower() == C3E.lower()):
            Edades = []
            for dict3 in dict:
                Edades.append(dict3.get('edad'))
            print("Valor maximo de edad: ", max(Edades))
        elif (Palabra[1].lower() == C3P.lower()):
            Promedios = []
            for dict3 in dict:
                Promedios.append(dict3.get('promedio'))
            print("Valor maximo de promedio: ", max(Promedios))

    if (Palabra[0].lower() == C5.lower()):
        if(Palabra[1].lower() == C3E.lower()):
            Edades = []
            for dict3 in dict:
                Edades.append(dict3.get('edad'))
            print("Valor minimo de edad: ", min(Edades))
        elif (Palabra[1].lower() == C3P.lower()):
            Promedios = []
            for dict3 in dict:
                Promedios.append(dict3.get('promedio'))
            print("Valor minimo de promedio: ", min(Promedios))























