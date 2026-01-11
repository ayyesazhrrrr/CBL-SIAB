# STRUKTUR LAPORAN PROYEK SIAB
## Case Based Learning: Sistem Informasi untuk Analitik Bisnis

---

## COVER/HALAMAN JUDUL
- Judul Proyek: **Desain dan Implementasi Sistem Informasi dan Analitik Bisnis untuk Pengambilan Keputusan Strategis (Studi Kasus: Prediksi Saham BBCA)**
- Logo Institusi
- Nama Kelompok & Anggota (NIM)
- Nama Dosen Pembimbing: Esi Putri Silmina, S.T., M.Cs.
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
- Pentingnya pengambilan keputusan berbasis data di bisnis modern
- Tantangan prediksi harga saham di pasar modal
- Peran data mining dan machine learning dalam analitik bisnis
- Studi kasus nyata: prediksi harga saham BBCA untuk mendukung keputusan investasi

### 1.2 Rumusan Masalah
- Bagaimana merancang sistem informasi analitik bisnis berbasis data mining untuk kasus nyata?
- Bagaimana memilih dan mengimplementasikan metode data mining yang efektif?
- Bagaimana mengintegrasikan model ML ke aplikasi web yang user friendly?
- Bagaimana mengevaluasi performa sistem dan model?

### 1.3 Tujuan
- Merancang dan mengimplementasikan sistem informasi analitik bisnis berbasis data mining
- Mengembangkan aplikasi web prediksi harga saham BBCA
- Mengintegrasikan model XGBoost ke dalam sistem
- Menyediakan visualisasi dan riwayat prediksi
- Melakukan evaluasi performa sistem dan model

### 1.4 Batasan Masalah
- Studi kasus: prediksi harga saham BBCA.JK
- Dataset: sumber publik (Yahoo Finance, Kaggle, dsb), 10 tahun terakhir
- Fitur input: Open, High, Low, Close, Volume, MA5, MA10, Return, Return_1, MA_diff
- Platform: Web application (Django)
- Model: XGBoost Classifier

### 1.5 Manfaat
- **Bagi Bisnis/Investor:** Mendukung keputusan investasi berbasis data
- **Bagi Akademisi:** Studi kasus nyata implementasi data mining
- **Bagi Pengembang:** Contoh integrasi ML dan web app
- **Bagi Tim:** Pengalaman proyek kolaboratif dan presentasi

### 1.6 Metodologi
- Studi literatur (jurnal, white paper, dokumentasi)
- Pengumpulan dataset publik
- Preprocessing & feature engineering
- Training & evaluasi model data mining
- Implementasi sistem web
- Pengujian sistem & analisis hasil
- Dokumentasi, demo, presentasi

### 1.7 Sistematika Penulisan
- Ringkasan isi setiap bab (lihat rubrik dan checklist di bawah)

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

## BAB IV: PERANCANGAN DAN IMPLEMENTASI SISTEM INFORMASI ANALITIK BISNIS

### 4.1 Studi Kasus dan Dataset Publik
**Isi yang harus dimasukkan:**
- Spesifikasi hardware
- Sistem operasi
- Software dan tools yang digunakan
- Library dan dependencies (dari requirements.txt)
- Versi Python, Django, dll

### 4.2 Analisis Kebutuhan Bisnis & User
**Isi yang harus dimasukkan:**
- Screenshot struktur database
- Kode model Django (models.py)
- Penjelasan setiap model dan field

### 4.3 Desain Arsitektur Sistem (diagram, flowchart, ERD)
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

### 4.4 Desain Database & Integrasi Data Mining
**Isi yang harus dimasukkan:**
- Kode views.py (penjelasan setiap function)
- Kode urls.py (routing)
- Kode forms.py (validasi input)
- Integrasi model ML dengan Django

### 4.5 Desain Antarmuka (UI/UX, wireframe, mockup)
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

### 4.6 Implementasi Fitur (Prediksi Manual, CSV, Visualisasi, Riwayat, API)
**Isi yang harus dimasukkan:**

### 4.6.1 Fitur Prediksi Manual
- Input data saham secara manual (form responsif, user friendly)
- Validasi input otomatis
- Proses prediksi real-time dengan XGBoost
- Tampilkan hasil prediksi (label, confidence, rekomendasi aksi)

