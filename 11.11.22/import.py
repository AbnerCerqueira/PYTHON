import sys

print('\nVersão Python: ')
print(sys.version)

print('\nInformações da versão instalada: ')
print(sys.version_info)

SO = sys.platform
print(f'\nA versão do seu sistema é: {SO}')