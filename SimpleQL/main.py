import json
import re
import os
import webbrowser



while(True):


    print("Ingrese un comando:")
    comando = input()
    Palabra = comando.split()
    Palabra2 = comando.split(',')
    A1 = Palabra2[0].lower().lstrip("cargar").lstrip("")
    Palabra2[0] = A1
    Condicion = False
    NR = True
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
    C6 = "Suma"
    C7 = "Cuenta"
    C8 = "Reportar"
    DN = False
    DE = False
    DA = False
    DP = False
    DM = False







    if (Palabra[0].lower() == C1.lower()):
        ruta = Palabra2[0].lstrip()
        if (ruta.endswith(".json")):
            NR = True
        else:
            ruta = ruta + ".json"


        with open(ruta) as contenido:
            dict = json.load(contenido)
        for i in range(len(Palabra2)):
            if(i!=0):
                ruta = Palabra2[i].lstrip()
                if(ruta.endswith(".json")):
                    NR = True
                else:
                    ruta = ruta + ".json"
                with open(ruta) as contenido:
                    dict2 = json.load(contenido)
                    dict = dict+dict2
        print("Archivos cargados a memoria")



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
                        print("-----------------------")

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
                        print("-----------------------")

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
                        print("-----------------------")

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
                        print("-----------------------")

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
                    print("-----------------------")

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

    if (Palabra[0].lower() == C6.lower()):
        if(Palabra[1].lower() == C3E.lower()):
            Edades = []
            for dict3 in dict:
                Edades.append(dict3.get('edad'))
            print("Suma de las edades: ", sum(Edades))
        elif (Palabra[1].lower() == C3P.lower()):
            Promedios = []
            for dict3 in dict:
                Promedios.append(dict3.get('promedio'))
            print("Suma de los promedios: ", sum(Promedios))

    if (Palabra[0].lower() == C7.lower()):
        Registros = []
        for dict3 in dict:
                Registros.append(dict3.get('nombre'))
        print("Numero total de registros:", len(Registros))

    if (Palabra[0].lower() == C8.lower()):
        datos = ""
        contador = 0
        for dict3 in dict:
            if (contador!=int(Palabra[1])):
                datos += "<tr>\n"
                datos += "<th scope=\"row\">" + str(contador) + "</th>\n"
                datos += "<td>" + dict3.get('nombre') + "</td>\n"
                datos += "<td>" + str(dict3.get('edad')) + "</td>\n"
                datos += "<td>" + str(dict3.get('activo')) + "</td>\n"
                datos += "<td>" + str(dict3.get('promedio')) + "</td>\n"
                datos += "</tr>\n"
                contador = contador + 1


        html_str = """
        <!DOCTYPE html>
        <html>
        <head>
          <title>Reporte</title>
           <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
        </head>
        <body>
        <table class="table table-hover table-dark">
          <thead>
            <tr>
              <th scope="col">Numero</th>
              <th scope="col">Nombre</th>
              <th scope="col">Edad</th>
              <th scope="col">Activo</th>
              <th scope="col">Promedio</th>
            </tr>
          </thead>
          <tbody>
          
          
          """+datos+"""    

          </tbody>
        </table>
        </body>
        </html>

        """

        Html_file = open("Reporte.html", "w")
        Html_file.write(html_str)
        Html_file.close()

        url = 'file://' + os.path.realpath('Reporte.html')

        webbrowser.open(url, new=2)
        print("Reporte creado, se abrira en el navegador")
