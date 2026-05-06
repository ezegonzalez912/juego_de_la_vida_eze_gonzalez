import argparse
import time

ROSCO = [
    ('A', 'Empieza por A: Unidad basica que forma las proteinas. El codigo genetico especifica el orden en que se encadenan.', 'AMINOACIDO'),
    ('C', 'Empieza por C: Triplete de nucleotidos del ARNm que especifica un aminoacido. Hay 64 combinaciones posibles.', 'CODON'),
    ('D', 'Empieza por D: ___ central de la biologia molecular: el flujo de informacion va del ADN al ARN y de este a las proteinas.', 'DOGMA'),
    ('E', 'Empieza por E: Secuencia codificante de un gen que se conserva en el ARNm maduro, a diferencia del intron que se elimina.', 'EXON'),
    ('I', 'Empieza por I: Secuencia no codificante dentro de un gen que interrumpe la secuencia codificante y se elimina del ARNm.', 'INTRON'),
    ('N', 'Empieza por N: Unidad basica del ADN y el ARN, formada por una base nitrogenada, un azucar y un grupo fosfato.', 'NUCLEOTIDO'),
    ('P', 'Empieza por P: Region del ADN que contiene la caja TATA y donde se une la ARN Polimerasa II para iniciar la transcripcion.', 'PROMOTOR'),
    ('R', 'Empieza por R: Organela donde el ARNm es decodificado para generar una cadena de aminoacidos durante la traduccion.', 'RIBOSOMA'),
    ('T', 'Empieza por T: Primer paso de la expresion genica, ocurre en el nucleo y produce una molecula de ARNm a partir del ADN.', 'TRANSCRIPCION'),
]

def mostrar_rosco(estados, tiempo_restante):
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
    mins = int(tiempo_restante) // 60
    segs = int(tiempo_restante) % 60
    print('\n ' + '  '.join(partes) + f'        ⏱  {mins:02d}:{segs:02d}\n')

def tiempo_restante(inicio, limite):
    return max(0, limite - (time.time() - inicio))

def jugar_ronda(pendientes, estados, inicio, limite):
    pasados = []
    for letra, pista, respuesta in pendientes:
        restante = tiempo_restante(inicio, limite)
        if restante == 0:
            print('\n\033[91m¡Se acabó el tiempo!\033[0m\n')
            for l, _, _ in pendientes:
                if estados[l] == 'pendiente' or estados[l] == 'pasado':
                    estados[l] = 'incorrecto'
            return []
        mostrar_rosco(estados, restante)
        print(f'[{letra}] {pista}')
        print('(escribi tu respuesta o "pp" para pasar)\n')
        resp = input('> ').strip().upper()
        if tiempo_restante(inicio, limite) == 0:
            print('\n\033[91m¡Se acabó el tiempo!\033[0m\n')
            for l, _, _ in pendientes:
                if estados[l] == 'pendiente' or estados[l] == 'pasado':
                    estados[l] = 'incorrecto'
            return []
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

while True:
    try:
        minutos = int(input('Cuantos minutos queres jugar? '))
        if minutos > 0:
            break
    except ValueError:
        pass
    print('Ingresa un numero valido.')

limite = minutos * 60

print(f'\nBienvenido/a al Rosco Bio, {nombre}! Tenes {minutos} minuto(s).')
print('Respondé cada pregunta o escribí "pp" para pasar.')
input('\n[Enter para empezar]\n')

inicio = time.time()
estados = {letra: 'pendiente' for letra, _, _ in ROSCO}
pendientes = list(ROSCO)

while pendientes:
    pendientes = jugar_ronda(pendientes, estados, inicio, limite)
    if pendientes:
        restante = tiempo_restante(inicio, limite)
        if restante == 0:
            break
        mostrar_rosco(estados, restante)
        print(f'Te quedan {len(pendientes)} sin responder.')
        continuar = input('¿Seguís con los que pasaste? (s/n) > ').strip().lower()
        if continuar != 's':
            for letra, _, _ in pendientes:
                estados[letra] = 'incorrecto'
            break

correctas = sum(1 for e in estados.values() if e == 'correcto')
total = len(ROSCO)
usado = int(time.time() - inicio)
mins_usado = usado // 60
segs_usado = usado % 60

mostrar_rosco(estados, 0)
print(f'{nombre}: {correctas}/{total} correctas  |  Tiempo usado: {mins_usado:02d}:{segs_usado:02d}\n')

if correctas == total:
    print('¡Rosco completo! Sos un crack de la biologia molecular.')
elif correctas >= total * 0.7:
    print('Muy bien! Dominas la mayoria de los conceptos.')
elif correctas >= total * 0.4:
    print('Bien, pero hay conceptos para repasar.')
else:
    print('A repasar el dogma central... ¡la proxima va mejor!')
print()
