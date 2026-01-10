# STRUKTUR LAPORAN PROYEK SIAB
## Stock Investment Analysis and Prediction System

---

## COVER/HALAMAN JUDUL
- Judul Proyek: **Sistem Prediksi Harga Saham Menggunakan Machine Learning**
- Logo Institusi
- Nama Kelompok & Anggota (NIM)
- Nama Dosen Pembimbing
- Program Studi
- Tanggal Penyusunan

---

## HALAMAN PENGESAHAN
- Tanda tangan ketua kelompok
- Tanda tangan dosen pembimbing
- Tanda tangan kepala program studi

---

## KATA PENGANTAR
- Ucapan syukur
- Tujuan pembuatan laporan
- Ucapan terima kasih kepada pihak terkait
- Harapan dan permohonan maaf
- Tempat, tanggal, dan nama penyusun

---

## DAFTAR ISI
- Daftar seluruh bab dan sub-bab dengan nomor halaman

---

## DAFTAR GAMBAR
- Daftar semua gambar/diagram/screenshot dengan nomor halaman

---

## DAFTAR TABEL
- Daftar semua tabel dengan nomor halaman

---

## DAFTAR LAMPIRAN
- Daftar lampiran yang disertakan

---

## BAB I: PENDAHULUAN

### 1.1 Latar Belakang
**Isi yang harus dimasukkan:**
- Pentingnya pasar saham dalam investasi
- Tantangan dalam memprediksi harga saham
- Peran teknologi dan machine learning dalam prediksi finansial
- Kebutuhan sistem prediksi yang akurat untuk investor
- Alasan pemilihan saham BBCA.JK sebagai studi kasus

### 1.2 Rumusan Masalah
**Isi yang harus dimasukkan:**
- Bagaimana membangun sistem prediksi harga saham yang akurat?
- Model machine learning apa yang paling efektif untuk prediksi saham?
- Bagaimana mengintegrasikan model ML ke dalam aplikasi web?
- Bagaimana memberikan visualisasi yang membantu pengambilan keputusan?

### 1.3 Tujuan
**Isi yang harus dimasukkan:**
- Mengembangkan sistem prediksi harga saham berbasis web
- Mengimplementasikan model machine learning untuk prediksi
- Menyediakan interface yang user-friendly
- Memberikan visualisasi data historis dan hasil prediksi
- Mengevaluasi akurasi model yang digunakan

### 1.4 Batasan Masalah
**Isi yang harus dimasukkan:**
- Fokus pada saham BBCA.JK (Bank Central Asia)
- Menggunakan data historis 10 tahun
- Fitur input: Open, High, Low, Close, Volume
- Platform: Web application menggunakan Django
- Model: [sebutkan model yang digunakan, misalnya LSTM, Random Forest, dll]

### 1.5 Manfaat
**Isi yang harus dimasukkan:**
- **Bagi Investor:** Membantu pengambilan keputusan investasi
- **Bagi Akademisi:** Referensi untuk penelitian serupa
- **Bagi Pengembang:** Contoh implementasi ML dalam web app
- **Bagi Tim:** Pengalaman dalam pengembangan proyek

### 1.6 Metodologi Penelitian
**Isi yang harus dimasukkan:**
- Studi literatur
- Pengumpulan data
- Pengembangan model
- Implementasi sistem
- Pengujian dan evaluasi
- Dokumentasi

### 1.7 Sistematika Penulisan
**Isi yang harus dimasukkan:**
- Ringkasan isi setiap bab dalam laporan

---

## BAB II: LANDASAN TEORI

### 2.1 Pasar Saham
**Isi yang harus dimasukkan:**
- Definisi pasar saham
- Cara kerja pasar saham
- Bursa Efek Indonesia (BEI)
- Indikator harga saham (Open, High, Low, Close, Volume)

### 2.2 Analisis Teknikal vs Fundamental
**Isi yang harus dimasukkan:**
- Perbedaan kedua metode analisis
- Alasan menggunakan analisis teknikal
- Kelebihan dan kekurangan

### 2.3 Machine Learning
**Isi yang harus dimasukkan:**
- Definisi machine learning
- Jenis-jenis machine learning (Supervised, Unsupervised, Reinforcement)
- Proses machine learning (Training, Testing, Validation)

