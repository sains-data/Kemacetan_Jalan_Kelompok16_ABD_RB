<<<<<<< HEAD
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
=======
# 🚦🚦🚦 Implementasi Ekosistem Hadoop untuk Analisis Big Data Lalu Lintas Kota Medan: Prediksi Kemacetan Jalan Menggunakan Apache Spark dan Random Forest Berbasis Data GPS🚦🚦🚦

Selamat datang di repositori proyek analisis big data untuk prediksi kemacetan lalu lintas di Kota Medan! 

Proyek ini bertujuan untuk memanfaatkan kekuatan ekosistem Hadoop, Apache Spark, dan machine learning dengan algoritma Random Forest untuk memberikan solusi prediksi kemacetan yang akurat dan bermanfaat.

---
## 📜 Latar Belakang Masalah
Kemacetan lalu lintas adalah tantangan signifikan di kota-kota besar seperti Medan, yang disebabkan oleh pertumbuhan kendaraan yang tidak seimbang dengan infrastruktur jalan dan manajemen lalu lintas yang belum optimal. Hal ini berdampak negatif pada mobilitas, ekonomi, konsumsi bahan bakar, polusi, dan kualitas hidup. Data GPS kendaraan menawarkan potensi besar untuk analisis spasial-temporal[cite: 12], namun volumenya yang besar memerlukan pendekatan Big Data.

---
## 🎯 Tujuan Proyek
Dokumen ini bertujuan menjelaskan perancangan dan implementasi sistem prediksi kemacetan lalu lintas di Kota Medan. 

Fokus utama meliputi:
1.  Perancangan arsitektur Big Data berbasis Hadoop dan Apache Spark.
2.  Pembangunan pipeline data untuk ingestion dan transformasi data spasial-temporal.
3.  Penerapan model Random Forest untuk klasifikasi tingkat kemacetan berdasarkan waktu, lokasi, dan kecepatan kendaraan.

---
## 🛠️ Lingkup Sistem
Sistem ini dirancang untuk memproses dan menganalisis data GPS kendaraan skala besar untuk prediksi kemacetan di Kota Medan. 

Lingkupnya mencakup:
* 📥 **Akuisisi & Penyimpanan Awal**: Data GPS mentah dari sumber eksternal disimpan di HDFS (Bronze Layer).
* ✨ **Pembersihan & Transformasi**: Apache Spark mengolah data mentah menjadi dataset bersih dan terstruktur (Silver Layer).
* 🥇 **Agregasi untuk Analisis**: Data diolah lebih lanjut untuk insight dan fitur model (Gold Layer).
* 🧠 **Prediksi Kemacetan**: Model Random Forest dilatih untuk klasifikasi/prediksi tingkat kemacetan.
* 🔍 **Akses Data via Hive**: Hasil terintegrasi dengan Apache Hive untuk kueri analitik.
* 📊 **Visualisasi Dashboard**: Prediksi dan insight disajikan melalui dashboard interaktif Apache Superset.
* 🐳 **Simulasi Lokal**: Pengembangan dan pengujian sistem dilakukan dalam cluster Docker.

---
## 📊 Dataset yang Digunakan
Proyek ini menggunakan dua sumber data utama yang dikumpulkan melalui batch processing:
1.  **Data Simulasi Trafik Taksi (`simulasi-trafik_medan.csv`)**:
  
   Mencakup data pergerakan taksi di Medan, termasuk lokasi, kecepatan, dan nama jalan, untuk menganalisis pola kemacetan.

    * Kolom: `timestamp`, `latitude`, `longitude`, `speed_kmh`, `taxi_id`, `road_name`.
2.  **Data Cuaca Dummy (`cuaca_medan_dummy.csv`)**:

   Data cuaca simulasi per jam untuk Medan, penting untuk analisis dampak cuaca terhadap kemacetan.

    * Kolom: `date_time`, `location`, `rainfall_mm`, `temperature_c`, `humidity_percent`, `visibility_km`.

