import numpy as np
import os


os.system('clear')

"""
2X1 + 4X2 + 3X3  = Z
3X1 + 4X2 + 2X3 <= 60
2X1 +  X2 + 2X3 <= 40
 X1 + 3X2 + 2X3 <= 80
"""

def getvals(cad):
    #2X1 + 4X2 + 3X3
    cad = cad.lower().replace('+', '#+').replace('-', '#-').split('#')



#tinput = [1]

#print('Ingrese los siguientes datos:')
#z1 = input('Z = ')

tinput = np.array(
    [
        [1, -2, -4, -3, 0, 0, 0, 0],
        [0, 3, 4, 2, 1, 0, 0, 60],
        [0, 2, 1, 2, 0, 1, 0, 40],
        [0, 1, 3, 2, 0, 0, 1, 80]
    ]
).astype(np.float32)

initr = 3
rowsname = [f'X{i + initr}' for i in range(tinput.shape[0])]
rowsname[0] = 'Z'


c = 1
while np.min(tinput[0]) < 0:
    print('-'*20, f'iteracion {c}', '-'*20)
    print('\tZ\t', '\t'.join([f'X{i+1}' for i in range(tinput.shape[1]-2)]), '\tR')

    k = 0
    for i in range(tinput.shape[0]):
        print(rowsname[k], '\t', ''.join(f'{np.round(v*1000)/1000}\t' for v in tinput[i]))
        k += 1

    idxcolpiv = np.argmin(tinput[0])
    idxfilpiv = np.argmin(tinput[1:, -1] / tinput[1:, idxcolpiv]) + 1
    valpiv = tinput[idxfilpiv, idxcolpiv]

    print(f'Columna pivote: {tinput[:, idxcolpiv]}')
    print(f'Fila pivote: {tinput[idxfilpiv]}')
    print(f'Valor pivote: {valpiv}')

    rowsname[idxfilpiv] = f'X{idxcolpiv}'
    tinput[idxfilpiv] = tinput[idxfilpiv] / valpiv

    # nueva = lambda fv, pf, fn: fv-(pf*fn)

    for i in range(tinput.shape[0]):
        if i != idxfilpiv:
            tinput[i] = tinput[i] - (tinput[i, idxcolpiv] * tinput[idxfilpiv])

    #input('\nProseguir con la siguiente iteracion?\n\n')
    print('\n\n')
    c += 1


print('-'*20, f'iteracion {c}', '-'*20)
print('\tZ\t', '\t'.join([f'X{i+1}' for i in range(tinput.shape[1]-2)]), '\tR')

k = 0
for i in range(tinput.shape[0]):
    print(rowsname[k], '\t', ''.join(f'{np.round(v*1000)/1000}\t' for v in tinput[i]))
    k += 1
