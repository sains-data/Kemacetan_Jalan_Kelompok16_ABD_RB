## 🚀 Skrip Inisialisasi Cerdas: Otomatisasi Setup Awal Cluster & Layanan

Folder ini menyimpan skrip-skrip yang dirancang untuk melakukan **inisialisasi dan konfigurasi pasca-deployment container**. Tujuannya adalah untuk mengotomatiskan tugas-tugas setup awal yang diperlukan agar layanan-layanan dalam ekosistem Big Data siap digunakan.

### Skrip Utama: `init_hdfs_dirs.sh`

* **Fungsi**: Skrip ini bertanggung jawab untuk membuat struktur direktori fundamental di HDFS yang akan digunakan oleh seluruh pipeline data, meliputi:
    * Direktori untuk Bronze Layer (penyimpanan data mentah).
    * Direktori untuk Silver Layer (penyimpanan data yang telah dibersihkan dan ditransformasi).
    * Direktori untuk Gold Layer (penyimpanan data agregat untuk analisis dan laporan).
    * Direktori untuk penyimpanan model Machine Learning yang telah dilatih.
    * Pengaturan perizinan (permissions) yang sesuai pada direktori tersebut agar dapat diakses oleh user/layanan yang relevan (misalnya, user `hive`, `spark`).
* **Eksekusi**: Skrip ini biasanya dijalankan secara otomatis melalui `entrypoint` container NameNode HDFS atau dieksekusi secara manual sekali setelah semua layanan Hadoop berjalan stabil.
* **Idempotensi**: Dirancang agar aman untuk dijalankan berulang kali. Jika direktori sudah ada, skrip tidak akan gagal atau membuat duplikat.

### Skrip Lain (Contoh Potensial):

* `init_hive_metastore.sh`: Jika menggunakan database eksternal untuk Hive Metastore (seperti PostgreSQL atau MySQL) yang perlu diinisialisasi skemanya saat pertama kali dijalankan.
* `init_airflow_db.sh`: Skrip untuk inisialisasi database backend Airflow.

**Manfaat**:
Penggunaan skrip inisialisasi ini memastikan bahwa **lingkungan HDFS dan layanan lain terkonfigurasi secara konsisten** setiap kali infrastruktur dijalankan. Ini mengurangi risiko kesalahan manual dan mempercepat proses penyiapan lingkungan untuk pengembangan atau analisis. Setiap skrip didokumentasikan dengan baik mengenai tujuannya dan cara kerjanya.