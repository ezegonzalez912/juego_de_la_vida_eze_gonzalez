import argparse

# cada aminoacido con un codon representativo
codigos = {
    'A': 'GCU', 'R': 'CGU', 'N': 'AAU', 'D': 'GAU',
    'C': 'UGU', 'Q': 'CAA', 'E': 'GAA', 'G': 'GGU',
    'H': 'CAU', 'I': 'AUU', 'L': 'UUA', 'K': 'AAA',
    'M': 'AUG', 'F': 'UUU', 'P': 'CCU', 'S': 'UCU',
    'T': 'ACU', 'W': 'UGG', 'Y': 'UAU', 'V': 'GUU',
}

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--secuencia', required=True)
args = parser.parse_args()

seq = args.secuencia.upper()
arn = ''

for aa in seq:
    if aa not in codigos:
        print(f'aminoacido desconocido: {aa}')
        exit(1)
    arn += codigos[aa]

arn += 'UAA'  # stop codon

print('Secuencia proteica:', seq)
print('ARN codificante:   ', arn)
