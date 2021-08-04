from Machine import *
import sys

def intro():
    print("############################### Máquina de Turing Simulação ###############################")
    print("#    (1) Incremento de binário                                                            #")
    print("#    (2) Verificar se binário é divisível por 3                                           #")
    print("#    (3) Cópia de string de 1's                                                           #")
    print("#    (4) Verificar se string de a's, b's, c's pertence a L =  { a^n b^n c^n| n >= 1}      #")
    print("#    (5) Verificar se string de a's, b's pertence a L =  { ww^r| w: a*b*}                 #")
    print("#    (6) Sair                                                                             #")
    print("###########################################################################################")


def run():
    running = True
    valid = ["s", "sim"]
    intro()
    while running:
        fun = int(input("Selecione a Máquina de Turing: "))
        if fun == 1:
            binary_increment()
        elif fun == 2:
            binary_divisible_3()
        elif fun == 3:
            copies_string_one()
        elif fun == 4:
            three_equal_lengths()
        elif fun == 5:
            palindrome()
        elif fun == 6:
            sys.exit(0)
        else:
            print("Máquina inexistente\n")
            intro()
            continue

        cont = str(input("Deseja sair (s/n)? ").lower())
        if cont in valid:
            sys.exit(0)
        else:
            intro()
            continue

        

if __name__ == '__main__':
    run()