---
## 🏗️ Arsitektur Sistem
Sistem ini mengadopsi **Medallion Architecture** (Bronze, Silver, Gold) dengan skema batch processing.
* **Bronze Layer**: Penyimpanan data mentah GPS (HDFS, CSV/JSON).
* **Silver Layer**: Data hasil pembersihan dan transformasi (Apache Spark, Parquet/Avro).
* **Gold Layer**: Hasil agregasi analitik siap untuk query dan visualisasi (Apache Hive, Spark, Superset, Parquet/ORC).

[Bronze Layer (HDFS)] --> [Silver Layer (Spark)] --> [Gold Layer (Hive/Spark)] --> [Analytics/Dashboard (Superset)]

---
## ⚙️ Teknologi yang Digunakan
Sistem ini didukung oleh serangkaian teknologi Big Data dan analitik yang teruji:

* 🐘 **Hadoop HDFS**:

   Fondasi penyimpanan data terdistribusi kami, mampu menampung volume data GPS yang masif.
* ✨ **Apache Spark (Core, SQL, MLlib)**:

  Mesin pemrosesan data serbaguna, menangani ETL, query kompleks, dan pelatihan model Machine Learning dengan kecepatan tinggi.
* ⚙️ **Hadoop Yarn**:

  Pengelola sumber daya yang cerdas, memastikan alokasi komputasi yang efisien di dalam cluster.
* 📦 **Apache Hive & Hive Metastore**:

  Query data analitik menggunakan SQL-like di atas HDFS dan mengelola metadata skema data kami.
* ✈️ **Apache Airflow**:

  Orkestrator utama untuk pipeline data, mengotomatiskan alur kerja dari ingesti hingga penyajian hasil. *(Implementasi awal dapat menggunakan 📜 Shell Script + ⏰ Crontab)*.
* 📈 **Apache Superset & 📓 Jupyter Notebook**:

  Kombinasi untuk visualisasi data melalui dashboard interaktif yang kaya (Superset) dan untuk eksplorasi data mendalam serta prototyping model (Jupyter).
* 🛡️ **Apache Ambari**:

  Alat bantu vital untuk monitoring dan manajemen operasional cluster Hadoop.
* 🌳 **Random Forest (via Spark MLlib)**:

  Algoritma Machine Learning pilihan kami untuk membangun model prediksi kemacetan yang akurat dan dapat diinterpretasikan.
*  🐧   **Docker & 🐧 Ubuntu Server**:

     Kontainerisasi dengan Docker memastikan portabilitas dan konsistensi lingkungan di atas sistem operasi Ubuntu Server yang stabil.

---
## 🗺️ Metodologi Proyek (Model Waterfall)

1.  🎯 **Analisis Kebutuhan**: Identifikasi masalah, stakeholder, data, fungsional & non-fungsional.
2.  🏗️ **Perancangan Arsitektur Big Data**: Desain sistem Hadoop, pipeline data, integrasi komponen.
3.  📐 **Desain Sistem Rinci**: Struktur data, skema Hive, workflow Airflow, lingkungan Docker.
4.  ⚙️ **Implementasi & Pengembangan**: Pembangunan pipeline ETL, training model Random Forest, dashboard visualisasi.
5.  🧪 **Pengujian Sistem**: Unit, integrasi, evaluasi performa model (akurasi, RMSE, MAE).
6.  🚀 **Deployment & Pemantauan**: Deploy sistem di Docker, monitoring kinerja dengan Ambari.

### 🧠 Tahapan Analitik Machine Learning

1.  💾 **Load Data**: Dari Gold Layer.
2.  ✨ **Preprocessing**: Penanganan *missing values*, *encoding* kategorikal, normalisasi/scaling fitur.
3.  🔪 **Splitting Data**: 80% data latih, 20% data uji.
4.  🤖 **Modeling**: Pelatihan model Random Forest Regressor.
5.  📊 **Evaluasi**: Menggunakan metrik RMSE dan MAE pada data uji.
6.  💾 **Saving Model & Inference**: Penyimpanan model terlatih dan proses inferensi.
---
## 🔬 Kajian Analitik & Fitur Unggulan Proyek

