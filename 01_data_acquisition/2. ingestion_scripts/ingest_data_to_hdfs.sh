#!/bin/bash

# Diasumsikan skrip ini dijalankan dari root proyek atau path sumber data sudah disesuaikan
# Atau, lebih baik, skrip ini ada di dalam container dan path data juga relatif terhadap struktur di container.

# Path relatif dari root proyek di host ke data mentah
HOST_RAW_DATASETS_PATH="./01_data_acquisition/raw_datasets/"
LOCAL_TRAFIK_DATA="${HOST_RAW_DATASETS_PATH}simulasi_trafik_medan.csv"
LOCAL_CUACA_DATA="${HOST_RAW_DATASETS_PATH}cuaca_medan_2013-07-01.csv"

# Path target di HDFS Bronze Layer (sesuaikan dengan definisi di init_hdfs_dirs.sh)
HDFS_BRONZE_BASE_PATH="/user/hive/warehouse/kemacetan_medan/bronze"
HDFS_BRONZE_TRAFIK_PATH="${HDFS_BRONZE_BASE_PATH}/trafik/"
HDFS_BRONZE_CUACA_PATH="${HDFS_BRONZE_BASE_PATH}/cuaca/"

# Nama file di HDFS (bisa ditambahkan timestamp jika ingin versi harian)
# Untuk contoh ini, kita gunakan nama file asli
TRAFIK_FILENAME_HDFS="simulasi_trafik_medan.csv"
CUACA_FILENAME_HDFS="cuaca_medan_2013-07-01.csv"

echo "Memulai proses ingestion data ke HDFS Bronze Layer..."

# Cek apakah file sumber ada (jika skrip dijalankan di host sebelum dicopy ke container)
if [ ! -f "$LOCAL_TRAFIK_DATA" ]; then
    echo "ERROR: File data trafik tidak ditemukan di $LOCAL_TRAFIK_DATA"
    exit 1
fi

if [ ! -f "$LOCAL_CUACA_DATA" ]; then
    echo "ERROR: File data cuaca tidak ditemukan di $LOCAL_CUACA_DATA"
    exit 1
fi

# Mengunggah data trafik ke HDFS
# Perintah hdfs dfs dijalankan di lingkungan yang memiliki akses ke HDFS (misal di dalam container)
echo "Mengunggah data trafik: $LOCAL_TRAFIK_DATA ke $HDFS_BRONZE_TRAFIK_PATH$TRAFIK_FILENAME_HDFS"
hdfs dfs -put -f "$LOCAL_TRAFIK_DATA" "$HDFS_BRONZE_TRAFIK_PATH$TRAFIK_FILENAME_HDFS"
if [ $? -eq 0 ]; then
    echo "Upload data trafik berhasil."
else
    echo "ERROR: Upload data trafik gagal."
    exit 1
fi

# Mengunggah data cuaca ke HDFS
echo "Mengunggah data cuaca: $LOCAL_CUACA_DATA ke $HDFS_BRONZE_CUACA_PATH$CUACA_FILENAME_HDFS"
hdfs dfs -put -f "$LOCAL_CUACA_DATA" "$HDFS_BRONZE_CUACA_PATH$CUACA_FILENAME_HDFS"
if [ $? -eq 0 ]; then
    echo "Upload data cuaca berhasil."
else
    echo "ERROR: Upload data cuaca gagal."
    exit 1
fi

echo "Proses ingestion data selesai."