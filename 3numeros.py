n1 = int(input("Digite o primeiro número "))
n2 = int(input("Digite o primeiro número "))
n3 = int(input("Digite o primeiro número "))

if n1 > n2 and n1 > n3:
    print(F"O número {n1} é maior")
elif n2 > n1 and n2 > n3:
    print(F"O número {n2} é maior")
else:
    print(F"O número {n3} é maior")