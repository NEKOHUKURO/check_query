import matplotlib.pyplot as plt
import networkx as nx

# 有向グラフの作成
G = nx.DiGraph()

f = open("reaned_data.txt")
moves = f.read().split("\n")

plt.figure(figsize=(10, 8))

G.add_node("start", node_color = "red")

for move in moves:
    separate = move.split(" ")
    pre_status = separate[0]
    condition = separate[1]
    after_status = separate[3]
    print(pre_status, condition, after_status)
    G.add_edge(pre_status, after_status)

# グラフの描画
pos = nx.spring_layout(G, k=1.75) 
nx.draw_networkx(G, pos, with_labels=True, alpha=0.5, node_size = 1000)

# 表示
plt.show()