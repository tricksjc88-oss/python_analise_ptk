#Desenv um código que leia a temperatur atual e o programa retorna frio - 1 a 18 / normal 19 a 24 e calor > 24 
t = float(input("Digite a temperatura atual: "))
    if t >=1 and t <= 18 :
        print(f"Está frio.")
    elif t >19 and t <= 24 :
        print(f"Está normal.")
    else:
        print("Calor")