### 2.4 Time Series Prediction
**Isi yang harus dimasukkan:**
- Definisi time series
- Karakteristik data time series
- Teknik prediksi time series

### 2.5 Model Machine Learning untuk Prediksi Saham
**Isi yang harus dimasukkan:**
- Model yang digunakan (misalnya: LSTM, GRU, Random Forest, dll)
- Cara kerja model
- Arsitektur model
- Kelebihan dan kekurangan model

### 2.6 Evaluasi Model
**Isi yang harus dimasukkan:**
- Metrik evaluasi (MAE, MSE, RMSE, MAPE, R²)
- Cara menghitung metrik
- Interpretasi hasil

### 2.7 Web Development
**Isi yang harus dimasukkan:**
- Django Framework
- Arsitektur MVC/MVT
- Frontend (HTML, CSS, JavaScript)
- Backend (Python)

### 2.8 Visualisasi Data
**Isi yang harus dimasukkan:**
- Pentingnya visualisasi
- Tools yang digunakan (Matplotlib, Plotly, Chart.js)
- Jenis-jenis chart untuk data finansial

### 2.9 Penelitian Terkait
**Isi yang harus dimasukkan:**
- Ringkasan 5-10 penelitian sebelumnya tentang prediksi saham
- Metodologi yang digunakan penelitian sebelumnya
- Hasil penelitian sebelumnya
- Gap yang akan diisi oleh proyek ini

---

## BAB III: ANALISIS DAN PERANCANGAN SISTEM

### 3.1 Analisis Sistem
**Isi yang harus dimasukkan:**

#### 3.1.1 Analisis Kebutuhan
- Kebutuhan fungsional
- Kebutuhan non-fungsional
- Kebutuhan data
- Kebutuhan hardware dan software

#### 3.1.2 Analisis Pengguna
- Profil pengguna (investor pemula, menengah, ahli)
- Kebutuhan pengguna
- Use case diagram

#### 3.1.3 Analisis Data
- Sumber data (Yahoo Finance)
- Karakteristik data BBCA.JK
- Statistik deskriptif data
- Visualisasi data historis
- Missing values dan outliers

### 3.2 Perancangan Sistem
**Isi yang harus dimasukkan:**

#### 3.2.1 Arsitektur Sistem
- Diagram arsitektur sistem secara keseluruhan
- Komponen-komponen sistem
- Alur kerja sistem

#### 3.2.2 Perancangan Database
- Entity Relationship Diagram (ERD)
- Struktur tabel database
- Relasi antar tabel

#### 3.2.3 Perancangan Model Machine Learning
- Flowchart preprocessing data
- Arsitektur model
- Hyperparameter yang digunakan
- Proses training dan testing

#### 3.2.4 Perancangan Interface
- Wireframe/mockup setiap halaman
- Navigasi sistem
- User flow diagram

#### 3.2.5 Perancangan Fitur
- **Prediksi Manual:** Input manual fitur untuk prediksi
- **Prediksi dari CSV:** Upload file untuk batch prediction
- **Visualisasi:** Grafik data historis dan prediksi
- **History Prediksi:** Menyimpan dan menampilkan riwayat

### 3.3 Perancangan Algoritma
**Isi yang harus dimasukkan:**
- Pseudocode atau flowchart algoritma prediksi
- Algoritma preprocessing data
- Algoritma training model
- Algoritma prediksi

---

## BAB IV: IMPLEMENTASI SISTEM

### 4.1 Lingkungan Pengembangan
**Isi yang harus dimasukkan:**
- Spesifikasi hardware
- Sistem operasi
- Software dan tools yang digunakan
- Library dan dependencies (dari requirements.txt)
- Versi Python, Django, dll

### 4.2 Implementasi Database
**Isi yang harus dimasukkan:**
- Screenshot struktur database
- Kode model Django (models.py)
- Penjelasan setiap model dan field

### 4.3 Implementasi Machine Learning
**Isi yang harus dimasukkan:**

#### 4.3.1 Preprocessing Data
- Kode cleaning data (clean_data.py)
- Penjelasan setiap tahap preprocessing
- Normalisasi/scaling data
- Train-test split

#### 4.3.2 Training Model
- Kode training model (ml_model.py)
- Parameter dan konfigurasi
- Proses training
- Hasil training (loss, accuracy, dll)
- Grafik learning curve

