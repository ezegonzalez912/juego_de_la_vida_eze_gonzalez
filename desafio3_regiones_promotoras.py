import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--archivo', required=True)
args = parser.parse_args()

with open(args.archivo, 'r') as f:
    seq = f.read().upper().replace('\n', '').replace(' ', '')

caja = 'TATAAA'
regiones = []
i = 0

while True:
    inicio = seq.find(caja, i)
    if inicio == -1:
        break
    fin = seq.find(caja, inicio + len(caja))
    if fin == -1:
        break
    fin_real = fin + len(caja)
    regiones.append((inicio, fin_real, seq[inicio:fin_real]))
    i = fin + 1

if not regiones:
    print('No se encontraron regiones promotoras.')
else:
    print(f'Se encontraron {len(regiones)} region(es) promotora(s):\n')
    for n, (ini, fin, region) in enumerate(regiones, 1):
        print(f'Region {n}: posicion {ini}-{fin}')
        print(f'  {region}\n')