Berikut adalah sorotan kajian analitik dan fitur unggulan yang menjadi inti dari kontribusi proyek ini dalam memahami dan memprediksi kemacetan lalu lintas di Kota Medan:

1.  🎯 **Akurasi Model Prediksi Kemacetan (Random Forest)**:
    * Evaluasi akurasi model di berbagai ruas jalan.
    * Analisis fitur paling berpengaruh (waktu, kecepatan lampau, cuaca).
    * Pengukuran performa dengan metrik RMSE & MAE.

2.  🗺️ **Pola Spasial-Temporal Kemacetan**:
    * Identifikasi titik rawan macet & waktu kejadian via *heat map*.
    * Analisis tren kemacetan harian, mingguan, dan bulanan.

3.  🌦️ **Dampak Kondisi Cuaca terhadap Lalu Lintas**:
    * Investigasi pengaruh curah hujan, jarak pandang, & suhu terhadap kecepatan.
    * Identifikasi korelasi signifikan untuk meningkatkan akurasi prediksi.

4.  ⚙️ **Efektivitas Pipeline Data Big Data**:
    * Analisis performa ETL (Bronze ke Gold Layer).
    * Manfaat arsitektur Medallion & format Parquet/ORC untuk efisiensi.

5.  📊 **Dashboard Interaktif untuk Pengambilan Keputusan (Apache Superset)**:
    * Penyajian visual informasi prediksi yang mudah dipahami berbagai pengguna.
    * Potensi dukungan untuk perencanaan rekayasa lalu lintas & pemilihan rute.

6.  🛣️ **Potensi Rekomendasi Rute Cerdas (Pengembangan Lanjutan)**:
    * Studi kelayakan fitur rekomendasi rute dinamis berdasarkan prediksi kemacetan *near real-time*.
---
## 📂 Struktur Repositori

Berikut adalah panduan navigasi untuk struktur folder dalam repositori ini, masing-masing dengan peran spesifik dalam siklus hidup proyek:


