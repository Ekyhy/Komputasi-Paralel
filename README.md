# 🚀 Parallel Computing

## 📖 Apa itu Parallel Computing?

**Parallel Computing** (Komputasi Paralel) adalah teknik komputasi yang memungkinkan beberapa proses atau tugas dijalankan **secara bersamaan** menggunakan lebih dari satu prosesor atau inti CPU (*multi-core processor*).

Pada sistem komputasi biasa (*serial computing*), tugas diproses satu per satu secara berurutan. Sedangkan pada parallel computing, sebuah pekerjaan besar akan dibagi menjadi beberapa bagian kecil agar dapat dikerjakan secara simultan oleh banyak prosesor sehingga proses menjadi lebih cepat dan efisien.

Teknik ini banyak digunakan pada:

* Artificial Intelligence (AI)
* Machine Learning
* Big Data Processing
* Rendering Video & 3D
* Simulasi Cuaca
* Cybersecurity
* Scientific Computing

---

# ⚙️ Cara Kerja Parallel Computing

Secara sederhana, proses kerja parallel computing adalah:

1. Sebuah tugas besar dibagi menjadi beberapa sub-tugas
2. Setiap sub-tugas diproses oleh CPU/Core yang berbeda
3. Semua hasil proses digabungkan kembali menjadi satu hasil akhir

---

# 🖥️ Ilustrasi Sederhana

## 🔹 Serial Computing

```text
Task 1 → Task 2 → Task 3 → Task 4
```

Semua tugas diproses satu per satu.

---

## 🔹 Parallel Computing

```text
Core 1 → Task 1
Core 2 → Task 2
Core 3 → Task 3
Core 4 → Task 4
```

Beberapa tugas diproses secara bersamaan sehingga waktu eksekusi menjadi lebih cepat.

---

# ✅ Kelebihan Parallel Computing

| Kelebihan                      | Penjelasan                                                      |
| ------------------------------ | --------------------------------------------------------------- |
| ⚡ Performa Lebih Cepat         | Banyak tugas dapat diproses secara bersamaan                    |
| 🧠 Efisiensi CPU               | Memanfaatkan banyak core/prosesor secara optimal                |
| 📈 Skalabilitas Tinggi         | Mudah menangani data atau proses besar                          |
| 🔄 Multitasking Lebih Baik     | Sistem mampu menjalankan banyak proses sekaligus                |
| 💻 Cocok Untuk Komputasi Berat | Sangat efektif untuk AI, simulasi, rendering, dan analisis data |

---

# ❌ Kekurangan Parallel Computing

| Kekurangan                    | Penjelasan                                            |
| ----------------------------- | ----------------------------------------------------- |
| 💰 Biaya Hardware Mahal       | Membutuhkan multi-core CPU atau banyak prosesor       |
| 🔗 Sinkronisasi Kompleks      | Proses antar thread/proses harus terkoordinasi        |
| 🐞 Debugging Lebih Sulit      | Error lebih sulit dilacak dibanding program biasa     |
| ⚠️ Ketergantungan Antar Tugas | Jika satu proses gagal, proses lain dapat terpengaruh |
| 🧩 Tidak Semua Program Cocok  | Beberapa algoritma sulit diparalelkan                 |

---

# 🧵 Jenis Parallel Computing

## 1️⃣ Data Parallelism

Data dibagi menjadi beberapa bagian lalu diproses secara bersamaan.

Contoh:

* Pemrosesan gambar
* Machine Learning

---

## 2️⃣ Task Parallelism

Berbeda tugas dijalankan secara paralel.

Contoh:

* Server Web
* Sistem Operasi

---

# 🛠️ Teknologi yang Digunakan

Beberapa teknologi populer dalam parallel computing:

* OpenMP
* MPI (Message Passing Interface)
* CUDA (GPU Computing)
* Multithreading
* multiprocessing Python

---

# 🐍 Contoh Parallel Computing Dengan Python

```python
from multiprocessing import Pool

def square(x):
    return x * x

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]

    with Pool(processes=4) as pool:
        result = pool.map(square, data)

    print(result)
```

📌 Program di atas menjalankan proses perhitungan secara paralel menggunakan beberapa proses CPU.

---

# 📊 Perbandingan Serial vs Parallel Computing

| Aspek          | Serial Computing | Parallel Computing |
| -------------- | ---------------- | ------------------ |
| Eksekusi       | Satu per satu    | Bersamaan          |
| Kecepatan      | Lebih lambat     | Lebih cepat        |
| Penggunaan CPU | Kurang optimal   | Lebih optimal      |
| Kompleksitas   | Sederhana        | Lebih kompleks     |

---

# 🎯 Kesimpulan

Parallel Computing adalah solusi penting dalam dunia komputasi modern untuk meningkatkan performa dan efisiensi pemrosesan data. Dengan memanfaatkan banyak prosesor atau core secara bersamaan, pekerjaan berat dapat diselesaikan lebih cepat dibandingkan metode komputasi biasa (*serial computing*).

Meskipun memiliki tantangan seperti sinkronisasi dan kompleksitas implementasi, parallel computing menjadi fondasi utama dalam perkembangan teknologi modern seperti AI, cloud computing, scientific computing, dan cybersecurity.

---

# 📚 Referensi

* [Python multiprocessing documentation](https://docs.python.org/3/library/multiprocessing.html?utm_source=chatgpt.com)
* [OpenMP Official Website](https://www.openmp.org/?utm_source=chatgpt.com)
* [MPI Forum](https://www.mpi-forum.org/?utm_source=chatgpt.com)
