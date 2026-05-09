import networkx as nx
import matplotlib.pyplot as plt

plt.style.use("dark_background")

G = nx.Graph()

relations = [
    ("Flood", "Chennai", 8),
    ("Flood", "Mumbai", 6),
    ("Flood", "Kerala", 9),
    ("Cyclone", "Andhra Pradesh", 7),
    ("Cyclone", "Odisha", 8),
    ("Earthquake", "Delhi", 5),
    ("Fire", "Bangalore", 4),
    ("Storm", "Kerala", 6)
]

for source, target, weight in relations:
    G.add_edge(source, target, weight=weight)

plt.figure(figsize=(15, 10))

pos = nx.spring_layout(
    G,
    seed=42,
    k=1.5
)

disasters = ["Flood", "Cyclone", "Earthquake", "Fire", "Storm"]

node_colors = []
node_sizes = []

for node in G.nodes():

    if node in disasters:
        node_colors.append("#ff4d4d")
        node_sizes.append(5000)
    else:
        node_colors.append("#4da6ff")
        node_sizes.append(3500)

edges = G.edges(data=True)
weights = [edge[2]['weight'] for edge in edges]

nx.draw_networkx_nodes(
    G,
    pos,
    node_color=node_colors,
    node_size=node_sizes,
    alpha=0.95,
    edgecolors="white",
    linewidths=2
)

nx.draw_networkx_edges(
    G,
    pos,
    width=weights,
    edge_color="#00ffff",
    alpha=0.7,
    connectionstyle="arc3,rad=0.15"
)

nx.draw_networkx_labels(
    G,
    pos,
    font_size=11,
    font_weight="bold",
    font_color="white"
)

edge_labels = {
    (u, v): f"Impact {d['weight']}"
    for u, v, d in G.edges(data=True)
}

nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=edge_labels,
    font_color="yellow",
    font_size=9
)

plt.title(
    "Real-Time Disaster Response Link Analytics",
    fontsize=22,
    fontweight="bold",
    color="white",
    pad=20
)

plt.text(
    0.5,
    -0.08,
    "Disaster nodes connected to high-risk affected regions",
    fontsize=12,
    ha='center',
    transform=plt.gca().transAxes,
    color='lightgray'
)

plt.axis("off")

plt.savefig(
    "advanced_link_analysis.png",
    dpi=400,
    bbox_inches="tight",
    facecolor="black"
)

plt.show()
