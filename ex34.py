for i in range(0,5):
    idd = float(input("Digite a sua idade?"))
    if idd < 18:
        print("Menor de idade")
    elif idd > 18 and idd < 65: 
        print("Maior de idade")
    else:
         print("Idosinho")