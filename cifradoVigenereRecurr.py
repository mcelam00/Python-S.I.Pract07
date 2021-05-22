
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

def cifradoVarianteVigenere(codNCA, claveExtendida, N):

    mensajeCifrado = []

    for i in range(0, len(codNCA)):
        mensajeCifrado.append((codNCA[i]+claveExtendida[i])%N)

    print(mensajeCifrado)
    return mensajeCifrado

def calcularSimbolosDeCadaBloque(MsjCifradoNumerico):
    C = ""
    
    for num in MsjCifradoNumerico:
        for letra, numero in alfyCodNca.items():
            if num == numero:
                C = C + letra


    return C




alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ ÁÉÍÓÚ"
N = len(alfabeto) #numero de simbolos del alfabeto
mensajeEnClaro = "CADA VEZ QUE CIFRO CAMBIO LA CLAVE" #M
clave_vigenere = "ENIGMA" #K

#Preparo la codificacion numerica asociada al alfabeto
codifNcaEstandar = codifNcaEstandar(N)

#Junto el alfabeto y la codificacion numerica en una misma estructura diccionario
alfyCodNca = {alfabeto[i]: codifNcaEstandar[i] for i in range(len(alfabeto))}


codNCAK = calcularCodifNca(clave_vigenere, alfyCodNca)

claveExtendida = ecuacionDeRecurrencia(codNCAK, mensajeEnClaro, N)

codNCAMsj = calcularCodifNca(mensajeEnClaro, alfyCodNca)


MsjCifradoNumerico = cifradoVarianteVigenere(codNCAMsj, claveExtendida, N)

MsjCifradoLetras = calcularSimbolosDeCadaBloque(MsjCifradoNumerico)

print()

print("\n======================================================================")
print("MENSAJE CIFRADO C:")
print(MsjCifradoLetras + "|FinMSJ")
print("======================================================================")

print("\nFIN DEL PROGRAMA")




