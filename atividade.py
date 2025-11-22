
# Definimos a função chamada saudacao
def saudacao():
    # Esta função exibe uma mensagem de boas-vindas
    print("Olá, bem-vindo ao curso de Python!")

# Chamamos a função para que ela execute o que foi definido
saudacao()

# Definimos a função chamada boas_vindas que recebe um parâmetro chamado nome
def boas_vindas(nome):
    # Exibe uma mensagem personalizada usando o nome fornecido
    print(f"{nome}! Seja bem-vindo!")

# Chamamos a função passando um nome como argumento
boas_vindas("Victor")

# Definimos a função chamada soma que recebe dois parâmetros: a e b
def soma(a, b):
    # Calcula a soma dos dois números
    resultado = a + b
    # Retorna o dobro da soma
    return resultado * 2

# Chamamos a função passando dois números e armazenamos o resultado
dobro_da_soma = soma(5, 3)

# Exibimos o resultado da função
print("O dobro da soma é:", dobro_da_soma)

# Definimos a função chamada somar que recebe dois parâmetros: a e b
def somar(a, b):
    # Retorna a soma dos dois números
    return a + b

# Solicitamos ao usuário que digite o primeiro número
num1 = float(input("Digite o primeiro número: "))

# Solicitamos ao usuário que digite o segundo número
num2 = float(input("Digite o segundo número: "))

# Chamamos a função somar passando os dois números digitados
resultado = somar(num1, num2)

# Exibimos o resultado da soma
print("A soma dos números é:", resultado)

def media(n1, n2, n3):
    resultado = (n1 + n2 + n3) / 3
    return f"{resultado:.2f}"  # retorna como string formatada com 2 casas decimais

# Exemplo de uso:
print("Média:", media(7.5, 8.0, 6.3))

Média: 7.27

def mensagem(texto="Olá!"):
    print(texto)

# Exemplos de uso:
mensagem("Bem-vindo ao programa!")  # Exibe: Bem-vindo ao programa!
mensagem()                          # Exibe: Olá!

def eh_par(numero):
    return numero % 2 == 0

# Testando com valor informado pelo usuário:
valor = int(input("Digite um número: "))
if eh_par(valor):
    print(f"O número {valor} é par.")
else:
    print(f"O número {valor} é ímpar.")


def calcular(a, b, operacao):
    if operacao == "+":
        return a + b
    elif operacao == "-":
        return a - b
    elif operacao == "*":
        return a * b
    elif operacao == "/":
        if b != 0:
            return a / b
        else:
            return "Erro: divisão por zero!"
    else:
        return "Operação inválida!"

# Exemplos de uso:
print(calcular(10, 5, "+"))  # Saída: 15
print(calcular(10, 5, "-"))  # Saída: 5
print(calcular(10, 5, "*"))  # Saída: 50
print(calcular(10, 5, "/"))  # Saída: 2.0

def exibir_lista(itens):
    for i, item in enumerate(itens, start=1):
        print(f"{i} - {item}")

# Exemplo de uso:
lista_compras = ["Arroz", "Feijão", "Macarrão", "Carne"]
exibir_lista(lista_compras)

