# Calculadora de Consumo de Combustível

#Dados da viajem
distancia_percorrida=int(input("Digite a distância percorrida em km: "))
combustivel_gasto=int(input("Digite a quantidade gasta de combustivel em Litros: "))

#Calculo do consumo
consumo=distancia_percorrida/combustivel_gasto
print("\nDados da Viajem: ")
print(f"Distancia percorrida: {distancia_percorrida} km")
print(f"Coombustivel Gasto: {combustivel_gasto} litro(s)")
print(f"Cnsumo Médio: {consumo:.2f} km/l")