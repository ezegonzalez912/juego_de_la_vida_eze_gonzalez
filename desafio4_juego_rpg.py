import argparse
import time

def escribir(texto, delay=0.03):
    for c in texto:
        print(c, end='', flush=True)
        time.sleep(delay)
    print()

def elegir(opciones):
    for i, op in enumerate(opciones, 1):
        print(f'  [{i}] {op}')
    while True:
        try:
            r = int(input('\n> '))
            if 1 <= r <= len(opciones):
                return r
        except ValueError:
            pass

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--nombre', default='Jugador')
args = parser.parse_args()

vida = 3
nombre = args.nombre

print()
escribir(f'Sos {nombre}, una molecula de ARN Polimerasa II.')
escribir('Tu mision: llegar al gen de la insulina y transcribirlo.')
escribir('El nucleo es un laberinto y el tiempo corre...')
input('\n[Enter para comenzar]\n')

# --- escena 1 ---
print('='*50)
escribir('\nLlegas a la cromatina. El gen esta empaquetado y no podes leerlo.')
escribir('Un complejo de histonas bloquea el acceso.\n')
r = elegir([
    'Esperas a que los factores de remodelacion abran la cromatina',
    'Intentas forzar el paso tu sola'
])
if r == 1:
    escribir('\nLos factores de remodelacion actuan y la cromatina se abre.')
    escribir('Encontras la region promotora: TATAAA.')
else:
    escribir('\nLa cromatina resiste. Perdes tiempo y una unidad de energia.')
    escribir('Terminas esperando igual... pero con un golpe en el orgullo.')
    vida -= 1

# --- escena 2 ---
print('\n' + '='*50)
escribir('\nEstas leyendo el molde de ADN y sintetizando el ARNm.')
escribir('De repente aparece un intrón disfrazado de exón.')
escribir('Quiere colarse en tu ARNm.\n')
r = elegir([
    'Lo dejas pasar, total despues se encarga el spliceosoma',
    'Lo identificas y lo marcas para que el spliceosoma lo elimine'
])
if r == 1:
    escribir('\nBuena decision estrategica. El spliceosoma corta el intron mas tarde.')
    escribir('El ARNm queda limpio igual.')
elif r == 2:
    escribir('\nExcelente. El ARNm sale del nucleo sin intrones, listo para traducirse.')

# --- escena 3 ---
print('\n' + '='*50)
escribir('\nEl ARNm cruza el poro nuclear y llega al ribosoma.')
escribir('Empieza la traduccion. Todo va bien hasta que...')
escribir('aparece un ARN de transferencia con el aminoacido EQUIVOCADO.\n')
r = elegir([
    'Confias en el ribosoma, el solo va a rechazar el tARN incorrecto',
    'Entras en panico y detenes la traduccion'
])
if r == 1:
    escribir('\nCorrecto. El ribosoma verifica el apareamiento de bases.')
    escribir('El tARN incorrecto no encaja y se va. La proteina se sintetiza bien.')
elif r == 2:
    escribir('\nLa traduccion se corta. La proteina queda incompleta y se degrada.')
    escribir('Hay que empezar de nuevo desde el ARNm.')
    vida -= 1

# --- escena final ---
print('\n' + '='*50)
escribir('\nEl codon STOP aparece en el ribosoma: UAA.')
escribir('La insulina esta lista. El ribosoma libera la proteina.')
print()

if vida == 3:
    escribir('Completaste la expresion genica sin errores. La celula te lo agradece.')
elif vida == 2:
    escribir('La insulina llego a destino, con algun tropiezo en el camino.')
else:
    escribir('La insulina existe, pero el camino estuvo lleno de obstaculos.')

print('\nADN -> transcripcion -> ARNm -> splicing -> traduccion -> Proteina\n')
