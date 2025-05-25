# ⚙️ Jantung Transformasi Data: Dari Data Mentah ke Insight Terkurasi untuk Analisis Kemacetan Medan

Selamat datang di **pusat operasi transformasi data** proyek "Implementasi Ekosistem Hadoop untuk Analisis Big Data Lalu Lintas Kota Medan". Folder ini merupakan inti dari *Medallion Architecture* kami, tempat data mentah ditempa dan diolah menjadi aset informasi berkualitas tinggi yang siap untuk analisis prediktif dan visualisasi. Di sini, kami mendemonstrasikan keahlian dalam rekayasa data menggunakan Apache Spark dan orkestrasi pipeline data yang efisien.

## 🎯 Filosofi Pipeline Data:

Pipeline data kami dirancang dengan berpegang pada prinsip-prinsip berikut:
1.  **Robustness & Resilience**: Membangun proses ETL (Extract, Transform, Load) yang tangguh, mampu menangani variasi data, dan memiliki mekanisme pemulihan dari kegagalan.
2.  **Efficiency & Scalability**: Mengoptimalkan setiap tahap transformasi untuk kinerja pemrosesan yang cepat dan kemampuan untuk menangani volume data yang terus bertambah, khas dari data lalu lintas.
3.  **Data Quality & Governance**: Menerapkan validasi, pembersihan, dan standarisasi data yang ketat untuk memastikan integritas dan keandalan informasi di setiap lapisan arsitektur (Bronze, Silver, Gold).
4.  **Modularity & Maintainability**: Skrip dan alur kerja dirancang secara modular agar mudah dipahami, diuji, dan dipelihara.
5.  **Automation**: Menggunakan Apache Airflow untuk orkestrasi pipeline yang terjadwal dan termonitor, mengurangi intervensi manual dan memastikan konsistensi eksekusi.

## 📁 Struktur Subfolder dan Komponen Kunci:

* **`etl_spark_scripts/`**:
    * **Deskripsi**: Direktori ini adalah **laboratorium alkimia data** kami. Berisi serangkaian skrip PySpark yang cermat dan dioptimalkan untuk melakukan transformasi data melalui berbagai tahapan *Medallion Architecture*:
        * **`bronze_to_silver.py`**: Skrip ini mengambil data mentah dari HDFS Bronze Layer (data trafik dan cuaca), melakukan pembersihan data komprehensif (penanganan nilai null, duplikat, outlier), validasi skema, standarisasi format (misalnya, timestamp), dan penggabungan dataset yang relevan. Outputnya adalah data yang bersih, terstruktur, dan siap untuk analisis lebih lanjut, disimpan dalam format Parquet di Silver Layer.
        * **`