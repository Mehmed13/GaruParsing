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

    for token in tokens_input:
        idx = tokens_input.index(token)
        if skip_for_string:  # Jika token bagian dari string
            if (token == "'") or (token == '"'):  # akhir dari string
                skip_for_string = False
                if (token != open_string):
                    next_idx = idx
                    while (tokens_input[next_idx][:7] != "endline"):
                        next_idx += 1
                    # tokens_input[idx][:7] == "endline"
                    # catatan lines error
                    error_Lines.append(tokens_input[next_idx][7:])

            else:  # mengubah token di dalam string menjadi word
                idx = tokens_input.index(token)
                tokens_input.insert(idx, "word")
                tokens_input.remove(token)
        else:  # jika token bukan bagian dari string
            if (token[:7] not in tokens_terminal):
                category = categorize_token(token)
                tokens_input.insert(idx, category)
                tokens_input.remove(token)
            else:
                if (token == '/'):
                    if (tokens_input[idx+1] == '/'):  # jika comment single line
                        for i in range(2):
                            tokens_input.remove(tokens_input[idx])
                        next_idx = idx
                        n_tokens_initial = len(tokens_input)
                        # remove semua elemen dalam comment
                        while (next_idx < n_tokens_initial) and (tokens_input[idx][:7] != 'endline'):
                            tokens_input.remove(tokens_input[idx])
                            next_idx += 1
                        # menghapus token endline
                        if tokens_input[idx][:7] == "endline":
                            tokens_input.remove(tokens_input[idx])
                    elif (tokens_input[idx+1] == '*'):  # jika  comment multiline
                        for i in range(2):
                            tokens_input.remove(tokens_input[idx])
                        next_idx = idx
                        n_tokens_initial = len(tokens_input)
                        while (next_idx < n_tokens_initial) and ((tokens_input[idx] != "*") or (tokens_input[idx + 1] != "/")):
                            tokens_input.remove(tokens_input[idx])
                            next_idx += 1
                        if (tokens_input):
                            if (tokens_input[idx] == "*") and (tokens_input[idx + 1] == "/"):
                                for i in range(2):
                                    tokens_input.remove(tokens_input[idx])
                        else:
                            break

                elif (token == "'"):
                    skip_for_string = True
                    open_string = "'"
                elif (token == '"'):
                    skip_for_string = True
                    open_string = '"'

    n_tokens_temp = len(tokens_input)
    initial_tokens_input = tokens_input.copy()
    for i in range(n_tokens_temp):
        if ("endline" in initial_tokens_input[i]):
            token = initial_tokens_input[i]
            tokens_input.remove(token)
    print(tokens_input)

    if (len(tokens_input) != 0):
        # Inisiasi cyk_table
        n_tokens_final = len(tokens_input)
        cyk_table = [[[] for i in range(n_tokens_final - j)]
                     for j in range(n_tokens_final)]

        # Algoritma filling table:
        # BASE LEVEL:
        # Mengisi baris pertama sesuai terminal dari tokens_input yang dibaca
        # tiap sel diisi dengan aturan produksi yang menghasilkan terminal tersebut
        # print(cnf_grammar)
        # print()
        # print()
        # print()
        for i, token in enumerate(tokens_input):
            for rule in cnf_grammar:
                for list_rule in cnf_grammar[rule]:
                    if list_rule[0] == token:
                        cyk_table[0][i].append(rule)
        # print(cyk_table)
        print()
        # print()
        # LEVEL DI ATAS BASE:
        # Misal kita ingin menentukan X[i][j] pada cyk_table
        # kita telah mengisi X pada baris-baris di atasnya
        # Misal:
        # [['B'] ['A','C']]
        # [[A -> B A] [S -> B C] maka diisi ['A','S']]
        # Pertama, iterasi semua cell pada cyk table
        # for i in range(1, n_tokens_final):
        #     for j in range(n_tokens_final-i):

        #         left_i = 0
        #         right_i = i - 1
        #         right_j = j + 1

        #         while (left_i < i and right_i >= 0):
        #             left = cyk_table[left_i][j]
        #             right = cyk_table[right_i][right_j]

        #             left_cell = [n for n in left]
        #             right_cell = [n for n in right]

        #             for first in left_cell:
        #                 for second in right_cell:
        #                     target_string = []
        #                     target_string.append(first)
        #                     target_string.append(second)
        #                     print(target_string)
        #                     print()
        #                     print()
        #                     for rule in cnf_grammar:
        #                         for alt in range(len(cnf_grammar[rule])):
        #                             if (target_string == cnf_grammar[rule][alt]) and (rule not in cyk_table[i][j]):
        #                                 cyk_table[i][j].append(rule)
        #             right_j += 1
        #             left_i += 1
        #             right_i -= 1
        for i in range(1, n_tokens_final):
            for j in range(n_tokens_final-i):
                for k in range(i):
                    # Test for combinations
                    for production1 in cyk_table[i-k-1][j]:
                        for production2 in cyk_table[k][j+i-k]:
                            # try:
                            #     cyk_table[i][j] = cnf_grammar[production1+production2]
                            # except KeyError:
                            #     continue
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
        return ["ALGORITHM"]


def check_validity(file_terminal, cnf_cnf_grammar, file_input):
    # I.S. file_terminal adalah nama file yang berisi kumpulan terminal dari cnf_grammar
    #     cnf_cnf_grammar adalah array of array of string yang berisikan rule dalam cnf
    #     file_input adalah nama file input yan g akan dicek validity-nya
    # F.S. Validity dari input file akan ditampilkan. Menampilkan "Accepted" jika valid
    #      dan menampilkan "Syntax Error" jika tidak valid.
    last_el, error_Lines = cyk_algorithm(
        file_terminal, cnf_cnf_grammar, file_input)
    valid = False
    print(last_el)
    for term in last_el:
        if term == "ALGORITHM":
            print("Accepted")
            valid = True
            break
    if (not valid):
        print("Syntax Error")
        for error in error_Lines:
            print("Error pada line ke-", error)
