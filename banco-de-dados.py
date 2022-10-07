#Rafael Duartes N-25, Luan Skovronsky N-18, Leonardo de Moura N-17, Bianca Caroline N-08
escolha = 0
escolha2 = 0
enquanto = 0

while enquanto < 1:
    c = 0
    f = 0
    print(
        " [ 1 ]Valor em Celsius   \n [ 2 ]Valor em Fahrenheit   \n [ 3 ]Valor em Kelvin"
    )
    escolha = int(input(">>> Sua opção:"))
    print("---" * 20)
    if escolha == 1:

        c = float(input("Coloque o valor em celsius:"))
        print("---" * 20)

        print(" [ 1 ]Converter em Kelvin   \n [ 2 ]Converter em Fahrenheit   ")
        escolha2 = int(input(">>> Sua opção:"))

        if escolha2 == 1:
            k = c + 273.15
            print(f"valor em Kelvin = {k:.2f}")
            if c <= 0:
                print("A água está em estado sólido")
            elif c >= 100:
                print("A água está em estado gasoso")
            else:
                print("A água está em estado liquido")
        elif escolha2 == 2:
            f = c * 1.8 + 32
            print(f"valor em Fahrenheit = {f:.2f}")
            if c <= 0:
                print("A água está em estado sólido")
            elif c >= 100:
                print("A água está em estado gasoso")
            else:
                print("A água está em estado liquido")

        else:
            print("---" * 20)
            print("ERROR")
            print("Tente novamente")
            print("---" * 20)
            break

        print("---" * 20)
    elif escolha == 2:

        f = float(input("Coloque o valor em Fahrenheit:"))
        print("---" * 20)

        print(" [ 1 ]Converter em Celsius   \n [ 2 ]Converter em Kelvin   ")
        escolha2 = int(input(">>> Sua opção:"))

        c = (f - 32) / 1.8

        if escolha2 == 1:
            print(f"valor em Celsius = {c:.4f}")
            if c <= 0:
                print("A água está em estado sólido")
            elif c >= 100:
                print("A água está em estado gasoso")
            else:
                print("A água está em estado liquido")
        elif escolha2 == 2:
            k = c + 273.15
            print(f"valor em Kelvin = {k:.4f}")
            if c <= 0:
                print("A água está em estado solido")
            elif c >= 100:
                print("A água está em estado gasoso")
            else:
                print("A água está em estado liquido")

        else:
            print("---" * 20)
            print("ERROR")
            print("Tente novamente")
            print("---" * 20)
            break

        print("---" * 20)

    elif escolha == 3:

        k = float(input("Coloque o valor em Kelvin:"))
        print("---" * 20)

        print(
            " [ 1 ]Converter em Celsius   \n [ 2 ]Converter em Fahrenheit   ")
        escolha2 = int(input(">>> Sua opção:"))

        c = k - 273.15

        if escolha2 == 1:
            print(f"valor em Celsius = {c:.2f}")
            if c <= 0:
                print("A água está em estado sólido")
            elif c >= 100:
                print("A água está em estado gasoso")
            else:
                print("A água está em estado liquido")
        elif escolha2 == 2:
            f = c * 1.8 + 32
            print(f"valor em Fahrenheit = {f:.2f}")
            if c <= 0:
                print("A água está em estado sólido")
            elif c >= 100:
                print("A água está em estado gasoso")
            else:
                print("A água está em estado liquido")

        else:
            print("---" * 20)
            print("ERROR")
            print("Tente novamente")
            print("---" * 20)
            break

        print("---" * 20)
    else:
        print("ERROR")
        print("Tente novamente")
        print("---" * 20)
        break
