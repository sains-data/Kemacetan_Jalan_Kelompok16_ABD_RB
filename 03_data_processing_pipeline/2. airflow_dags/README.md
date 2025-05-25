## 🎶 Orkestrasi Cerdas: Otomatisasi Alur Kerja Data dengan Apache Airflow

Folder ini adalah **ruang kendali orkestrasi** untuk pipeline data proyek analisis kemacetan Medan. Di sini, kami mendefinisikan Directed Acyclic Graphs (DAGs) menggunakan Apache Airflow untuk mengotomatiskan, menjadwalkan, dan memonitor seluruh alur kerja pemrosesan data secara sistematis dan andal.

### 📜 Filosofi Desain DAG Airflow:

* **Atomicity & Idempotency**: Setiap tugas dalam DAG dirancang untuk menjadi atomik (melakukan satu hal dengan baik) dan idempoten (dapat dijalankan berulang kali dengan hasil yang sama atau tanpa efek samping negatif jika sudah berhasil).
* **Clear Dependencies**: Ketergantungan antar tugas didefinisikan secara eksplisit, memastikan urutan eksekusi yang benar.
* **Monitoring & Alerting**: Memanfaatkan fitur monitoring bawaan Airflow UI dan (opsional) mengintegrasikan mekanisme notifikasi untuk kegagalan tugas.
* **Parameterized & Configurable**: DAGs dirancang agar dapat dikonfigurasi melalui variabel Airflow atau parameter eksternal untuk fleksibilitas.
* **Scalability**: Meskipun dijalankan pada infrastruktur lokal berbasis Docker, desain DAG mempertimbangkan prinsip-prinsip yang dapat diskalakan untuk lingkungan yang lebih besar.

### 🛠️ DAG Utama dan Fungsinya:

**`traffic_analysis_pipeline_dag.py`**:
* **Deskripsi**: Ini adalah DAG sentral yang mengorkestrasi keseluruhan pipeline data, mulai dari akuisisi hingga persiapan data untuk analisis dan pemodelan.
* **Jadwal Eksekusi**: Dikonfigurasi untuk berjalan secara periodik (misalnya, harian atau mingguan, tergantung pada frekuensi pembaruan data sumber atau kebutuhan analisis).
* **Tugas-tugas Utama (Operators) dalam DAG**:
    1.  **`start_pipeline` (DummyOperator)**: Titik awal DAG.
    2.  **`ingest_raw_data_task` (BashOperator/PythonOperator)**: Memicu skrip ingesti data (misalnya, `ingest_data_to_hdfs.sh`) untuk memuat data mentah ke HDFS Bronze Layer.
    3.  **`run_spark_bronze_to_silver_job_task` (SparkSubmitOperator/BashOperator)**: Menjalankan skrip PySpark `bronze_to_silver.py` untuk membersihkan dan mentransformasi data.
    4.  **`run_spark_silver_to_gold_job_task` (SparkSubmitOperator/BashOperator)**: Menjalankan skrip PySpark `silver_to_gold.py` untuk agregasi dan rekayasa fitur.
    5.  **(Opsional) `update_hive_metastore_task` (HiveOperator/BashOperator)**: Memperbarui metadata tabel Hive setelah data di Gold Layer diperbarui.
    6.  **(Opsional) `trigger_model_training_dag_task` (TriggerDagRunOperator)**: Memicu DAG lain yang khusus untuk proses training model Machine Learning.
    7.  **`data_quality_checks_task` (PythonOperator/BranchPythonOperator)**: (Opsional, praktik terbaik) Melakukan pengecekan kualitas data dasar pada output setiap tahap.
    8.  **`end_pipeline` (DummyOperator)**: Titik akhir DAG.
* **Penanganan Kegagalan**: Setiap tugas dikonfigurasi dengan jumlah *retry* yang sesuai dan interval *retry delay*. Notifikasi email dapat diaktifkan untuk kegagalan kritis.

**Manfaat Penggunaan Airflow**:
Dengan Apache Airflow, kami memastikan bahwa pipeline data yang kompleks dapat dijalankan secara **otomatis, terjadwal, dan termonitor dengan baik**. Ini menghilangkan kebutuhan akan intervensi manual yang rentan kesalahan, meningkatkan keandalan proses, dan menyediakan visibilitas penuh terhadap status setiap tahapan pemrosesan data. Kemampuan untuk melihat dependensi, log eksekusi, dan menjadwalkan ulang tugas secara mudah melalui UI Airflow adalah aset krusial dalam mengelola proyek Big Data yang dinamis.

Penggunaan Airflow dalam proyek ini mencerminkan **pendekatan rekayasa data yang matang dan modern**, menunjukkan kemampuan kami untuk tidak hanya mengembangkan skrip pemrosesan tetapi juga mengorkestrasikannya dalam sebuah sistem yang terintegrasi dan andal.