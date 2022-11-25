def categorize_token(token):
    # Fungsi menerima token yang tidak terdapat dalam terminal. Apabila berbentuk variabel yang dapat diterima oleh python, maka
    # fungsi akan mengembalikan 'word'. Apabila berbentuk variabel, maka fungsi akan mengembalikan 'num'. Apabila tidak memenuhi
    # keduanya, maka fungsi akan mengembalikan 'undef'.

    # Deklarasi character yang termasuk ke dalam number dan
    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    variable_prefix = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L',
                       'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'u', 'U', 'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z', '_']
    if token[0] not in variable_prefix:
        if token[0] in number:
            for char in token[1:]:
                if char not in number:
                    return "undef"  # kasus kalo ada nama variabel yang diawali dengan angka
            return "num"
        else:
            return "undef"
    else:
        for char in token[1:]:
            if (char not in number) and (char not in variable_prefix):
                return "undef"
        return "word"


def js_to_tokens(js_file):
    # Fungsi menerima file *.js yang telah dalam format list of lines
    # Fungsi ini lalu mengubahnya menjadi dalam bentuk List of List of string (tokenisasi)
    line_index = 1
    tokens_temp = []

    for line in js_file:
        line = line.replace('~LO_AN~', '@')
        line = line.replace('~LO_OR~', '@')
        line = line.replace('~EX~', '@')
        line = line.replace('~GR_EQ~', '@')
        line = line.replace('~LE_EQ~', '@')
        line = line.replace('~EQ_TO~', '@')
        line = line.replace('~NO_EQ~', '@')
        line = line.replace('~E_E_E~', '@')
        line = line.replace('~N_E_E~', '@')
        line = line.replace('~P_P~', '@')
        line = line.replace('~M_M~', '@')
        line = line.replace('~C_A~', '@')
        line = line.replace('~C_O~', '@')
        line = line.replace('~C_C~', '@')  # KALAU MISAL ADA WORD YG NEGASI GMN ? 
        line = line.replace('~F_R_S~', '@')
        line = line.replace('~R_S~', '@')
        line = line.replace('~L_S~', '@')
        # replacement 
        line = line.replace('~', ' ~ ')
        line = line.replace('!=', ' ~NO_EQ~ ')
        line = line.replace('===', ' ~E_E_E~ ')
        line = line.replace('!==', ' ~N_E_E~ ')
        line = line.replace('&&', ' ~LO_AN~ ')
        line = line.replace('||', ' ~LO_OR~ ')
        line = line.replace('**', ' ~EX~ ')
        line = line.replace('>=', ' ~GR_EQ~ ')
        line = line.replace('<=', ' ~LE_EQ~ ')
        line = line.replace('==', ' ~EQ_TO~ ')
        line = line.replace('++', ' ~P_P~ ')
        line = line.replace('--', ' ~M_M~ ')
        line = line.replace('//', ' ~C_A~ ')
        line = line.replace('/*', ' ~C_O~ ')
        line = line.replace('*/', ' ~C_C~ ')
    
        line = line.replace('>>>', ' ~F_R_S~ ')
        line = line.replace('>>', ' ~R_S~ ')
        line = line.replace('<<', ' ~L_S~ ')
        line = line.replace('&', ' & ')
        line = line.replace('|', ' ~OR~ ')
        line = line.replace('^', ' ^ ')
        
        line = line.replace('(', ' ( ')
        line = line.replace(')', ' ) ')
        line = line.replace(':', ' : ')
        line = line.replace(';', ' ; ')
        line = line.replace('-', ' - ')
        line = line.replace('+', ' + ')
        line = line.replace('*', ' * ')
        line = line.replace('/', ' / ')
        line = line.replace('%', ' % ')
        line = line.replace('=', ' = ')
        line = line.replace('>', ' > ')
        line = line.replace('<', ' < ')
        line = line.replace(',', ' , ')
        line = line.replace('.', ' . ')
        line = line.replace('{', ' { ')
        line = line.replace('}', ' } ')
        line = line.replace('[', ' [ ')
        line = line.replace(']', ' ] ')
        line = line.replace('"', ' " ')
        line = line.replace("'", " ' ")
        line = line.split()
        line.append('endlineYaa'+str(line_index))
        tokens_temp.append(line)
        line_index += 1

    return tokens_temp
