import argparse
import time

ROSCO = [
    ('A', 'Empieza por A: Una de las cuatro bases nitrogenadas del ADN, se empareja con la Timina.', 'ADENINA'),
    ('B', 'Empieza por B: Virus que infecta bacterias, muy usado en investigacion genetica.', 'BACTERIOFAGO'),
    ('C', 'Empieza por C: Triplete de nucleotidos del ARNm que codifica un aminoacido.', 'CODON'),
    ('D', 'Empieza por D: Proceso por el cual el ADN se copia a si mismo antes de dividirse la celula.', 'DUPLICACION'),
    ('E', 'Empieza por E: Secuencia codificante de un gen que se conserva en el ARNm maduro.', 'EXON'),
    ('F', 'Empieza por F: Conjunto de caracteristicas observables de un organismo.', 'FENOTIPO'),
    ('G', 'Empieza por G: Composicion genetica de un organismo, el conjunto de sus genes.', 'GENOTIPO'),
    ('H', 'Empieza por H: Proteina alrededor de la cual se enrolla el ADN para compactarse en el nucleo.', 'HISTONA'),
    ('I', 'Empieza por I: Secuencia no codificante de un gen que se elimina durante el splicing.', 'INTRON'),
    ('L', 'Empieza por L: Enzima que une fragmentos de ADN, clave en la replicacion y reparacion.', 'LIGASA'),
    ('M', 'Empieza por M: Cambio permanente en la secuencia del ADN de un organismo.', 'MUTACION'),
    ('N', 'Empieza por N: Unidad basica del ADN y el ARN, formada por una base, un azucar y un fosfato.', 'NUCLEOTIDO'),
    ('O', 'Empieza por O: Unidad funcional de regulacion genetica tipica de procariotas.', 'OPERON'),
    ('P', 'Empieza por P: Region del ADN donde se une la ARN Polimerasa para iniciar la transcripcion.', 'PROMOTOR'),
    ('R', 'Empieza por R: Organela celular donde ocurre la traduccion del ARNm a proteina.', 'RIBOSOMA'),
    ('S', 'Empieza por S: Proceso de eliminacion de intrones y union de exones del ARNm.', 'SPLICING'),
    ('T', 'Empieza por T: Proceso por el cual se sintetiza ARN a partir de una cadena molde de ADN.', 'TRANSCRIPCION'),
    ('U', 'Empieza por U: Base nitrogenada del ARN que reemplaza a la Timina del ADN.', 'URACILO'),
    ('V', 'Empieza por V: Molecula usada para introducir ADN exogeno en una celula huesped.', 'VECTOR'),
    ('Z', 'Empieza por Z: Celula resultante de la fusion de un ovulo y un espermatozoide.', 'ZIGOTO'),
]

def mostrar_rosco(estados):
    partes = []
    for letra, estado in estados.items():
        if estado == 'correcto':
            partes.append(f'\033[92m{letra}✓\033[0m')
        elif estado == 'incorrecto':
            partes.append(f'\033[91m{letra}✗\033[0m')
        elif estado == 'pasado':
            partes.append(f'\033[93m{letra}?\033[0m')
        else:
            partes.append(letra)
    print('\n ' + '  '.join(partes) + '\n')

def jugar_ronda(pendientes, estados):
    pasados = []
    for letra, pista, respuesta in pendientes:
        mostrar_rosco(estados)
        print(f'[{letra}] {pista}')
        print('(escribi tu respuesta o "pp" para pasar)\n')
        resp = input('> ').strip().upper()
        if resp == 'PP':
            estados[letra] = 'pasado'
            pasados.append((letra, pista, respuesta))
        elif resp == respuesta:
            print('\n\033[92m¡Correcto!\033[0m')
            estados[letra] = 'correcto'
            time.sleep(1)
        else:
            print(f'\n\033[91mIncorrecto. Era: {respuesta}\033[0m')
            estados[letra] = 'incorrecto'
            time.sleep(1.5)
        print()
    return pasados

parser = argparse.ArgumentParser(description='Rosco Bio - juego de preguntas sobre expresion genica')
parser.add_argument('-n', '--nombre', default=None, help='Tu nombre')
args = parser.parse_args()

print()
if args.nombre:
    nombre = args.nombre
else:
    nombre = input('Como te llamás? ').strip() or 'Jugador'
print(f'\nBienvenido/a al Rosco Bio, {nombre}!')
print('Respondé cada pregunta o escribí "pp" para pasar.')
input('\n[Enter para empezar]\n')

estados = {letra: 'pendiente' for letra, _, _ in ROSCO}
pendientes = list(ROSCO)

while pendientes:
    pendientes = jugar_ronda(pendientes, estados)
    if pendientes:
        mostrar_rosco(estados)
        print(f'Te quedan {len(pendientes)} sin responder.')
        continuar = input('¿Seguís con los que pasaste? (s/n) > ').strip().lower()
        if continuar != 's':
            for letra, _, _ in pendientes:
                estados[letra] = 'incorrecto'
            break

correctas = sum(1 for e in estados.values() if e == 'correcto')
total = len(ROSCO)

mostrar_rosco(estados)
print(f'{nombre}: {correctas}/{total} correctas\n')

if correctas == total:
    print('¡Rosco completo! Sos un crack de la biologia molecular.')
elif correctas >= total * 0.7:
    print('Muy bien! Dominas la mayoria de los conceptos.')
elif correctas >= total * 0.4:
    print('Bien, pero hay conceptos para repasar.')
else:
    print('A repasar el dogma central... ¡la proxima va mejor!')
print()
