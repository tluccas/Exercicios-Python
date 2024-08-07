entrada = (int(input("Insira um valor ")))
ent = str(input("Deseja continuar? [S/N]").upper())
par = []
impar = []
todos = []
if entrada % 2 == 0:
        par.append(entrada)
elif entrada % 2 != 0: 
        impar.append(entrada)
todos.append(entrada)
while ent == "S":
  entrada = (int(input("Insira um valor ")))
  ent = str(input("Deseja continuar? [S/N]").upper())
  if entrada % 2 == 0:
        par.append(entrada)
  elif entrada % 2 != 0: 
        impar.append(entrada)
  todos.append(entrada)


print("Numeros impares", impar, "\nNumeros pares", par, "\nForam inseridos {} valores".format(len(todos)))
