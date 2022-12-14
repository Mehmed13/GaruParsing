from lib.cfg_to_cnf import *


def cyk_algorithm(file_terminal, cnf_grammar, file_input):
    # Mengembalikan array of string yang merupakan elemen terakhir dari cyk table (puncak)
    tokens_terminal, tokens_terminal_rule = read_terminal(file_terminal)
    tokens_input = read_input(file_input)
    error_Lines = []
    cyk_table = None

    # Checker
    # print(tokens_input)
    # print(tokens_terminal)

    # Preprocessing tokens_terminal dengan menghapus semua token yang merupakan comment
    # mengubah semua token yang berada di dalam string menjadi kategori word
    # mengubah token yang bukan terminal sesuai kategori {word, num, undef}
    skip_for_string = False
    open_string = None

    idx = 0  # inisialisasi index tokens_input
    tokens_input_final = []  # inisialisasi list yang akan menampung tokens semifinal
    n_tokens_initial = len(tokens_input)
    while (idx < n_tokens_initial):
        token = tokens_input[idx]
        if skip_for_string:  # sesudah string dibuka
            if ((token == "'") or (token == '"')):
                if (token == open_string):  # jika bertemu penutup string
                    skip_for_string = False
                    tokens_input_final.append(token)
                    idx += 1
                else:  # jika bukan penutup string
                    tokens_input_final.append("word")
                    idx += 1
            else:  # Jika token berada dalam string
                tokens_input_final.append("word")
                idx += 1
        else:  # Jika tidak berada di dalam string
            if (token[:10] not in tokens_terminal):  # Jika token bukan merupakan terminal
                category = categorize_token(token)
                tokens_input_final.append(category)
                idx += 1
                if (category == "undef"):
                    next_idx = idx
                    while (tokens_input[next_idx][:10] != "endlineYaa"):
                        next_idx += 1
                    error_Lines.append(tokens_input[next_idx][10:])
            else:  # jika token merupakan terminal
                if (token == "~C_A~"):
                    idx += 1
                    while ((idx < n_tokens_initial) and (tokens_input[idx][:10] != "endlineYaa")):
                        idx += 1
                    if (tokens_input[idx][:10] == "endlineYaa"):
                        tokens_input_final.append(tokens_input[idx])
                        idx += 1

                elif (token == "~C_O~"):
                    idx += 1
                    while ((idx < n_tokens_initial) and (tokens_input[idx] != "~C_C~")):
                        idx += 1
                    if (idx < n_tokens_initial):
                        if (tokens_input[idx] == "~C_C~"):
                            idx += 1
                    else:
                        tokens_input_final.append("undef")

                elif ((token == "'") or (token == '"')):  # Jika pembuka string
                    skip_for_string = True
                    tokens_input_final.append(token)
                    open_string = token
                    idx += 1
                else:  # jika token terminal lain
                    tokens_input_final.append(token)
                    idx += 1
    # print(tokens_input_final)

    # Menghapus endlineYaa pada tokens
    n_tokens_temp = len(tokens_input_final)
    tokens_input_semifinal = tokens_input_final.copy()
    for i in range(n_tokens_temp):
        if ("endlineYaa" in tokens_input_semifinal[i]):
            token = tokens_input_semifinal[i]
            tokens_input_final.remove(token)
    # print()
    # print()
    # print(tokens_input_final)
    n_tokens_final = len(tokens_input_final)

    if (n_tokens_final != 0):
        # Inisiasi cyk_table
        cyk_table = [[[] for i in range(n_tokens_final - j)]
                     for j in range(n_tokens_final)]

        # Algoritma filling table:
        # BASE LEVEL:
        # Mengisi baris pertama sesuai terminal dari tokens_input yang dibaca
        # tiap sel diisi dengan aturan produksi yang menghasilkan terminal tersebut
        # print(cnf_grammar)
        for i, token in enumerate(tokens_input_final):
            for rule in cnf_grammar:
                for list_rule in cnf_grammar[rule]:
                    if list_rule[0] == token:
                        cyk_table[0][i].append(rule)
        # print(cyk_table)
        # print()

        # REKURENS:
        # Mengisi cyk table bottom to top (Dalam representasi matriks kali ini terbalik)
        # Berhenti hingga di puncak (level n_tokens final)
        for i in range(1, n_tokens_final):
            for j in range(n_tokens_final-i):
                for k in range(i):
                    # Fill the cell in cyk_table
                    for production1 in cyk_table[i-k-1][j]:
                        for production2 in cyk_table[k][j+i-k]:
                            target_string = [production1, production2]
                            # print(target_string)
                            for rule in cnf_grammar:
                                for list_rule in cnf_grammar[rule]:
                                    # print(list_rule)
                                    if (target_string == list_rule) and (rule not in cyk_table[i][j]):
                                        cyk_table[i][j].append(rule)
                                # break
            #                 break
            #             break
            #         break
            #     break
            # break

        # print(cyk_table)
        return cyk_table[n_tokens_final-1][0], error_Lines

    else:
        return ["START"], []


def check_validity(file_terminal, cnf_cnf_grammar, file_input):
    # I.S. file_terminal adalah nama file yang berisi kumpulan terminal dari cnf_grammar
    #     cnf_cnf_grammar adalah array of array of string yang berisikan rule dalam cnf
    #     file_input adalah nama file input yan g akan dicek validity-nya
    # F.S. Validity dari input file akan ditampilkan. Menampilkan "Accepted" jika valid
    #      dan menampilkan "Syntax Error" jika tidak valid.
    last_el, error_Lines = cyk_algorithm(
        file_terminal, cnf_cnf_grammar, file_input)
    valid = False
    # print(last_el)
    # Pengecekan elemen top
    for term in last_el:
        if term == "START":
            print("Accepted")
            valid = True
            break
    if (not valid):
        print("Syntax Error")
        for error in error_Lines:
            print("Error pada line ke-", error)
