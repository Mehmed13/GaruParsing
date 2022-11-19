def categorize_token(token):
    # Fungsi menerima token yang tidak terdapat dalam terminal. Apabila berbentuk variabel yang dapat diterima oleh python, maka
    # fungsi akan mengembalikan 'variabel'. Apabila berbentuk variabel, maka fungsi akan mengembalikan 'num'. Apabila tidak memenuhi
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
    return "variabel"


def js_to_tokens(js_file):
    # Fungsi menerima file *.js yang telah dalam format list of lines
    # Fungsi ini lalu mengubahnya menjadi dalam bentuk List of List of string (tokenisasi)
    tokens_temp = []

    for line in js_file:
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
        line = line.replace('[', ' [ ')
        line = line.replace(']', ' ] ')
        line = line.replace('"', ' " ')
        line = line.replace("'", " ' ")
        line = line.split()
        line.append('endline')
        tokens_temp.append(line)

    return tokens_temp
