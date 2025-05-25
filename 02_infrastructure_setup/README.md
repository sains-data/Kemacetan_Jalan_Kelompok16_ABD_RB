# 🛠️ Fondasi Infrastruktur: Orkestrasi Lingkungan Big Data via Docker untuk Analisis Kemacetan Medan

Folder ini adalah **pusat kendali infrastruktur** untuk proyek "Implementasi Ekosistem Hadoop untuk Analisis Big Data Lalu Lintas Kota Medan". Di sini, kami merinci dan menyediakan semua konfigurasi yang diperlukan untuk membangun lingkungan Big Data yang *reproducible*, *scalable*, dan *isolated* menggunakan teknologi **Docker dan Docker Compose**.

## 🎯 Filosofi Desain Infrastruktur:

1.  **Reproducibility & Portability**: Memastikan bahwa seluruh lingkungan pengembangan dan pemrosesan data dapat dengan mudah direplikasi di berbagai mesin atau platform, menghilangkan masalah "works on my machine".
2.  **Isolation**: Setiap layanan (Hadoop, Spark, Hive, dll.) berjalan dalam container terisolasi, mencegah konflik dependensi dan memudahkan manajemen versi.
3.  **Modularity**: Desain modular memungkinkan penambahan, penghapusan, atau pembaruan komponen individual tanpa mengganggu keseluruhan sistem.
4.  **Ease of Deployment**: Dengan Docker Compose, seluruh stack teknologi dapat dijalankan dengan satu perintah, menyederhanakan proses setup yang kompleks.
5.  **Simulation of Production Environment**: Meskipun dijalankan secara lokal, arsitektur ini mensimulasikan cluster terdistribusi, memberikan pengalaman yang mendekati lingkungan produksi.

## 📁 Struktur Subfolder dan Komponen Kunci:

* **`docker_configs/`**:
    * **Deskripsi**: Direktori ini adalah jantung dari konfigurasi individual setiap layanan dalam ekosistem Big Data. Setiap subfolder di dalamnya (misalnya, `hadoop/`, `spark/`, `hive/`, `superset/`, `airflow/`) berisi `Dockerfile` khusus dan file konfigurasi terkait (`.xml`, `.conf`, `.properties`, skrip entrypoint) yang diperlukan untuk membangun dan menjalankan image Docker untuk layanan tersebut.
    * **Penekanan**: Perhatian khusus diberikan pada konfigurasi jaringan antar-container, manajemen volume untuk persistensi data (misalnya, data HDFS, metadata Hive), dan optimalisasi resource (CPU, memori) per layanan. Setiap Dockerfile dirancang untuk menciptakan lingkungan yang bersih dan efisien, hanya menyertakan dependensi yang benar-benar dibutuhkan.

* **`cluster_init_scripts/`**:
    * **Deskripsi**: Berisi skrip-skrip otomatisasi yang dijalankan setelah container-container utama aktif. Contoh utamanya adalah `init_hdfs_dirs.sh`, yang secara cerdas mempersiapkan struktur direktori awal di HDFS (Bronze, Silver, Gold, models) dan mengatur perizinan yang diperlukan. Skrip lain mungkin mencakup inisialisasi database untuk Hive Metastore atau Airflow.
    * **Penekanan**: Skrip ini dirancang untuk menjadi *idempotent* (dapat dijalankan berulang kali tanpa efek samping negatif), memastikan konsistensi setup awal dan mengurangi intervensi manual.

* **`docker-compose.yml`**:
    * **Deskripsi**: File ini adalah **orkestrator utama** yang mendefinisikan seluruh layanan, jaringan, volume, dan dependensi antar layanan. Dengan satu file ini, seluruh ekosistem Big Data dapat dihidupkan atau dimatikan secara terkoordinasi.
    * **Penekanan**: File `docker-compose.yml` dirancang dengan cermat untuk:
        * Mendefinisikan nama host yang konsisten untuk setiap layanan agar mudah dirujuk dalam konfigurasi dan skrip.
        * Mengatur dependensi layanan (misalnya, Spark worker baru dimulai setelah Spark master siap).
        * Memetakan port dari container ke host untuk akses UI web dan koneksi eksternal.
        * Mengelola volume data untuk memastikan persistensi data HDFS, log aplikasi, dan metadata penting lainnya meskipun container dihentikan atau dibuat ulang.
        * Mengkonfigurasi variabel lingkungan yang diperlukan untuk setiap layanan.

**Kredibilitas dan Keandalan**: Pendekatan infrastruktur berbasis Docker ini menunjukkan penerapan praktik DevOps modern dalam proyek data science. Dokumentasi yang detail dalam setiap `Dockerfile` dan komentar yang jelas dalam `docker-compose.yml` serta skrip inisialisasi memastikan bahwa setup infrastruktur ini tidak hanya berfungsi, tetapi juga **dapat dipahami, dimodifikasi, dan dipelihara dengan baik**. Setiap konfigurasi telah dipertimbangkan untuk mendukung alur kerja analisis data dari *end-to-end*, mulai dari ingesti hingga visualisasi.