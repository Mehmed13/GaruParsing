from .tokenizer import *


def simplify_cfg(cfg_grammar):
    # I. S. cfg_grammar berbentuk list of list Production Rule suatu CFG
    # F. S. cfg_grammar berbentuk list of list Production Rule suatu CFG yang telah disimplifikasi
    #       Contoh: {'A': [['B']], 'B': [['C']]} menjadi {'A': [['C']]}.
    # Proses: Melakukan simplifikasi terhadap cfg_grammar
    
    tokens_terminal, terminal_rule = read_terminal('terminal.txt')

    listremove = []

    for rule in cfg_grammar:
        list_rule = cfg_grammar[rule]
        if ((len(list_rule) == 1) and (len(list_rule[0]) == 1) and (list_rule[0][0] in cfg_grammar) and ((list_rule[0][0] in terminal_rule) or (list_rule[0][0] not in tokens_terminal))):
            while ((len(list_rule) == 1) and (list_rule[0][0] in cfg_grammar)):
                for i in range(len(cfg_grammar[list_rule[0][0]])):
                    list_rule.append((cfg_grammar[list_rule[0][0]])[i])
                if (list_rule[0][0] not in listremove):
                    listremove.append(list_rule[0][0])
                list_rule.remove(list_rule[0])

    for i in range(len(listremove)):
        cfg_grammar.pop(listremove[i])


def cnf_algorithm(cfg_grammar):
    # I.S. cfg_grammar adalah grammar dalam cfg yang sudah disimplifikasi
    # F.S. cfg_grammar berubah menjadi dalam bentuk cnf
    #      Contoh: ['S','A','B','C'] diubah menjadi ['S','A','X'], ['X','B','C']    ['M','D','E','F']
    # Proses: Konversi cfg menjadi cnf
    list1 = []
    list2 = []
    addition = 1
    for rule in cfg_grammar:
        list_rule = cfg_grammar[rule]
        for i in range(len(list_rule)):
            if (len(list_rule[i])) > 2:
                new_rule = []
                for j in range(1, len(list_rule[i])):
                    new_rule.append(list_rule[i][j])
                for k in range(1, len(list_rule[i])):
                    list_rule[i].pop()
                new_nonterm = new_rule[0] + "_trans"
                if new_nonterm in list1:
                    new_nonterm += "{}".format(addition)
                    addition += 1
                elif new_nonterm in cfg_grammar:
                    new_nonterm += "{}".format(addition)
                    addition += 1
                list_rule[i].append(new_nonterm)
                new_rule.insert(0, new_nonterm)
                list1.append(new_rule[0])
                list2.append(new_rule[1:])

    for i in range(len(list1)):
        list3 = []
        list3.append(list2[0])
        cfg_grammar[list1[i]] = list3
        list2 = list2[1:]

    cfg_grammar2 = cfg_grammar.copy()
    for rule2 in cfg_grammar2:
        list_rule = cfg_grammar[rule2]
        if (len(list_rule[0]) > 2):
            cnf_algorithm(cfg_grammar)


def write_cnf_file(cnf_grammar):
    # I.S. cnf_grammar adalah list of list of production rule yang berada dalam bentuk cnf
    # F.S. terbentuk sebuah file *.txt yang berisi cnf
    #      List ['S','A','B'] akan ditulis sebagai S -> A B

    # filename = input("Enter the output file name: ")
    # file = open('filename', 'w')
    file = open('cnf.txt', 'w')
    for rule in cnf_grammar:
        list_rule = cnf_grammar[rule]
        file.write(rule)
        file.write(" ->")
        if (len(list_rule) > 1):
            for i in range(len(list_rule[0])):
                file.write(" {}".format(list_rule[i]))
        else:
            for i in range(len(list_rule)):
                for j in range(len(list_rule[0])):
                    file.write(" {}".format(list_rule[i][j]))
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

    terminal_rulefile = open("terminal_rule.txt", "r")
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
    for rule in grammar:
        list_rule = grammar[rule]
        if (len(list_rule) == 0):
            grammar.pop(rule)

    # Melakukan simplifikasi dari cfg_grammar
    simplify_cfg(grammar)
    # Mengubah cfg menjadi cnf
    cnf_algorithm(grammar)
    # Menulis grammar cnf ke dalam file *.txt
    write_cnf_file(grammar)