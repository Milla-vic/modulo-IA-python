def calculadora():
    while True:
        try:
            numero1= float(input("Digite o primeiro numero: "))
            numero2= float(input("Digite o segundo numero: "))
            operacao= (input("Digite a operação (+ - * /): "))
            
            if operacao == '+':
                resultado = numero1 + numero2
            elif operacao == '-': 
                resultado = numero1 - numero2 
            elif operacao == '*': 
                resultado = numero1 * numero2 
            elif operacao == '/': 
                resultado = numero1 / numero2 
            else:
                raise ValueError("Operação invalida")
                        
        except ValueError as e:
            print(f"Erro: {e}. Tente Novamente!")
        except ZeroDivisionError:
            print("Invalido:Divisão por zero não é permitida. Tente novamente ")
        else:
            print(f"Resultado: {numero1} {operacao} {numero2} = {resultado}") 
            
calculadora()               