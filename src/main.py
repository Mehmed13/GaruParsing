import sys
from lib.cfg_to_cnf import *
from lib.cyk_op import *
from lib.tokenizer import *
import time

# Setup


# run program
if __name__ == "__main__":
    # start = time.time()
    # simpan input nama file ke dalam variabel
    file_input = "lib/test/"+sys.argv[1]
    # cfg.txt diubah terlebih dahulu menjadi cnf.txt
    cnf_text = convert_cfg("lib/cfg.txt")
    # cnf.txt yang sudah ada diconvert menjadi rule dalam bentuk List of List of string untuk digunakan dalam cyk algorithm
    cnf_grammar = read_grammar_text("lib/cnf.txt")
    # print(len(cnf_grammar))
    # write_cnf_file(cnf_grammar)

    check_validity("lib/Terminal_CFG.txt", cnf_grammar, file_input)
    # print(time.time()-start)
