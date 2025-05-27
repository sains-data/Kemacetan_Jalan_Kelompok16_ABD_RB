# 📂 Tahap Akuisisi Data Proyek Analisis Kemacetan Medan

Folder ini merupakan **gerbang utama data** untuk proyek "Implementasi Ekosistem Hadoop untuk Analisis Big Data Lalu Lintas Kota Medan". Di sini, kami mendokumentasikan dan menyimpan semua aset yang berkaitan dengan perolehan data mentah yang menjadi fondasi analisis prediktif kemacetan.

## 🎯 Tujuan Folder Ini:

1.  **Transparansi Sumber Data**: Menyediakan informasi yang jelas mengenai asal-usul, format, dan karakteristik data mentah yang digunakan.
2.  **Reproducibility**: Memastikan bahwa proses akuisisi data dapat dipahami dan, jika memungkinkan, direplikasi.
3.  **Penyimpanan Terpusat**: Menjadi lokasi penyimpanan standar untuk dataset mentah sebelum diproses lebih lanjut dalam pipeline Big Data.
4.  **Dokumentasi Skrip Ingesti**: Menyimpan dan menjelaskan skrip yang digunakan untuk memindahkan data mentah ke dalam sistem penyimpanan awal (misalnya, HDFS Bronze Layer).

## 📁 Struktur Subfolder:

* **`raw_datasets/`**: Berisi file dataset mentah yang digunakan dalam proyek ini. Setiap dataset disertai dengan deskripsi singkat mengenai konten dan strukturnya.
    * `simulasi_trafik_medan.csv`: Data simulasi pergerakan kendaraan (taksi) di Kota Medan.
    * `cuaca_medan_2013-07-01.csv`: Data simulasi kondisi cuaca di Kota Medan.
* **`ingestion_scripts/`**: Berisi skrip-skrip yang dirancang untuk proses ingesti data, yaitu memuat data dari `raw_datasets/` atau sumber eksternal lainnya ke dalam HDFS Bronze Layer.
