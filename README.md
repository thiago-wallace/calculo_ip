# Cálculo IP

Esta aplicação recebe o número de uma filial e retorna o endereço de IP dessa filial. Essas filiais e IPs são da rede interna de uma empresa.

Função validar_filial: função para validar o número da filial, verificando se o usuário um número válido e se o número está entre 0 e 4000.
    Recece o número da filial em str, e valida se o número da filial está correto.
    Caso sim, retorna o número da filial em int.
    Caso não, retorna None.

Função calcular_ip_filial: função para efetuar o cálculo do IP.
    Recece o número da filial em int, e retorna o ip em str,
    ou retorna uma frase em str explicando o porquê não foi possível calcular.

Nesta empresa, as filiais com números entre 2000 e 4000, e algumas filiais abaixo de 2000, utilizam um IP fora do cálculo padrão, então para obter esse IP, foi criado o módulo dicionario_filial_ip com o dict dicionario, que contem o número da filial (chave) e o endereço IP (valor). A função calcular_ip_filial consulta se o número da filial digitado pelo usuário está nesta lista, e caso esteja, a função busca o IP nesse dicionário e retorna o IP.
Caso o número da filial digitado não esteja na lista, e o número da filial for entre 1 e 1999, é efetuado o cálculo padrão.
Obs: Para preservar os dados sigilosos, esse módulo dicionario_filial_ip não estará publicado no github.
