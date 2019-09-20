[TOC]



# 12 Materi Python

- [ ] Memahami apa itu Git dan cara menggunakan Git - **2 Materi**
- [ ] Dasar Python - **6 Materi**
- [ ] Lanjutan Python - **10 Materi**
- [ ] Menggunakan Framework Flask - **4 Materi**
- [ ] CRUD 







# Git



![](materi/image/1_N6oVTvcFjYdSLgkR3CZgvg.png)



### Apa itu Git?

Git adalah *version control system* yang digunakan para developer untuk mengembangkan software secara bersama-bersama. Fungsi utama git yaitu mengatur versi dari source code program anda dengan mengasih tanda baris dan code mana yang ditambah atau diganti.

Git ini sebenernya memudahkan programmer untuk mengetahui perubahan source codenya daripada harus membuat file baru seperti *Program.java, ProgramRevisi.java,  ProgramRevisi2.java, ProgramFix.java*. Selain itu, dengan git kita tak perlu khawatir code yang kita kerjakan bentrok, karena setiap developer bias membuat branch sebagai *workspace*nya.Fitur yang tak kalah keren lagi, pada git kita bisa memberi komentar pada source code yang telah ditambah/diubah, hal ini mempermudah developer lain untuk tahu  kendala apa yang dialami developer lain.



### Apa yang dilakukan oleh Git?

Git sebenarnya akan memantau semua perubahan yang terjadi pada file proyek. Lalu menyimpannya ke dalam database.



Contoh penggunaan pada Git:

![c](/home/hinha/Documents/fasilitator/mcqueen/image/fork-git.png)







# Dasar Python

Python adalah bahasa pemrograman multifungsi yang dibuat oleh Guido van Rossum dan dirilis pada tahun 1991. GvR, begitu ia biasa disebut di komunitas Python, menciptakan Python untuk menjadi interpreter yang memiliki kemampuan *exception handling* dan mengutamakan keterbacaan. Didesain untuk memudahkan dalam prototyping, Python menjadi bahasa yang sangat mudah dipahami dan fleksibel.



### **Mengapa Python?**

Python dapat digunakan dalam mengakomodasi berbagai gaya pemrograman, termasuk structured, prosedural, berorientasi-objek, maupun fungsional. Python juga dapat berjalan pada berbagai sistem operasi yang tersedia. Beberapa pemanfaatan bahasa Python di antaranya:

1. Web development (server-side),
2. Software development,
3. Mathematics & data science,
4. Machine learning,
5. System scripting.



### Dynamic Typing

Python dikenal sebagai salah satu bahasa yang menerapkan dynamic typing, yakni bahasa pemrograman yang hanya mengetahui tipe variabel saat program berjalan dan dilakukan assignment. Tentu saja, pada Python juga umumnya tidak ada deklarasi variabel, hanya berupa assignment statement. Cara ini adalah salah satu bentuk simplifikasi alokasi memori dalam bahasa Python. Anda dapat selalu memeriksa tipe variabel yang digunakan dengan fungsi type() dan memastikan tipe variabel yang tepat dengan metode isinstance().

```python
x = 6  
print(type(x))
# Kemudian Berikan string “hello” pada variabel x di baris selanjutnya
x = 'hello'
print(type(x))
```

Output:

```
<class 'int'>
<class 'str'>
```



### Tipe Data

- #### **Numbers**

- #### **List**

- #### **Tuple**

- #### **Strings**

- #### **Set**

- #### **Dictionary**

- #### Konversi antar tipe data





### Kondisi If

None



### Input Output

Untuk memungkinkan user memberikan input pada program Anda, gunakan fungsi input(), dengan argumen dalam kurung () adalah teks yang ingin ditampilkan (*prompt*) dan variabel sebelum tanda sama dengan (=) adalah penampung hasil dari input pengguna:

```python
num = input('Enter a number: ')
```

