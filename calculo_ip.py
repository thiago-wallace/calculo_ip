import dicionario_filial_ip

print('### Cálculo IP - atualização 2026.09.15')
while True:
    entrada = input('\nDigite o número da filial (Ou "s" para sair): ').lower()
    # Validar se o usuário deseja sair
    if entrada == 's':
        break
    # Validar se o usuário digitou um número inteiro
    if not entrada.isdigit():
        print('Número inválido')
        continue
    filial = int(entrada)
    # Validar se o usuário digitou um número de filial inexistente
    if filial <= 0 or filial > 4000:
        print('Filial inválida')
        continue
    # Validar se a filial está dentro do dicionário de IPs fora do padrão
    if filial in dicionario_filial_ip.dicionario:
        endereco_ip = dicionario_filial_ip.dicionario[filial]
    # Validar se o número da filial está entre 0 e 2000
    elif filial > 0 and filial < 2000:
        ip = ['10', '0', '0', '100']
        ip[1] = str(filial % 200)
        if filial >= 0 and filial < 200:
            ip[2] = '100'
        elif filial >= 200 and filial < 400:
            ip[2] = '104'
        elif filial >= 400 and filial < 600:
            ip[2] = '108'
        elif filial >= 600 and filial < 800:
            ip[2] = '112'
        elif filial >= 800 and filial < 1000:
            ip[2] = '116'
        elif filial >= 1000 and filial < 1200:
            ip[2] = '80'
        elif filial >= 1200 and filial < 1400:
            ip[2] = '84'
        elif filial >= 1400 and filial < 1600:
            ip[2] = '88'
        elif filial >= 1600 and filial < 1800:
            ip[2] = '92'
        elif filial >= 1800 and filial < 2000:
            ip[2] = '96'
        endereco_ip = '.'.join(ip)
    # Caso a filial seja acima de 2000, e não esteja no dicionário de IPs fora do padrão
    else:
        print(
            f'Filial {filial} utiliza um IP fora do padrão e não cadastrado, necessário consultar o IP no monitoramento')
        continue
    print('IP:', endereco_ip)
