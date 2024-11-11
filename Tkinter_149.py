import tkinter as tk
from tkinter import messagebox # Mengimpor tkinter dan messagebox untuk membuat GUI dan menampilkan pesan error

#fungsi untuk memvalidasi input dan menampilkan hasil prediksi
def hasil_prediksi():
    try:
         # Loop melalui setiap kolom input yang disimpan di 'entries'
        for entry in entries:
             # Mengambil nilai dari setiap kolom input dan mengonversinya menjadi integer
            nilai = int(entry.get())
            # Memeriksa apakah nilai berada dalam rentang 0 hingga 100
            if not (0 <= nilai <= 100):
                raise ValueError("Nilai harus antara 0 dan 100.")  # Muncul error jika tidak dalam rentang
        # Menampilkan hasil prediksi jika semua nilai valid
        hasil_label.config(text="Prediksi Prodi: Teknologi Informasi")
    except ValueError as ve:
         # Menampilkan kotak pesan error jika ada input yang tidak valid
        messagebox.showerror("Input Error", "Pastikan semua input adalah angka 0 dan 100.")


# Membuat jendela utama aplikasi
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan") # Menetapkan judul jendela aplikasi
root.geometry("500x600") # Mengatur ukuran jendela menjadi 500x600 piksel
root.configure(bg="#DDA0DD") # Mengatur warna latar belakang jendela

# Label judul
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Franklin Gothic Medium", 16), bg="#DDA0DD")
judul_label.pack(pady=10) # Menempatkan label dengan jarak vertikal 10 piksel dari elemen lain

# Membuat list untuk menyimpan input nilai mata pelajaran
entries = [] # List kosong untuk menampung semua kolom input nilai
for i in range(10): # Loop untuk membuat 10 input nilai
     # Membuat frame untuk mengelompokkan label dan kolom input secara horizontal
    frame = tk.Frame(root, bg="#DDA0DD")
    frame.pack(pady=5) # Menempatkan frame dengan jarak vertikal 5 piksel dari elemen lain
    
     # Membuat label untuk setiap input nilai mata pelajaran
    label = tk.Label(frame, text=f"Nilai Mata Pelajaran {i+1}: ", font=("Franklin Gothic Medium", 12), bg="#DDA0DD")
    label.pack(side="left")  # Menempatkan label di dalam frame di sisi kiri
    
    # Membuat kolom input untuk memasukkan nilai
    entry = tk.Entry(frame, font=("Franklin Gothic Medium", 12), width=10)
    entry.pack(side="left") # Menempatkan kolom input di sisi kiri frame, setelah label
    
     # Menambahkan kolom input ke dalam list 'entries' agar bisa diakses nanti
    entries.append(entry)

# Tombol untuk menghitung prediksi
prediksi_button = tk.Button(root, text="Hasil Prediksi", font=("Franklin Gothic Medium", 14), command=hasil_prediksi, bg="#D3D3D3", fg="black")
prediksi_button.pack(pady=20)  # Menempatkan tombol dengan jarak vertikal 20 piksel dari elemen lain

# Label untuk menampilkan hasil prediksi
hasil_label = tk.Label(root, text="", font=("Franklin Gothic Medium", 14), bg="#DDA0DD")
hasil_label.pack(pady=10)  # Menempatkan label hasil dengan jarak vertikal 10 piksel dari elemen lain

# Menjalankan aplikasi
root.mainloop()