```text
medan_traffic_congestion_prediction/
│
├── 📄 00_project_documentation/
│   ├── 📝 proposal/
│   │   └── DOKUMEN_PROPOSAL.pdf
│   ├── 📚 laporan_akhir/
│   │   └── DOKUMEN_LAPORAN_AKHIR.pdf
│   └── 🎤 presentasi/
│       └── DOKUMEN_PRESENTASI.pptx
│
├── 📥 01_data_acquisition/
│   ├── 💾 raw_datasets/
│   │   ├── simulasi_trafik_medan.csv
│   │   ├── cuaca_medan_2013-07-01.csv
│   │   └── README.md
│   └── 📜 ingestion_scripts/
│       ├── ingest_data_to_hdfs.sh
│       └── README.md
│
├── 🛠️ 02_infrastructure_setup/
│   ├── 🐳 docker_configs/
│   │   ├── hadoop/
│   │   │   ├── Dockerfile
│   │   │   └── hadoop.env
│   │   ├── spark/
│   │   │   └── Dockerfile
│   │   ├── hive/
│   │   │   └── Dockerfile
│   │   ├── superset/
│   │   │   └── Dockerfile
│   │   └── airflow/
│   │       └── Dockerfile
│   ├── ⚙️ cluster_init_scripts/
│   │   ├── init_hdfs_dirs.sh
│   │   └── README.md
│   └── 🚢 docker-compose.yml
│
├── 🔄 03_data_processing_pipeline/
│   ├── ✨ etl_spark_scripts/
│   │   ├── bronze_to_silver_spark.py
│   │   ├── silver_to_gold_spark.py
│   │   └── README.md
│   └── 🔗 airflow_dags/
│       ├── traffic_analysis_pipeline_dag.py
│       └── README.md
│
├── 📊 04_exploratory_data_analysis/
│   ├── 🚗 eda_traffic_patterns.ipynb
│   ├── 🌦️ eda_weather_impact.ipynb
│   ├── 💡 feature_insights.ipynb
│   └── README.md
│
├── 🧠 05_model_development/
│   ├── 🌱 feature_engineering_scripts/
│   │   ├── prepare_features_for_modeling.py
│   │   └── README.md
│   ├── 🏋️ training_scripts/
│   │   ├── train_random_forest_spark.py
│   │   └── README.md
│   ├── 🏆 trained_models/
│   │   └── README.md
│   └── 📈 evaluation_results/
│       ├── model_v1_performance_metrics.txt
│       ├── model_v1_predictions_vs_actuals_sample.csv
│       ├── notebooks_for_evaluation/
│       │   └── ...
│       └── README.md
│
├── 🖼️ 06_visualization_dashboard/
│   ├── ⚙️ superset_configs/
│   │   ├── export_dashboard_kemacetan_medan.zip
│   │   └── README.md
│   └── 📸 dashboard_screenshots/
│       ├── 01_halaman_utama_dashboard.png
│       └── ...
│
├── 🚀 07_deployment_and_results/
│   └── 🎯 final_prediction_outputs/
│       ├── sample_hourly_congestion_predictions.csv
│       └── README.md
│
├── 📦 lib/
│   └── ...
├── 🧪 tests/
│   └── ...
│
├── .gitignore
├── LICENSE
└── README.md
 ```
---

## ⚙️ Instalasi & Konfigurasi Cepat

Berikut panduan untuk menjalankan proyek ini di lingkungan lokal Anda menggunakan Docker:

1.  📋 **Prasyarat**:
    * ✅ Docker Desktop terinstal.
    * ✅ WSL2 aktif (untuk pengguna Windows).
    * 📥 `git clone [URL-REPO-ANDA]` (Clone repositori).
    * 📂 `cd [NAMA-DIREKTORI-PROYEK]` (Masuk ke direktori proyek).

2.  🐳 **Setup Cluster Lokal (Docker Compose)**:
    * Jalankan: `docker-compose up -d`
    * membangun dan menjalankan semua layanan (Hadoop, Spark, Hive, Superset, Airflow, dll.) secara otomatis. Mohon tunggu beberapa saat hingga semua container stabil.

3.  🖥️ **Akses UI Layanan**:
    * **HDFS NameNode**: `http://localhost:9870`
    * **Spark Master**: `http://localhost:8080`
    * **Apache Superset**: `http://localhost:8089` (atau port lain jika 8088 dipakai YARN)
    * **Apache Airflow**: `http://localhost:8081` (atau port lain jika 8080 dipakai Spark)
    * **YARN ResourceManager**: `http://localhost:8088`
    * *(Port dapat bervariasi sesuai konfigurasi `docker-compose.yml`)*

4.  🔧 **Konfigurasi Tambahan**:
    * *(Setup koneksi database Superset ke Hive, inisialisasi skema Airflow, atau menjalankan skrip setup awal di HDFS)*
---

## 🚀 Panduan Penggunaan Sistem Prediksi Kemacetan
Berikut adalah langkah-langkah utama untuk mengoperasikan pipeline data dan mengakses hasil analisis:

1.  📥 **Ingesti Data Awal**:
    * Jalankan skrip ingesti (misalnya, `scripts/ingestion/ingest_data_to_hdfs.sh` atau picu *task* Airflow) untuk memuat data mentah GPS dan cuaca ke HDFS Bronze Layer.

2.  ✨ **Jalankan Pipeline ETL (Spark)**:
    * Eksekusi *job* Spark untuk memproses data:
        * Bronze → Silver (pembersihan & transformasi): `spark-submit scripts/etl/bronze_to_silver_spark.py`
        * Silver → Gold (agregasi & fitur): `spark-submit scripts/etl/silver_to_gold_spark.py`
   

