```markdown
# Prediksi Kemacetan Lalu Lintas Medan dengan Hadoop & Spark

## Ringkasan Proyek

Proyek ini mengimplementasikan sebuah *pipeline* Big Data yang komprehensif untuk memprediksi tingkat kemacetan lalu lintas di kota Medan, Indonesia. Dengan memanfaatkan ekosistem Hadoop, kami memproses data GPS taksi dan data cuaca skala besar untuk melakukan transformasi Extract-Transform-Load (ETL) dan melatih model *Machine Learning* (ML) menggunakan Apache Spark. Hasil prediksi kemudian divisualisasikan melalui Apache Superset.

## Arsitektur Big Data

Arsitektur *pipeline* ini dirancang untuk lingkungan terdistribusi, yang di-*deploy* menggunakan Docker Compose untuk simulasi *cluster* lokal. Komponen-komponen utamanya adalah:

* **Penyimpanan Data Terdistribusi (HDFS)**: Apache Hadoop Distributed File System (HDFS) berfungsi sebagai *data lake* untuk menyimpan data mentah, data yang sudah diproses (Silver Layer), dan hasil prediksi (Gold Layer).
* **Manajemen Sumber Daya (YARN)**: Yet Another Resource Negotiator (YARN) mengelola dan mengalokasikan sumber daya komputasi di seluruh *cluster* untuk *job* Spark.
* **Pemrosesan Data & ML (Apache Spark)**: Apache Spark adalah *engine* pemrosesan inti yang digunakan untuk operasi ETL yang kompleks dan pelatihan model Random Forest Regressor untuk memprediksi kecepatan lalu lintas.
* **Abstraksi SQL (Apache Hive)**: Apache Hive menyediakan lapisan abstraksi SQL di atas data HDFS, memungkinkan definisi skema dan *query* data yang terstruktur. Hive Metastore menggunakan PostgreSQL sebagai *backend* database-nya.
* **Visualisasi Data (Apache Superset)**: Superset adalah alat *Business Intelligence* (BI) yang digunakan untuk membuat *dashboard* interaktif dari hasil prediksi yang disajikan melalui HiveServer2.
* **Koordinasi Layanan (ZooKeeper)**: Apache ZooKeeper digunakan oleh beberapa komponen (seperti Hive) untuk koordinasi terdistribusi dan manajemen konfigurasi.

**Diagram Arsitektur:**
*(Anda bisa menambahkan diagram arsitektur di sini, mungkin menggunakan gambar yang Anda buat atau alat seperti Draw.io)*

```

[Diagram Arsitektur Anda di sini]

```

## Struktur Proyek

```

.
├── .gitignore
├── README.md
├── docker-compose.yml
├── hadoop\_simple.env
├── hive.env
├── superset.env
├── configs/
│   ├── hadoop/
│   │   ├── core-site.xml
│   │   ├── hdfs-site.xml
│   │   └── yarn-site.xml
│   ├── hive/
│   │   └── hive-site.xml
│   └── spark/
│       └── spark-defaults.conf
├── scripts/
│   ├── ingest.sh
│   └── etl\_ml\_spark.py
├── data/
│   ├── simulasi\_trafik\_medan.csv
│   └── cuaca\_medan\_2013-07-01.csv
├── notebooks/
│   ├── exploratory\_data\_analysis.ipynb
│   └── model\_evaluation\_visualization.ipynb
├── screenshots/
│   ├── hdfs\_ui.png
│   ├── spark\_ui.png
│   ├── superset\_dashboard.png
│   └── ...
└── https://www.google.com/search?q=LICENSE

````

## Persyaratan Sistem

* Docker Desktop terinstal dan berjalan (dengan dukungan WSL2 di Windows).
* RAM minimal 8GB (direkomendasikan 16GB atau lebih untuk performa optimal).
* Koneksi internet untuk mengunduh *image* Docker.

## Setup & Menjalankan Proyek

Ikuti langkah-langkah di bawah ini untuk mengaktifkan *pipeline* Big Data Anda.

### 1. Kloning Repository

