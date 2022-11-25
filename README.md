# IF2124 - Teori Bahasa Formal dan Otomata 
## GaruParsing
## Tugas Besar TBFO - Parsing node.js
## PROGRAM COMPILER BAHASA JAVASCRIPT
### ANGGOTA
    1. Nigel Sahl (13521043)
    2. Ghazi Akmal Fauzan (13521058)
    3. Muhammad Fadhil Amri (13521066)

### Bagian-bagian program
  1. main.py : Program utama dari syntax checker, file ini memanggil fungsi-fungsi pada file-file lain 
  2. cyk_op.py : Pada file ini terdapat fungsi cyk_algorithm yang berfungsi menerapkan algoritma CYK untuk menentukan apakah suatu string (pada kasus ini, kumpulan    token dari file .js) termasuk ke dalam suatu bahasa (dalam hal ini javaScript)
  3. cfg_to_cnf.py : Pada file ini terdapat fungsi-fungsi yang digunakan untuk melakukan konversi dari CFG menjadi CNF
  4. tokenizer.py: Pada file ini terdapat fungsi untuk mengubah file .js menjadi dalam representasi list of tokens. Selain itu, pada file ini juga terdapat FA yang berfungsi untuk mengkategorikan token. (word, num, atau undef). 
 
### Cara menjalankan program
    1. Pastikan working directory berada pada '''GaruParsing/src'''
    2. Jalankan program dengan mengetikkan '''python main.py nama_file.js''' pada terminal dengan nama_file.js adalah file yang akan diuji
    3. Program akan berjalan dan akan mengeluarkan output status "Accepted" atau "Syntax Error" sesuai dengan input anda.

#### Selamat mencoba! 
