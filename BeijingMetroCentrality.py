# coding=utf-8
import json
import networkx as nx
from networkx.algorithms.centrality import *

with open("1100_drw_beijing.json", "r", encoding="utf-8") as dump_f:
    datas = json.load(dump_f)

line_list = datas["l"]

G = nx.Graph()

for line in line_list:
    station_list = line["st"]
    for index in range(len(station_list)):
        if index + 1 < len(station_list):
            G.add_edge(station_list[index]["n"], station_list[index + 1]["n"])
        else:
            G.add_edge(station_list[index]["n"], station_list[0]["n"])

# print(G.edges._adjdict["西直门"])
# print(G.edges._adjdict["积水潭"])

degree_centrality = nx.degree_centrality(G)
closeness_centrality = nx.closeness_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)

degree_centrality = sorted(degree_centrality.items(), key=lambda d: d[1], reverse=True)
closeness_centrality = sorted(closeness_centrality.items(), key=lambda d: d[1], reverse=True)
betweenness_centrality = sorted(betweenness_centrality.items(), key=lambda d: d[1],
                                reverse=True)

# print(degree_centrality)
print(closeness_centrality)
# print(betweenness_centrality)
