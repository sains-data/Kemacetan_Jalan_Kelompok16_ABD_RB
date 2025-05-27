## 📄 Deskripsi Dataset Mentah

Folder ini berisi dataset mentah yang digunakan sebagai input utama untuk proyek analisis kemacetan lalu lintas Kota Medan.

### 1. Dataset Simulasi Trafik Medan (`simulasi_trafik_medan.csv`)

* **Sumber**: Data simulasi pergerakan taksi di Kota Medan.
* **Periode Data**: Mencakup data historis (contoh dari dokumen PDF: 1 Juli 2013).
* **Format File**: CSV (Comma Separated Values)
* **Pemisah Kolom**: Koma (`,`)
* **Encoding**: UTF-8
* **Deskripsi Kolom**:
    * `timestamp`: Waktu pencatatan data pergerakan taksi (Format: `YYYY-MM-DD, HH:MM:SS` pada contoh data, namun bisa juga `YYYY-MM-DD HH:MM:SS` tergantung file aktual).
    * `latitude`: Koordinat lintang lokasi taksi (Tipe: Float).
    * `longitude`: Koordinat bujur lokasi taksi (Tipe: Float).
    * `speed_kmh`: Kecepatan taksi dalam kilometer per jam (Tipe: Float).
    * `taxi_id`: ID unik untuk setiap taksi (Tipe: Integer).
    * `index_right`: (Jika ada, jelaskan peruntukannya berdasarkan dokumen Anda, misal: Indeks internal untuk join atau pelacakan).
    * `road_name`: Nama jalan tempat taksi berada (Tipe: String). Kolom ini mungkin memiliki nilai kosong atau "Unknown".
* **Catatan Penting**: Data ini digunakan untuk menganalisis pola kecepatan kendaraan, identifikasi ruas jalan, dan sebagai dasar untuk menghitung tingkat kepadatan lalu lintas.

### 2. Dataset Cuaca Medan (`cuaca_medan_2013-07-01.csv`)

* **Sumber**: Data simulasi kondisi cuaca per jam untuk Kota Medan, dibuat berdasarkan karakteristik iklim tropis dan dikorelasikan dengan kecepatan rata-rata taksi (berdasarkan dokumen PDF).
* **Periode Data**: Sesuai dengan periode data trafik (contoh: 1 Juli 2013).
* **Format File**: CSV (Comma Separated Values)
* **Pemisah Kolom**: Koma (`,`)
* **Encoding**: UTF-8
* **Deskripsi Kolom**:
    * `date_time`: Waktu pengukuran data cuaca (Format: `YYYY-MM-DD HH:MM:SS`).
    * `location`: Lokasi pengukuran cuaca (diasumsikan selalu "Medan").
    * `rainfall_mm`: Curah hujan dalam milimeter per jam (Tipe: Float; 0 = tidak hujan, >5 = hujan sedang/lebat).
    * `temperature_c`: Suhu udara dalam derajat Celcius (Tipe: Float).
    * `humidity_percent`: Kelembaban relatif udara dalam persen (Tipe: Float).
    * `visibility_km`: Jarak pandang dalam kilometer (Tipe: Float; rendah saat hujan, tinggi saat cerah).
* **Catatan Penting**: Data ini krusial untuk menganalisis dampak faktor eksternal (cuaca) terhadap kondisi lalu lintas dan akurasi model prediksi kemacetan.

**Integritas Data**: Data yang disajikan di sini adalah data mentah apa adanya dari sumber. Proses pembersihan, validasi, dan transformasi akan dilakukan pada tahap selanjutnya dalam pipeline data (Silver Layer).
