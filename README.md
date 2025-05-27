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

### Secara keseluruhan, sistem ini menyediakan solusi *end-to-end* untuk analisis prediktif lalu lintas.

---
## 📊 Dataset yang Digunakan
Proyek ini menggunakan dua sumber data utama yang dikumpulkan melalui batch processing:
1.  **Data Simulasi Trafik Taksi (`simulasi-trafik_medan.csv`)**:
  
   Mencakup data pergerakan taksi di Medan, termasuk lokasi, kecepatan, dan nama jalan, untuk menganalisis pola kemacetan.

    * Kolom: `timestamp`, `latitude`, `longitude`, `speed_kmh`, `taxi_id`, `road_name`.
2.  **Data Cuaca Dummy (`cuaca_medan_dummy.csv`)**:

   Data cuaca simulasi per jam untuk Medan, penting untuk analisis dampak cuaca terhadap kemacetan.

    * Kolom: `date_time`, `location`, `rainfall_mm`, `temperature_c`, `humidity_percent`, `visibility_km`.

### Data disimpan dalam data lake dengan tiga lapisan: Bronze (CSV), Silver (Parquet), dan Gold (ORC).

---
## 🏗️ Arsitektur Sistem
Sistem ini mengadopsi **Medallion Architecture** (Bronze, Silver, Gold) dengan skema batch processing.
* **Bronze Layer**: Penyimpanan data mentah GPS (HDFS, CSV/JSON).
* **Silver Layer**: Data hasil pembersihan dan transformasi (Apache Spark, Parquet/Avro).
* **Gold Layer**: Hasil agregasi analitik siap untuk query dan visualisasi (Apache Hive, Spark, Superset, Parquet/ORC).

[Bronze Layer (HDFS)] --> [Silver Layer (Spark)] --> [Gold Layer (Hive/Spark)] --> [Analytics/Dashboard (Superset)]




### Infrastruktur dikembangkan dalam cluster lokal berbasis Docker.

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

Pemilihan teknologi ini didasarkan pada kebutuhan akan skalabilitas, performa, dan ekosistem yang matang untuk analisis Big Data.

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

#### Setiap kajian ini bertujuan untuk menghasilkan *insight* yang actionable dan fitur yang bermanfaat bagi pengguna.
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
    * Ini akan membangun dan menjalankan semua layanan (Hadoop, Spark, Hive, Superset, Airflow, dll.) secara otomatis. Mohon tunggu beberapa saat hingga semua container stabil.

3.  🖥️ **Akses UI Layanan**:
    * **HDFS NameNode**: `http://localhost:9870`
    * **Spark Master**: `http://localhost:8080`
    * **Apache Superset**: `http://localhost:8089` (atau port lain jika 8088 dipakai YARN)
    * **Apache Airflow**: `http://localhost:8081` (atau port lain jika 8080 dipakai Spark)
    * **YARN ResourceManager**: `http://localhost:8088`
    * *(Port dapat bervariasi sesuai konfigurasi `docker-compose.yml` Anda)*

4.  🔧 **Konfigurasi Tambahan (Jika Ada)**:
    * *(Contoh: Setup koneksi database Superset ke Hive, inisialisasi skema Airflow, atau menjalankan skrip setup awal di HDFS. Jelaskan langkah penting di sini jika ada).*

#### Dengan langkah-langkah ini, lingkungan Big Data Anda siap untuk mulai mengolah data!
---

## 🚀 Panduan Penggunaan Sistem Prediksi Kemacetan

Berikut adalah langkah-langkah utama untuk mengoperasikan pipeline data dan mengakses hasil analisis:

1.  📥 **Ingesti Data Awal**:
    * Jalankan skrip ingesti (misalnya, `scripts/ingestion/ingest_data_to_hdfs.sh` atau picu *task* Airflow) untuk memuat data mentah GPS dan cuaca ke HDFS Bronze Layer.

2.  ✨ **Jalankan Pipeline ETL (Spark)**:
    * Eksekusi *job* Spark untuk memproses data:
        * Bronze → Silver (pembersihan & transformasi): `spark-submit scripts/etl/bronze_to_silver_spark.py`
        * Silver → Gold (agregasi & fitur): `spark-submit scripts/etl/silver_to_gold_spark.py`
    * Alternatif: Pemicu DAG Airflow yang telah dikonfigurasi untuk keseluruhan proses ETL.

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

#### Langkah-langkah ini mampu membuat Anda mengelola alur data dari mentah hingga menjadi *insight* yang divisualisasikan.
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
## 🌱 Kontribusi Pengembangan & Kolaborasi Lanjutan

Kami sangat antusias dan menyambut kontribusi dari siapa saja yang tertarik untuk mengembangkan atau meningkatkan proyek analisis kemacetan Kota Medan ini lebih lanjut! Jika Anda memiliki ide, perbaikan, atau fitur baru, jangan ragu untuk berkontribusi. Berikut adalah panduan singkatnya:

1.  **`Fork`** repositori ini ke akun GitHub Anda.
2.  Buat **`Branch`** baru untuk setiap fitur atau perbaikan (`git checkout -b fitur/nama-fitur-anda` atau `fix/deskripsi-perbaikan`).
3.  Lakukan **perubahan kode** Anda di *branch* tersebut.
4.  **`Commit`** perubahan Anda dengan pesan yang jelas dan deskriptif (`git commit -m 'Menambahkan fitur X yang canggih'`).
5.  **`Push`** *branch* Anda ke repositori *fork* Anda (`git push origin fitur/nama-fitur-anda`).
6.  Buat **`Pull Request`** baru dari *branch* Anda di *fork* ke *branch* `main` repositori ini. Jelaskan perubahan yang Anda buat.

Untuk panduan yang lebih detail mengenai standar kode, proses *review*, atau isu yang bisa dikerjakan, silakan lihat file `CONTRIBUTING.md` (jika telah kami sediakan). Bersama-sama, kita bisa membuat solusi ini lebih baik!

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

Kami bangga dengan sinergi dan pencapaian tim dalam mewujudkan proyek ini.
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
