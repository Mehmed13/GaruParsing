from .tokenizer import *


def get_idx_rule(cfg_grammar, nonterminal):
    # Prekondisi: variabel tersedia dalam grammar
    # Mengembalikan index dari rule dengan variabel yang dicari dalam cfg_grammar
    # dalam bentuk list. Contoh: [1, 2].
    pass


def simplify_cfg(cfg_grammar):
    # I. S. cfg_grammar berbentuk list of list Production Rule suatu CFG
    # F. S. cfg_grammar berbentuk list of list Production Rule suatu CFG yang telah disimplifikasi
    #       Contoh: ['S', 'A'] dan ['A','Aa','Ab'] menjadi ['S','Aa','Ab'].
    # Proses: Melakukan simplifikasi terhadap cfg_grammar

    pass


def cnf_algorithm(cfg_grammar):
    # I.S. cfg_grammar adalah grammar dalam cfg yang sudah disimplifikasi
    # F.S. cfg_grammar berubah menjadi dalam bentuk cnf
    #       Contoh: ['S', 'A','B','C'] diubah menjadi ['S','A','X'], ['X','B','C']
    # Proses: Konversi cfg menjadi cnf
    pass


def write_cnf_file(cnf_grammar):
    # I.S. cnf_grammar adalah list of list of production rule yang berada dalam bentuk cnf
    # F.S. terbentuk sebuah file *.txt yang berisi cnf
    #      List ['S','A','B'] akan ditulis sebagai S -> A B
    pass


def read_grammar_text(grammar_text):
    # Membaca file grammar_text, production rule tiap baris akan diubah menjadi bentuk list
    # Contoh : Production rule berbentuk A -> B C D akan diubah menjadi ['A', 'B', 'C', 'D'].
    # Production rule yang memiliki dua bentuk atau lebih akan dipisah menjadi 2 list atau lebih
    # Contoh: S -> A | B akan diubah menjadi bentuk ['S', 'A'] dan ['S', 'B']
    # Fungsi akan mengembalikan list of list yang berisi production rule tiap baris
    pass


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

    return tokens_terminal


def convert_cfg(cfg_text):
    # I. S. cfg_text merupakan suatu file berisi production rule suatu CFG
    # F. S. terbentuk sebuah file yang berisi cnf hasil convert dari cfg

    # Menampung bentuk list of list of production rule dari cfg_text
    grammar = read_grammar_text(cfg_text)

    # Membersihkan rule kosong
    for rule in grammar:
        if (len(rule) == 0):
            grammar.remove(rule)

    # Melakukan simplifikasi dari cfg_grammar
    simplify_cfg(grammar)
    # Mengubah cfg menjadi cnf
    cnf_algorithm(grammar)
    # Menulis grammar cnf ke dalam file *.txt
    write_cnf_file(grammar)


def write_to_file(cfg_grammar):
    # I. S. cfg_grammar berbentuk list of list Production Rule suatu CFG
    # F. S. Menuliskan grammar dalam bentuk dalam file .txt
    #       List ['S','A','B'] akan ditulis sebagai S -> A B
    pass
