from pyspark.sql import SparkSession
from pymongo import MongoClient
import time

client = MongoClient("mongodb://localhost:27017/")

db = client["disasterDB"]
collection = db["alerts"]

spark = SparkSession.builder \
    .appName("DisasterMongoAlerts") \
    .getOrCreate()

df = spark.read.csv(
    "/mnt/d/HadoopCluster/nlp-getting-started/train.csv",
    header=True
)

keywords = ['flood', 'earthquake', 'fire', 'cyclone', 'storm']

print("Monitoring disaster tweets...\n")

for row in df.collect():

    text = row['text']
    location = row['location']

    if text:

        for keyword in keywords:

            if keyword in text.lower():

                alert = {
                    "disaster": keyword,
                    "location": location,
                    "tweet": text,
                    "severity": "High"
                }

                collection.insert_one(alert)

                print("ALERT STORED IN MONGODB")
                print(alert)
                print("-" * 60)

                break

    time.sleep(1)
