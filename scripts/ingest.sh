#!/bin/bash
# scripts/ingest.sh - Skrip untuk memasukkan data mentah ke HDFS
# Akan dipanggil secara manual dari terminal.

# Definisikan path HDFS untuk Bronze Layer
HDFS_BRONZE_TRAFFIC="hdfs://namenode:9000/data/bronze/trafik"
HDFS_BRONZE_WEATHER="hdfs://namenode:9000/data/bronze/cuaca"

# Buat direktori HDFS jika belum ada.
echo "Membuat direktori HDFS: ${HDFS_BRONZE_TRAFFIC} dan ${HDFS_BRONZE_WEATHER}"
hdfs dfs -mkdir -p ${HDFS_BRONZE_TRAFFIC}
hdfs dfs -mkdir -p ${HDFS_BRONZE_WEATHER}

# Dapatkan tanggal saat ini untuk penamaan file yang unik
CURRENT_DATE=$(date +%Y-%m-%d)

# Masukkan data lalu lintas dari volume /data_input (folder data lokal Anda) ke HDFS
echo "Memasukkan data lalu lintas dari /data_input/simulasi-trafik-medan.csv ke HDFS..."
hdfs dfs -put -f /data_input/simulasi-trafik-medan.csv ${HDFS_BRONZE_TRAFFIC}/gps_${CURRENT_DATE}.csv

# Masukkan data cuaca dari volume /data_input ke HDFS
echo "Memasukkan data cuaca dari /data_input/cuaca-medan-dummy.csv ke HDFS..."
hdfs dfs -put -f /data_input/cuaca-medan-dummy.csv ${HDFS_BRONZE_WEATHER}/weather_${CURRENT_DATE}.csv

echo "Proses ingestion ke HDFS Bronze Layer selesai untuk ${CURRENT_DATE}"
