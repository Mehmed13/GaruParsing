from .cfg_to_cnf import *


def cyk_algorithm(file_terminal, cnf_grammar, file_input):
    # Mengembalikan array of string yang merupakan elemen terakhir dari cyk table (puncak)
    tokens_terminal = read_terminal(file_terminal)
    tokens_input = read_input(file_input)
    cyk_table = None

    # Checker
    print(tokens_input)
    print(tokens_terminal)

    # Pengisian cyk_table, Belum sleesai
    n_tokens = len(tokens_input)

    return cyk_table[n_tokens-1][0]


def check_validity(file_terminal, cnf_grammar, file_input):
    # I.S. file_terminal adalah nama file yang berisi kumpulan terminal dari grammar
    #     cnf_grammar adalah array of array of string yang berisikan rule dalam cnf
    #     file_input adalah nama file input yang akan dicek validity-nya
    # F.S. Validity dari input file akan ditampilkan. Menampilkan "Accepted" jika valid
    #      dan menampilkan "Syntax Error" jika tidak valid.
    last_el = cyk_algorithm(file_terminal, cnf_grammar, file_input)
    valid = False
    for term in last_el:
        if term == "SS":
            print("Accepted")
            valid = True
            break
    if (not valid):
        print("Syntax Error")
