# algoritmo do bubble sort
def bubble_sort(dados):
    # Loop externo: controla quantas passagens serão feitas
    # Começa no último índice e vai até o índice 1 (de trás para frente)
    for ultimo in range(len(dados) - 1, 0, -1):

        # Loop interno: percorre a lista até o índice 'ultimo'
        for interno in range(ultimo):

            # Compara o elemento atual com o próximo
            if dados[interno] > dados[interno + 1]:
                # Se estiver fora de ordem, realiza a troca usando uma variável temporária
                temporario = dados[interno]
                dados[interno] = dados[interno + 1]
                dados[interno + 1] = temporario

# Cria um vetor com os elementos
elementos = [-10, 15, 19, 44, 21, 33, -50]

# Executando o Bublle Sort:
bubble_sort(elementos)

print(elementos)