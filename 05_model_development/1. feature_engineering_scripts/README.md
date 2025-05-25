## 🎨 Seni Membentuk Fitur: Transformasi Data untuk Performa Model Optimal

Direktori ini menyimpan skrip-skrip PySpark yang didedikasikan untuk proses **rekayasa fitur (feature engineering)**. Tahap ini adalah salah satu pilar terpenting dalam membangun model Machine Learning yang efektif, karena kualitas dan relevansi fitur secara langsung menentukan kemampuan model untuk belajar dan membuat prediksi yang akurat.

### Skrip Utama: `prepare_features_for_modeling.py`

* **Tujuan Skrip**:
    1.  Memuat data agregat dari HDFS Gold Layer (output dari `silver_to_gold.py`).
    2.  Melakukan transformasi dan pembuatan fitur yang diperlukan sebelum data dimasukkan ke dalam model Random Forest.
    3.  Menghasilkan DataFrame Spark yang berisi kolom fitur vektor dan kolom label (target prediksi).

* **Langkah-langkah Kunci dalam Skrip**:
    1.  **Pemuatan Data**: Membaca dataset agregat dari Gold Layer (format ORC atau Parquet).
    2.  **Penanganan Nilai Hilang (Final Check)**: Memastikan tidak ada nilai null pada kolom-kolom yang akan digunakan sebagai fitur atau label, atau menerapkan strategi imputasi terakhir.
    3.  **Encoding Fitur Kategorikal**:
        * Menggunakan `StringIndexer` untuk mengubah kolom string (misalnya, `road_name`) menjadi representasi numerik (indeks). Disarankan untuk menangani nilai yang tidak dikenal (`handleInvalid="keep"` atau `"skip"`).
        * (Opsional) Menggunakan `OneHotEncoder` setelah `StringIndexer` jika algoritma mendapat manfaat dari representasi one-hot.
    4.  **Pembuatan Fitur Baru (Contoh)**:
        * Ekstraksi fitur berbasis waktu dari `timestamp` (misalnya, `hour_of_day`, `day_of_week`, `is_weekend`).
        * (Opsional) Pembuatan fitur *lag* (misalnya, `avg_speed_kmh_prev_hour` di segmen jalan yang sama).
        * (Opsional) Pembuatan fitur interaksi antar variabel.
    5.  **Seleksi Fitur**: Mengidentifikasi dan memilih subset fitur yang paling relevan dan informatif. Kolom yang tidak digunakan akan di-drop.
    6.  **Assembly Fitur**: Menggunakan `VectorAssembler` untuk menggabungkan semua kolom fitur terpilih (baik numerik maupun hasil encoding kategorikal) ke dalam satu kolom vektor tunggal (biasanya bernama `features`). Ini adalah format input standar untuk algoritma di Spark MLlib.
    7.  **Persiapan Kolom Label**: Memastikan kolom target prediksi (misalnya, `avg_speed_kmh` atau `congestion_level` yang sudah dikategorikan) siap digunakan dan memiliki nama yang sesuai (biasanya `label`).
    8.  **Penyimpanan Output (Opsional)**: DataFrame dengan fitur dan label yang sudah diproses dapat disimpan kembali ke HDFS atau langsung digunakan oleh skrip pelatihan.

* **Struktur Kode (Konseptual)**:
    ```python
    # Inisialisasi SparkSession
    # Definisi path input (Gold Layer) dan output (opsional)
    # Baca data Gold

    # Lakukan StringIndexing untuk road_name
    # Lakukan ekstraksi fitur waktu

    # Definisikan kolom-kolom fitur numerik dan kategorikal yang sudah di-index
    # Gunakan VectorAssembler

    # Pilih kolom fitur vektor dan kolom label

    # (Opsional) Tulis DataFrame yang sudah siap ke HDFS
    # Spark stop
    ```

Proses rekayasa fitur ini adalah **kombinasi antara pemahaman domain lalu lintas, analisis data eksploratif, dan teknik Machine Learning**. Skrip ini memastikan bahwa data yang "dilihat" oleh model adalah representasi terbaik dari masalah yang ingin dipecahkan, sehingga memaksimalkan potensi prediktif model.