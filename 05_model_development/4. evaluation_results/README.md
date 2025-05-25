## 📊 Validasi Kinerja: Analisis Komprehensif Akurasi dan Keandalan Model

... (bagian deskripsi umum tetap sama) ...

### Artefak Evaluasi Rinci:

Berikut adalah rincian dari file-file hasil evaluasi yang dapat Anda temukan di direktori ini, yang secara kolektif memberikan gambaran utuh tentang performa model prediksi kemacetan (`random_forest_congestion_v1`):

1.  **`model_v1_performance_metrics.txt`**:
    * **Tujuan**: Menyajikan ringkasan kuantitatif utama dari performa model secara ringkas dan mudah dibaca.
    * **Isi Kunci**:
        * **Metrik Utama**: Nilai RMSE, MAE, dan R2 yang dihitung pada *test set*.
        * **Konteks Pelatihan**: Tanggal evaluasi, versi model, jumlah data training/test, dan parameter kunci model (misalnya, `numTrees`, `maxDepth`) untuk memberikan konteks pada metrik.
        * **Interpretasi Singkat**: Penjelasan singkat tentang arti metrik (misalnya, "RMSE sebesar X km/jam menunjukkan error prediksi rata-rata sebesar X km/jam").
    * **File Contoh `model_v1_performance_metrics.txt`**:
        ```
        ====================================================
        MODEL EVALUATION REPORT: random_forest_congestion_v1
        ====================================================
        Date of Evaluation         : 2025-05-25
        Target Variable            : avg_speed_kmh (Kecepatan Rata-rata Kendaraan)
        Training Data Size         : [Jumlah Baris Training Data]
        Test Data Size             : [Jumlah Baris Test Data]

        Model Parameters:
        -----------------
        Algorithm                  : RandomForestRegressor (Spark MLlib)
        Number of Trees (numTrees) : 100
        Max Depth (maxDepth)       : 10
        Features Col               : features
        Label Col                  : label
        Seed                       : 54321

        Performance Metrics on Test Data:
        ---------------------------------
        Root Mean Squared Error (RMSE) : 5.7531 km/h
        Mean Absolute Error (MAE)    : 3.2015 km/h
        R-squared (R2)               : 0.7822

        Interpretasi Singkat:
        ---------------------
        - RMSE menunjukkan bahwa rata-rata, prediksi kecepatan model meleset sekitar 5.75 km/jam dari kecepatan aktual.
        - R2 sebesar 0.7822 mengindikasikan bahwa sekitar 78.22% variabilitas dalam kecepatan rata-rata kendaraan
          dapat dijelaskan oleh fitur-fitur yang digunakan dalam model pada data uji.

        Catatan Tambahan:
        -----------------
        - Evaluasi dilakukan pada data uji yang tidak digunakan selama proses pelatihan.
        - Hasil ini merupakan baseline; iterasi lebih lanjut dengan hyperparameter tuning atau
          rekayasa fitur tambahan dapat meningkatkan performa.
        ```

2.  **`model_v1_predictions_vs_actuals_sample.csv`**:
    * **Tujuan**: Memberikan contoh konkret dari prediksi model dibandingkan dengan nilai aktual untuk inspeksi manual dan pemahaman kualitatif.
    * **Isi Kunci**: Kolom untuk `actual_label` (misalnya, `actual_avg_speed_kmh`), `predicted_label` (misalnya, `predicted_avg_speed_kmh`), dan beberapa fitur kunci yang digunakan untuk prediksi tersebut agar bisa dilihat konteksnya.
    * **File Contoh `model_v1_predictions_vs_actuals_sample.csv`**:
        ```csv
        actual_avg_speed_kmh,predicted_avg_speed_kmh,prediction_error,road_name_index,jam,hari_minggu,vehicle_count,avg_rainfall_mm
        35.5,33.2,2.3,10,8,2,50,0.0
        22.1,25.8,-3.7,5,17,6,120,5.5
        50.2,48.9,1.3,23,14,3,25,0.0
        15.0,18.5,-3.5,10,18,2,200,2.1
        45.8,43.1,2.7,3,11,7,30,0.0
        ```
        *(Tambahkan kolom `prediction_error = actual - predicted` bisa sangat membantu)*

