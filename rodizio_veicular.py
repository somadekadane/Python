placa = int(input("Digite o final da placa do veiculo: "))

if placa==1 or placa==2:
    print("Rodozio na segunda-feira")
elif placa==3 or placa==4:
    print("Rodozio na terça-feira")
elif placa==5 or placa==6:
    print("Rodozio na quarta-feira")
elif placa==7 or placa==8:
    print("Rodozio na quinta-feira")
elif placa==9 or placa==0:
    print("Rodozio na sexta-feira")
else:
    print("Placa invalida")