# 📈 Jendela Insight: Dashboard Interaktif Prediksi Kemacetan Lalu Lintas Kota Medan dengan Apache Superset

Selamat datang di **pusat visualisasi dan presentasi hasil akhir** proyek "Implementasi Ekosistem Hadoop untuk Analisis Big Data Lalu Lintas Kota Medan". Folder ini didedikasikan untuk mendokumentasikan **Dashboard Interaktif** yang telah kami kembangkan menggunakan **Apache Superset**. Dashboard ini berfungsi sebagai antarmuka utama bagi pengguna untuk menjelajahi data, memahami pola kemacetan, dan melihat hasil prediksi model secara intuitif dan menarik.

## 🎯 Tujuan Dashboard:

1.  **Demokratisasi Data**: Menyajikan insight kompleks dari analisis Big Data dalam format yang mudah diakses dan dipahami oleh berbagai pemangku kepentingan, termasuk perencana kota, Dinas Perhubungan, peneliti, hingga masyarakat umum.
2.  **Monitoring Kondisi Lalu Lintas**: Memberikan gambaran visual mengenai pola kemacetan historis dan (jika sistem dikembangkan lebih lanjut) *near real-time*.
3.  **Visualisasi Hasil Prediksi**: Menampilkan prediksi tingkat kemacetan yang dihasilkan oleh model Machine Learning (Random Forest) untuk berbagai ruas jalan dan rentang waktu.
4.  **Dukungan Pengambilan Keputusan**: Menyediakan alat bantu visual bagi pengambil kebijakan untuk merencanakan intervensi lalu lintas atau strategi mitigasi kemacetan berbasis data.
5.  **Platform Eksplorasi Interaktif**: Memungkinkan pengguna untuk memfilter, mengurutkan, dan menjelajahi data sesuai dengan kebutuhan spesifik mereka.

## 🛠️ Teknologi dan Pendekatan:

* **Platform Visualisasi**: **Apache Superset** dipilih karena kemampuannya yang *open-source*, skalabilitas, kemudahan integrasi dengan berbagai sumber data (termasuk Apache Hive yang digunakan dalam proyek ini), dan kekayaan pilihan *chart* serta fitur pembuatan dashboard.
* **Sumber Data Dashboard**: Data yang divisualisasikan bersumber langsung dari **Gold Layer** dalam arsitektur data lake kami (disajikan melalui tabel Hive), memastikan bahwa informasi yang ditampilkan adalah data yang telah terkurasi, diagregasi, dan siap untuk analisis.
* **Desain User-Centric**: Dashboard dirancang dengan mempertimbangkan kebutuhan pengguna akhir, mengedepankan kejelasan informasi, kemudahan navigasi, dan estetika visual yang menarik.

## 📁 Struktur Subfolder dan Konten Kunci:

* **`superset_configs/`**:
    * **Deskripsi**: Direktori ini bertujuan untuk menyimpan **aset konfigurasi terkait Apache Superset** yang dapat diekspor dan diimpor, guna memudahkan replikasi dashboard di lingkungan Superset lain atau sebagai *backup*.
    * **Isi Potensial**:
        * `export_dashboard_kemacetan_medan.zip` (atau `.json`): File hasil ekspor dashboard utama dari Superset. (Superset memiliki fitur untuk ekspor/impor dashboard dan chart).
        * `koneksi_database_hive.json` (konseptual): Catatan atau ekspor konfigurasi koneksi database ke Hive.
        * `custom_css_superset.css` (jika ada): File CSS kustom yang mungkin diterapkan pada Superset untuk branding atau penyesuaian tampilan.
        * `catatan_pembuatan_chart.md`: Dokumen singkat yang menjelaskan bagaimana chart-chart utama dibuat, termasuk query SQL atau konfigurasi spesifik di Superset.
    * **Penekanan**: Menyediakan konfigurasi ini menunjukkan profesionalisme dan upaya untuk membuat hasil kerja dapat direplikasi dan dipelihara.

* **`dashboard_screenshots/`**:
    * **Deskripsi**: Ini adalah **galeri visual** yang menampilkan fitur-fitur utama dan *insight* penting dari dashboard interaktif kami. Screenshot ini memberikan gambaran cepat mengenai kemampuan dan tampilan dashboard bagi mereka yang mungkin tidak memiliki akses langsung ke lingkungan Superset.
    * **Isi Potensial (Daftar Screenshot dengan Nama Deskriptif)**:
        1.  `01_halaman_utama_dashboard.png`: Tampilan keseluruhan dashboard utama.
        2.  `02_peta_panas_kemacetan_medan.png`: Visualisasi geografis tingkat kemacetan (misalnya, menggunakan latitude/longitude atau nama jalan).
        3.  `03_tren_kecepatan_harian.png`: Grafik garis yang menunjukkan fluktuasi kecepatan rata-rata per jam dalam sehari.
        4.  `04_perbandingan_hari_kerja_vs_akhir_pekan.png`: Grafik perbandingan pola lalu lintas.
        5.  `05_distribusi_tingkat_kemacetan_prediksi.png`: Pie chart atau bar chart yang menunjukkan proporsi prediksi tingkat kemacetan (misalnya, Lancar, Sedang, Padat).
        6.  `06_detail_ruas_jalan_tertentu.png`: Contoh tampilan saat memfilter atau *drill-down* ke ruas jalan spesifik.
        7.  `07_dampak_cuaca_terhadap_kecepatan.png`: Grafik yang mengilustrasikan korelasi antara cuaca (misalnya, curah hujan) dan kecepatan.
        8.  `08_filter_interaktif_dashboard.png`: Menunjukkan contoh penggunaan filter tanggal, waktu, atau lokasi.
    * **Penekanan**: Setiap screenshot harus berkualitas tinggi, jelas, dan diberi *caption* singkat yang menjelaskan apa yang ditampilkan dan *insight* apa yang bisa didapatkan. **Ini adalah etalase visual proyek Anda.**

**Menyampaikan Cerita Melalui Visualisasi**:
Dashboard yang dikembangkan bukan hanya sekumpulan grafik, melainkan sebuah **narasi visual yang dipandu oleh data**. Kami telah berupaya untuk memilih jenis visualisasi yang paling tepat untuk setiap jenis informasi, menggunakan warna secara efektif, dan menyusun tata letak yang intuitif. Tujuannya adalah agar pengguna dapat dengan cepat menangkap *insight* penting, menjawab pertanyaan analitik, dan pada akhirnya, membuat keputusan yang lebih baik berdasarkan bukti data yang solid dan mudah diakses.

Kombinasi antara konfigurasi yang dapat diekspor dan galeri screenshot yang representatif menunjukkan bahwa aspek visualisasi dan komunikasi hasil proyek ini telah ditangani dengan **serius, profesional, dan berorientasi pada pengguna akhir.**