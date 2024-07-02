from imports import *

option = int(input("""
=======MENU=======
1 - Dolar / Real
2 - Euro / Real
3 - Bit / Real
                   
0 - Sair
==================
"""))

match option:
    case 1:
        os.system('cls')
        cotacoes_dolar = float(cotacoes_dolar)
        entry = float(input("======Dolar para Real======\nValor em Real: R$"))
        print("Cotação do Dolar: {:.2f}".format(cotacoes_dolar))
        entry = entry* float(cotacoes_dolar)
        print("Real para Dolar: R$ {:.2f}".format(entry))
    case 2:
        os.system('cls')
        cotacoes_euro = float(cotacoes_euro)
        entry = float(input("======Euro para Real======\nValor em Real: R$"))
        print("Cotação do Euro: {:.2f}".format(cotacoes_euro))
        entry = entry* float(cotacoes_euro)
        print("Real para Euro: R$ {:.2f}".format(entry))
    case 3:
        os.system('cls')
        cotacoes_bit = float(cotacoes_bit)
        entry = float(input("======Bit-Coin para Real======\nValor em Real: R$"))
        print("Cotação do Bit: {:.2f}".format(cotacoes_bit))
        entry = entry* float(cotacoes_bit)
        print("Real para Bit-coin: R$ {:.2f}".format(entry))