#### 4.3.3 Saving dan Loading Model
- Cara menyimpan model
- Cara memuat model untuk prediksi

### 4.4 Implementasi Backend
**Isi yang harus dimasukkan:**
- Kode views.py (penjelasan setiap function)
- Kode urls.py (routing)
- Kode forms.py (validasi input)
- Integrasi model ML dengan Django

### 4.5 Implementasi Frontend
**Isi yang harus dimasukkan:**
- Screenshot dan kode setiap halaman:
  - **Homepage (index.html):** Penjelasan dan screenshot
  - **Prediksi Manual (predict_manual.html):** Form input dan screenshot
  - **Hasil Prediksi (predict_result.html):** Tampilan hasil
  - **Prediksi CSV (predict_csv.html):** Upload file
  - **Hasil CSV (predict_csv_result.html):** Hasil batch prediction
  - **Visualisasi (visualize.html):** Grafik interaktif
  - **History (predictions_list.html):** Daftar prediksi
- Kode HTML, CSS, JavaScript penting

### 4.6 Implementasi Fitur
**Isi yang harus dimasukkan:**

#### 4.6.1 Fitur Prediksi Manual
- Cara kerja
- Validasi input
- Proses prediksi
- Tampilan hasil

#### 4.6.2 Fitur Prediksi CSV
- Upload dan validasi file
- Batch processing
- Export hasil

#### 4.6.3 Fitur Visualisasi
- Library yang digunakan
- Jenis grafik
- Interaktivitas

#### 4.6.4 Fitur History
- Penyimpanan data prediksi
- Tampilan riwayat
- Filter dan search

### 4.7 Integrasi Sistem
**Isi yang harus dimasukkan:**
- Cara semua komponen terintegrasi
- Alur data dari user ke hasil
- Error handling

---

## BAB V: PENGUJIAN DAN EVALUASI

### 5.1 Pengujian Model Machine Learning
**Isi yang harus dimasukkan:**

#### 5.1.1 Evaluasi Performa Model
- Tabel hasil metrik (MAE, MSE, RMSE, MAPE, R²)
- Interpretasi hasil
- Grafik actual vs predicted
- Grafik residual

#### 5.1.2 Pengujian dengan Data Testing
- Hasil prediksi pada test set
- Analisis kesalahan prediksi
- Perbandingan dengan model baseline

#### 5.1.3 Cross Validation (jika ada)
- Metode yang digunakan
- Hasil cross validation
- Analisis variance dan bias

### 5.2 Pengujian Sistem
**Isi yang harus dimasukkan:**

#### 5.2.1 Pengujian Unit
- Tabel test case untuk setiap fungsi
- Hasil pengujian
- Bug yang ditemukan dan solusi

#### 5.2.2 Pengujian Integrasi
- Pengujian koneksi antar modul
- Pengujian database
- Pengujian API/endpoint

#### 5.2.3 Pengujian Fungsional
- Tabel test case untuk setiap fitur
- Skenario pengujian
- Expected vs actual result
- Status (Pass/Fail)

#### 5.2.4 Pengujian User Interface
- Pengujian responsiveness
- Pengujian usability
- Pengujian browser compatibility

#### 5.2.5 Pengujian Performa
- Response time
- Load testing
- Resource usage

### 5.3 User Acceptance Testing (UAT)
**Isi yang harus dimasukkan:**
- Kuesioner untuk user
- Hasil feedback user
- Analisis kepuasan user

### 5.4 Analisis Hasil
**Isi yang harus dimasukkan:**
- Kelebihan sistem
- Kekurangan sistem
- Perbandingan dengan sistem sejenis
- Lesson learned

---

## BAB VI: KESIMPULAN DAN SARAN

### 6.1 Kesimpulan
**Isi yang harus dimasukkan:**
- Ringkasan pencapaian tujuan
- Hasil utama dari pengembangan sistem
- Performa model dan sistem
- Kontribusi proyek

### 6.2 Saran
**Isi yang harus dimasukkan:**
- Saran pengembangan fitur tambahan
- Saran perbaikan model (hyperparameter tuning, model lain)
- Saran implementasi di production
- Saran untuk penelitian selanjutnya

---

