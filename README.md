# 🚦 Implementasi Ekosistem Hadoop untuk Analisis Big Data Lalu Lintas Kota Medan: Prediksi Kemacetan Jalan Menggunakan Apache Spark dan Random Forest Berbasis Data GPS

Selamat datang di repositori proyek analisis big data untuk prediksi kemacetan lalu lintas di Kota Medan! Proyek ini bertujuan untuk memanfaatkan kekuatan ekosistem Hadoop, Apache Spark, dan machine learning dengan algoritma Random Forest untuk memberikan solusi prediksi kemacetan yang akurat dan bermanfaat.

---
## 📌 Daftar Isi
* [Latar Belakang Masalah](#latar-belakang-masalah)
* [Tujuan Proyek](#tujuan-proyek)
* [Lingkup Sistem](#lingkup-sistem)
* [Dataset yang Digunakan](#dataset-yang-digunakan)
* [Arsitektur Sistem](#arsitektur-sistem)
* [Teknologi yang Digunakan](#teknologi-yang-digunakan)
* [Metodologi Proyek](#metodologi-proyek)
* [🔬 Kajian Analitik & Fitur Unggulan](#-kajian-analitik--fitur-unggulan)
* [Struktur Repositori](#struktur-repositori)
* [Instalasi & Konfigurasi](#instalasi--konfigurasi)
* [Cara Penggunaan](#cara-penggunaan)
* [Hasil dan Temuan](#hasil-dan-temuan)
* [Kontribusi Pengembangan](#kontribusi-pengembangan)
* [Lisensi](#lisensi)
* [Tim Pengembang](#tim-pengembang)

---
## 📜 Latar Belakang Masalah
Kemacetan lalu lintas adalah tantangan signifikan di kota-kota besar seperti Medan, yang disebabkan oleh pertumbuhan kendaraan yang tidak seimbang dengan infrastruktur jalan dan manajemen lalu lintas yang belum optimal[cite: 9, 10]. Hal ini berdampak negatif pada mobilitas, ekonomi, konsumsi bahan bakar, polusi, dan kualitas hidup[cite: 11]. Data GPS kendaraan menawarkan potensi besar untuk analisis spasial-temporal[cite: 12], namun volumenya yang besar memerlukan pendekatan Big Data[cite: 14, 15].

---
## 🎯 Tujuan Proyek
Dokumen ini bertujuan menjelaskan perancangan dan implementasi sistem prediksi kemacetan lalu lintas di Kota Medan[cite: 19]. Fokus utama meliputi:
1.  Perancangan arsitektur Big Data berbasis Hadoop dan Apache Spark[cite: 20].
2.  Pembangunan pipeline data untuk ingestion dan transformasi data spasial-temporal[cite: 20].
3.  Penerapan model Random Forest untuk klasifikasi tingkat kemacetan berdasarkan waktu, lokasi, dan kecepatan kendaraan[cite: 20].

---
## 🛠️ Lingkup Sistem
Sistem ini dirancang untuk memproses dan menganalisis data GPS kendaraan skala besar untuk prediksi kemacetan di Kota Medan[cite: 22]. Lingkupnya mencakup[cite: 23]:
* Pengambilan data GPS dari sumber eksternal.
* Penyimpanan data mentah dalam HDFS (bronze layer)[cite: 23].
* Pembersihan dan transformasi data menggunakan Apache Spark (silver layer)[cite: 23].
* Agregasi dan analisis data pada gold layer[cite: 23].
* Pelatihan model Random Forest untuk klasifikasi kemacetan[cite: 24].
* Integrasi hasil ke Hive untuk query analitik[cite: 24].
* Penyajian visualisasi prediksi melalui dashboard interaktif (Apache Superset)[cite: 24].
* Simulasi cluster lokal menggunakan Docker[cite: 25].

---
## 📊 Dataset yang Digunakan
Proyek ini menggunakan dua sumber data utama yang dikumpulkan melalui batch processing[cite: 162]:
1.  **Data Simulasi Trafik Taksi (`simulasi-trafik_medan.csv`)**: Mencakup data pergerakan taksi di Medan, termasuk lokasi, kecepatan, dan nama jalan, untuk menganalisis pola kemacetan[cite: 166, 167].
    * Kolom: `timestamp`, `latitude`, `longitude`, `speed_kmh`, `taxi_id`, `road_name`[cite: 168, 170].
2.  **Data Cuaca Dummy (`cuaca_medan_dummy.csv`)**: Data cuaca simulasi per jam untuk Medan, penting untuk analisis dampak cuaca terhadap kemacetan[cite: 173, 174].
    * Kolom: `date_time`, `location`, `rainfall_mm`, `temperature_c`, `humidity_percent`, `visibility_km`[cite: 175].

Data disimpan dalam data lake dengan tiga lapisan: Bronze (CSV), Silver (Parquet), dan Gold (ORC)[cite: 177, 178, 179].

---
## 🏗️ Arsitektur Sistem
Sistem ini mengadopsi **Medallion Architecture** (Bronze, Silver, Gold) dengan skema batch processing[cite: 89, 90].
* **Bronze Layer**: Penyimpanan data mentah GPS (HDFS, CSV/JSON)[cite: 91].
* **Silver Layer**: Data hasil pembersihan dan transformasi (Apache Spark, Parquet/Avro)[cite: 91].
* **Gold Layer**: Hasil agregasi analitik siap untuk query dan visualisasi (Apache Hive, Spark, Superset, Parquet/ORC)[cite: 91].

[Bronze Layer (HDFS)] --> [Silver Layer (Spark)] --> [Gold Layer (Hive/Spark)] --> [Analytics/Dashboard (Superset)]
-->

Infrastruktur dikembangkan dalam cluster lokal berbasis Docker[cite: 93].

---
## ⚙️ Teknologi yang Digunakan
* **Penyimpanan & Pemrosesan Data**: Hadoop HDFS, Apache Spark (Core, SQL, MLlib) [cite: 36, 37, 97, 99]
* **Manajemen Resource**: Hadoop YARN [cite: 97]
* **Query Engine & Metadata**: Apache Hive, Hive Metastore [cite: 38, 97, 99]
* **Orkestrasi Workflow**: Apache Airflow [cite: 41, 99] (atau Shell Script + Crontab untuk implementasi awal [cite: 108])
* **Visualisasi & Dashboard**: Apache Superset, Jupyter Notebook [cite: 42, 99, 120, 142]
* **Manajemen Cluster**: Apache Ambari [cite: 43, 99]
* **Machine Learning**: Random Forest (via Spark MLlib) [cite: 17, 151]
* **Lingkungan**: Docker, Ubuntu Server [cite: 108]

---
## 🗺️ Metodologi Proyek
Proyek ini menggunakan model pengembangan sistem **Waterfall**[cite: 60], meliputi tahapan:
1.  Analisis Kebutuhan (Requirement Analysis)[cite: 61].
2.  Perancangan Arsitektur Big Data[cite: 62].
3.  Desain Sistem (Struktur Data, Skema Hive, Workflow Airflow, Lingkungan Docker)[cite: 63].
4.  Implementasi (Pipeline Data, ETL, Pelatihan Model, Dashboard)[cite: 64].
5.  Pengujian (Unit, Integrasi, Performa Model)[cite: 65].
6.  Deployment & Pemantauan (Docker, Ambari)[cite: 66, 67].

**Tahapan Analitik Machine Learning**[cite: 152, 153, 154, 155, 156, 157]:
1.  Load Data (Gold Layer)[cite: 152].
2.  Preprocessing (Handling missing values, encoding kategorikal, normalisasi)[cite: 153, 154, 155].
3.  Splitting Data (80% train, 20% test)[cite: 156].
4.  Modeling (Random Forest Regressor)[cite: 156].
5.  Evaluasi (RMSE, MAE)[cite: 157].
6.  Saving Model & Inference[cite: 157].

---
## 🔬 Kajian Analitik & Fitur Unggulan

Berikut adalah beberapa kajian dan fitur menarik dari proyek ini yang dapat dieksplorasi lebih lanjut:

1.  **Akurasi Model Prediksi Kemacetan**:
    * Seberapa akurat model Random Forest dalam memprediksi tingkat kemacetan di berbagai ruas jalan Kota Medan?
    * Analisis fitur mana yang paling berpengaruh terhadap prediksi (misalnya, waktu, kecepatan rata-rata sebelumnya, kondisi cuaca).
    * Perbandingan performa dengan metrik evaluasi seperti RMSE dan MAE[cite: 157].

2.  **Pola Spasial-Temporal Kemacetan**:
    * Visualisasi peta panas (heat map) untuk mengidentifikasi titik-titik rawan macet dan kapan saja kemacetan tersebut sering terjadi.
    * Analisis tren kemacetan harian, mingguan, atau bahkan bulanan.

3.  **Dampak Kondisi Cuaca terhadap Lalu Lintas**:
    * Bagaimana curah hujan, jarak pandang, atau suhu mempengaruhi kecepatan rata-rata kendaraan dan tingkat kemacetan? [cite: 163]
    * Apakah ada korelasi signifikan yang dapat dimanfaatkan untuk prediksi yang lebih baik?

4.  **Efektivitas Pipeline Data Big Data**:
    * Analisis performa proses ETL (Extract, Transform, Load) dari Bronze ke Gold layer.
    * Bagaimana arsitektur Medallion dan penggunaan format Parquet/ORC membantu efisiensi penyimpanan dan query? [cite: 86, 91]

5.  **Dashboard Interaktif untuk Pengambilan Keputusan**:
    * Menampilkan kemampuan dashboard Apache Superset dalam menyajikan informasi prediksi kemacetan secara visual dan mudah dipahami oleh berbagai pengguna (Dinas Perhubungan, masyarakat)[cite: 24, 42].
    * Potensi dashboard dalam mendukung perencanaan rekayasa lalu lintas atau pemilihan rute alternatif.

6.  **Analisis Rekomendasi Rute (Potensi Pengembangan)**:
    * Studi kelayakan untuk mengembangkan fitur rekomendasi rute tercepat berdasarkan prediksi kemacetan secara real-time atau near real-time.

---
## 📂 Struktur Repositori
├── data/ # (Opsional, jika dataset kecil atau sampel disertakan)
│   ├── simulasi-trafik_medan.csv
│   └── cuaca_medan_dummy.csv
├── notebooks/ # Jupyter notebooks untuk eksplorasi, analisis, atau modeling
│   ├── 01_data_exploration.ipynb
│   └── 02_model_training_random_forest.ipynb
├── scripts/ # Script untuk pipeline data, ETL, dll.
│   ├── ingest_data.sh
│   ├── spark_etl_silver.py
│   └── spark_aggregation_gold.py
├── src/ # Kode sumber utama aplikasi (jika ada)
├── docker-compose.yml # Definisi layanan untuk lingkungan Docker
├── Dockerfile # (Jika ada custom image Docker)
├── .gitignore
├── LICENSE
└── README.md

---
## ⚙️ Instalasi & Konfigurasi

Langkah-langkah untuk menjalankan proyek ini di lingkungan lokal menggunakan Docker:

1.  **Prasyarat**:
    * Install Docker Desktop.
    * Aktifkan WSL2 di Windows (jika menggunakan Windows)[cite: 109].
    * Clone repositori ini: `git clone [URL-REPO-ANDA]`
    * Pindah ke direktori proyek: `cd [NAMA-DIREKTORI-PROYEK]`

2.  **Setup Cluster Lokal dengan Docker Compose**:
    * Jalankan perintah: `docker-compose up -d`
    * Perintah ini akan menjalankan semua layanan yang didefinisikan dalam `docker-compose.yml` (Hadoop, Spark, Hive, Superset, Airflow, dll.)[cite: 110].
    * Tunggu beberapa saat hingga semua container berjalan dan stabil.

3.  **Akses Layanan**:
    * HDFS NameNode UI: `http://localhost:9870` (atau port yang dikonfigurasi)
    * Spark Master UI: `http://localhost:8080` (atau port yang dikonfigurasi)
    * Apache Superset: `http://localhost:8088` (atau port yang dikonfigurasi)
    * Apache Ambari (jika digunakan): `http://localhost:8080` (cek port spesifik Ambari)
    * Apache Airflow UI (jika digunakan): `http://localhost:8080` (cek port spesifik Airflow)

4.  **Konfigurasi Tambahan**:
    * (Jelaskan jika ada konfigurasi spesifik yang perlu dilakukan setelah cluster up, misalnya setup koneksi di Superset ke Hive).

---
## 🚀 Cara Penggunaan

1.  **Ingestion Data**:
    * Jalankan script ingestion untuk mengambil data awal ke HDFS Bronze layer (misalnya, menggunakan `scripts/ingest_data.sh` atau task Airflow)[cite: 114].

2.  **Menjalankan Pipeline ETL**:
    * Submit Spark job untuk memproses data dari Bronze ke Silver, lalu ke Gold layer (misalnya, menggunakan `spark-submit scripts/spark_etl_silver.py` dan `spark-submit scripts/spark_aggregation_gold.py`, atau melalui Airflow DAGs)[cite: 115].

3.  **Akses Data melalui Hive**:
    * Buka Hive CLI atau tool query SQL yang terhubung ke HiveServer2.
    * Jalankan query pada tabel yang telah dibuat di Gold Layer (misalnya `gps_summary`)[cite: 116].

4.  **Visualisasi di Apache Superset**:
    * Login ke Apache Superset.
    * Buat koneksi ke database Hive.
    * Import dataset dari tabel Hive Gold Layer.
    * Buat chart dan dashboard untuk visualisasi pola kemacetan dan hasil prediksi[cite: 118].

---
## ✨ Hasil dan Temuan
*(Di bagian ini, Anda akan merangkum hasil utama dari analisis dan kajian yang telah dilakukan. Misalnya, tingkat akurasi model, pola kemacetan yang teridentifikasi, dampak cuaca, dll.)*

Contoh:
* Model Random Forest berhasil mencapai akurasi prediksi sebesar XX% (RMSE: Y.YY, MAE: Z.ZZ).
* Teridentifikasi bahwa ruas jalan A, B, dan C merupakan titik paling rawan macet pada jam sibuk pagi (07.00-09.00) dan sore (16.00-18.00).
* Curah hujan di atas N mm/jam menunjukkan penurunan kecepatan rata-rata kendaraan sebesar M%.

---
## 🌱 Kontribusi Pengembangan
Kami menyambut kontribusi dari siapa saja! Jika Anda ingin berkontribusi, silakan:
1.  Fork repositori ini.
2.  Buat branch baru (`git checkout -b fitur/nama-fitur-anda`).
3.  Lakukan perubahan Anda.
4.  Commit perubahan Anda (`git commit -m 'Menambahkan fitur X'`).
5.  Push ke branch Anda (`git push origin fitur/nama-fitur-anda`).
6.  Buat Pull Request baru.

Pastikan untuk membaca `CONTRIBUTING.md` (jika ada) untuk panduan lebih lanjut.

---
## 📄 Lisensi
Proyek ini dilisensikan di bawah [Sains Data] - lihat file `LICENSE` untuk detailnya.

---
## 🧑‍💻 Tim Pengembang
* Dwi Ratna Anggraeni (122450008) [cite: 2]
* Febiya Jomy Pratiwi (122450074) [cite: 2]
* Residen Nusantara R M (122450080) [cite: 2]
* Fayyaza Aqila S A (122450131) [cite: 2]

Dibimbing oleh: [Ardika Satria S.Si]
Program Studi Sains Data, Fakultas Sains, Institut Teknologi Sumatera[cite: 1, 3].

---
## 🙏 Ucapan Terima Kasih (Opsional)
* Terima kasih kepada Segenap Elemen.