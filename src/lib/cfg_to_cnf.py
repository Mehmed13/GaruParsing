from lib.tokenizer import *


def simplify_cfg(cfg_grammar):
    # I. S. cfg_grammar berbentuk list of list Production Rule suatu CFG
    # F. S. cfg_grammar berbentuk list of list Production Rule suatu CFG yang telah disimplifikasi
    #       Contoh: {'A': [['B']], 'B': [['C']]} menjadi {'A': [['C']]}.
    # Proses: Melakukan simplifikasi terhadap cfg_grammar

    tokens_terminal, terminal_rule = read_terminal('lib/Terminal_CFG.txt')

    # Mengubah ditionary menjadi list untuk memudahkan pemrosesan list
    list_grammar = []

    for rule in cfg_grammar:
        list_rule = cfg_grammar[rule]
        for i in range(len(list_rule)):
            listconv = list_rule[i]
            listconv.insert(0, rule)
            list_grammar.append(listconv)

    cfg_grammar.clear()

    # Proses simplifikasi
    i = 0
    while i < len(list_grammar):
        if ((len(list_grammar[i]) == 2) and ((list_grammar[i][1] in terminal_rule) or (list_grammar[i][1] not in tokens_terminal))):
            idx_terminal = []
            for j in range(0, len(list_grammar)):
                if list_grammar[j][0] == list_grammar[i][1]:
                    idx_terminal.append(j)
            insertion_idx = i + 1
            addition = 0
            for k in idx_terminal:
                new_rule = []
                for termnonterm in list_grammar[k + addition]:
                    new_rule.append(termnonterm)
                new_rule[0] = list_grammar[i][0]
                list_grammar.insert(insertion_idx, new_rule)
                addition += 1
            list_grammar.remove(list_grammar[i])
        i += 1

    # Mengubah list menjadi dictionary
    key = list_grammar[0][0]
    list_of_rule = []
    for i in range(len(list_grammar)):
        if (list_grammar[i][0] == key):
            list_of_rule.append(list_grammar[i][1:])
        else:
            cfg_grammar[key] = list_of_rule
            list_of_rule = []
            key = list_grammar[i][0]
            list_of_rule.append(list_grammar[i][1:])
            if (i == len(list_grammar)-1):
                cfg_grammar[key] = list_of_rule


def cnf_algorithm(cfg_grammar):
    # I.S. cfg_grammar adalah grammar dalam cfg yang sudah disimplifikasi
    # F.S. cfg_grammar berubah menjadi dalam bentuk cnf
    #      Contoh: {'S':[['A','B','C']]} diubah menjadi {'S':['A','X']}, {'X':[['B','C']]}

    # Proses: Konversi cfg menjadi cnf

    addition = 1
    repeat = 0
    while repeat < len(cfg_grammar):
        new_dict = {}
        for rule in cfg_grammar:
            list_rule = cfg_grammar[rule]
            for i in range(len(list_rule)):
                if (len(list_rule[i]) > 2):
                    new_rule = []
                    for j in range(1, len(list_rule[i])):
                        new_rule.append(list_rule[i][j])
                    for k in range(len(list_rule[i])-1, 0, -1):
                        list_rule[i].pop(k)
                    new_nonterm = new_rule[0] + "_trans"
                    if new_nonterm in new_dict:
                        new_nonterm += "{}".format(addition)
                        addition += 1
                    elif new_nonterm in cfg_grammar:
                        new_nonterm += "{}".format(addition)
                        addition += 1
                    list_rule[i].append(new_nonterm)
                    new_rule.insert(0, new_nonterm)
                    listEl = []
                    listEl.append(new_rule[1:])
                    new_dict[new_rule[0]] = listEl
        cfg_grammar.update(new_dict)
        repeat += 1


def write_cnf_file(cnf_grammar):
    # I.S. cnf_grammar adalah dictionary of production rule yang berada dalam bentuk cnf
    # F.S. terbentuk sebuah file *.txt yang berisi cnf
    #      Dictionary {'S': [['A','B']]} akan ditulis sebagai S -> A B

    # filename = input("Enter the output file name: ")
    # file = open('filename', 'w')
    file = open('lib/cnf.txt', 'w')

    for rule in cnf_grammar:
        list_rule = cnf_grammar[rule]
        file.write(rule)
        file.write(" ->")
        if (len(list_rule) == 1):
            for i in range(len(list_rule[0])):
                file.write(" {}".format(list_rule[0][i]))
        else:
            for i in range(len(list_rule)):
                for j in range(len(list_rule[i])):
                    file.write(" {}".format(list_rule[i][j]))
                if (i != len(list_rule)-1):
                    file.write(" |")
        file.write("\n")
    file.close()


