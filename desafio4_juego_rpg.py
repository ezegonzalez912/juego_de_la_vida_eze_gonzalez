import argparse
import time

def escribir(texto, delay=0.025):
    for c in texto:
        print(c, end='', flush=True)
        time.sleep(delay)
    print()

def menu(pregunta, opciones):
    print(pregunta)
    for i, op in enumerate(opciones, 1):
        print(f'  [{i}] {op}')
    while True:
        try:
            r = int(input('\n> '))
            if 1 <= r <= len(opciones):
                return r
        except ValueError:
            pass
        print('Ingresa un numero valido')

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--nombre', default='Jugador')
args = parser.parse_args()
nombre = args.nombre
aciertos = 0

print('\n' + '='*55)
escribir(f'\nBienvenido/a, {nombre}.')
escribir('Sos una molecula de ARN Polimerasa II recien activada.')
escribir('Mision: transcribir el gen de la insulina.')
input('\n[Enter para comenzar]\n')

# escena 1 - promotor
print('='*55)
print('\nESCENA 1 - El promotor\n')
escribir('Llega a la region promotora. Tres secuencias candidatas.')
escribir('Tenes que identificar la caja TATA para unirte.\n')

r = menu('Cual es la caja TATA?', ['ATCGAT', 'TATAAA', 'GCGCGC'])
if r == 2:
    escribir('Correcto! Te unis al promotor.')
    aciertos += 1
else:
    escribir('No es esa. La correcta es TATAAA.')

# escena 2 - transcripcion
print('\n' + '='*55)
print('\nESCENA 2 - Transcripcion\n')
escribir('Empezas a leer el ADN molde y sintetizar el ARNm.')
escribir('Molde: 3\'-TACGGGCTA-5\'')
escribir('(recordá: en ARN la T se reemplaza por U)\n')

r = menu('Cual es el ARNm resultante?', ['AUGCCCGAU', 'TACGGGCTA', 'ATGCCCGAT'])
if r == 1:
    escribir('Perfecto! ARNm: 5\'-AUGCCCGAU-3\'')
    aciertos += 1
else:
    escribir('Regla: A->U, T->A, G->C, C->G. El ARNm es AUGCCCGAU.')

# escena 3 - splicing
print('\n' + '='*55)
print('\nESCENA 3 - Procesamiento (splicing)\n')
escribir('El ARNm tiene intrones que hay que sacar.')
escribir('ARNm pre-procesado: [exon1] - [INTRON] - [exon2]\n')

r = menu('Que partes se conservan en el ARNm maduro?', ['Los intrones', 'Los exones', 'Ambos'])
if r == 2:
    escribir('Exacto! Los exones se unen y el ARNm sale del nucleo.')
    aciertos += 1
else:
    escribir('Los intrones se eliminan. Los exones son los que codifican.')

# escena 4 - traduccion
print('\n' + '='*55)
print('\nESCENA 4 - Traduccion\n')
escribir('El ARNm llega al ribosoma en el citoplasma.')
escribir('Se lee de 5\' a 3\' en grupos de 3 nucleotidos (codones).')
escribir('\nARNm: AUG-CCU-GAA-UAA')
escribir('AUG=Met(inicio)  CCU=Pro  GAA=Glu  UAA=STOP\n')

r = menu('Cual es la proteina resultante?', ['Met-Pro-Glu', 'Pro-Glu-Met', 'Met-Pro-Glu-STOP'])
if r == 1:
    escribir('Correcto! El codon STOP termina la sintesis pero no se traduce.')
    aciertos += 1
else:
    escribir('El STOP no se traduce a aminoacido. La proteina es Met-Pro-Glu.')

# final
print('\n' + '='*55)
print(f'\nFIN - {nombre}')
print(f'Respondiste {aciertos}/4 correctamente en el primer intento.\n')

if aciertos == 4:
    escribir('Perfecto! Dominas el dogma central de la biologia molecular.')
elif aciertos >= 2:
    escribir('Buen trabajo, con un poco mas de practica lo dominas.')
else:
    escribir('El camino ADN -> ARN -> Proteina es largo, segui estudiando!')

print('\n[ADN -> transcripcion -> ARNm -> splicing -> traduccion -> Proteina]\n')
