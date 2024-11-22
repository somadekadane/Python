salario = float(input("Digite seu salário: "))
aumento = 0
novo_salario = 0

if salario <= 1500:
    aumento = salario * 0.2
    novo_salario = salario + aumento
    print(f"Reajuate de 20%. Salário antigo {salario}, aumento {aumento} e novo salário {novo_salario}")

elif salario <= 700:
     aumento = salario * 0.15
     novo_salario = salario + aumento
     print(f"Reajuate de 15%. Salário antigo {salario}, aumento {aumento} e novo salário")
           
elif salario <= 1500:
     aumento = salario * 0.1
     novo_salario = salario + aumento
     print(f"Reajuate de 10%. Salário antigo {salario}, aumento {aumento} e novo salário")

else:
     aumento = salario * 0.5
     novo_salario = salario + aumento
     print(f"Reajuate de 5%. Salário antigo {salario}, aumento {aumento} e novo salário")