3.  **`notebooks_for_evaluation/` (Subfolder Opsional)**:
    * **Tujuan**: Menyimpan Jupyter Notebook yang digunakan untuk melakukan analisis evaluasi yang lebih mendalam dan menghasilkan visualisasi.
    * **Isi Potensial**:
        * **`plot_feature_importances.ipynb`**: Notebook untuk memuat model terlatih dan menghasilkan plot *feature importance*.
            * **Kode Kunci (PySpark di Notebook)**:
              ```python
              from pyspark.ml.regression import RandomForestRegressionModel
              import matplotlib.pyplot as plt
              import pandas as pd

              # Asumsi SparkSession 'spark' sudah ada
              model_path = "/user/hive/warehouse/kemacetan_medan/models/random_forest_congestion_v1"
              rf_model = RandomForestRegressionModel.load(model_path)

              # Anda perlu daftar nama fitur asli sesuai urutan di VectorAssembler
              # Misal dari skrip feature engineering:
              # feature_columns = ["road_name_index", "jam", "hari_minggu", "vehicle_count", "avg_rainfall_mm", "avg_temperature_c"]
              
              importances = rf_model.featureImportances
              feature_importance_df = pd.DataFrame(list(zip(feature_columns, importances.toArray())),
                                                 columns=['feature', 'importance']).sort_values('importance', ascending=False)
              
              plt.figure(figsize=(10, 6))
              plt.barh(feature_importance_df['feature'], feature_importance_df['importance'])
              plt.xlabel("Importance")
              plt.ylabel("Feature")
              plt.title("Feature Importances from Random Forest Model")
              plt.gca().invert_yaxis()
              plt.tight_layout()
              plt.savefig("output_visuals/feature_importances_plot.png") # Simpan plot
              plt.show()
              ```
        * **`plot_residuals_and_actual_vs_predicted.ipynb`**: Notebook untuk membuat scatter plot prediksi vs aktual, dan plot distribusi residu.
            * **Kode Kunci (PySpark & Matplotlib di Notebook)**:
              ```python
              # Asumsi 'predictions' DataFrame (hasil model.transform(test_data)) sudah ada atau dimuat
              # predictions_pd = predictions.select("label", "prediction").sample(False, 0.1).toPandas() # Ambil sampel jika data besar

              plt.figure(figsize=(8, 8))
              plt.scatter(predictions_pd['label'], predictions_pd['prediction'], alpha=0.5)
              plt.plot([predictions_pd['label'].min(), predictions_pd['label'].max()], [predictions_pd['label'].min(), predictions_pd['label'].max()], 'k--', lw=2) # Garis y=x
              plt.xlabel("Actual Avg Speed (km/h)")
              plt.ylabel("Predicted Avg Speed (km/h)")
              plt.title("Actual vs. Predicted Speeds")
              plt.savefig("output_visuals/actual_vs_predicted_plot.png")
              plt.show()

              # Analisis Residu
              predictions_pd['residuals'] = predictions_pd['label'] - predictions_pd['prediction']
              plt.figure(figsize=(8, 6))
              plt.hist(predictions_pd['residuals'], bins=30, edgecolor='k')
              plt.xlabel("Residuals (Actual - Predicted)")
              plt.ylabel("Frequency")
              plt.title("Distribution of Residuals")
              plt.axvline(0, color='k', linestyle='dashed', linewidth=1)
              plt.savefig("output_visuals/residuals_distribution_plot.png")
              plt.show()
              ```
    * **`output_visuals/` (Subfolder di dalam `notebooks_for_evaluation/`)**: Tempat menyimpan file gambar (`.png`, `.jpg`) hasil plot dari notebook.

### Menuju Kepercayaan:

**Kunci untuk membuat bagian evaluasi ini meyakinkan adalah:**
* **Transparansi Data**: Jelaskan dengan jelas dataset mana yang digunakan untuk evaluasi (yaitu, *test set* yang tidak terlihat oleh model saat pelatihan).
* **Metrik yang Tepat**: Gunakan metrik evaluasi yang standar dan relevan untuk masalah regresi (RMSE, MAE, R2).
* **Visualisasi yang Mendukung**: Plot seperti *actual vs. predicted* dan distribusi residu membantu memahami perilaku model lebih dari sekadar angka metrik. *Feature importance* menunjukkan apa yang dipelajari model.
* **Interpretasi yang Jujur**: Akui keterbatasan model jika ada (misalnya, "model cenderung *overpredict* pada kecepatan rendah"). Jangan hanya menyoroti hasil yang baik.
* **Reproducibility**: Jika menggunakan notebook, pastikan kode di dalamnya bersih dan dapat dijalankan ulang untuk menghasilkan plot dan metrik yang sama.

Dengan menyajikan hasil evaluasi secara detail, terstruktur, dan visual, Anda menunjukkan bahwa Anda tidak hanya membuat model, tetapi juga secara kritis menilai kinerjanya. Ini membangun kepercayaan yang kuat terhadap validitas temuan proyek Anda.