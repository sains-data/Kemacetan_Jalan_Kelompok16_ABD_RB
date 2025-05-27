# 🛠️ Fondasi Infrastruktur: Orkestrasi Ekosistem Big Data Analisis Kemacetan Medan dengan Docker

Selamat datang di **pusat kendali infrastruktur** proyek kami! Di sini, kami merinci konfigurasi untuk membangun lingkungan Big Data yang *reproducible*, *scalable*, dan *isolated* menggunakan **Docker dan Docker Compose**.

## 🎯 Filosofi Desain Infrastruktur:

1.  🌐 **Reproducibility & Portability**: Lingkungan mudah direplikasi di berbagai platform.
2.  🛡️ **Isolation**: Setiap layanan (Hadoop, Spark, Hive) berjalan terisolasi dalam container.
3.  🧱 **Modularity**: Komponen individual mudah ditambah, dihapus, atau diperbarui.
4.  🚀 **Ease of Deployment**: Seluruh stack teknologi dijalankan dengan satu perintah Docker Compose.
5.  🌍 **Simulation of Production**: Arsitektur lokal mensimulasikan cluster terdistribusi.

## 📁 Komponen Kunci Infrastruktur:

* **`docker_configs/`**: 📜 Berisi `Dockerfile` kustom dan file konfigurasi spesifik untuk setiap layanan (Hadoop, Spark, Hive, Superset, Airflow), memastikan jaringan, volume, dan resource optimal.
* **`cluster_init_scripts/`**: 🪄 Skrip otomatisasi (seperti `init_hdfs_dirs.sh`) untuk setup awal HDFS (Bronze, Silver, Gold, models) dan perizinan, dirancang agar *idempotent*.
* **`docker-compose.yml`**: 🎼 Orkestrator utama yang mendefinisikan seluruh layanan, jaringan, volume, dan dependensi, memungkinkan seluruh ekosistem dihidupkan atau dimatikan secara terkoordinasi.

**Kredibilitas dan Keandalan**: Pendekatan berbasis Docker ini menerapkan praktik DevOps modern. Dokumentasi detail dan konfigurasi yang cermat memastikan infrastruktur ini berfungsi, mudah dipahami, dimodifikasi, dan dipelihara, mendukung alur kerja analisis data *end-to-end*.
