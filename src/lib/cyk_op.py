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
    # print(tokens_input)
    # print(tokens_terminal)
    idx = 0  # inisialisasi index tokens_input
    tokens_input_final = []  # inisialisasi list yang akan menampung tokens semifinal
    n_tokens_initial = len(tokens_input)
    while (idx < n_tokens_initial):
        token = tokens_input[idx]
        if skip_for_string:  # sesudah string dibuka
            if (token == "'" or token == '"'):
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
            if (token[:7] not in tokens_terminal):  # Jika token bukan merupakan terminal
                category = categorize_token(token)
                tokens_input_final.append(category)
                idx += 1
            else:  # jika token merupakan terminal
                if (token == '/'):
                    if (tokens_input[idx+1] == '/'):  # comment single line
                        idx += 2
                        while ((idx < n_tokens_initial) and (tokens_input[idx][:7] != "endline")):
                            idx += 1
                        if (tokens_input[idx][:7] == "endline"):
                            tokens_input_final.append(tokens_input[idx])
                            idx += 1
                    elif (tokens_input[idx+1] == '*'):  # comment multiline
                        idx += 2
                        while ((idx < n_tokens_initial) and (tokens_input[idx] != '*' and tokens_input[idx+1] != '/')):
                            idx += 1
                        if ((tokens_input[idx] == '*') and (tokens_input[idx+1] == '/')):
                            idx += 2
                    else:  # jika token terminal lain
                        tokens_input_final.append(token)
                        idx += 1
                elif ((token == "'") or (token == '"')):  # Jika pembuka string
                    skip_for_string = True
                    tokens_input_final.append(token)
                    open_string = token
                else:  # jika token terminal lain
                    tokens_input_final.append(token)
                    idx += 1

                    # for token in tokens_input:
                    #     idx = tokens_input.index(token)
                    #     print(idx, ":", token)
                    #     if skip_for_string:  # Jika token bagian dari string
                    #         if (token == "'") or (token == '"'):  # akhir dari string
                    #             skip_for_string = False
                    #             if (token != open_string):
                    #                 next_idx = idx
                    #                 while (tokens_input[next_idx][:7] != "endline"):
                    #                     next_idx += 1
                    #                 # tokens_input[idx][:7] == "endline"
                    #                 # catatan lines error
                    #                 error_Lines.append(tokens_input[next_idx][7:])

                    #         else:  # mengubah token di dalam string menjadi word
                    #             idx = tokens_input.index(token)
                    #             tokens_input.pop(idx)
                    #             tokens_input.insert(idx, "word")
                    #             # tokens_input.remove(token)
                    #     else:  # jika token bukan bagian dari string
                    #         if (token[:7] not in tokens_terminal):
                    #             category = categorize_token(token)
                    #             tokens_input.pop(idx)
                    #             tokens_input.insert(idx, category)
                    #             # tokens_input.remove(token)
                    #         else:
                    #             if (token == '/'):
                    #                 if (tokens_input[idx+1] == '/'):  # jika comment single line
                    #                     for i in range(2):
                    #                         # tokens_input.remove(tokens_input[idx])
                    #                         tokens_input.pop(idx)
                    #                     next_idx = idx
                    #                     n_tokens_initial = len(tokens_input)
                    #                     # remove semua elemen dalam comment
                    #                     while (next_idx < n_tokens_initial) and (tokens_input[idx][:7] != 'endline'):
                    #                         # tokens_input.remove(tokens_input[idx])
                    #                         tokens_input.pop(idx)
                    #                         next_idx += 1
                    #                     # menghapus token endline
                    #                     if tokens_input[idx][:7] == "endline":
                    #                         # tokens_input.remove(tokens_input[idx])
                    #                         tokens_input.pop(idx)
                    #                 elif (tokens_input[idx+1] == '*'):  # jika  comment multiline
                    #                     for i in range(2):
                    #                         # tokens_input.remove(tokens_input[idx])
                    #                         tokens_input.pop(idx)
                    #                     next_idx = idx
                    #                     n_tokens_initial = len(tokens_input)
                    #                     while (next_idx < n_tokens_initial) and ((tokens_input[idx] != "*") and (tokens_input[idx + 1] != "/")):
                    #                         # tokens_input.remove(tokens_input[idx])
                    #                         tokens_input.pop(idx)
                    #                         next_idx += 1
                    #                     if (tokens_input):
                    #                         if (tokens_input[idx] == "*") and (tokens_input[idx + 1] == "/"):
                    #                             for i in range(2):
                    #                                 # tokens_input.remove(tokens_input[idx])
                    #                                 tokens_input.pop(idx)
                    #                     else:
                    #                         break

                    #             elif (token == "'"):
                    #                 skip_for_string = True
                    #                 open_string = "'"
                    #             elif (token == '"'):
                    #                 skip_for_string = True
                    #                 open_string = '"'
    print(tokens_input_final)

    # Menghapus endline pada tokens
    n_tokens_temp = len(tokens_input_final)
    tokens_input_semifinal = tokens_input_final.copy()
    for i in range(n_tokens_temp):
        if ("endline" in tokens_input_semifinal[i]):
            token = tokens_input_semifinal[i]
            tokens_input_final.remove(token)
    print()
    print()
    print(tokens_input_final)
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
        print()
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
    print(last_el)
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
