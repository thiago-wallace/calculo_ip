from dicionario_filial_ip import dicionario


def validar_filial(filial: str) -> int | None:
    """ Válidar filial: 

    Recece o número da filial em str, e valida se o número da filial está correto.
    Caso sim, retorna o número da filial em int.
    Caso não, retorna None.
    Obs: Caso o número da filial recebido esteja com 21 na frente, o 21 é retirado automaticamente.
    """
    # Validar se o usuário digitou um número inteiro
    if not filial.isdigit():
        return
    numero_filial = int(filial)
    # Validar se o usuário digitou o número da filial com 21 na frente
    if numero_filial >= 210000 and numero_filial <= 214000:
        numero_filial -= 210000
    # Validar se o usuário digitou um número de filial inexistente
    if numero_filial <= 0 or numero_filial > 4000:
        return
    return numero_filial


def calcular_ip_filial(filial: int) -> str:
    """ Cálcular IP da filial:

    Recece o número da filial em int, e retorna o ip em str,
    ou retorna uma frase em str explicando o porquê não foi possível calcular. """
    # Validar se a filial está dentro do dicionário de IPs fora do padrão do cálculo
    if filial in dicionario:
        ip = dicionario[filial]
    # Validar se o número da filial está entre 0 e 2000
    elif filial > 0 and filial < 2000:
        octetos = ['10', '0', '0', '100']
        octetos[1] = str(filial % 200)
        if filial >= 0 and filial < 200:
            octetos[2] = '100'
        elif filial >= 200 and filial < 400:
            octetos[2] = '104'
        elif filial >= 400 and filial < 600:
            octetos[2] = '108'
        elif filial >= 600 and filial < 800:
            octetos[2] = '112'
        elif filial >= 800 and filial < 1000:
            octetos[2] = '116'
        elif filial >= 1000 and filial < 1200:
            octetos[2] = '80'
        elif filial >= 1200 and filial < 1400:
            octetos[2] = '84'
        elif filial >= 1400 and filial < 1600:
            octetos[2] = '88'
        elif filial >= 1600 and filial < 1800:
            octetos[2] = '92'
        elif filial >= 1800 and filial < 2000:
            octetos[2] = '96'
        ip = '.'.join(octetos)
    # Caso a filial seja acima de 2000, e não esteja no dicionário de IPs fora do padrão
    else:
        ip = f'Filial fora do cálculo padrão e sem IP cadastrado.'
    return ip


if __name__ == '__main__':
    print('### Cálculo IP - atualização 2026.10.12 - Desenvolvido por Thiago Wallace')
    while True:
        entrada = input(
            '\nDigite o número da filial (Ou "s" para sair): ').lower()
        # Validar se o usuário deseja sair
        if entrada == 's':
            break
        # Validar se a filial é válida
        filial = validar_filial(entrada)
        if filial is None:
            print('Filial inválida')
            continue
        endereco_ip = calcular_ip_filial(filial)
        if endereco_ip[0].isdigit():
            print('IP:', endereco_ip)
        else:
            print(
                f'Filial {filial} utiliza um IP fora do padrão e não cadastrado, necessário consultar o IP no monitoramento.')