```bash
git clone [https://github.com/yourusername/medan-traffic-prediction-big-data-pipeline.git](https://github.com/yourusername/medan-traffic-prediction-big-data-pipeline.git)
cd medan-traffic-prediction-big-data-pipeline
````

### 2\. Persiapan Data & Konfigurasi

  * Pastikan file data `simulasi_trafik_medan.csv` dan `cuaca_medan_2013-07-01.csv` berada di dalam folder `data/`.
  * Verifikasi dan pastikan file-file konfigurasi XML di folder `configs/` sudah ada dan sesuai dengan konfigurasi *cluster* Hadoop Anda.
  * Pastikan file `.env` (`hadoop_simple.env`, `hive.env`, `superset.env`) ada di *root* proyek. **PENTING: Ubah `SUPERSET_SECRET_KEY` di `superset.env` dengan kunci acak yang unik.**

### 3\. Setup Lingkungan Docker

Sebelum memulai, pastikan Docker Desktop berjalan dan **File Sharing** diatur dengan benar untuk *drive* tempat proyek ini berada.

```bash
# Hentikan dan bersihkan kontainer sebelumnya (jika ada)
docker-compose down -v --rmi all

# Pastikan Docker Desktop berjalan dan File Sharing sudah diatur.
# Jika ada masalah persisten, pertimbangkan untuk mereset jaringan Docker Desktop atau menginstal ulang Docker Desktop.

# Mulai semua layanan Docker
docker-compose up -d
```

Tunggu hingga semua *image* terunduh dan kontainer mulai berjalan. Anda bisa memantau statusnya:

```bash
docker-compose ps
```

Semua layanan harus berstatus `Up` (dan `healthy` untuk beberapa layanan).

### 4\. Akses UI Web (Verifikasi Layanan)

Setelah semua kontainer `Up`, beri waktu 1-2 menit agar layanan berinisialisasi.

  * **HDFS Namenode UI**: `http://localhost:9870`
  * **Spark Master UI**: `http://localhost:8080`
  * **YARN ResourceManager UI**: `http://localhost:8089`
  * **HiveServer2 Web UI (Opsional)**: `http://localhost:10002`
  * **Superset UI**: `http://localhost:8088`
      * *Login* dengan: **Username: `superset`**, **Password: `superset`** (kredensial awal yang dibuat di `docker-compose.yml`).

### 5\. Jalankan Pipeline Data

Pipeline akan dijalankan secara manual dalam dua tahap utama: Ingestion ke HDFS dan ETL/ML dengan Spark.

#### a. Ingestion Data ke HDFS (Bronze Layer)

Kita akan menggunakan *shell* kontainer `spark-master` untuk menjalankan skrip *ingestion*.

```bash
# Masuk ke dalam kontainer spark-master
docker exec -it spark-master bash

# Dari dalam kontainer, jalankan skrip ingestion
# (Pastikan path ke spark-submit sudah benar di lingkungan kontainer)
/opt/spark-apps/ingest.sh

# Setelah skrip selesai, ketik 'exit' untuk keluar dari kontainer
exit
```

Verifikasi bahwa file-file CSV (`simulasi_trafik_medan.csv` dan `cuaca_medan_2013-07-01.csv`) sudah ada di `http://localhost:9870/explorer.html#/data/bronze/`.

#### b. Jalankan Job ETL & ML dengan Spark (Silver & Gold Layer)

Kita akan menggunakan *shell* kontainer `spark-master` lagi untuk menjalankan skrip PySpark utama.

```bash
# Masuk kembali ke dalam kontainer spark-master
docker exec -it spark-master bash

# Dari dalam kontainer, jalankan skrip PySpark utama
# PENTING: Gunakan path lengkap untuk spark-submit dan pastikan Python 3 digunakan
# (Berdasarkan pengalaman debugging sebelumnya, path ini mungkin /spark/bin/spark-submit)
env PYSPARK_PYTHON=/usr/bin/python3 /spark/bin/spark-submit --master spark://spark-master:7077 --executor-memory 1G --driver-memory 1G /opt/spark-apps/etl_ml_spark.py

# Setelah skrip selesai (akan memakan waktu), ketik 'exit' untuk keluar dari kontainer
exit
```

Perhatikan log yang akan muncul di terminal. Setelah selesai, verifikasi file Parquet di HDFS UI di `http://localhost:9870/explorer.html#/data/silver/` dan `http://localhost:9870/explorer.html#/data/gold/`. Pastikan juga tabel `traffic_predictions` sudah dibuat di Hive.

### 6\. Konfigurasi dan Visualisasi di Superset

Setelah data Gold Layer tersedia di HDFS dan tabel Hive sudah dibuat, Anda bisa menyiapkan Superset.

