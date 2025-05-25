## 🏛️ Artefak Kecerdasan: Model Terlatih Siap Digunakan

Folder ini berfungsi sebagai penunjuk ke **model-model Machine Learning yang telah berhasil dilatih dan divalidasi** dalam proyek analisis kemacetan Medan. Mengingat sifat terdistribusi dan skala dari model yang dilatih dengan Apache Spark MLlib, artefak model aktual disimpan di **Hadoop Distributed File System (HDFS)**.

### Lokasi Penyimpanan Model di HDFS:

Model prediksi kemacetan utama (Random Forest) disimpan pada path berikut di HDFS:

* **Model Versi 1 (Contoh)**:
    * **Path HDFS**: `/user/hive/warehouse/kemacetan_medan/models/random_forest_congestion_v1`
    * **Algoritma**: Random Forest Regressor (dari Spark MLlib)
    * **Dilatih pada Tanggal**: [Tanggal Pelatihan Model, misal: 2025-05-24]
    * **Dataset Pelatihan**: Menggunakan data fitur yang diproses dari Gold Layer, mencakup periode [Periode Data].
    * **Fitur Utama yang Digunakan**: `road_name_index`, `jam`, `hari_minggu`, `vehicle_count`, `avg_rainfall_mm`, `avg_temperature_c`.
    * **Metrik Performa Kunci (pada data uji)**:
        * RMSE: [Nilai RMSE Anda, misal: 5.75 km/jam]
        * MAE: [Nilai MAE Anda, misal: 3.20 km/jam]
        * R2: [Nilai R2 Anda, misal: 0.78]
    * **Catatan**: Model ini dilatih untuk memprediksi `avg_speed_kmh`.

* **(Tambahkan entri untuk versi model lainnya jika ada)**

### Cara Memuat Model dari HDFS (Contoh PySpark):

Untuk menggunakan model yang tersimpan ini dalam aplikasi inferensi atau evaluasi lebih lanjut, Anda dapat memuatnya menggunakan Spark MLlib:

```python
from pyspark.ml.regression import RandomForestRegressionModel # atau PipelineModel jika pipeline lengkap disimpan
# from pyspark.ml import PipelineModel # Jika Anda menyimpan seluruh pipeline (termasuk feature transformers)

# Inisialisasi SparkSession
# spark = SparkSession.builder.appName("LoadTrainedModel").getOrCreate()

model_path_hdfs = "/user/hive/warehouse/kemacetan_medan/models/random_forest_congestion_v1"

# Memuat model Random Forest yang sudah dilatih
loaded_rf_model = RandomForestRegressionModel.load(model_path_hdfs)
# Jika Anda menyimpan PipelineModel:
# loaded_pipeline_model = PipelineModel.load(model_path_hdfs)

print(f"Model berhasil dimuat dari: {model_path_hdfs}")

# Model (loaded_rf_model atau loaded_pipeline_model) sekarang siap digunakan untuk .transform(data_baru)