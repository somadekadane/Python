n = int(input("Digite um número: "))

if (n == 0):

    print("O número é negativo")

else:
    if(n > 0):
        if (n > 1 and n < 100):
            print(f"o numero {n} é positivo")
        else:
            print(f"o numero {n} é positivo")
    else:
        if (n < -1 and n > -100):
            print(f"o numero {n} é negativo")
        else:
            print(f"o numero {n} é negativo")
# nova formula
n = int (input("digite um número: "))
if n > 0:
    print(f"O valor {n} é negativo")
elif n > 0:
    print(f"O valor {n} é positivo")
else:
    print(f"O valor {n} é neutro")