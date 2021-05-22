
def calcularCodifNca(bloqueKLetras, alfyCodNca):
    listaCN = []
    
    for simbolo in bloqueKLetras:
        for letra, numero in alfyCodNca.items():
            if simbolo == letra:
                listaCN.append(numero)

    return listaCN

def codifNcaEstandar(modulo):

    cne = []

    #el modulo es la longitud del alfabeto. La codificación numérica estándar empezaría en el 0 e iría hasta el N-1 incluido
    for i in range(modulo):
        cne.append(i)

    return cne

def ecuacionDeRecurrencia(codNCA, mensajeEnClaro, N):

    claveExtendida = []
    ecRecParcial = 0


    for caracter in range(0, len(mensajeEnClaro)): #marca las posiciones a completar de la extendida
        ecRecParcial = 0
        i = len(codNCA)-1
        if(caracter < len(codNCA)): #para poner la codNCA directamente en la extendida
            claveExtendida.append(codNCA[caracter])
            continue

        for num in range(1, len(codNCA)+1):    
            ecRecParcial = ecRecParcial + codNCA[i]*claveExtendida[caracter-num]
            i = i - 1 
                
        claveExtendida.append((ecRecParcial)%N)
        

    print(claveExtendida)
    return claveExtendida

def DesCifradoVarianteVigenere(codNCA, opuestoClaveExtendida, N):

    mensajeDesCifrado = []

    for i in range(0, len(codNCA)):
        mensajeDesCifrado.append((codNCA[i]+opuestoClaveExtendida[i])%N)

    print(mensajeDesCifrado)
    return mensajeDesCifrado

def calcularSimbolosDeCadaBloque(MsjCifradoNumerico):
    C = ""
    
    for num in MsjCifradoNumerico:
        for letra, numero in alfyCodNca.items():
            if num == numero:
                C = C + letra


    return C

def calcularClaveOpuestaDescifrado(claveExtendida, N):

    opuestoClaveExtendida = []

    for i in claveExtendida:
        opuestoClaveExtendida.append((i*(-1))%N) #calculo el opuesto de cada numero de la clave extendida en modulo N y lo guardo en la clave extendida opuesta

    return opuestoClaveExtendida



alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ ÁÉÍÓÚ"
N = len(alfabeto) #numero de simbolos del alfabeto
mensajeCifrado = "EAMGCÍGJKTLÁRMKZÓXÚÉÓQBÓIGÉÍY" #C
clave_vigenere_Claro = "MARTES" #K

#Preparo la codificacion numerica asociada al alfabeto
codifNcaEstandar = codifNcaEstandar(N)

#Junto el alfabeto y la codificacion numerica en una misma estructura diccionario
alfyCodNca = {alfabeto[i]: codifNcaEstandar[i] for i in range(len(alfabeto))}


codNCAK = calcularCodifNca(clave_vigenere_Claro, alfyCodNca)

claveExtendida = ecuacionDeRecurrencia(codNCAK, mensajeCifrado, N)

codNCAMsj = calcularCodifNca(mensajeCifrado, alfyCodNca)

opuestoClaveExtendida = calcularClaveOpuestaDescifrado(claveExtendida, N) #necesitaremos restar para descifrar, que es multiplicar por el opuesto


MsjDesCifradoNumerico = DesCifradoVarianteVigenere(codNCAMsj, opuestoClaveExtendida, N)

MsjDesCifradoLetras = calcularSimbolosDeCadaBloque(MsjDesCifradoNumerico)

print()

print("\n======================================================================")
print("MENSAJE EN CLARO M:")
print(MsjDesCifradoLetras + "|FinMSJ")
print("======================================================================")

print("\nFIN DEL PROGRAMA")




