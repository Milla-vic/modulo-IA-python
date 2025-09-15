#Calculadora de desconto de uma loja

# Informacoes do produto
nome_do_produto= input("Digite o nome do produto: ")
preco_original=float(input("Digite o valor do produto: "))
porcentagem_desconto=float(input("Digite a porcentagem de desconto: "))

# Calculo do desconto e preço final
valor_desconto= preco_original * (porcentagem_desconto/100)
preco_final= preco_original - valor_desconto 

# Exibição dos resultados
print(f"\nProduto: {nome_do_produto}")
print(f"Preço: {preco_original}")
print(f"Desconto: {porcentagem_desconto}%")
print(f"\nValor Desconto: R$ {valor_desconto:.2f}")
print(f"Total com Desconto: R$ {preco_final:.2f}")





