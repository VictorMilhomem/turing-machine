from Machine.machine import TuringMachine


def binary_increment():
    """ Turing machine that increment by 1 a binary number """

    number = str(input("Digite um número binário:\n"))
    sep = {}
    for i in range(len(number)):
        if int(number[i]) == 1 or int(number[i]) == 0:
            sep[i] = number[i]
        else:
            raise KeyError("O número deve ser binário!")

    turing_machine = TuringMachine(states={'q0', 'q1', 'q2'},
                       symbols={'0', '1'},
                       blank_symbol=' ',
                       input_symbols={'1'},
                       initial_state='q0',
                       accepting_states={'q2'},
                       transitions={
                           ('q0', '0'): ('q0', '0', 1),
                           ('q0', '1'): ('q0', '1', 1),
                           ('q0', ' '): ('q1', ' ', -1),
                           ('q1', '1'): ('q1', '0', -1),
                           ('q1', '0'): ('q2', '1', -1),
                           ('q1', ' '): ('q2', '1', -1),
                       })
    turing_machine.initialize(sep)
    turing_machine.runMachine(show_accepted=False)

def binary_divisible_3():
    """ Turing machine that verify if a binary number is divisible by 3 """
    
    number = str(input("Digite um número binário:\n"))
    sep = {}
    for i in range(len(number)):
        if int(number[i]) == 1 or int(number[i]) == 0:
            sep[i] = number[i]
        else:
            raise KeyError("O número deve ser binário!")

    turing_machine = TuringMachine(states={'q0', 'q1', 'q2', 'q3'},
                       symbols={'0', '1'},
                       blank_symbol=' ',
                       input_symbols={'1', '0'},
                       initial_state='q0',
                       accepting_states={'q3'},
                       transitions={
                           ('q0', '0'): ('q0', '0', 1),
                           ('q0', '1'): ('q1', '1', 1),
                           ('q0', ' '): ('q3', ' ', 1),
                           ('q1', '1'): ('q0', '1', 1),
                           ('q1', '0'): ('q2', '0', 1),
                           ('q2', '0'): ('q1', '0', 1),
                           ('q2', '1'): ('q2', '1', 1),
                       })
    turing_machine.initialize(sep)
    turing_machine.runMachine(show_accepted=False)

def copies_string_one():
    """ Turing machine that copies a string sequence of 1's  """

    number = str(input("Digite uma string de 1's:\n"))
    sep = {}
    for i in range(len(number)):
        if int(number[i]) == 1:
            sep[i] = number[i]
        else:
            raise KeyError("String inválido!")

    turing_machine = TuringMachine(states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5'},
                       symbols={'0', '1'},
                       blank_symbol='0',
                       input_symbols={'1'},
                       initial_state='q0',
                       accepting_states={'q5'},
                       transitions={
                           ('q0', '0'): ('q5', '0', 1),
                           ('q0', '1'): ('q1', '0', 1),
                           ('q1', '0'): ('q2', '0', 1),
                           ('q1', '1'): ('q1', '1', 1),
                           ('q2', '0'): ('q3', '1', -1),
                           ('q2', '1'): ('q2', '1', 1),
                           ('q3', '0'): ('q4', '0', -1),
                           ('q3', '1'): ('q3', '1', -1),
                           ('q4', '0'): ('q0', '1', 1),
                           ('q4', '1'): ('q4', '1', -1),
                       })
    turing_machine.initialize(sep)
    turing_machine.runMachine(show_accepted=False)

def three_equal_lengths():
    """ Turing machine that accepts a string in L = {a^n b^n c^n | n >= 1} """

    number = str(input("Digite uma string de a*b*c*:\n"))
    sep = {}
    for i in range(len(number)):
        if number[i] == 'a' or number[i] == 'b' or number[i] == 'c':
            sep[i] = number[i]
        else:
            raise KeyError("String inválido!")

    turing_machine = TuringMachine(states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5'},
                       symbols={'a', 'b', 'c'},
                       blank_symbol=' ',
                       input_symbols={'a', 'b', 'c'},
                       initial_state='q0',
                       accepting_states={'q5'},
                       transitions={
                           ('q0', 'a'): ('q1', 'A', 1),
                           ('q0', 'B'): ('q4', 'B', 1),
                           ('q1', 'a'): ('q1', 'a', 1),
                           ('q1', 'B'): ('q1', 'B', 1),
                           ('q1', 'b'): ('q2', 'B', 1),
                           ('q2', 'b'): ('q2', 'b', 1),
                           ('q2', 'C'): ('q2', 'C', 1),
                           ('q2', 'c'): ('q3', 'C', -1),
                           ('q3', 'a'): ('q3', 'a', -1),
                           ('q3', 'B'): ('q3', 'B', -1),
                           ('q3', 'b'): ('q3', 'b', -1),
                           ('q3', 'C'): ('q3', 'C', -1),
                           ('q3', 'A'): ('q0', 'A', 1),
                           ('q4', 'B'): ('q4', 'B', 1),
                           ('q4', 'C'): ('q4', 'C', 1),
                           ('q4', ' '): ('q5', ' ', 1),
                       })
    turing_machine.initialize(sep)
    turing_machine.runMachine()

def palindrome():
    """ Turing machine that accepts a string in L =  { ww^r| w: a*b*} """

    number = str(input("Digite uma string de a's e b's:\n"))
    sep = {}
    for i in range(len(number)):
        if number[i] == 'a' or number[i] == 'b':
            sep[i] = number[i]
        else:
            raise KeyError("String inválida!")

    turing_machine = TuringMachine(states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7'},
                       symbols={'a', 'b'},
                       blank_symbol=' ',
                       input_symbols={'a', 'b'},
                       initial_state='q0',
                       accepting_states={'q6'},
                       transitions={
                           ('q0', 'a'): ('q1', ' ', 1),
                           ('q0', 'b'): ('q2', ' ', 1),
                           ('q0', ' '): ('q6', ' ', 1),
                           ('q1', 'a'): ('q1', 'a', 1),
                           ('q1', 'b'): ('q1', 'b', 1),
                           ('q1', ' '): ('q3', ' ', -1),
                           ('q2', 'a'): ('q2', 'a', 1),
                           ('q2', 'b'): ('q2', 'b', 1),
                           ('q2', ' '): ('q4', ' ', -1),
                           ('q3', 'a'): ('q5', ' ', -1),
                           ('q3', 'b'): ('q7', 'b', 1),
                           ('q3', ' '): ('q6', ' ', 1),
                           ('q4', 'a'): ('q7', 'a', 1),
                           ('q4', 'b'): ('q5', ' ', -1),
                           ('q4', ' '): ('q6', ' ', 1),
                           ('q5', 'a'): ('q5', 'a', -1),
                           ('q5', 'b'): ('q5', 'b', -1),
                           ('q5', ' '): ('q0', ' ', 1),
                       })
    turing_machine.initialize(sep)
    turing_machine.runMachine()