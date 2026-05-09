import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter

# Load dataset
df = pd.read_csv(
    "/mnt/d/HadoopCluster/nlp-getting-started/train.csv"
)

# Keywords
keywords = ['flood', 'earthquake', 'fire', 'cyclone', 'storm']

# Count disaster keywords
keyword_counts = {}

for keyword in keywords:
    keyword_counts[keyword] = df['text'].str.lower().str.contains(keyword).sum()

# -------------------------------
# 1. BAR CHART
# -------------------------------

plt.figure(figsize=(8,5))

plt.bar(
    keyword_counts.keys(),
    keyword_counts.values()
)

plt.title("Disaster Frequency Analysis")
plt.xlabel("Disaster Type")
plt.ylabel("Tweet Count")

plt.savefig("bar_chart.png")
plt.close()

# -------------------------------
# 2. PIE CHART
# -------------------------------

plt.figure(figsize=(7,7))

plt.pie(
    keyword_counts.values(),
    labels=keyword_counts.keys(),
    autopct='%1.1f%%'
)

plt.title("Disaster Distribution")

plt.savefig("pie_chart.png")
plt.close()

# -------------------------------
# 3. TOP AFFECTED LOCATIONS
# -------------------------------

locations = df['location'].dropna()

top_locations = Counter(locations).most_common(10)

loc_names = [x[0] for x in top_locations]
loc_counts = [x[1] for x in top_locations]

plt.figure(figsize=(10,5))

plt.bar(loc_names, loc_counts)

plt.xticks(rotation=45)

plt.title("Top Affected Locations")
plt.xlabel("Location")
plt.ylabel("Tweet Count")

plt.tight_layout()

plt.savefig("locations_chart.png")
plt.close()

# -------------------------------
# 4. REAL-TIME ALERT TREND
# -------------------------------

trend = list(range(1, len(keywords)+1))

plt.figure(figsize=(8,5))

plt.plot(
    trend,
    list(keyword_counts.values()),
    marker='o'
)

plt.title("Real-Time Alert Trend")
plt.xlabel("Time Window")
plt.ylabel("Detected Alerts")

plt.savefig("trend_graph.png")
plt.close()

# -------------------------------
# 5. WORD CLOUD
# -------------------------------

text = " ".join(df['text'].dropna().astype(str))

wordcloud = WordCloud(
    width=1200,
    height=600,
    background_color='white'
).generate(text)

plt.figure(figsize=(12,6))

plt.imshow(wordcloud)

plt.axis("off")

plt.title("Disaster Tweet Word Cloud")

plt.savefig("wordcloud.png")
plt.close()

print("All analytics graphs generated successfully.")
