import tkinter as tk
from tkinter import (
    messagebox,
)  # Tkinter untuk membuat antarmuka grafis (GUI), messagebox untuk menampilkan kotak pesan
import sqlite3  # Untuk berinteraksi dengan database


# Membuat fungsi
def submit_data():
    # Mendapatkan data dari input pengguna
    nama_mahasiswa = nama_entry.get()  # Membuat inputan nama mahasiswa
    biologi = int(
        biologi_entry.get()
    )  # Membuat inputan nilai biologi mahasiwa dengan bertipe data integer yang berisi angka
    fisika = int(
        fisika_entry.get()
    )  # Membuat inputan nilai fisika mahasiwa dengan bertipe data integer yang berisi angka
    inggris = int(
        inggris_entry.get()
    )  # Membuat inputan nilai inggris mahasiwa dengan bertipe data integer yang berisi angka

    # Membuat prediksi fakultas berdasarkan nilai
    if (
        biologi > fisika and biologi > inggris
    ):  #  Jika nilai biologi lebih besar dari nilai fisika dan nilai bahasa Inggris, maka prediksi fakultas dinyatakan sebagai "Kedokteran". Artinya, program ini mengasumsikan bahwa jika nilai biologi tertinggi, maka mahasiswa cenderung masuk ke fakultas Kedokteran.
        prediksi_fakultas = "Kedokteran"
    elif (
        fisika > biologi and fisika > inggris
    ):  # Jika nilai fisika lebih besar dari nilai biologi dan nilai bahasa Inggris, maka prediksi fakultas dinyatakan sebagai "Teknik". Dengan kata lain, jika nilai fisika tertinggi, maka mahasiswa cenderung masuk ke fakultas Teknik.
        prediksi_fakultas = "Teknik"
    else:
        prediksi_fakultas = "Bahasa"  # Jika kedua kondisi sebelumnya tidak terpenuhi, maka blok else akan dijalankan. Ini berarti bahwa nilai bahasa Inggris memiliki nilai tertinggi atau ada nilai yang sama tertinggi dengan nilai lainnya. Dalam hal ini, prediksi fakultas dinyatakan sebagai "Bahasa". Jadi, program mengasumsikan bahwa jika tidak ada nilai yang jelas tertinggi, maka fokus pada fakultas Bahasa.

    # Input data ke databse
    conn = sqlite3.connect("giza.db")  # Membuat koneksi ke database SQLite
    cursor = conn.cursor()  # Membuat objek cursor untuk berinteraksi dengan database
    # Mengeksekusi perintah SQL untuk membuat tabel
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS nilai_mahasiswa (
            id INTEGER PRIMARY KEY,
            nama_mahasiswa TEXT,
            biologi INTEGER,
            fisika INTEGER,
            inggris INTEGER,
            prediksi_fakultas TEXT
        )
    """
    )  # Mengeksekusi perintah SQL untuk membuat tabel nilai_mahasiswa jika tabel tersebut belum ada. Tabel ini memiliki kolom-kolom seperti id, nama_mahasiswa, biologi, fisika, inggris, dan prediksi_fakultas.

    # Mengeksekusi perintah SQL untuk memasukkan data ke dalam tabel
    cursor.execute(
        """
        INSERT INTO nilai_mahasiswa (nama_mahasiswa, biologi, fisika, inggris, prediksi_fakultas) VALUES (?, ?, ?, ?, ?)
    """,
        (nama_mahasiswa, biologi, fisika, inggris, prediksi_fakultas),
    )  # Mengeksekusi perintah SQL untuk memasukkan data ke dalam tabel. Menggunakan parameterized query dengan menggunakan tanda tanya (?) sebagai placeholder untuk nilai yang akan dimasukkan.

    # Commit perubahan ke database
    conn.commit()
    # Menutup koneksi ke database
    conn.close()

    # Menampilkan kotak pesan informasi yang memberi tahu bahwa data telah berhasil disubmit
    messagebox.showinfo("info", "Data berhasil disubmit!")

    # Menampilkan hasil Prediksi Fakultas
    result_label.config(text="Prodi: " + prediksi_fakultas)


# Membuat window utama untuk aplikasi dengan judul "Aplikasi Prediksi Prodi Pilihan"
root = (
    tk.Tk()
)  # Membuat instance dari objek Tkinter yang mewakili window utama aplikasi. Tkinter adalah toolkit GUI bawaan untuk Python yang memungkinkan pembuatan aplikasi dengan antarmuka grafis.
root.title(
    "Aplikasi Prediksi Prodi Pilihan"
)  # Mengatur judul untuk window utama. Dalam hal ini, judulnya adalah "Aplikasi Prediksi Prodi Pilihan"

# Membuat input Fields
nama_label = tk.Label(root, text="Nama Siswa")
nama_label.grid(row=0, column=0, padx=10, pady=10)
nama_entry = tk.Entry(root)
nama_entry.grid(row=0, column=1, padx=10, pady=10)

biologi_label = tk.Label(root, text="Nilai Biologi")
biologi_label.grid(row=1, column=0, padx=10, pady=10)
biologi_entry = tk.Entry(root)
biologi_entry.grid(row=1, column=1, padx=10, pady=10)

fisika_label = tk.Label(root, text="Nilai Fisika")
fisika_label.grid(row=2, column=0, padx=10, pady=10)
fisika_entry = tk.Entry(root)
fisika_entry.grid(row=2, column=1, padx=10, pady=10)

inggris_label = tk.Label(root, text="Nilai Inggris")
inggris_label.grid(row=3, column=0, padx=10, pady=10)
inggris_entry = tk.Entry(root)
inggris_entry.grid(row=3, column=1, padx=10, pady=10)

# Membuat tombol dengan label "Submit Nilai" yang terhubung dengan fungsi submit_data.
button_submit = tk.Button(root, text="Submit Nilai", command=submit_data)
button_submit.grid(row=4, column=0, columnspan=2, pady=10)

# Membuat label untuk menampilkan hasil prediksi fakultas
result_label = tk.Label(root, text="Prodi: ")
result_label.grid(row=5, columnspan=2)

# Memulai loop utama yang memungkinkan GUI merespons interaksi pengguna
root.mainloop()
