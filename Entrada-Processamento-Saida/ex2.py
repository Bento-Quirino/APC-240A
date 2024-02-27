#ENTRADA
sr = float(input("Digite o peso do saco de ração em kg: "))
rg = int(input("Digite o consumo em gramas para cada gato: "))

#PROCESSAMENTO
#Converter o sr de kg para g
sr = sr * 1000
res = sr - ((rg*2)*5)

#SAÍDA
print("O peso restante do saco de ração é: ", res, "g")



#int() - INTEIRO
#float() - DECIMAL

