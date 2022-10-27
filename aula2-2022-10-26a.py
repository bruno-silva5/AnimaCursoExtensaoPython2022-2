# comando input(): quero permitir que
# o usuario digite algo

#nome = input('Digite o seu nome: ')
#print(f"O nome eh {nome}")

idade = int(input("Qual a sua idade? "))
sexo = input("Qual o sexo?")

#print(f"A sua idade eh: {idade}")

# print(f"O dobro da sua idade eh: {idade * 2}")

if (idade >= 18):
  print('Você é maior de idade')
  if (sexo == 'M'):
    print('Você também deve prestar o serviço militar obrigatório')
else:
    print('Você é menor de idade')
