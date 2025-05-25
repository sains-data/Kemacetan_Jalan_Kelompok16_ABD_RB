from pyspark.sql import SparkSession
from pyspark.sql.functions import col, hour, dayofweek, when
from pyspark.ml.feature import StringIndexer, VectorAssembler, Imputer
from pyspark.ml import Pipeline

def main():
    spark = SparkSession.builder \
        .appName("FeatureEngineeringTrafficMedan") \
        .getOrCreate()

    print("Memulai proses rekayasa fitur untuk model prediksi kemacetan...")

    # Path HDFS (sesuaikan)
    hdfs_base_path = "/user/hive/warehouse/kemacetan_medan/"
    gold_input_path = f"{hdfs_base_path}gold/trafik_cuaca_agg/agregat_kemacetan.orc"
    # Output bisa langsung ke model training atau disimpan jika prosesnya kompleks
    # feature_output_path = f"{hdfs_base_path}features_for_modeling/"

    df_gold = spark.read.orc(gold_input_path)
    print(f"Data agregat Gold dimuat, jumlah baris: {df_gold.count()}")
    df_gold.printSchema()

    # 1. Final Missing Value Handling (Contoh: Imputasi untuk kolom numerik)
    # Kolom yang akan diimputasi
    numerical_cols_for_imputation = ["avg_speed_kmh", "vehicle_count", "avg_rainfall_mm", "avg_temperature_c"]
    imputer = Imputer(inputCols=numerical_cols_for_imputation, outputCols=[f"{c}_imputed" for c in numerical_cols_for_imputation])
    imputer.setStrategy("mean") # atau median, mode

    df_imputed = imputer.fit(df_gold).transform(df_gold)

    # Ganti kolom asli dengan yang sudah diimputasi dan drop kolom _imputed sementara
    for c in numerical_cols_for_imputation:
        df_imputed = df_imputed.withColumn(c, col(f"{c}_imputed")).drop(f"{c}_imputed")

    # Hapus baris jika label (avg_speed_kmh) masih null setelah imputasi (seharusnya tidak jika diimputasi)
    # atau jika fitur kategorikal penting (road_name) null
    df_cleaned = df_imputed.na.drop(subset=["road_name", "avg_speed_kmh"])
    print(f"Data setelah final cleaning & imputation, jumlah baris: {df_cleaned.count()}")


    # 2. Encoding Fitur Kategorikal (road_name)
    # `jam` dan `hari_minggu` sudah numerik dari tahap gold
    road_name_indexer = StringIndexer(inputCol="road_name", outputCol="road_name_index", handleInvalid="keep")
    # `handleInvalid="keep"` akan menempatkan nilai invalid ke dalam kategori tersendiri

    # 3. Definisi Kolom Fitur untuk VectorAssembler
    # Kolom fitur yang akan digunakan model
    # 'latitude', 'longitude' dari df_gold_agg juga bisa dipertimbangkan jika relevan per segmen
    feature_columns = [
        "road_name_index",
        "jam",              # Sudah numerik (0-23)
        "hari_minggu",      # Sudah numerik (1-7)
        "vehicle_count",
        "avg_rainfall_mm",
        "avg_temperature_c"
        # Tambahkan fitur lain hasil rekayasa jika ada
    ]

    # 4. VectorAssembler
    vector_assembler = VectorAssembler(inputCols=feature_columns, outputCol="features_unscaled")

    # 5. (Opsional) Scaling Fitur Numerik, jika diperlukan oleh model atau untuk konvergensi
    # from pyspark.ml.feature import MinMaxScaler
    # scaler = MinMaxScaler(inputCol="features_unscaled", outputCol="features")
    # Jika tidak ada scaling, ganti nama output VectorAssembler menjadi "features"
    # Atau ganti nama input di model training

    # 6. Membuat pipeline untuk preprocessing fitur
    # Jika tanpa scaling:
    feature_pipeline = Pipeline(stages=[road_name_indexer, vector_assembler])
    # Jika dengan scaling:
    # feature_pipeline = Pipeline(stages=[road_name_indexer, vector_assembler, scaler])


    # 7. Transformasi data menggunakan pipeline fitur
    feature_model = feature_pipeline.fit(df_cleaned)
    df_features_prepared = feature_model.transform(df_cleaned)

    # 8. Pilih kolom yang relevan untuk training: 'features' dan kolom label 'avg_speed_kmh'
    # Kolom label harus bernama 'label' jika tidak dispesifikasikan di model, atau kita bisa rename
    df_final_for_modeling = df_features_prepared.select(col("features_unscaled").alias("features"), col("avg_speed_kmh").alias("label"))
    # Jika menggunakan scaling, gunakan col("features")

    print("DataFrame dengan fitur siap untuk modeling:")
    df_final_for_modeling.show(5, truncate=False)
    df_final_for_modeling.printSchema()

    # Data ini sekarang siap untuk diteruskan ke skrip training model
    # Anda bisa menyimpannya ke HDFS jika tahap ini dipisah dari training
    # df_final_for_modeling.write.mode("overwrite").parquet(feature_output_path + "prepared_features.parquet")
    # print(f"Data fitur siap model disimpan di HDFS: {feature_output_path}prepared_features.parquet")

    # Untuk contoh ini, kita asumsikan df_final_for_modeling akan langsung digunakan oleh skrip training
    # Jika skrip training terpisah, skrip training akan memuat dari path output di atas

    spark.stop()

if __name__ == "__main__":
    main()