from pyspark.sql import SparkSession
import json

spark = SparkSession.builder \
    .appName("GenerateAlerts") \
    .getOrCreate()

df = spark.read.csv(
    "/mnt/d/HadoopCluster/nlp-getting-started/train.csv",
    header=True
)

keywords = ['flood', 'earthquake', 'fire', 'cyclone', 'storm']

alerts = []

for row in df.collect():

    text = row['text']
    location = row['location']

    if text:

        for keyword in keywords:

            if keyword in text.lower():

                alerts.append({
                    "disaster": keyword,
                    "location": location,
                    "tweet": text,
                    "severity": "High"
                })

                break

with open("alerts.json", "w") as f:
    json.dump(alerts, f, indent=4)

print("Alerts saved to alerts.json")
