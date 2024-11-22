# upper -> converte para caracteres maiúsculos
# lower -> converte para caracteres minuscúlos

sexo = input("Digite F para feminino ou M Masculino): ").lower()
# sexo = sexo.lower()
if sexo.lower() == "f":
    print("Feminino")
elif sexo.lower() == "m":
    print("Masculino")
else:
    print("Inválido")
    