1.  **Tambahkan Koneksi Database Hive di Superset:**

      * Buka Superset UI (`http://localhost:8088`).
      * Navigasi ke **`Data` \> `Databases`**.
      * Klik **`+ Database`** dan pilih **`Apache Hive`**.
      * **`Database Name`**: `Hive_Cluster` (atau nama lain yang mudah diingat).
      * **`SQLAlchemy URI`**: `hive://hiveserver2:10000/default`
      * Klik **`Test Connection`** untuk memverifikasi.
      * Klik **`Add`** untuk menyimpan.

2.  **Buat Dataset dari Tabel Hive:**

      * Navigasi ke **`Data` \> `Datasets`**.
      * Klik **`+ Dataset`**.
      * Pilih Database yang baru Anda buat (`Hive_Cluster`).
      * Pilih Skema `default`.
      * Untuk **`Table Name`**, pilih `traffic_predictions`.
      * Klik **`Add`**.

3.  **Mulai Membangun Dashboard:**
    Sekarang Anda dapat mulai membuat *chart* dan *dashboard* interaktif di Superset menggunakan dataset `traffic_predictions`. Contoh visualisasi bisa berupa *line chart* tren kecepatan per jam, *count plot* tingkat kemacetan, atau peta kemacetan (membutuhkan data geospasial yang lebih kompleks dan mungkin pustaka visualisasi yang berbeda).

## Hasil Prediksi (Contoh dari Log Eksekusi)

  * **Metrik Evaluasi Model Random Forest:**

      * Root Mean Squared Error (RMSE) pada data uji: `104.90524701330426`
      * Mean Absolute Error (MAE) pada data uji: `39.20311083420466`

  * **Contoh Data Hasil Prediksi (seperti terlihat di `final_gold_df.show(5)`):**

    ```
    +--------------------+----+-----------+-------------+----------+-----------+--------------------+-------------+-----------------------+--------------------------+
    |           road_name|hour|rainfall_mm|temperature_c|  latitude|  longitude|actual_avg_speed_kmh|vehicle_count|predicted_avg_speed_kmh|predicted_congestion_level|
    +--------------------+----+-----------+-------------+----------+-----------+--------------------+-------------+-----------------------+--------------------------+
    |Jalan H.O.S. Cokro...|   1|        0.0|          0.0|3.591672  |98.69175   |    43.33487319946289 |           2|      30.52813454979675|                    Medium|
    |['Gang Kasan Jaya...|   0|        0.0|          0.0|3.615342  |98.64587   |   126.44354248046875|           2|      30.52813454979675|                    Medium|
    |         Gang Rakit |   1|        0.0|          0.0|3.642756  |98.66238   |   118.02767181396484|           1|      30.52813454979675|                    Medium|
    |      Jalan Elang II|   0|        0.0|          0.0|3.589728  |98.718666  |   32.734764099121094|           1|      195.0622512646441|                       Low|
    |   Jalan Tangkul I  |   0|        0.0|          0.0|3.617133  |98.69789   |   0.3602720573544502|           1|       0.0             |                     High|
    +--------------------+----+-----------+-------------+----------+-----------+--------------------+-------------+-----------------------+--------------------------+
    ```

## Pembahasan & Kesimpulan

Proyek ini berhasil mendemonstrasikan implementasi *pipeline* Big Data fungsional pada lingkungan Hadoop yang disimulasikan. Meskipun ada tantangan dalam *setup* awal *dependency* dan konfigurasi PySpark di lingkungan Docker, masalah-masalah ini berhasil diatasi dengan pendekatan *debugging* yang sistematis, termasuk penyesuaian versi Python dan parameter `maxBins` pada model ML.

Data telah berhasil melalui tahapan Bronze, Silver, dan Gold Layer, dengan data yang dibersihkan, ditransformasi, dan diperkaya disimpan di HDFS. Model Random Forest Regressor berhasil dilatih untuk memprediksi kecepatan lalu lintas, dan hasil prediksinya telah dibuat dan tersedia untuk analisis lebih lanjut. Integrasi dengan Apache Hive memungkinkan Superset untuk dengan mudah mengakses dan memvisualisasikan hasil ini, menunjukkan kemampuan *stack* Big Data dalam mendukung pengambilan keputusan berbasis data.

Proyek ini menjadi bukti pemahaman akan konsep-konsep Big Data, rekayasa data, *machine learning*, dan *deployment* infrastruktur. Untuk pengembangan lebih lanjut, optimasi model dan penanganan *edge cases* dalam data akan menjadi fokus utama.

## Kontributor

  * [Nama Lengkap Anda]

## Lisensi

Proyek ini dilisensikan di bawah [Lisensi MIT](https://www.google.com/search?q=LICENSE) - lihat file `LICENSE` untuk detail lebih lanjut.

```
```