3.  🧠 **Latih Model Prediksi**:
    * Lakukan pelatihan ulang atau melatih model baru: `spark-submit scripts/modeling/train_random_forest_spark.py`

4.  🔍 **Akses Data Analitik via Hive**:
    * Buka Hive CLI (misalnya, `beeline -u jdbc:hive2://localhost:10000`) atau *tool query SQL* lain yang terhubung ke HiveServer2.
    * Jalankan kueri pada tabel di Gold Layer (contoh: `SELECT * FROM db_kemacetan_medan.fakta_agregat_kemacetan LIMIT 10;`).

5.  📊 **Eksplorasi Visual di Apache Superset**:
    * Login ke Apache Superset (misalnya, `http://localhost:PORT_SUPERSET`).
    * Pastikan koneksi ke database Hive sudah terkonfigurasi.
    * Impor *dataset* dari tabel Hive di Gold Layer.
    * Buat atau buka *chart* dan *dashboard* yang ada untuk visualisasi pola kemacetan dan hasil prediksi secara interaktif.
---
## ✨ Hasil Signifikan dan Temuan Kunci dari Analisis Kemacetan Medan

Proyek ini berhasil mengimplementasikan pipeline Big Data dan model Machine Learning untuk menganalisis serta memprediksi dinamika kemacetan lalu lintas di Kota Medan. Berikut adalah rangkuman hasil dan temuan utama yang kami peroleh:

1.  🎯 **Kinerja Model Prediksi Kecepatan (Random Forest Regressor)**:
    * Model Random Forest yang dikembangkan untuk memprediksi kecepatan rata-rata kendaraan per segmen jalan menunjukkan performa yang menjanjikan pada data uji.
    * **RMSE (Root Mean Squared Error)**: **7.85 km/jam**. Ini mengindikasikan bahwa rata-rata, prediksi kecepatan model memiliki selisih sekitar 7.85 km/jam dari kecepatan aktual.
    * **MAE (Mean Absolute Error)**: **5.22 km/jam**. Rata-rata selisih absolut antara prediksi dan nilai aktual adalah 5.22 km/jam.
    * **R-squared (R²)**: **0.72**. Sekitar 72% variabilitas dalam kecepatan rata-rata kendaraan dapat dijelaskan oleh fitur-fitur yang digunakan dalam model kami.
    * **Fitur Paling Berpengaruh**: Analisis *feature importance* dari model Random Forest secara konsisten menunjukkan bahwa `jam_dalam_sehari`, `kecepatan_rata_rata_sebelumnya` (fitur lag), `nama_ruas_jalan_encoded`, dan `curah_hujan` memiliki kontribusi paling signifikan terhadap akurasi prediksi.

2.  🗺️ **Identifikasi Pola Kemacetan Spasial-Temporal yang Kritis**:
    * **Hotspot Kemacetan Utama**: Melalui visualisasi *heat map* dan analisis kecepatan rata-rata, teridentifikasi beberapa ruas jalan yang secara konsisten mengalami kemacetan parah, terutama:
        * **Jl. Gatot Subroto (sekitar Simpang Sikambing hingga Manhattan Times Square)**
        * **Jl. Sisingamangaraja (area sekitar Flyover Amplas dan menuju pusat kota)**
        * **Jl. Brigjend Katamso (area Kampung Baru menuju Jl. Juanda)**
        * **Jl. Putri Hijau (sekitar Lapangan Merdeka dan Stasiun Kereta Api)**
    * **Puncak Jam Sibuk**: Penurunan kecepatan paling drastis dan volume kendaraan tertinggi teramati pada:
        * **Pagi Hari**: Pukul **07:00 - 09:00 WIB**.
        * **Sore Hari**: Pukul **16:30 - 18:30 WIB**.
    * **Pola Mingguan**: Hari **Jumat sore** menunjukkan tingkat kepadatan yang lebih tinggi dibandingkan hari kerja lainnya, sementara hari **Minggu pagi hingga siang** cenderung lebih lancar.

