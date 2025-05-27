## 🎯 Sampel Output Prediksi Kemacetan dari Model

Folder ini berisi sampel data output yang dihasilkan oleh model prediksi kemacetan Random Forest. Output ini merepresentasikan jenis informasi yang dapat diekspor atau disajikan kepada pengguna setelah proses inferensi model pada data baru atau data historis untuk periode tertentu.

### Format dan Isi Sampel Output:

Kami menyajikan sampel output dalam format CSV untuk kemudahan inspeksi. Dalam implementasi nyata, output ini bisa disimpan dalam tabel database, file Parquet/ORC di HDFS, atau disajikan melalui API.

**File Contoh: `sample_hourly_congestion_predictions.csv`**

* **Deskripsi File**: File CSV ini berisi prediksi tingkat kemacetan (atau kecepatan rata-rata yang diprediksi) untuk berbagai ruas jalan pada jam-jam tertentu.
* **Kolom-kolom Utama (Contoh)**:
    * `prediction_timestamp`: Waktu untuk kapan prediksi ini berlaku (misalnya, `2025-05-26 08:00:00`).
    * `road_name`: Nama ruas jalan yang diprediksi.
    * `latitude_segment_center`: (Opsional) Latitude pusat segmen jalan.
    * `longitude_segment_center`: (Opsional) Longitude pusat segmen jalan.
    * `predicted_avg_speed_kmh`: Kecepatan rata-rata kendaraan yang diprediksi oleh model untuk ruas jalan dan waktu tersebut.
    * `predicted_congestion_level`: (Jika Anda mengkategorikan kecepatan menjadi level kemacetan) Tingkat kemacetan yang diprediksi (misalnya, "Lancar", "Cukup Padat", "Padat", "Sangat Padat"). Ini bisa diturunkan dari `predicted_avg_speed_kmh` berdasarkan *threshold* tertentu.
        * *Contoh Threshold:*
            * *Lancar: > 40 km/jam*
            * *Cukup Padat: 25 - 40 km/jam*
            * *Padat: 15 - 25 km/jam*
            * *Sangat Padat: < 15 km/jam*
    * `confidence_score` / `prediction_interval_lower` / `prediction_interval_upper`: (Pengembangan Lanjutan) Metrik kepercayaan atau interval prediksi jika model mendukungnya. Untuk Random Forest standar, ini mungkin tidak langsung tersedia tetapi bisa diestimasi.

* **Contoh Isi Data dalam `sample_hourly_congestion_predictions.csv`**:
    ```csv
    prediction_timestamp,road_name,predicted_avg_speed_kmh,predicted_congestion_level
    2025-05-26 07:00:00,Jalan Gatot Subroto,18.5,Padat
    2025-05-26 07:00:00,Jalan Sisingamangaraja,22.1,Padat
    2025-05-26 07:00:00,Jalan Jenderal Sudirman,30.5,Cukup Padat
    2025-05-26 08:00:00,Jalan Gatot Subroto,15.2,Sangat Padat
    2025-05-26 08:00:00,Jalan Sisingamangaraja,19.8,Padat
    2025-05-26 08:00:00,Jalan Jenderal Sudirman,25.6,Cukup Padat
    2025-05-26 09:00:00,Jalan Gatot Subroto,23.0,Padat
    2025-05-26 09:00:00,Jalan Sisingamangaraja,28.7,Cukup Padat
    2025-05-26 09:00:00,Jalan Jenderal Sudirman,35.1,Lancar
    ...
    ```

### Cara Menghasilkan Output Ini (Konseptual):

1.  **Muat Model Terlatih**: Model Random Forest yang disimpan di HDFS (`/user/hive/warehouse/kemacetan_medan/models/random_forest_congestion_v1`) dimuat menggunakan Spark.
2.  **Siapkan Data Input untuk Inferensi**: Data baru (misalnya, data cuaca terbaru dan data historis lalu lintas hingga jam sebelumnya) disiapkan dengan fitur yang sama seperti saat pelatihan model.
3.  **Lakukan Prediksi**: Model digunakan untuk melakukan `.transform()` pada data input baru untuk menghasilkan kolom prediksi (misalnya, `predicted_avg_speed_kmh`).
4.  **(Opsional) Kategorisasi Tingkat Kemacetan**: Terapkan logika bisnis atau *threshold* untuk mengubah prediksi kecepatan menjadi kategori tingkat kemacetan.
5.  **Simpan/Ekspor Hasil**: Output prediksi disimpan ke format yang diinginkan (misalnya, CSV untuk sampel ini, atau tabel di database/HDFS untuk penggunaan operasional).

**Pemanfaatan Output Prediksi**:
* **Informasi bagi Pengguna Jalan**: Dapat diintegrasikan ke dalam aplikasi peta atau layanan informasi lalu lintas untuk membantu pengguna memilih rute terbaik.
* **Perencanaan oleh Dinas Perhubungan**: Membantu dalam mengidentifikasi waktu dan lokasi rawan macet untuk penempatan petugas atau rekayasa lalu lintas.
* **Analisis Tren Jangka Panjang**: Mengumpulkan output prediksi dari waktu ke waktu dapat digunakan untuk menganalisis tren kemacetan dan efektivitas intervensi.

Contoh output ini menunjukkan bagaimana hasil komputasi kompleks dari model Machine Learning dapat diterjemahkan menjadi informasi yang konkret dan berpotensi actionable.