def read_grammar_text(grammar_text):
    # Membaca file grammar_text, production rule tiap baris akan diubah menjadi bentuk dictionary
    # Contoh : Production rule berbentuk A -> B C D akan diubah menjadi {'A':[['B', 'C', 'D']]}.
    # Production rule yang memiliki dua bentuk atau lebih akan dipisah menjadi 2 list atau lebih
    # Contoh: S -> A | B akan diubah menjadi bentuk {'S':[['A'],['B']]}
    # Fungsi akan mengembalikan dictionary yang berisi production rule tiap baris

    text = open(grammar_text, 'r')
    textlines = text.readlines()
    text.close()

    grammar = {}

    for line in textlines:
        rule = line.replace(" ->", "").split()
        list_of_rules = []
        list_of_rules.append(rule[1:])
        grammar[rule[0]] = list_of_rules

    for rule in grammar:
        list_rule = grammar[rule]
        for item in list_rule:
            try:
                # Memisahkan rule yang berbentuk X -> Y | Z menjadi X -> Y dan X -> Z
                pipe_idx = item.index("|")

            except ValueError:
                # Apabila sebuah nonterminal tidak mengandung 2 production rule yang berbeda
                pipe_idx = -1

            if (pipe_idx != -1):
                insertion_idx = list_rule.index(item) + 1
                rule_branch = []
                for i in range(pipe_idx + 1, len(item)):
                    rule_branch.append(item[i])
                for j in range(pipe_idx, len(item)):
                    item.pop()
                list_rule.insert(insertion_idx, rule_branch)
    return grammar


def read_input(file_input_name):
    # Fungsi membaca file_input_name lalu mengembalikannya dalam bentuk list of string

    # Menampung file dalam format list of lines
    file_input = open(file_input_name, 'r')
    file_input_lines = file_input.readlines()
    file_input.close()

    # Tokenisasi dari list of lines
    raw_input = js_to_tokens(file_input_lines)

    # Mengubah raw_input menjadi dalam bentuk list of string yang disimpan dalam variabel tokens_input
    tokens_input = []

    for line in raw_input:
        for string in line:
            tokens_input.append(string)

    return tokens_input


def read_terminal(terminal_file_name):
    # Membaca file terminal dan menyimpannya dalam list of string
    # Fungsi mengembalikan terminal yang berisi list of string terminal

    file_terminal = open(terminal_file_name, "r")
    terminal_lines = file_terminal.readlines()
    file_terminal.close()

    tokens_terminal = []
    for line in terminal_lines:
        optimized_line = line.replace("\n", "")
        tokens_terminal.append(optimized_line)

    terminal_rulefile = open("lib/Rule_Terminal_CFG.txt", "r")
    terminal_ruletemp = terminal_rulefile.readlines()
    terminal_rulefile.close()

    terminal_rule = []
    for line in terminal_ruletemp:
        rule = line.replace("\n", "")
        terminal_rule.append(rule)

    return tokens_terminal, terminal_rule


def convert_cfg(cfg_text):
    # I. S. cfg_text merupakan suatu file berisi production rule suatu CFG
    # F. S. terbentuk sebuah file yang berisi cnf hasil convert dari cfg

    # Menampung bentuk list of list of production rule dari cfg_text
    grammar = read_grammar_text(cfg_text)

    # Membersihkan rule kosong
    removerule = []
    for rule in grammar:
        list_rule = grammar[rule]
        if (len(list_rule) == 0):
            removerule.append(rule)
    for i in removerule:
        grammar.pop(i)

    """
    Code testing

    sum = 0
    for rule in grammar:
        sum += len(grammar[rule])
        print(rule)
        for i in range(len(grammar[rule])):
            print((grammar[rule])[i])
        print(len(grammar[rule]))
        print('')
    print(sum)
    """

    # Melakukan simplifikasi dari cfg_grammar
    simplify_cfg(grammar)

    # Mengubah cfg menjadi cnf
    cnf_algorithm(grammar)
    # Menulis grammar cnf ke dalam file *.txt
    write_cnf_file(grammar)