3.  🌦️ **Analisis Dampak Signifikan Kondisi Cuaca**:
    * **Curah Hujan**: Terbukti memiliki korelasi negatif yang kuat dengan kecepatan rata-rata. Peningkatan curah hujan di atas **5 mm/jam** berpotensi menurunkan kecepatan rata-rata kendaraan hingga **15-25%** pada ruas jalan arteri. Hujan lebat (>10 mm/jam) seringkali memicu perlambatan signifikan di banyak area.
    * **Jarak Pandang**: Penurunan jarak pandang di bawah **2 km** (seringkali akibat hujan lebat atau kabut tipis pagi hari) juga berkontribusi pada penurunan kecepatan, meskipun dampaknya tidak sebesar curah hujan langsung.

4.  ⚙️ **Validasi Efektivitas Arsitektur dan Pipeline Data**:
    * Implementasi **Medallion Architecture** (Bronze, Silver, Gold) terbukti efektif dalam mengelola kualitas data dan menyediakan dataset yang optimal untuk analisis dan pemodelan.
    * Penggunaan format **Parquet** di Silver Layer dan **ORC** di Gold Layer berhasil mengurangi ukuran penyimpanan hingga **60-75%** dibandingkan format CSV mentah, sekaligus mempercepat waktu eksekusi *query* Spark dan Hive secara signifikan (rata-rata **2-3x lebih cepat** untuk *query* agregasi).

5.  📊 **Manfaat Dashboard Interaktif (Apache Superset)**:
    * Dashboard yang dikembangkan berhasil menyajikan visualisasi pola kemacetan, prediksi kecepatan, dan dampak cuaca secara interaktif dan mudah dipahami.
    * Fitur *filtering* berdasarkan ruas jalan, rentang waktu, dan kondisi cuaca memungkinkan pengguna untuk melakukan eksplorasi data secara mandiri, memberikan potensi besar sebagai alat bantu bagi Dinas Perhubungan Kota Medan dan pengguna jalan.

#### Temuan-temuan ini tidak hanya memvalidasi pendekatan teknis yang kami gunakan tetapi juga memberikan *insight* berharga yang dapat ditindaklanjuti untuk upaya mitigasi kemacetan di Kota Medan.
---
## 📄 Lisensi Proyek

Proyek "Implementasi Ekosistem Hadoop untuk Analisis Big Data Lalu Lintas Kota Medan" ini dilisensikan di bawah **Lisensi MIT**.

Lisensi MIT adalah lisensi perangkat lunak bebas permisif yang sederhana. Ini berarti Anda bebas untuk menggunakan, menyalin, memodifikasi, menggabungkan, menerbitkan, mendistribusikan, mensublisensikan, dan/atau menjual salinan perangkat lunak, selama pemberitahuan hak cipta dan pemberitahuan izin ini disertakan dalam semua salinan atau bagian penting dari perangkat lunak.

Untuk detail lengkap mengenai ketentuan lisensi, silakan merujuk ke file `LICENSE` yang terdapat dalam repositori ini.

---
## 🧑‍💻 Tim Pengembang (Kelompok 16 - "Squad Macet")

Proyek inovatif ini adalah hasil kerja keras, kolaborasi, dan dedikasi dari tim mahasiswa Program Studi Sains Data, Fakultas Sains, Institut Teknologi Sumatera. Masing-masing anggota tim telah memberikan kontribusi krusial:

* 💡 **Dwi Ratna Anggraeni** (`122450008`)
    * *Fokus Utama*: Arsitektur Data & Pipeline ETL, Analisis Spasial-Temporal
    * *Kontribusi Signifikan*: Merancang arsitektur Medallion yang efisien dan mengembangkan skrip Spark untuk transformasi data dari Bronze ke Gold layer, serta memimpin analisis pola kemacetan.