## DAFTAR PUSTAKA
**Isi yang harus dimasukkan:**
- Semua referensi yang digunakan (buku, jurnal, website, dokumentasi)
- Format: gunakan style citation (APA, IEEE, atau Harvard)
- Contoh referensi:
  - Buku tentang machine learning
  - Paper tentang stock prediction
  - Dokumentasi Django
  - Dokumentasi library (scikit-learn, pandas, numpy, dll)
  - Website sumber data (Yahoo Finance)

---

## LAMPIRAN

### Lampiran A: Kode Program Lengkap
- File settings.py
- File models.py
- File views.py
- File ml_model.py
- File clean_data.py
- dll (kode penting)

### Lampiran B: Dataset
- Sample data BBCA.JK
- Statistik dataset

### Lampiran C: Hasil Pengujian Detail
- Log hasil training
- Error log
- Screenshot detail setiap fitur

### Lampiran D: User Manual
- Panduan instalasi
- Panduan penggunaan sistem
- FAQ

### Lampiran E: Dokumentasi API (jika ada)
- Endpoint yang tersedia
- Request/response format

### Lampiran F: Kuesioner UAT
- Template kuesioner
- Hasil kuesioner

### Lampiran G: Surat-surat (jika ada)
- Surat tugas
- Surat keterangan penelitian

---

## CHECKLIST KELENGKAPAN LAPORAN

### Format Dokumen
- [ ] Font: Times New Roman 12pt (isi), 14pt (sub judul), 16pt (judul bab)
- [ ] Spasi: 1.5 atau 2.0
- [ ] Margin: 4cm (kiri), 3cm (kanan, atas, bawah)
- [ ] Numbering: Angka Romawi (i, ii, iii) untuk bagian awal, Angka Arab (1, 2, 3) untuk isi
- [ ] Justify alignment untuk isi
- [ ] Bahasa Indonesia yang baik dan benar

### Komponen Wajib
- [ ] Cover yang rapi dan profesional
- [ ] Halaman pengesahan dengan tanda tangan
- [ ] Kata pengantar
- [ ] Daftar isi dengan nomor halaman
- [ ] Daftar gambar (minimal 10 gambar)
- [ ] Daftar tabel (minimal 5 tabel)
- [ ] 6 Bab lengkap dengan sub-bab
- [ ] Daftar pustaka (minimal 15 referensi)
- [ ] Lampiran lengkap

### Konten Teknis
- [ ] Diagram arsitektur sistem
- [ ] ERD/Database schema
- [ ] Use case diagram
- [ ] Flowchart algoritma
- [ ] Wireframe/mockup UI
- [ ] Screenshot semua fitur
- [ ] Kode program penting
- [ ] Grafik hasil training model
- [ ] Tabel metrik evaluasi
- [ ] Tabel test case
- [ ] Grafik perbandingan actual vs predicted

### Review Akhir
- [ ] Pengecekan ejaan dan grammar
- [ ] Konsistensi format
- [ ] Semua gambar dan tabel diberi caption dan nomor
- [ ] Semua referensi disebutkan di daftar pustaka
- [ ] Nomor halaman benar
- [ ] PDF final untuk submission

---

## TIPS PENULISAN

1. **Gunakan bahasa formal dan baku**
2. **Setiap gambar/tabel harus direferensikan dalam teks**
   - Contoh: "Seperti terlihat pada Gambar 3.1, arsitektur sistem terdiri dari..."
3. **Berikan caption yang jelas untuk setiap gambar/tabel**
4. **Pastikan semua kode yang dicantumkan diberi penjelasan**
5. **Gunakan bullet points atau numbering untuk mempermudah pembacaan**
6. **Hindari plagiarisme - selalu cite sumber**
7. **Screenshot harus jelas dan tidak blur**
8. **Konsisten dalam penamaan (misalnya: model ML, bukan kadang model ML kadang model machine learning)**
9. **Proofread berkali-kali sebelum submit**
10. **Minta feedback dari dosen pembimbing**

---

**ESTIMASI JUMLAH HALAMAN:** 80-150 halaman (tergantung detail dan lampiran)

**WAKTU PENGERJAAN YANG DISARANKAN:**
- Minggu 1-2: Bab I, II
- Minggu 3-4: Bab III, IV
- Minggu 5: Bab V
- Minggu 6: Bab VI, penyempurnaan, lampiran
- Minggu 7: Revisi dan finalisasi

---

Semoga struktur laporan ini membantu! Sesuaikan dengan panduan dari institusi/dosen pembimbing Anda.
