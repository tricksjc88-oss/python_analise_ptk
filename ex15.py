gen=input("Qual o seu genero? Digite H para homem e M para mulher: ")
idd=int(input("Qual a sua idade? "))
if gen == "H" and idd >= 18:
    print("Você esta apto para se alistar")
else:
    print("Você não esta apto para se alistar")