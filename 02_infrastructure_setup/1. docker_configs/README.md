## 📦 Blueprints Layanan: Konfigurasi Detail Docker untuk Setiap Komponen Ekosistem

Folder ini berisi direktori-direktori yang masing-masing didedikasikan untuk konfigurasi Docker dari satu layanan spesifik dalam arsitektur Big Data proyek ini. Setiap subfolder (misalnya, `hadoop/`, `spark/`, `hive/`) menyimpan:

1.  **`Dockerfile`**: Instruksi untuk membangun image Docker kustom untuk layanan tersebut. Ini mencakup:
    * Pemilihan *base image* yang sesuai (misalnya, image resmi Hadoop, Spark, atau image dasar Linux seperti Ubuntu/Alpine).
    * Instalasi dependensi perangkat lunak yang diperlukan.
    * Penyalinan file konfigurasi kustom dari direktori ini ke dalam image.
    * Pengaturan variabel lingkungan.
    * Definisi *entrypoint* atau *command default* untuk menjalankan layanan saat container dimulai.
    * Pengaturan user dan perizinan yang sesuai di dalam container.

2.  **File Konfigurasi Kustom**: File-file konfigurasi asli dari layanan yang telah dimodifikasi atau ditambahkan untuk kebutuhan proyek ini. Contoh:
    * Untuk Hadoop: `core-site.xml`, `hdfs-site.xml`, `mapred-site.xml`, `yarn-site.xml`.
    * Untuk Spark: `spark-defaults.conf`, `spark-env.sh`, `log4j.properties`.
    * Untuk Hive: `hive-site.xml`, `hive-env.sh`.
    * Untuk Airflow: `airflow.cfg`.
    * Untuk Superset: `superset_config.py`.

3.  **(Opsional) Skrip Pendukung**: Skrip kecil yang mungkin diperlukan oleh `Dockerfile` atau `entrypoint` untuk setup awal di dalam container (misalnya, memformat NameNode HDFS, menginisialisasi skema database Metastore Hive).

**Prinsip Desain Konfigurasi**:
* **Minimalis**: Hanya konfigurasi yang benar-benar diperlukan dan berbeda dari default yang disertakan, untuk menjaga kejelasan.
* **Parametrik**: Sebisa mungkin, nilai-nilai konfigurasi yang sering berubah (seperti nama host, port, path) diatur melalui variabel lingkungan yang didefinisikan dalam `docker-compose.yml` agar `Dockerfile` lebih generik.
* **Terstruktur**: File konfigurasi diorganisir dengan rapi di dalam subfolder layanan masing-masing.

Pendekatan ini memastikan bahwa setiap layanan dikonfigurasi secara optimal untuk berinteraksi dalam ekosistem Docker dan mendukung kebutuhan spesifik dari pipeline data analisis kemacetan. **Setiap konfigurasi telah diuji** untuk memastikan interoperabilitas dan stabilitas layanan.