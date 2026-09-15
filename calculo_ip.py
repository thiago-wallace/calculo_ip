print('### Cálculo IP - atualização 2026.09.14 - Desenvolvido por Thiago Wallace ###\n')
while True:
    entrada = input('\nDigite o número da filial (Ou "s" para sair): ').lower()
    if entrada == 's':
        break
    if not entrada.isdigit():
        print('Número inválido')
        continue
    filial = int(entrada)
    if filial <= 0 or filial > 4000:
        print('Filial inválida')
        continue
    if filial == 1128 or filial == 1328 or filial >= 2000:
        print(
            f'Filial {filial} utiliza um IP fora do padrão, necessário consultar o IP no monitoramento')
        continue
    ip = ['10', '0', '0', '100']
    ip[1] = str(filial % 200)
    if filial >= 1000 and filial < 1200:
        ip[2] = '80'
    elif filial >= 1200 and filial < 1400:
        ip[2] = '84'
    elif filial >= 1400 and filial < 1600:
        ip[2] = '88'
    elif filial >= 1600 and filial < 1800:
        ip[2] = '92'
    elif filial >= 1800 and filial < 2000:
        ip[2] = '96'
    elif filial >= 0 and filial < 200:
        ip[2] = '100'
    elif filial >= 200 and filial < 400:
        ip[2] = '104'
    elif filial >= 400 and filial < 600:
        ip[2] = '108'
    elif filial >= 600 and filial < 800:
        ip[2] = '112'
    elif filial >= 800 and filial < 1000:
        ip[2] = '116'
    endereco_ip = '.'.join(ip)
    print('IP:', endereco_ip)
