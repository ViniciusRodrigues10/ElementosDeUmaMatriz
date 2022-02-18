quantlinhasEColunas = str(input()).split()
quantLinhas = int(quantlinhasEColunas[0])
quantColunas = int(quantlinhasEColunas[1])

if quantLinhas > 0 and quantColunas > 0:
    valoresPositivos = 0
    valoresNegativos = 0
    matriz = []
    for i in range(quantLinhas):
        linhas = []
        for j in range(quantColunas):
            valores = int(input())
            if valores > 0:
                valoresPositivos += 1
            elif valores < 0:
                valoresNegativos += 1
            linhas.append(valores)
        matriz.append(linhas)

    print("Matriz formada:")
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j != (len(matriz[i]) - 1):
                print(matriz[i][j], end = " ")
            else:
                print(matriz[i][j])

    diagonalPrincipal = 0
    diagonalSecundaria = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i == j:
                diagonalPrincipal += matriz[i][j]
            if j == quantColunas - (i + 1):
                diagonalSecundaria += matriz[i][j]

    if quantLinhas == quantColunas:
        print(f"A diagonal principal e secundaria tem valor(es) {diagonalPrincipal} e {diagonalSecundaria} respectivamente.")
    else:
        print("A diagonal principal e secundaria nao pode ser obtida.")
    print(f"A matriz possui {valoresNegativos} numero(s) menor(es) que zero.")
    print(f"A matriz possui {valoresPositivos} numero(s) maior(es) que zero.")

else:
    print("Matriz formada:\nA diagonal principal e secundaria nao pode ser obtida.\nA matriz possui 0 "
          "numero(s) menor(es) que zero.\nA matriz possui 0 numero(s) maior(es) que zero.")