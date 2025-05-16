from datetime import datetime  # Importa o módulo para pegar o ano atual

while True:
    try:
        idade = int(input("Digite sua idade: "))
        break  # Sai do loop se a idade for um número válido
    except ValueError:
        print("Por favor, digite apenas números. Tente novamente.")

# Verifica a faixa etária
if idade < 18:
    print("Você é menor de idade.")
elif idade < 60:
    print("Você é maior de idade.")
else:
    print("Você é idoso.")

# Calcula o ano de nascimento
ano_atual = datetime.now().year
ano_nascimento = ano_atual - idade

print(f"Você nasceu em {ano_nascimento}")