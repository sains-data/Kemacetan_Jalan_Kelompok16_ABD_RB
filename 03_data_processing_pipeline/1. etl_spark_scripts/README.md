## ✨ Alkimia Data dengan Spark: Skrip Pembersihan, Transformasi, dan Agregasi

Selamat datang di koleksi skrip PySpark yang menjadi motor penggerak utama transformasi data dalam proyek analisis kemacetan Medan. Setiap skrip di sini dirancang dengan presisi untuk mengolah data mentah menjadi dataset yang bersih, terstruktur, dan kaya fitur, siap untuk analisis mendalam dan pemodelan prediktif.

### 📜 Filosofi Desain Skrip Spark:

* **Efisiensi**: Menggunakan operasi Spark DataFrame yang dioptimalkan, menghindari *shuffling* data yang tidak perlu, dan memanfaatkan *caching* secara bijak.
* **Keterbacaan**: Kode ditulis dengan jelas, menggunakan nama variabel yang deskriptif, dan disertai komentar untuk menjelaskan logika yang kompleks.
* **Modularitas**: Fungsi-fungsi transformasi yang kompleks dipecah menjadi unit-unit yang lebih kecil dan dapat diuji.
* **Ketahanan**: Penanganan error dan logging dasar diimplementasikan untuk memudahkan debugging dan pemantauan.
* **Reproducibility**: Skrip dirancang untuk menghasilkan output yang konsisten jika dijalankan dengan input yang sama.

### 🛠️ Skrip Utama dan Fungsinya:

1.  **`bronze_to_silver.py`**:
    * **Input**: Data mentah trafik (`simulasi_trafik_medan.csv`) dan cuaca (`cuaca_medan_2013-07-01.csv`) dari HDFS Bronze Layer.
    * **Proses Inti**:
        * **Validasi Skema & Tipe Data**: Memastikan data dibaca dengan benar dan melakukan *casting* tipe data ke format yang sesuai (timestamp, float, integer).
        * **Pembersihan Data (Cleansing)**:
            * Penanganan nilai null (missing values) dengan strategi yang tepat (misalnya, menghapus baris, mengisi dengan nilai default atau statistik).
            * Deteksi dan penghapusan data duplikat.
            * (Opsional) Penanganan outlier pada kolom numerik penting seperti `speed_kmh`.
        * **Standarisasi Format**: Menyeragamkan format `timestamp` dan mengekstrak komponen waktu yang relevan (jam, hari).
        * **Penggabungan Dataset (Join)**: Menggabungkan data trafik dan data cuaca berdasarkan `timestamp` (setelah disesuaikan ke resolusi jam yang sama) untuk memperkaya data trafik dengan informasi kontekstual cuaca.
    * **Output**: Dataset gabungan yang bersih dan terstruktur, disimpan dalam format **Parquet** di HDFS Silver Layer (`/user/hive/warehouse/kemacetan_medan/silver/trafik_cuaca/`). Format Parquet dipilih karena efisiensi penyimpanan dan performa query yang superior.

2.  **`silver_to_gold.py`**:
    * **Input**: Data bersih dari HDFS Silver Layer (output dari `bronze_to_silver.py`).
    * **Proses Inti**:
        * **Agregasi Data**: Melakukan agregasi data berdasarkan dimensi kunci seperti ruas jalan (`road_name`), jam (`jam`), dan hari dalam seminggu (`hari_minggu`). Metrik yang dihitung meliputi:
            * Kecepatan rata-rata (`avg_speed_kmh`).
            * Jumlah kendaraan (`vehicle_count`).
            * Rata-rata kondisi cuaca (misalnya, `avg_rainfall_mm`, `avg_temperature_c`) pada segmen dan waktu tersebut.
        * **Rekayasa Fitur (Feature Engineering)**:
            * (Opsional) Membuat fitur lag (misalnya, kecepatan rata-rata pada jam sebelumnya di segmen yang sama).
            * (Opsional) Membuat fitur kategorikal dummy/one-hot encoding jika diperlukan oleh model.
            * Memastikan semua fitur siap untuk dimasukkan ke dalam model Machine Learning.
    * **Output**: Dataset agregat yang sangat terkurasi dan kaya fitur, disimpan dalam format **ORC** (atau Parquet) di HDFS Gold Layer (`/user/hive/warehouse/kemacetan_medan/gold/trafik_cuaca_agg/`). Format ORC sering dipilih untuk tabel analitik karena kompresi dan optimasi *predicate pushdown*-nya. Dataset ini juga seringkali didaftarkan sebagai tabel eksternal di Hive untuk kemudahan query.

**Catatan Implementasi**:
Setiap skrip dapat dijalankan menggunakan `spark-submit` pada cluster Spark yang telah dikonfigurasi. Detail parameter eksekusi (seperti alokasi memori, jumlah core) dapat disesuaikan untuk optimalisasi performa. Log eksekusi Spark memberikan informasi detail mengenai jalannya proses transformasi.

Dedikasi terhadap kualitas kode dan ketelitian dalam setiap langkah transformasi data ini adalah fondasi yang memastikan bahwa hasil analisis dan model prediksi yang dibangun memiliki tingkat keandalan dan akurasi yang tinggi.