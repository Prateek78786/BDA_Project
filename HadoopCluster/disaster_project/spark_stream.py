from pyspark.sql import SparkSession
import time

spark = SparkSession.builder \
    .appName("DisasterResponseSystem") \
    .getOrCreate()

df = spark.read.csv(
    "/mnt/d/HadoopCluster/nlp-getting-started/train.csv",
    header=True
)

keywords = ['flood', 'earthquake', 'fire', 'cyclone', 'storm']

print("Starting Real-Time Disaster Monitoring...\n")

for row in df.collect():

    text = row['text']

    if text:
        if any(word in text.lower() for word in keywords):

            print("ALERT DETECTED:")
            print(text)
            print("-" * 60)

    time.sleep(1)
