from imports import *

def main():
    lauching = bool(True)
    try:
        option = int(input("""
        -=======MENU=======-
         |1 - Dolar / Real|
         |2 - Euro / Real |
         |3 - Bit / Real  |
         |                |
         |0 - Sair        |
        -==================-
        ---Selecionar: """))

        if option == 1:
            convert_dolar()
        elif option == 2:
            convert_euro()
        elif option == 3:
            convert_bit()
        elif option == 0:
            sair()
    except:
        print("Opção inexistente ou formato errado, verifique seu valor de entrada e tente novamente!!!")
        time.sleep(2)
        os.system('cls')
        main()

def convert_dolar():
    try:
        os.system('cls')
        entry = float(input("======Dolar para Real======\nValor em Real: R$"))
        print("Cotação do Dolar: {:.2f}".format(float(cotacoes_dolar)))
        entry = entry* float(cotacoes_dolar)
        print("Real para Dolar: R$ {:.2f}".format(entry))
        time.sleep(2)
    except:
        print("Valor inválido verifique sua entrada e tente novamente")
        time.sleep(1.5)
        convert_dolar()

def convert_euro():
    try:
        os.system('cls')
        entry = float(input("======Euro para Real======\nValor em Real: R$"))
        print("Cotação do Euro: {:.2f}".format(float(cotacoes_euro)))
        entry = entry* float(cotacoes_euro)
        print("Real para Euro: R$ {:.2f}".format(entry))
        time.sleep(2)
    except:
        print("Valor inválido verifique sua entrada e tente novamente")
        time.sleep(1.5)
        convert_euro()

def convert_bit():
    try:
        os.system('cls')
        entry = float(input("======Bit-Coin para Real======\nValor em Real: R$"))
        print("Cotação do Bit: {:.2f}".format(float(cotacoes_bit)))
        entry = entry* float(cotacoes_bit)
        print("Real para Bit-coin: R$ {:.2f}".format(entry))
        time.sleep(2)
    except:
        print("Valor inválido verifique sua entrada e tente novamente")
        time.sleep(1.5)
        convert_bit()

def sair():
    i=3
    print("Encerrando sistema...")
    while i != 0:
        time.sleep(0.6)
        print(f"{i}...")
        i-=1
    lauching = bool(False)

if __name__ == "__main__":
    main()  