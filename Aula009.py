# Anotações da aula.

# O índice de caracteres do Python se inicia em 0. 21 índices, de 0 a 20.

# Fatiamento de String:
    # 1 Letra: Frase[9]: Identifica o caractere de número 9.
    # Várias letras: Frase[9:13]: Identifica de 9 a 13, porém 13 será exclúido. (Sempre um a menos no final).
    # Pulando Casas: Frase[9:21:2]: Identifica de 9 a 21 e pula duas casas.
    # Omitindo o início: Frase [:5]: Inicia de 0 e vai até 5.
    # Omitindo o final: Frase [5:]: Inicia em 5 e vai até o final.
    # Frase [9::3] Inicia do 9, vai até o final e vai pulando de 3 em 3 caracteres.

# Análises de String:
    # len(frase): Identifica quantos caracteres a frase possui.
    # frase.count('o'): Conta quantoas vezes a letra 'o' aparece.
    # frase.find('deo'): Demonstra onde se inicia essa cadeia de caracteres.
    # frase.find('Android'): Não existe, então o Python retorna o valor -1, significando que a string não existe.
    # 'Curso' in frase: Retorna verdadeiro ou falso se existe a string na frase.

# Transformações:
    # frase.replace('A', 'B'): Substitui a letra A pela letra B.
    # frase.upper(): Coloca as letras em maiúsculas.
    # frase.lower(): Coloca as letras em minúsculas.
    # frase.capitalize(): Apenas o primeiro caractere da frase fica em maiúscula.
    # frase.title(): Cada frase fica em maiúscula.
    # frase.strip(): Remove os espaços inúteis no início e no final da string.
        # rstrip(): remove somente os últimos espaços.
        # lstrip(): remove os espaços da esquerda.

# Divisão:
    # frase.split(): Divide a string considerando os espaços. Separa as palavras em listas.
    #'-'.join(frase): Junta os elementos da frase usando o espaçador desejado.

