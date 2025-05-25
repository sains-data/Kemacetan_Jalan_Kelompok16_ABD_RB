# 🧠 Laboratorium Prediktif: Dari Data Menjadi Kecerdasan Buatan untuk Prediksi Kemacetan Medan

Selamat datang di **pusat pengembangan model Machine Learning** untuk proyek "Implementasi Ekosistem Hadoop untuk Analisis Big Data Lalu Lintas Kota Medan". Folder ini adalah tempat di mana data yang telah terkurasi dari Gold Layer diubah menjadi model prediktif yang cerdas menggunakan algoritma **Random Forest** dengan **Apache Spark MLlib**. Kami mendokumentasikan setiap langkah krusial, mulai dari rekayasa fitur hingga evaluasi model, untuk memastikan transparansi, reproduktifitas, dan pemahaman mendalam terhadap proses pembangunan kecerdasan buatan ini.

## 🎯 Filosofi Pengembangan Model:

Pengembangan model kami didasarkan pada prinsip-prinsip berikut:
1.  **Relevansi Fitur**: Memilih dan merekayasa fitur yang paling signifikan dan informatif untuk memprediksi tingkat kemacetan secara akurat.
2.  **Validasi Rigorous**: Menerapkan teknik validasi silang (jika memungkinkan dalam skala besar) dan evaluasi yang ketat pada data uji terpisah untuk mendapatkan estimasi performa model yang objektif.
3.  **Interpretability (Sejauh Mungkin)**: Meskipun Random Forest bisa kompleks, kami berusaha memahami kontribusi fitur dan perilaku model.
4.  **Scalability**: Menggunakan Spark MLlib untuk memastikan bahwa proses pelatihan dan inferensi model dapat diskalakan untuk menangani volume data yang besar.
5.  **Reproducibility**: Menyimpan skrip, parameter, dan versi model untuk memastikan hasil dapat direproduksi.

## 📁 Struktur Subfolder dan Komponen Kunci:

* **`feature_engineering_scripts/`**:
    * **Deskripsi**: Direktori ini berisi skrip-skrip PySpark yang didedikasikan untuk **seni membentuk fitur (feature engineering)**. Proses ini krusial karena kualitas fitur secara langsung memengaruhi performa model. Skrip di sini akan mengambil data dari Gold Layer dan melakukan transformasi seperti:
        * Penanganan variabel kategorikal (misalnya, `StringIndexer` untuk `road_name`).
        * Pembuatan fitur baru (misalnya, fitur waktu seperti jam dalam sehari, hari dalam seminggu; fitur lag dari kecepatan).
        * Seleksi fitur (jika diperlukan).
        * Normalisasi atau scaling fitur numerik.
        * Penggabungan semua fitur terpilih menjadi satu kolom vektor fitur menggunakan `VectorAssembler`.
    * **Penekanan**: Setiap keputusan rekayasa fitur didasarkan pada pemahaman domain dan analisis data eksploratif, dengan tujuan memaksimalkan sinyal prediktif dan meminimalkan noise.

* **`training_scripts/`**:
    * **Deskripsi**: Ini adalah **ruang pelatihan model presisi**. Berisi skrip utama (`train_random_forest_spark.py`) yang mengimplementasikan proses pelatihan model Random Forest Regressor (karena kita memprediksi `avg_speed_kmh` yang bisa dikonversi ke tingkat kemacetan) menggunakan Spark MLlib. Skrip ini mencakup:
        * Pembagian data Gold Layer (yang sudah direkayasa fiturnya) menjadi set pelatihan dan set pengujian.
        * Inisialisasi model Random Forest dengan parameter yang telah ditentukan (atau dioptimalkan melalui hyperparameter tuning).
        * Pelatihan model menggunakan data pelatihan.
        * Penggunaan Spark ML Pipeline untuk mengorganisir tahapan *preprocessing* fitur dan pelatihan model secara sistematis.
    * **Penekanan**: Implementasi dilakukan dengan mengikuti praktik terbaik Spark MLlib, memastikan proses pelatihan yang efisien dan dapat diskalakan. Parameter model dipilih berdasarkan eksperimen awal atau studi literatur.

* **`trained_models/`**:
    * **Deskripsi**: Folder ini secara konseptual mewakili tempat **penyimpanan artefak kecerdasan**, yaitu model Machine Learning yang telah berhasil dilatih dan divalidasi. Dalam implementasi Big Data dengan Spark, model biasanya disimpan langsung di HDFS (atau sistem file terdistribusi lainnya) menggunakan mekanisme `save()` dari Spark ML.
    * **Isi**: Folder ini mungkin berisi file `README.md` kecil yang menjelaskan path HDFS tempat model disimpan, versi model, dan metadata penting lainnya (misalnya, fitur yang digunakan saat pelatihan, metrik performa utama).
    * **Penekanan**: Memastikan model tersimpan dengan baik adalah kunci untuk deployment dan inferensi di masa depan. Versi model juga penting untuk dilacak.

* **`evaluation_results/`**:
    * **Deskripsi**: Di sinilah **validasi kinerja model** didokumentasikan secara komprehensif. Setelah model dilatih, performanya diukur pada data uji yang tidak pernah dilihat sebelumnya.
    * **Isi**: Dapat berisi:
        * Skrip atau *notebook* yang menjalankan evaluasi.
        * File teks atau CSV yang berisi metrik evaluasi utama (misalnya, RMSE, MAE, R-squared untuk regresi kecepatan).
        * Visualisasi hasil evaluasi (misalnya, plot *actual vs. predicted*, plot residu).
        * (Jika mengklasifikasikan tingkat kemacetan secara langsung) *Confusion matrix*, metrik presisi, recall, F1-score.
    * **Penekanan**: Evaluasi yang jujur dan menyeluruh sangat penting untuk memahami kekuatan dan keterbatasan model. Hasil evaluasi ini menjadi dasar untuk iterasi model selanjutnya atau keputusan apakah model siap untuk digunakan.

**Proses yang Terstruktur dan Terukur**: Pengembangan model dalam proyek ini bukan sekadar menjalankan algoritma, melainkan sebuah proses ilmiah yang terstruktur. Mulai dari pemahaman data, rekayasa fitur yang cermat, pemilihan model yang tepat, pelatihan yang sistematis, hingga evaluasi yang objektif. Setiap langkah didokumentasikan untuk memastikan transparansi dan memberikan kepercayaan bahwa model prediksi kemacetan yang dihasilkan memiliki dasar yang kuat dan kinerja yang dapat dipertanggungjawabkan.