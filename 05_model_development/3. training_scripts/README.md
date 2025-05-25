## 🚀 Pelatihan Model Presisi: Implementasi Random Forest dengan Spark MLlib

... (bagian filosofi dan tujuan skrip tetap sama) ...

### Skrip Utama: `train_random_forest_spark.py`

* **Pendekatan Implementasi**:
    * **Modularitas Data**: Skrip ini dirancang untuk memuat data yang fiturnya *sudah dipersiapkan* (biasanya output dari `prepare_features_for_modeling.py` yang disimpan dalam format Parquet di HDFS). Ini memisahkan concerns antara rekayasa fitur dan pelatihan model.
    * **Reproducibility**: Penggunaan `seed` pada `randomSplit` untuk pembagian data dan pada inisialisasi `RandomForestRegressor` memastikan bahwa hasil pelatihan dapat direproduksi jika dijalankan ulang dengan data dan parameter yang sama.
    * **Logging & Output**: Skrip menyertakan `print` statement untuk melacak progres utama dan mencetak metrik evaluasi dasar. Dalam implementasi produksi, logging yang lebih robust (misalnya, ke file atau sistem logging terpusat) akan digunakan.
    * **Manajemen Resource Spark**: Meskipun tidak secara eksplisit diatur dalam skrip Python (lebih sering di `spark-submit`), pemilihan parameter seperti `--driver-memory`, `--executor-memory`, dan `--num-executors` saat menjalankan `spark-submit` sangat krusial untuk performa pelatihan pada data besar. Skrip ini ditulis agar kompatibel dengan konfigurasi resource tersebut.

* **Alur Kerja Detail dalam Skrip (`train_random_forest_spark.py`)**:
    1.  **Inisialisasi SparkSession**: Mengkonfigurasi sesi Spark dengan nama aplikasi yang relevan.
    2.  **Definisi Path**: Menentukan path input untuk data fitur yang sudah diproses (dari HDFS) dan path output untuk model yang akan disimpan (di HDFS).
    3.  **Pemuatan Data Fitur**: Membaca data Parquet yang berisi kolom `features` (vektor fitur) dan `label` (target prediksi `avg_speed_kmh`).
    4.  **Pembagian Data**: Membagi dataset secara acak menjadi set pelatihan (misalnya, 80%) dan set pengujian (misalnya, 20%). Penggunaan `cache()` pada DataFrame hasil split dapat mempercepat akses berulang.
    5.  **Inisialisasi Model `RandomForestRegressor`**:
        * `featuresCol="features"`: Menunjuk ke kolom vektor fitur.
        * `labelCol="label"`: Menunjuk ke kolom target.
        * `numTrees`: Jumlah pohon keputusan yang akan dibangun. Nilai yang lebih tinggi umumnya meningkatkan performa tetapi juga waktu training.
        * `maxDepth`: Kedalaman maksimum setiap pohon. Membatasi ini membantu mencegah overfitting.
        * `featureSubsetStrategy`: Strategi pemilihan fitur pada setiap node split (misal, "auto", "sqrt").
        * `seed`: Untuk konsistensi hasil.
    6.  **Pelatihan Model**: Memanggil `rf_model = rf.fit(training_data)`. Tahap ini adalah inti dari pembelajaran mesin.
    7.  **(Opsional) Analisis Feature Importance**: Setelah model dilatih, `rf_model.featureImportances` dapat diakses untuk memahami kontribusi relatif dari setiap fitur. Ini penting untuk interpretasi dan iterasi model.
    8.  **Prediksi pada Data Uji**: Menggunakan model terlatih (`rf_model.transform(test_data)`) untuk menghasilkan prediksi pada data yang belum pernah dilihat.
    9.  **Evaluasi Kinerja**: Menggunakan `RegressionEvaluator` untuk menghitung metrik standar:
        * **RMSE (Root Mean Squared Error)**: Mengukur rata-rata magnitudo error prediksi dalam unit yang sama dengan target.
        * **MAE (Mean Absolute Error)**: Mirip RMSE, tetapi kurang sensitif terhadap outlier besar.
        * **R-squared (R2)**: Menunjukkan proporsi varians dalam variabel dependen yang dapat diprediksi dari variabel independen.
    10. **Penyimpanan Model**: Menyimpan objek model terlatih (`rf_model.write().overwrite().save(model_output_path)`) ke HDFS. Ini memungkinkan model untuk dimuat dan digunakan kembali nanti tanpa perlu melatih ulang.
    11. **Pembersihan Cache & Stop Spark**: Memanggil `unpersist()` pada DataFrame yang di-cache dan menghentikan sesi Spark.

**Pentingnya Eksperimen**:
Nilai parameter seperti `numTrees` dan `maxDepth` yang digunakan dalam skrip contoh (`train_random_forest_spark.py`) adalah titik awal. Dalam praktik nyata, proses **hyperparameter tuning** (misalnya, menggunakan `CrossValidator` dan `ParamGridBuilder` di Spark MLlib) sangat penting untuk menemukan kombinasi optimal yang memberikan performa terbaik pada data Anda. Hasil dari eksperimen tersebut akan menjadi dasar pemilihan parameter final.

Dokumentasi dan implementasi skrip pelatihan ini menunjukkan **pendekatan yang sistematis dan berbasis data** dalam membangun model prediktif, bukan sekadar "trial and error" tanpa arah.