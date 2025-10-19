# 🧠 AI Support Log — IBM Granite  
Project: Coding Timer Tracker  
Developer: Fadil  
Date Range: 16–18 October 2025  

---

## 🗓️ 2025-10-16 — Ide dan Rancangan Awal  
Saya meminta bantuan **IBM Granite** untuk mencari ide proyek Python sederhana yang sesuai kriteria SDI namun tetap bisa diselesaikan cepat.  
Granite menyarankan membuat aplikasi **Streamlit** untuk mencatat waktu coding harian, menyimpan data ke **CSV**, dan menampilkan **grafik line chart**.  
Ide ini langsung saya gunakan sebagai dasar proyek *Coding Timer Tracker*.

---

## 🗓️ 2025-10-17 — Penyusunan Struktur Kode  
Saya meminta Granite membantu menyusun logika dasar untuk:
- Input waktu coding harian
- Tombol simpan data
- Menyimpan ke file `coding_log.csv`

Granite menjelaskan urutan logika:
1. Buat input angka (`st.number_input`)
2. Gunakan tombol (`st.button`) untuk trigger penyimpanan  
3. Simpan data tanggal dan jam ke CSV  
4. Gunakan `try/except FileNotFoundError` agar tidak error saat file belum ada  

Penjelasan tersebut saya terapkan langsung di dalam `app.py` dan berhasil berjalan dengan baik.

---

## 🗓️ 2025-10-17 — Penanganan Error  
Saya meminta solusi ke Granite agar program tidak error kalau file CSV belum ada.  
Granite menyarankan:
> “Gunakan blok `try/except FileNotFoundError` agar data baru tetap tersimpan walau file belum dibuat.”

Saran ini sangat membantu karena mencegah error saat aplikasi dijalankan pertama kali.

---

## 🗓️ 2025-10-18 — Visualisasi dan Statistik  
Saya meminta bantuan Granite untuk menambahkan fitur visualisasi agar pengguna dapat melihat total waktu coding dan grafik perkembangan.  
Granite menyarankan untuk:
- Menggunakan `pd.read_csv()` untuk membaca file  
- Menjumlahkan kolom `Jam`  
- Menampilkan hasil dengan `st.subheader`  
- Menampilkan grafik dengan `st.line_chart(df.set_index("Tanggal"))`

Hasilnya diterapkan langsung dan bekerja sesuai harapan.

---

## 🗓️ 2025-10-18 — UX Enhancement  
Saya meminta Granite agar aplikasi tidak error ketika file data belum ada dan tetap menampilkan pesan ramah pengguna.  
Granite menyarankan menambahkan:
> `except FileNotFoundError: st.info("Belum ada data tersimpan.")`

Saran ini diterapkan di bagian akhir kode agar aplikasi tetap stabil dan user-friendly.

---

## 🗓️ 2025-10-18 — Dokumentasi  
Saya meminta Granite membuat draft README.md untuk proyek Streamlit sederhana.  
AI memberikan struktur dengan bagian:
- Deskripsi proyek  
- Fitur  
- Teknologi yang digunakan  
- Cara menjalankan aplikasi  
- Penjelasan penggunaan AI  

Draft tersebut saya edit ulang menjadi README final yang lebih personal.

---

## 🧩 Ringkasan Penggunaan AI  
| Aspek | Peran IBM Granite | Status |
|-------|-------------------|--------|
| Ide Proyek | Memberikan konsep aplikasi Streamlit sederhana | ✅ Digunakan |
| Struktur Kode | Membantu menyusun logika input dan penyimpanan data | ✅ Digunakan |
| Error Handling | Menyarankan `try/except FileNotFoundError` | ✅ Digunakan |
| Visualisasi | Menjelaskan cara menampilkan grafik line chart | ✅ Digunakan |
| UX | Menambahkan pesan `st.info()` jika belum ada data | ✅ Digunakan |
| Dokumentasi | Menyusun draft README.md | ✅ Digunakan |

---

## ✅ Kesimpulan  
IBM Granite digunakan selama pengembangan proyek **Coding Timer Tracker** untuk mempercepat penulisan kode, memperbaiki error handling, menambah fitur visualisasi, dan menyusun dokumentasi awal.  
Semua bantuan AI dilakukan **hanya pada tahap pengembangan**.  
Aplikasi akhir sepenuhnya berjalan menggunakan **Python + Streamlit**, tanpa integrasi AI atau dependensi eksternal.