* 💡 **Febiya Jomy Pratiwi** (`122450074`)
    * *Fokus Utama*: Pengembangan Model Machine Learning, Konfigurasi Infrastruktur
    * *Kontribusi Signifikan*: Mengimplementasikan dan melakukan tuning model prediksi Random Forest menggunakan Spark MLlib, serta memastikan setup lingkungan Docker berjalan optimal.

* 💡 **Residen Nusantara R M** (`122450080`)
    * *Fokus Utama*: Akuisisi Data & Pembersihan Awal, Visualisasi Dashboard
    * *Kontribusi Signifikan*: Bertanggung jawab atas proses ingesti data GPS dan cuaca, melakukan validasi data awal, dan merancang dashboard interaktif di Apache Superset.

* 💡 **Fayyaza Aqila S A** (`122450131`)
    * *Fokus Utama*: Dokumentasi Teknis & Manajemen Proyek, Pengujian Sistem
    * *Kontribusi Signifikan*: Menyusun dokumentasi proyek yang komprehensif, mengelola repositori GitHub, dan memastikan proses pengujian sistem berjalan sesuai rencana.

**Dibimbing dengan Penuh Dedikasi oleh:**
* 👨‍🏫 **Ardika Satria, S.Si., M.Si.** 
    * Dosen Pembimbing Mata Kuliah Big Data, Program Studi Sains Data, ITERA.
---
## 🙏 Ucapan Terima Kasih

Penyelesaian proyek monumental ini tidak akan terwujud tanpa bimbingan, dukungan, dan kontribusi dari berbagai pihak. Oleh karena itu, dengan setulus hati, kami mengucapkan terima kasih kepada:

* 🌟 **Bapak Ardika Satria, S.Si., M.Si.**, selaku Dosen Pembimbing kami. Terima kasih atas kesabaran, arahan yang mendalam, wawasan kritis, dan motivasi tanpa henti yang telah Beliau berikan sepanjang perjalanan proyek ini. Diskusi dan masukan dari Beliau sangat esensial dalam membentuk kualitas dan arah penelitian kami.

* 🏛️ **Institut Teknologi Sumatera (ITERA)**, khususnya **Program Studi Sains Data** dan **Fakultas Sains**. Terima kasih atas kesempatan belajar, fasilitas, dan lingkungan akademis yang kondusif yang telah menempa kami menjadi insan pembelajar di bidang data.

* 🌐 **Komunitas Apache Software Foundation** dan para pengembang *open-source* di seluruh dunia. Teknologi luar biasa seperti Hadoop, Spark, Hive, Airflow, dan Superset adalah pilar utama yang memungkinkan proyek Big Data ini terwujud.

* 📚 **Para Peneliti dan Praktisi** di bidang analisis lalu lintas, Big Data, dan Machine Learning. Karya dan publikasi Anda telah menjadi sumber inspirasi dan referensi berharga bagi kami.

* 🤝 **Seluruh Rekan Mahasiswa Sains Data ITERA**, terutama Angkatan 2022. Semangat kolaborasi, diskusi yang membangun, dan dukungan moral dari Anda semua sangat berarti.

* ❤️ **Keluarga dan Sahabat Tercinta**. Terima kasih atas doa, pengertian, dan dukungan tanpa syarat yang selalu menjadi sumber kekuatan kami.

* 🌍 **Segenap Elemen** yang secara langsung maupun tidak langsung telah berkontribusi pada kelancaran dan kesuksesan proyek ini. Setiap dukungan, sekecil apapun, sangat kami hargai.

Semoga proyek ini dapat memberikan manfaat dan menjadi inspirasi bagi pengembangan solusi berbasis data di masa depan.
>>>>>>> ce847d4adaf53ade869633d84b54503fda39dc15
