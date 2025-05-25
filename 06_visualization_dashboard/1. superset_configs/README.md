## ⚙️ Konfigurasi & Aset Apache Superset

Folder ini berisi aset-aset yang berkaitan dengan konfigurasi dan ekspor dari *dashboard* serta *chart* yang telah dikembangkan di Apache Superset untuk proyek analisis kemacetan Medan. Tujuannya adalah untuk memfasilitasi proses *backup*, restorasi, dan potensi replikasi *dashboard* di *instance* Superset yang berbeda.

### Isi Direktori:

1.  **`export_dashboard_kemacetan_medan.zip` (Contoh Nama File)**
    * **Deskripsi**: Ini adalah file arsip (`.zip` atau format lain yang didukung Superset untuk ekspor) yang berisi definisi dari *dashboard* utama "Prediksi Kemacetan Medan" beserta semua *chart*, *dataset*, dan dependensi terkait yang ada di dalamnya.
    * **Cara Menggunakan**: File ini dapat diimpor kembali ke Apache Superset melalui fitur "Import Dashboards".
    * **Catatan**: Pastikan koneksi database ke Hive (dengan nama yang sama seperti saat ekspor) sudah ada di *instance* Superset target sebelum melakukan impor.

2.  **`catatan_koneksi_database_hive.txt` (Contoh Nama File)**
    * **Deskripsi**: File teks yang berisi detail konfigurasi yang digunakan untuk menghubungkan Superset ke Apache Hive. Ini penting untuk memastikan koneksi yang benar saat mencoba mereplikasi *dashboard*.
    * **Isi Contoh**:
        ```
        Nama Koneksi Database di Superset: Hive Cluster Medan Traffic
        SQLAlchemy URI: hive://<nama_container_hiveserver2_dari_jaringan_docker_atau_hostnya>:10000/db_kemacetan_medan
        (Ganti <nama_container_hiveserver2...> dan db_kemacetan_medan sesuai konfigurasi Anda)

        Opsi Tambahan (jika ada):
        - Engine Parameters: {"connect_args": {"auth": "NOSASL"}} (tergantung konfigurasi Hive Anda)
        - Security: (kosong jika tidak ada impersonation)
        - Advanced: (pengaturan spesifik lainnya)
        ```

3.  **`daftar_dataset_superset.txt` (Contoh Nama File)**
    * **Deskripsi**: Daftar dataset virtual atau fisik yang dibuat di Superset yang digunakan oleh *chart* dan *dashboard*. Mencakup informasi sumber tabel Hive.
    * **Isi Contoh**:
        ```
        1. Dataset: Agregat Kemacetan Harian
           - Sumber Tabel Hive: db_kemacetan_medan.fakta_agregat_kemacetan
           - Kolom Utama Digunakan: road_name, jam, hari_minggu, avg_speed_kmh, vehicle_count, avg_rainfall_mm, prediksi_kecepatan
           - Metrik Kustom Dibuat di Superset: (jika ada, sebutkan)

        2. Dataset: Prediksi Kemacetan Real-time (jika ada)
           - Sumber Tabel Hive: ...
        ```

4.  **(Opsional) `queries_penting_charts.sql`**
    * **Deskripsi**: Kumpulan query SQL (HiveQL) yang digunakan sebagai dasar untuk beberapa *chart* kustom atau kompleks di Superset, jika tidak langsung menggunakan fitur *explore* Superset.
    * **Isi Contoh**:
        ```sql
        -- Query untuk Chart: Top 10 Ruas Jalan Terpadat Berdasarkan Jumlah Kendaraan Rata-rata Harian
        SELECT
            road_name,
            AVG(vehicle_count) as avg_daily_vehicle_count
        FROM db_kemacetan_medan.fakta_agregat_kemacetan
        GROUP BY road_name
        ORDER BY avg_daily_vehicle_count DESC
        LIMIT 10;

        -- Query untuk Chart: Kecepatan Rata-rata vs Curah Hujan
        SELECT
            CASE
                WHEN avg_rainfall_mm = 0 THEN 'Tidak Hujan'
                WHEN avg_rainfall_mm > 0 AND avg_rainfall_mm <= 5 THEN 'Hujan Ringan'
                ELSE 'Hujan Sedang/Lebat'
            END as kategori_hujan,
            AVG(avg_speed_kmh) as rata_rata_kecepatan
        FROM db_kemacetan_medan.fakta_agregat_kemacetan
        GROUP BY 1;
        ```

**Penting**: Kemampuan untuk mengekspor dan mengimpor konfigurasi secara penuh dapat bervariasi tergantung pada versi Apache Superset yang digunakan dan bagaimana ia di-deploy. File-file di sini bertujuan untuk menangkap sebanyak mungkin informasi konfigurasi agar proses restorasi atau replikasi menjadi lebih mudah.