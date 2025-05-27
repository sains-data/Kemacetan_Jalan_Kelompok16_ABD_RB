# ...
# Inisialisasi Spark Session
spark = SparkSession.builder \
    .appName("MedanTrafficETLAndML") \
    .config("spark.sql.warehouse.dir", "hdfs://namenode:9000/user/hive/warehouse") \
    .config("spark.hadoop.javax.jdo.option.ConnectionURL", "jdbc:postgresql://postgres-hive-metastore-db:5432/metastore") \
    .config("spark.hadoop.javax.jdo.option.ConnectionDriverName", "org.postgresql.Driver") \
    .config("spark.hadoop.javax.jdo.option.ConnectionUserName", "hiveuser") \
    .config("spark.hadoop.javax.jdo.option.ConnectionPassword", "hivepassword") \
    .config("spark.sql.catalogImplementation", "hive") \
    .enableHiveSupport() \
    .getOrCreate()

# Path data input (sesuaikan jika berbeda di image Jupyter)
# Contoh: jika Anda mount ke /home/jovyan/data_input
traffic_input_path = "hdfs://namenode:9000/data/bronze/trafik/*.csv" # Tetap HDFS karena Anda ingin HDFS
weather_input_path = "hdfs://namenode:9000/data/bronze/cuaca/*.csv" # Tetap HDFS

# ...
# Output path
# final_output_path = "/home/jovyan/output_data/traffic_prediction_results.parquet" # Opsional untuk output lokal
# ...