### 4.6.2 Fitur Prediksi CSV
- Upload file CSV (format: Date,Open,High,Low,Close,Volume)
- Validasi format dan isi file
- Sistem otomatis menghitung indikator teknikal (MA5, MA10, Return, Return_1, MA_diff)
- Proses prediksi batch dengan XGBoost
- Tampilkan hasil batch, simpan ke database, dan bisa diunduh
#### 4.6.3 Fitur Visualisasi
- Visualisasi interaktif (Chart.js, Bootstrap)
- Jenis grafik: line chart harga, pie chart distribusi prediksi, bar chart confidence
- Interaktif dan responsif di semua device

#### 4.6.4 Fitur Riwayat Prediksi
- Semua hasil prediksi (manual/CSV) otomatis tersimpan di database
- Halaman riwayat: tampilkan, hapus, dan kelola prediksi
- Fitur filter/search riwayat

### 4.7 Integrasi Sistem, Alur Data, dan Error Handling
- User input data (manual/CSV) → sistem validasi → hitung indikator teknikal → data diformat → prediksi dengan model XGBoost (file .pkl hasil training notebook) → hasil (label, probability, rekomendasi) ditampilkan & disimpan ke database → user bisa lihat riwayat & visualisasi.
- Semua prediksi di web menggunakan model yang sama dengan notebook (konsistensi hasil).
- Error handling: validasi input, notifikasi error user-friendly, log error di backend.

---

## BAB V: PENGUJIAN, EVALUASI, DAN DEMO SISTEM

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

### 5.2 Pengujian Sistem & Demo
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
- Pengujian responsiveness (mobile, tablet, desktop)
- Pengujian usability (form mudah diisi, tombol jelas, feedback error)
- Pengujian browser compatibility (Chrome, Firefox, Edge, dsb)

#### 5.2.5 Pengujian Performa
- Response time
- Load testing
- Resource usage

### 5.3 User Acceptance Testing (UAT) & Presentasi
- Kuesioner untuk user (apakah mudah digunakan, hasil mudah dipahami, dsb)
- Hasil feedback user
- Analisis kepuasan user dan saran perbaikan

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
- Pengembangan fitur tambahan (misal: notifikasi, prediksi saham lain, integrasi API eksternal)
- Perbaikan model (hyperparameter tuning, uji model lain seperti LSTM, ensemble)
- Saran implementasi production (deploy ke cloud, monitoring, backup)
- Saran penelitian lanjutan (eksperimen fitur baru, dataset lebih besar, dsb)

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

### Lampiran D: User Manual & Demo
- Panduan instalasi
- Panduan penggunaan sistem (web, API, CSV)
- FAQ
- Link/penjelasan demo aplikasi

### Lampiran E: Dokumentasi API (jika ada)
- Endpoint yang tersedia
- Request/response format

### Lampiran F: Kuesioner UAT
- Template kuesioner
- Hasil kuesioner

### Lampiran G: Surat-surat (jika ada)
- Surat tugas, surat keterangan penelitian, dsb

---

## CHECKLIST KELENGKAPAN & RUBRIK PENILAIAN

### Format Dokumen
- [ ] Font: Times New Roman 12pt (isi), 14pt (sub judul), 16pt (judul bab)
- [ ] Spasi: 1.5 atau 2.0
- [ ] Margin: 4cm (kiri), 3cm (kanan, atas, bawah)
- [ ] Numbering: Angka Romawi (i, ii, iii) untuk bagian awal, Angka Arab (1, 2, 3) untuk isi
- [ ] Justify alignment untuk isi
- [ ] Bahasa Indonesia yang baik dan benar

### Komponen Wajib & Rubrik
- [ ] Cover, pengesahan, kata pengantar, daftar isi, gambar, tabel, pustaka, lampiran
- [ ] Struktur & sistematika penulisan (20%)
- [ ] Deskripsi arsitektur & teknologi (20%)
- [ ] Langkah teknis & implementasi (20%)
- [ ] Evaluasi & analisis (20%)
- [ ] Source code (10%)
- [ ] Referensi (10%)

### Konten Teknis & Demo
- [ ] Diagram arsitektur sistem, ERD, flowchart, use case
- [ ] Wireframe/mockup UI, screenshot fitur, demo aplikasi
- [ ] Kode program penting, hasil training model, tabel evaluasi, test case, grafik hasil

### Review Akhir & Format Output
- [ ] Pengecekan ejaan, format, caption, referensi, nomor halaman
- [ ] Output: PPT (SIAB_PPTKelompokX.pptx), Laporan (SIAB_LaporanX.pdf/jpg), Source code, Demo

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
