nome = input("Qual o seu nome? ")
nota = float(input("Qual a sua nota? "))

if (nota == 10):
  print(f"{nome}, você é o bixão mesmo!")
elif(nota >= 6 and nota < 10):
  print("Não se preocupe, estude e você irá bem na próxima!")
else:
  print("Aí é complcado....")

