# 📊 Mengungkap Cerita Data: Eksplorasi Mendalam Pola Lalu Lintas & Cuaca di Kota Medan

Selamat datang di **ruang investigasi data** proyek "Implementasi Ekosistem Hadoop untuk Analisis Big Data Lalu Lintas Kota Medan". Folder ini adalah tempat di mana kami melakukan **Analisis Data Eksploratif (EDA)** secara mendalam terhadap dataset trafik dan cuaca. EDA adalah langkah krusial yang memungkinkan kami untuk memahami karakteristik data, menemukan pola tersembunyi, mengidentifikasi anomali, menguji hipotesis awal, dan yang terpenting, **menggali insight yang akan memandu proses rekayasa fitur dan pemilihan model Machine Learning**.

## 🎯 Tujuan Utama EDA dalam Proyek Ini:

1.  **Pemahaman Data Komprehensif**: Mendapatkan pemahaman intuitif dan statistik mengenai distribusi, variabilitas, dan kualitas data trafik (kecepatan, volume, lokasi) serta data cuaca.
2.  **Identifikasi Pola dan Tren**: Menemukan pola temporal (jam sibuk, hari kerja vs. akhir pekan) dan spasial (ruas jalan rawan macet) terkait kemacetan lalu lintas.
3.  **Analisis Korelasi**: Menyelidiki hubungan antara berbagai variabel, khususnya dampak kondisi cuaca (hujan, suhu, jarak pandang) terhadap kecepatan kendaraan dan potensi kemacetan.
4.  **Deteksi Anomali dan Outlier**: Mengidentifikasi data yang tidak biasa atau berpotensi error yang mungkin memerlukan penanganan khusus sebelum pemodelan.
5.  **Dasar Rekayasa Fitur**: Memberikan wawasan yang kuat untuk pemilihan dan pembuatan fitur yang relevan dan prediktif untuk model Machine Learning.

## 📓 Struktur Notebook Eksplorasi:

Setiap Jupyter Notebook dalam folder ini dirancang untuk fokus pada aspek tertentu dari data, menggunakan **PySpark** untuk analisis pada data skala besar dan pustaka visualisasi Python (seperti **Matplotlib**, **Seaborn**, atau **Plotly**) untuk menyajikan temuan secara grafis.

* **`eda_traffic_patterns.ipynb`**:
    * **Fokus**: Membedah data trafik untuk mengungkap pola-pola pergerakan dan kepadatan kendaraan.
    * **Analisis Kunci**: Distribusi kecepatan kendaraan, identifikasi jam-jam sibuk, analisis kecepatan rata-rata per ruas jalan, pemetaan spasial titik-titik dengan kecepatan rendah.

* **`eda_weather_impact.ipynb`**:
    * **Fokus**: Menyelidiki bagaimana berbagai kondisi cuaca berkorelasi dengan dan memengaruhi dinamika lalu lintas.
    * **Analisis Kunci**: Korelasi antara curah hujan/suhu/jarak pandang dengan kecepatan rata-rata kendaraan, perbandingan pola lalu lintas pada hari cerah vs. hari hujan.

* **`feature_insights.ipynb`**:
    * **Fokus**: Menggali lebih dalam variabel-variabel yang berpotensi menjadi prediktor kuat untuk model kemacetan.
    * **Analisis Kunci**: Distribusi variabel kandidat fitur, analisis hubungan bivariate antara fitur potensial dengan target variabel (kecepatan rata-rata), identifikasi interaksi antar fitur.

**Pendekatan Analitik yang Teliti**: Setiap notebook menyajikan alur analisis yang logis: mulai dari pemuatan data (biasanya dari Silver atau Gold Layer HDFS), pembersihan data spesifik untuk EDA, analisis statistik deskriptif, visualisasi data yang kaya, hingga interpretasi temuan dan hipotesis awal. Kami menekankan pada **narasi berbasis data**, di mana setiap grafik dan statistik digunakan untuk menceritakan kisah yang terkandung dalam data lalu lintas Kota Medan.

Proses EDA yang terdokumentasi dengan baik ini adalah **fondasi intelektual** untuk keputusan desain model dan rekayasa fitur, memastikan bahwa pendekatan kami didasarkan pada bukti empiris dari data itu sendiri, bukan sekadar asumsi.